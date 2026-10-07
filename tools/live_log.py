#!/usr/bin/env python3
"""対話ログを 1 ターンごとに作り直し、検査してから作業ブランチに push する。

使い方:
    # セッションの始めに一度（回の情報を logs/live.json に書く）
    python3 tools/live_log.py start --number 29 --slug operations-improvement \\
        --title "2026-10-06 第 29 回: 運用の改善（T-0025 の 1・3）" --since 2026-10-06T03:58:20Z
    # 各応答の始めと終わりに
    python3 tools/live_log.py sync

第 29 回にユーザーと決めた運用（T-0025 の 1。案 A）:

- 公開側の対話ログ（logs/）は、発言とタイムスタンプだけを残す。ツールの呼び出しと結果は含めない。
  ツールの呼び出しを含む記録（ツールの結果は先頭だけに切り詰め、置き換えは当てない）は、
  非公開リポジトリの logs/ に置く。元のセッション記録そのものは保存しない。
- 集めるのは、この作業ディレクトリ（リポジトリの親）のセッション記録で、作業ディレクトリが
  その下にある行だけ（ほかのプロジェクトの会話を混ぜない）。
- 保証できるのは「次の同期までに記録された発言」である。応答の最後の同期の後に書いた文は、
  次の同期で保存される。次の回の start は、前の回のログを先に同期して閉じる。
- 毎回、セッション記録（/clear などで分かれた複数のファイルを含む）から、その回のログの全体を
  作り直す。追記を積み重ねないので、二重の記録や抜けが起きない。
- push 先は作業ブランチ（main ではない）。ログは、セッションの終わりの PR で main に入る。
- push の前に、伏せ字の照合と、登録していない個人情報・秘密情報・長い引用の疑いの検査を行う。
  照合が 0 件でないか、疑いがあれば、公開側には書かずに非公開リポジトリの held/ に保留し、
  終了コード 1 で終わる（確認してから公開する）。
- 自動の検査で見つかるのは、既知の形式（export_log.REDACTIONS。見つけたものは伏せ字にする）と、
  形からの推定（32 文字以上の高エントロピーの文字列、電話番号、長い引用・長い英文）だけで、
  漏れがないことは保証しない。
- 確認の結果は、非公開リポジトリの log-overrides.json に、発言の uuid ごとに書く。
  {"<uuid>": {"replace": "要約"}} はその発言の本文を要約で置き換え（他者の文章の長い引用など）、
  {"<uuid>": {"approve": "理由"}} は長い引用の疑いの検査を外す（誤検出）。
  {"<uuid>": {"approve_tokens": {"t-<ハッシュ>": "理由"}}} は、その発言の中の、ハッシュが一致する
  高エントロピーの文字列だけを誤検出として通す（ハッシュは保留のときに表示される。文字列そのものは
  書かない）。伏せ字の照合、メールアドレス・電話番号・既知の形式のキーの検査は外せない
  （語句は redactions.txt に追記して伏せ字にする）。
"""

import argparse
import contextlib
import fcntl
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_log  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
PRIVATE = REPO.parent / "point-free-spacetime-private"
STATE = REPO / "logs" / "live.json"
OVERRIDES = PRIVATE / "log-overrides.json"
# sync を実行したセッションの ID の登録簿（非公開）。この研究の会話と確かめたセッションとして扱う
SESSIONS = PRIVATE / "live-sessions.json"
PROJECTS = Path.home() / ".claude" / "projects"
LOCK = REPO.parent / ".live_log.lock"


@contextlib.contextmanager
def exclusive_lock(path: Path, timeout: float = 300.0):
    """排他ロック（ほかの start・sync が終わるまで待つ。timeout 秒を過ぎたら止める）。"""
    with open(path, "a") as f:
        deadline = time.monotonic() + timeout
        while True:
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise SystemExit(f"ほかの start・sync が終わらない（{path} のロックを取れない）")
                time.sleep(0.2)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def valid_date(text: str) -> bool:
    from datetime import date
    if not DATE.fullmatch(text):
        return False
    try:
        date.fromisoformat(text)
    except ValueError:
        return False
    return True


def project_dirs(projects: Path, workdir: Path = REPO.parent) -> list[Path]:
    """作業ディレクトリ（とその下のリポジトリ）に対応する、Claude Code のセッション記録のディレクトリ。"""
    sanitize = lambda p: re.sub(r"[^A-Za-z0-9]", "-", str(p))
    root = sanitize(workdir)
    repos = [sanitize(workdir / r.name) for r in (REPO, PRIVATE)]
    # 作業ディレクトリそのものと、両リポジトリ（とそのサブディレクトリ）から起動したセッションの記録。
    # 名前の変換で区切りが「-」になるので、名前が似ているだけの兄弟ディレクトリも拾い得るが、
    # その行は collect() が行ごとの作業ディレクトリで除く
    dirs = [d for d in (projects.iterdir() if projects.is_dir() else []) if d.is_dir()
            and (d.name == root or any(d.name == r or d.name.startswith(r + "-") for r in repos))]
    return sorted(dirs)

PUBLIC_HEADER = [
    "> この記録は Claude Code のセッション記録から `tools/live_log.py` で、1 ターンごとに自動変換したものです。",
    "> 発言とタイムスタンプ（UTC）だけを残し、ツールの呼び出しと結果は含めません（第 29 回にユーザーと決めた運用）。",
    "> 見出しの「記録 N」は、`/clear` などで分かれたセッション記録の別を示します。個人情報などは伏せ字にしています。",
]


# ---- セッション記録の収集 ----

def _parses(line: str) -> bool:
    if not line.strip():
        return True
    try:
        json.loads(line)
    except json.JSONDecodeError:
        return False
    return True


def collect(projects: Path, since: str, until: str | None = None, workdir: Path = REPO.parent,
            known_sessions: set[str] = frozenset(), untimed: list | None = None,
            excluded_sessions: set[str] = frozenset(), unconfirmed: list | None = None,
            broken: list | None = None) -> list[dict]:
    """作業ディレクトリのセッション記録から、この研究の会話の、期間内の行を集める。

    ほかのプロジェクトのディレクトリは読まない。さらに、この研究の会話と確かめられた
    セッション（sessionId）の行だけを採る。確かめ方：known_sessions（sync を実行したセッションの
    登録簿）にあるか、そのセッションのどれかの行の
    作業ディレクトリ（cwd）が、公開・非公開のリポジトリの下にあること（Claude は各応答で
    公開リポジトリの下から sync を実行するので、この研究の会話は必ずこの条件を満たす）。
    確かめたセッションの行のうち、cwd が親ディレクトリそのもの、両リポジトリの下、
    または cwd のない行を採り、兄弟ディレクトリの別のプロジェクトでの行は除く。
    同じ行（uuid が同じもの）が複数のファイルにあれば一つにまとめ、時刻の順に並べる。
    """
    root = str(workdir.resolve())
    subtrees = [str(workdir.resolve() / r.name) for r in (REPO, PRIVATE)]

    def in_repos(cwd: str) -> bool:
        return any(cwd == t or cwd.startswith(t + "/") for t in subtrees)

    since_dt = export_log.parse_time(since)
    until_dt = export_log.parse_time(until) if until else None
    seen, rows, sessions = set(), [], set(known_sessions)
    no_time = []  # 時刻がなく、どの回のものか判定できない発言
    files = [f for d in project_dirs(projects, workdir) for f in sorted(d.glob("*.jsonl"))]
    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        if lines and not _parses(lines[-1]):
            time.sleep(0.5)  # 末尾の行は書き込み途中のことがあるので、一度読み直す
            lines = f.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                # 読めない行（壊れた行、読み直しても書き込み途中の末尾の行）は、黙って飛ばさずに知らせる
                if broken is not None:
                    broken.append(f"{f.name} の {lineno} 行目")
                continue
            cwd = d.get("cwd")
            if cwd and in_repos(cwd) and d.get("sessionId"):
                sessions.add(d["sessionId"])  # 期間の外の行でも、セッションの確認には使う
            ts = d.get("timestamp")
            if cwd and not (cwd == root or in_repos(cwd)):
                continue
            if not ts:
                # 公開ログに出る行（発言の本文、人が送った途中の発言）だけを問題にする
                if export_log.convert_records([d], "", include_tools=False, header=[]).strip() != "#":
                    no_time.append(d)
                continue
            t = export_log.parse_time(ts)
            if t < since_dt or (until_dt and t >= until_dt):
                continue
            # uuid のない行は、行の中身（セッション・発言・途中の発言）で同じ行かを判定する
            key = d.get("uuid") or (ts, d.get("type"), d.get("sessionId"), json.dumps(d.get("message"), sort_keys=True),
                                    json.dumps(d.get("attachment"), sort_keys=True))
            if key in seen:
                continue
            seen.add(key)
            rows.append(d)
    if untimed is not None:
        # セッションの分からない行も、どの回のものか判定できないので保留の対象にする
        untimed += [d for d in no_time if d.get("sessionId") in sessions or not d.get("sessionId")]
        untimed += [d for d in rows if not d.get("sessionId")
                    and export_log.convert_records([d], "", include_tools=False, header=[]).strip() != "#"]
    sessions -= set(excluded_sessions)
    if unconfirmed is not None:
        # この研究の会話と確かめられず、除くとも決めていないセッションの発言（/clear の後に同期しなかった
        # 分岐など）。黙って除かず、確かめるまで保留する
        unconfirmed += [d for d in rows if d.get("sessionId") and d["sessionId"] not in sessions
                        and d["sessionId"] not in excluded_sessions
                        and export_log.convert_records([d], "", include_tools=False, header=[]).strip() != "#"]
    rows = [d for d in rows if d.get("sessionId") in sessions]
    rows.sort(key=lambda d: export_log.parse_time(d["timestamp"]))
    return rows


def row_id(d: dict) -> str:
    """行の識別子（log-overrides.json のキー）。uuid のない行は、中身から作る（同じ行なら毎回同じになる）。"""
    if d.get("uuid"):
        return d["uuid"]
    key = json.dumps([d.get("timestamp"), d.get("type"), d.get("sessionId"), d.get("message"), d.get("attachment")],
                     sort_keys=True, ensure_ascii=False)
    return "h-" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def override_for(d: dict, overrides: dict) -> dict:
    """その行に当てる確認の結果。途中に届いた発言は、同じ発言の通常の行（source_uuid）への指定も当てる
    （公開ログに出るのは途中の発言の方なので）。"""
    o = overrides.get(row_id(d))
    if o is None and d.get("type") == "attachment":
        o = overrides.get((d.get("attachment") or {}).get("source_uuid"))
    return o or {}


def apply_overrides(rows: list[dict], overrides: dict) -> list[dict]:
    """log-overrides.json の replace を当てる（発言の本文を要約で置き換える）。"""
    out = []
    for d in rows:
        rep = override_for(d, overrides).get("replace")
        if rep is not None:
            d = json.loads(json.dumps(d))
            note = f"（この発言は、公開前に要約に置き換えた）\n\n{rep}"
            if d.get("type") == "attachment":
                d["attachment"]["prompt"] = note
            elif d.get("type") == "user":
                d["message"]["content"] = note
            else:
                d["message"]["content"] = [{"type": "text", "text": note}]
        out.append(d)
    return out


# ---- 検査 ----

# 電話番号の形：ハイフンか空白の区切り、+ で始まる国際形式、区切りのない 0 で始まる 10・11 桁
PHONE = re.compile(r"(?<![0-9A-Za-z_-])(?:0\d{1,4}[- ]\d{1,4}[- ]\d{3,4}|\+\d{1,3}[ -]\d{1,4}[ -]\d{2,4}[ -]\d{3,4}"
                   r"|\+\d{10,15}|0\d{9,10})(?![0-9A-Za-z_-])")
TOKEN = re.compile(r"[A-Za-z0-9+/_=-]{32,}")
JAPANESE = re.compile(r"[぀-ヿ㐀-鿿]")
QUOTE_LINE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?>")
# 長い引用の疑いの目安
MAX_QUOTE_LINES = 8
MAX_ENGLISH_CHARS = 600


def entropy(s: str) -> float:
    n = len(s)
    return -sum(c / n * math.log2(c / n) for c in Counter(s).values())


def is_commit(token: str) -> bool:
    """公開・非公開のリポジトリに、この SHA のコミットが実在するか。"""
    return any(
        subprocess.run(["git", "-C", str(r), "cat-file", "-e", f"{token}^{{commit}}"], capture_output=True).returncode == 0
        for r in (REPO, PRIVATE) if (r / ".git").exists())


def looks_secret(token: str) -> bool:
    """キーの疑いのある長い文字列か。

    16 進数の文字列は、リポジトリに実在するコミットの SHA（40 文字）だけを例外とし、それ以外の
    32 文字以上は疑う（長さだけでは SHA と同じ形のトークンと区別できない。16 進数はエントロピーが
    最大でも 4 なので、下の基準は使えない）。パスやファイル名の形（英小文字・数字・区切り / - _
    だけからなり、区切りを含むもの）は除き、それ以外はエントロピーが 4.0 以上のものを疑う。
    """
    if re.fullmatch(r"[0-9a-fA-F]+", token):
        return not (len(token) == 40 and is_commit(token.lower()))
    # パスやファイル名の形（英小文字・数字・区切り / - _ だけからなり、区切りを含むもの）は除く。
    # 長い 16 進数でない限り、パスとキーを区別できないため（既知の形式のキーは別に検査する）
    if re.fullmatch(r"[a-z0-9/_-]+", token) and re.search(r"[/_-]", token):
        return False
    # それ以外は、文字種によらず（英大文字だけ、base64 の形の / + = を含むものなども）エントロピーで判定する
    return entropy(token) >= 4.0


def paragraphs(text: str) -> list[str]:
    """段落の一覧。コードブロックは、中身全体を一つの段落とみなす（中の長い引用も検査するため）。"""
    paras, buf, in_code = [], [], False
    for line in text.splitlines():
        if re.match(r"\s*(```|~~~)", line):
            if buf:
                paras.append("\n".join(buf))
                buf = []
            in_code = not in_code
            continue
        if in_code:
            buf.append(line)
        elif line.strip():
            buf.append(line)
        elif buf:
            paras.append("\n".join(buf))
            buf = []
    if buf:
        paras.append("\n".join(buf))
    return paras


def token_hash(token: str) -> str:
    """高エントロピーの文字列の承認に使うハッシュ（SHA-256 の先頭 16 桁。短いので、それ自体は検査に掛からない）。"""
    return "t-" + hashlib.sha256(token.encode("utf-8")).hexdigest()[:16]


def check(text: str, terms: list[str], header_lines: int = len(PUBLIC_HEADER),
          approved_tokens: frozenset[str] = frozenset()) -> list[str]:
    """公開してよいかを検査し、問題の一覧を返す（空なら公開してよい）。

    approved_tokens（token_hash の値）に一致する高エントロピーの文字列は、誤検出として通す。"""
    problems = []
    lower = text.lower()
    hits = sum(lower.count(t.lower()) for t in terms)
    if hits:
        problems.append(f"伏せ字の語句が {hits} 件残っている")
    if export_log.REDACTIONS[0][0].search(text):
        problems.append("メールアドレスの形の文字列がある")
    if PHONE.search(text):
        problems.append("電話番号の形の文字列がある")
    known = sum(len(pat.findall(text)) for pat, _ in export_log.REDACTIONS[:4])
    if known:
        problems.append(f"既知の形式のキー・秘密情報が {known} 件ある")
    secrets = [t for t in TOKEN.findall(text) if looks_secret(t) and token_hash(t) not in approved_tokens]
    if secrets:
        hashes = ", ".join(dict.fromkeys(token_hash(t) for t in secrets))
        problems.append(f"キーの形の高エントロピーの文字列が {len(secrets)} 件ある（ハッシュ {hashes}）")
    run = longest = 0
    for i, line in enumerate(text.splitlines()):
        # 字下げした引用や、箇条書きの中の引用も数える
        if QUOTE_LINE.match(line) and i > header_lines + 1:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    if longest >= MAX_QUOTE_LINES:
        problems.append(f"{longest} 行続く引用のブロックがある（長い引用の疑い）")
    for p in paragraphs(text):
        if len(p) >= MAX_ENGLISH_CHARS and len(JAPANESE.findall(p)) < len(p) * 0.05:
            problems.append(f"日本語をほとんど含まない {len(p)} 文字の段落がある（長い引用の疑い）")
            break
    return problems


def check_rows(rows: list[dict], terms: list[str], overrides: dict) -> list[str]:
    """発言ごとに疑いの検査を行い、問題を発言の uuid と時刻つきで返す。"""
    problems = []
    # 公開ログへの変換と同じく、途中に届いた発言と同じ発言の通常の行は出力されないので、検査しない
    queued_sources = export_log.queued_source_uuids(rows)
    for d in rows:
        if d.get("type") == "user" and d.get("uuid") and d["uuid"] in queued_sources:
            continue
        o = override_for(d, overrides)
        approved = bool(o.get("approve"))
        # approve_tokens で外せるのは、ハッシュが一致する高エントロピーの文字列だけ
        tokens = frozenset(o.get("approve_tokens") or {})
        text = export_log.convert_records([d], "", terms, include_tools=False, header=[])
        if text.strip() == "#":
            continue  # 公開側に出ない行
        for p in check(text, [], header_lines=0, approved_tokens=tokens):
            if approved and p.endswith("（長い引用の疑い）"):
                continue  # approve で外せるのは、長い引用・長文の疑いだけ（個人情報・キーの検査は外せない）
            problems.append(f"{p}（識別子 {row_id(d)}、{d.get('timestamp')}）")
    return problems


# ---- git ----

def git(repo: Path, *args: str, check_: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], check=check_, capture_output=True, text=True)


def published_refs(repo: Path, branch: str) -> list[str]:
    """公開済みとみなす追跡参照（origin の作業ブランチと main のうち、ローカルにあるもの）。

    どちらか一方から辿れるコミットは公開済みとみなす。作業ブランチの追跡参照だけを基準にすると、
    前の PR のマージでリモートのブランチが消えた後も古い参照が残っている場合に、main に入った
    マージのコミットを未 push と誤って判定する（第 30〜32 回に start が止まった原因。T-0027 の 1）。"""
    refs = []
    for ref in (f"origin/{branch}", "origin/main"):
        if git(repo, "rev-parse", "--verify", "-q", ref, check_=False).returncode == 0:
            refs.append(ref)
    return refs


def unpushed_commits(repo: Path, branch: str) -> list[str]:
    """公開済みの参照（published_refs）のどれからも辿れないコミット。"""
    refs = published_refs(repo, branch)
    return git(repo, "rev-list", "HEAD", *(["--not", *refs] if refs else [])).stdout.split()


def unpushed_non_log_commits(repo: Path, branch: str) -> list[str]:
    """まだ push していないコミットのうち、logs/ 以外のファイルを変えたもの（マージコミットは第一親との差分）。"""
    out = []
    for c in unpushed_commits(repo, branch):
        # -z で、日本語などをエスケープしない実際のパスを得る（エスケープされると logs/ で始まらなくなる）
        names = [x for x in git(repo, "diff-tree", "-z", "--no-commit-id", "--name-only", "-r", "--root",
                                "--no-renames", "-m", "--first-parent", c).stdout.split("\0") if x]
        if any(not n.startswith("logs/") for n in names):
            out.append(c)
    return out


def unpushed_log_versions(repo: Path, branch: str) -> list[tuple[str, str, str]]:
    """まだ push していないコミットに含まれる logs/ のファイルの版を、(コミット, パス, 中身) で返す。

    公開済みの版と同じ中身でも、パスが新しいもの（名前を変えたファイル）は返す（ファイル名を検査するため）。"""
    out = []
    def blobs(rev: str) -> dict[str, str]:
        """その時点の logs/ の各ファイルの blob（マージコミットでも、その時点の版を見るため木から読む）。"""
        # -z で、日本語などをエスケープしない実際のパスを得る
        ls = git(repo, "ls-tree", "-r", "-z", rev, "--", "logs/", check_=False).stdout
        return {e.split("\t", 1)[1]: e.split()[2] for e in ls.split("\0") if "\t" in e}

    seen = set()  # 公開済みの版（パスと中身の組）は検査しない
    for ref in published_refs(repo, branch):
        seen |= set(blobs(ref).items())
    for c in unpushed_commits(repo, branch):
        for path, blob in blobs(c).items():
            if (path, blob) in seen:
                continue
            seen.add((path, blob))
            out.append((c, path, git(repo, "cat-file", "blob", blob).stdout))
    return out


def undo_last_commit(repo: Path) -> None:
    """直前のコミットを取り消す（変更は作業ツリーとインデックスに残す）。最初のコミットでもよい。"""
    if git(repo, "rev-parse", "--verify", "-q", "HEAD~1", check_=False).returncode == 0:
        git(repo, "reset", "-q", "--soft", "HEAD~1")
    else:
        git(repo, "update-ref", "-d", "HEAD")


def commit_and_push(repo: Path, paths: list[str], message: str, verify=None) -> str:
    """paths だけをコミットし、今の作業ブランチを push する。main には push しない。

    verify（中身を受け取り、問題の一覧を返す関数）を渡すと、push の前に、まだ push していない
    すべてのコミットの logs/ の版を検査し、問題があれば push しない（作り直した最新の版だけでなく、
    送る履歴も検査する）。push に失敗したら、この呼び出しで作ったコミットを取り消す
    （未 push のログのコミットを積み残さない。次の sync が作り直す）。
    """
    branch = git(repo, "branch", "--show-current").stdout.strip()
    if branch in ("", "main", "master"):
        raise SystemExit(f"{repo}: 作業ブランチではない（{branch or 'detached'}）ので push しない")
    git(repo, "add", "--", *paths)
    changed = git(repo, "diff", "--cached", "--quiet", "--", *paths, check_=False).returncode != 0
    if changed:
        # ほかにステージした変更があっても、paths だけをコミットする
        git(repo, "commit", "-q", "-m", message, "--only", "--", *paths)
    # 変更がなくても、前に push に失敗したコミットが残っていれば push する
    remote = git(repo, "rev-parse", "--verify", "-q", f"origin/{branch}", check_=False).stdout.strip()
    if remote and git(repo, "rev-parse", "HEAD").stdout.strip() == remote:
        return f"{repo.name}: 変更なし"
    if verify is not None:
        # 先に、まだ push していない logs/ の全版とファイル名を検査する
        versions = unpushed_log_versions(repo, branch)
        bad = [f"{c[:7]} の {path}: {p}" for c, path, text in versions for p in verify(text)]
        # ファイル名も公開されるので検査する（今の版では消したファイルの名前も、履歴には残る）
        bad += [f"{c[:7]} のファイル名 {path}: {p}" for c, path, _ in versions
                for p in check(path, verify_terms(verify), header_lines=-2)]
        if bad:
            if changed:
                undo_last_commit(repo)
            raise SystemExit(f"{repo}: まだ push していない履歴に、公開できない版がある（push しない）。"
                             "その版を含むコミットを作り直してから sync をやり直すこと:\n" + "\n".join(bad))
        # ログ以外の未 push のコミット（ふだんの作業）は、sync では送らない。ふだんの push で先に送る。
        # この案内は、上の履歴の検査に通った後だけ出す（ふだんの push でも、未 push のログの履歴は公開されるため）
        other = unpushed_non_log_commits(repo, branch)
        if other:
            if changed:
                undo_last_commit(repo)
            raise SystemExit(f"{repo}: logs/ 以外を変えた未 push のコミットがあるので、ログだけを送れない（push しない）。"
                             "作業のコミットを確かめて、ふだんの push で先に送ってから sync をやり直すこと: "
                             + ", ".join(c[:7] for c in other))
    for wait in (0, 2, 4, 8, 16):
        time.sleep(wait)
        r = git(repo, "push", "-q", "-u", "origin", branch, check_=False)
        if r.returncode == 0:
            return f"{repo.name}: {branch} に push した"
    if changed:
        undo_last_commit(repo)
    raise SystemExit(f"{repo}: push に失敗した（この同期のコミットは取り消した）: {r.stderr.strip()}")


def verify_terms(verify) -> list[str]:
    return getattr(verify, "terms", [])


def history_problems(terms: list[str], checked: set[str] = frozenset()):
    """送る履歴の検査。すべての検査（長い引用の疑いを含む）を行う。

    checked（発言ごとの確認の結果つきで検査を通した、今の版の中身）と同じ版は検査済みとして除く。
    それ以外の版で、確認済みの長い引用が引っかかる場合は、その版を含むコミットを作り直す。
    """
    def verify(text: str) -> list[str]:
        return [] if text in checked else check(text, terms)
    verify.terms = terms
    return verify


HEADING = re.compile(r"^## (ユーザー|Claude)（([^、）]+)", re.M)


def message_blocks(text: str) -> list[tuple[str, str, str]]:
    """ログを発言ごとに分け、(発言者, 時刻, 本文) の一覧にする。"""
    marks = list(HEADING.finditer(text))
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        line_end = text.find("\n", m.start())
        body = text[line_end + 1:end].strip() if 0 <= line_end < end else ""
        out.append((m.group(1), m.group(2), body))
    return out


def lost_messages(old: str, new: str) -> list[str]:
    """既存のログにあって、作り直した版にない発言（発言者と時刻）の一覧。

    本文まで比べる（同じ秒の発言が別の本文に置き換わった場合も見つける。後ろに続きが加わっただけなら残ったとみなす）。同じ秒に同じ発言者の
    発言が複数あることもあるので、件数で比べる。伏せ字の語句の追加や要約への置き換えで本文が
    変わった場合も、ここに挙がる（意図した変更なら --allow-loss を付ける）。
    """
    lost = _lost_counter(old, new)
    return [f"{who}（{ts}）" + (f" × {n}" if n > 1 else "") for (who, ts), n in lost.items()]


def missing_messages(old: str, new: str) -> list[str]:
    """既存のログにあって、作り直した版では発言そのもの（発言者と時刻）がなくなったものの一覧。

    lost_messages のうち、ここに挙がらないものは、発言は残っているが本文が変わったもの
    （伏せ字の語句の追加や、要約への置き換えなど）である。
    """
    keys = lambda t: Counter((w, ts) for w, ts, _ in message_blocks(t))
    gone = keys(old) - keys(new)
    return [f"{who}（{ts}）" + (f" × {n}" if n > 1 else "") for (who, ts), n in gone.items()]


def _lost_counter(old: str, new: str) -> Counter:
    """既存の版の発言のうち、作り直した版に対応する発言がないものを、(発言者, 時刻) ごとに数える。

    本文が同じか、後ろに続きが加わっただけのもの（非公開側では、発言の後にツールの結果が続く）を
    残ったとみなす。同じ秒の複数の発言を正しく対応づけるため、まず完全に一致するものを対応づけ、
    残りを、長い本文から順に「後ろに続きが加わったもの」として対応づける。
    """
    remaining = message_blocks(new)
    unmatched = []
    for blk in message_blocks(old):
        if blk in remaining:
            remaining.remove(blk)
        else:
            unmatched.append(blk)
    lost = Counter()
    for who, ts, body in sorted(unmatched, key=lambda b: len(b[2]), reverse=True):
        hit = next((i for i, (w, t, b) in enumerate(remaining) if (w, t) == (who, ts) and b.startswith(body)), None)
        if hit is None:
            lost[(who, ts)] += 1
        else:
            remaining.pop(hit)
    return lost


def body_changed(old: str, new: str) -> bool:
    """発言そのものは残っているが、本文が変わったものが一件でもあるか。"""
    keys = lambda t: Counter((w, ts) for w, ts, _ in message_blocks(t))
    gone = keys(old) - keys(new)
    return any(n > gone[k] for k, n in _lost_counter(old, new).items())


def load_registry() -> list[str]:
    return json.loads(SESSIONS.read_text(encoding="utf-8")) if SESSIONS.exists() else []


def load_sessions() -> set[str]:
    """登録簿のうち、この研究の会話と確かめたセッション。"""
    return {x for x in load_registry() if not x.startswith("!")}


def load_excluded() -> set[str]:
    """登録簿のうち、この研究の会話ではないと確かめたセッション（「!」を付けて書く）。"""
    return {x[1:] for x in load_registry() if x.startswith("!")}


def current_session(explicit: str | None = None) -> str | None:
    """今のセッションの ID（--session-id か、環境変数 CLAUDE_CODE_SESSION_ID）。

    更新時刻などから推測はしない（別のセッションを取り違えるおそれがあるため）。分からなければ None。
    """
    return explicit or os.environ.get("CLAUDE_CODE_SESSION_ID") or None


def register_session(explicit: str | None = None) -> tuple[set[str], str | None]:
    """今のセッションを登録簿に加え、(登録簿, 今のセッションの ID) を返す。"""
    known = load_sessions()
    sid = current_session(explicit)
    if sid and sid not in known:
        known.add(sid)
        SESSIONS.write_text(json.dumps(sorted(set(load_registry()) | {sid}), indent=2) + "\n", encoding="utf-8")
    return known, sid


# ---- コマンド ----

def log_name(state: dict) -> str:
    """ログのファイル名。日付・番号・話題を検証し、logs/ の外を指さないことを確かめる。"""
    if not valid_date(str(state.get("date"))) or not isinstance(state.get("number"), int) \
            or not SLUG.fullmatch(str(state.get("slug"))):
        raise SystemExit(f"logs/live.json の日付・番号・話題が不正: {state!r}")
    name = f"{state['date']}_{state['number']:02d}_{state['slug']}.md"
    if (REPO / "logs" / name).resolve().parent != (REPO / "logs").resolve():
        raise SystemExit(f"ログのファイル名が logs/ の外を指す: {name!r}")
    return name


def load_redactions() -> list[str]:
    """伏せ字の語句（非公開リポジトリの redactions.txt）。ないときは照合できないので止める。"""
    path = PRIVATE / "redactions.txt"
    if not path.exists():
        raise SystemExit(f"{path} がないので、伏せ字の照合ができない（非公開リポジトリを用意してから実行する）")
    return export_log.load_terms(path)


def private_settings() -> list[str]:
    return [p.name for p in (PRIVATE / "redactions.txt", OVERRIDES, SESSIONS) if p.exists()]


# cmd_sync の終了コード：検査で保留した、保存済みの発言が消える（記録の消失）、保存済みの発言の本文が変わる
HELD, LOSS, CHANGED = 1, 2, 3


def cmd_start(a) -> int:
    if not SLUG.fullmatch(a.slug):
        raise SystemExit(f"--slug は英小文字・数字とハイフンだけにする: {a.slug!r}")
    if not valid_date(a.date or a.since[:10]):
        raise SystemExit(f"--date（または --since の日付）は YYYY-MM-DD にする: {a.date or a.since[:10]!r}")
    try:
        since_dt = export_log.parse_time(a.since)
    except ValueError:
        raise SystemExit(f"--since は ISO 8601 の時刻（例: 2026-10-06T03:58:00Z）にする: {a.since!r}")
    state = {"number": a.number, "slug": a.slug, "title": a.title, "since": a.since,
             "date": a.date or a.since[:10]}
    # 公開側の logs/live.json に書く前に、新しい回の情報を検査する（検査に当たれば書かない）。
    # 前の回を閉じる前に行う（新しい回の情報が検査に当たったのに、前の回だけが閉じられることを避ける）
    terms = load_redactions()
    meta = json.dumps(state, ensure_ascii=False, indent=2)
    # 長い引用の疑いも含めて、すべての検査を行う。タイトルは JSON にする前の形でも検査する
    # （JSON では改行が \n に変わり、引用の行が続くことを見落とすため）
    bad = check(meta, terms, header_lines=-2) + check(a.title, terms, header_lines=-2)
    if bad:
        raise SystemExit("回の情報（タイトルなど）が検査に当たったので、logs/live.json に書かない:\n" + "\n".join(bad))
    if STATE.exists():
        prev = json.loads(STATE.read_text(encoding="utf-8"))
        if prev.get("number") == a.number:
            # 同じ回のやり直しは、回の情報が一致するときだけ許す（別名のログを作って、保存済みの発言を見失わない）
            same = {k: prev.get(k) for k in ("slug", "title", "since", "date")}
            if same != {k: state[k] for k in same}:
                raise SystemExit(f"logs/live.json に同じ番号（第 {a.number:02d} 回）の別の情報がある。"
                                 f"回の情報を合わせるか、logs/live.json を確かめて直すこと: {same}")
            if prev.get("until"):
                raise SystemExit(f"第 {a.number:02d} 回は既に閉じている（until: {prev['until']}）")
            return cmd_sync(a)
        if export_log.parse_time(prev["since"]) >= since_dt:
            raise SystemExit(f"新しい回の始め（{a.since}）が、前の回の始め（{prev['since']}）より後でない")
        if prev.get("number") != a.number:
            # 前の回の最後の発言（最後の同期の後に書いた文）を残してから閉じる。同期が成功するまで
            # 新しい回の状態は書かないので、失敗しても start をやり直せば同期を再試行する
            if prev.get("until") and prev["until"] != a.since:
                raise SystemExit(f"前の回の終わり（until: {prev['until']}）と、新しい回の始め（--since: {a.since}）が"
                                 "一致しない。間の発言がどちらのログにも入らなくなるので、区切りを決め直すこと"
                                 "（logs/live.json の until を直すか、--since を合わせる）")
            prev["until"] = a.since
            STATE.write_text(json.dumps(prev, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"前の回（第 {prev['number']:02d} 回）のログを、{a.since} までで閉じる")
            r = cmd_sync(a)
            if r in (HELD, CHANGED):
                raise SystemExit("前の回のログの同期が、検査の保留か、保存済みの本文の変更で止まったので、"
                                 "新しい回を始めない（前の回のログと公開済みの履歴を確かめてから start をやり直す）")
            if r == LOSS:
                # 前の回のセッション記録が失われている。保存済みのログはそのまま残し、回収できなかった
                # 末尾があることを知らせて、新しい回を始める（--allow-loss で消すことはしない）
                print(f"注意：前の回（第 {prev['number']:02d} 回）のセッション記録が失われているので、"
                      "保存済みのログをそのまま残す。最後の同期の後の発言は回収できなかった", file=sys.stderr)
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {STATE.relative_to(REPO)}（ログ: logs/{log_name(state)}）")
    return cmd_sync(a)


def cmd_sync(a) -> int:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    terms = load_redactions()
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    untimed = []
    known, sid = register_session(getattr(a, "session_id", None))
    unconfirmed, broken = [], []
    raw = collect(a.projects, state["since"], state.get("until"), known_sessions=known, untimed=untimed,
                  excluded_sessions=load_excluded(), unconfirmed=unconfirmed, broken=broken)
    rows = apply_overrides(raw, overrides)
    name = log_name(state)
    public = export_log.convert_records(rows, state["title"], terms, include_tools=False, show_time=True,
                                        header=PUBLIC_HEADER)
    # 非公開側：ツールの呼び出しを含み、置き換えを当てない記録
    full = export_log.convert_records(raw, state["title"] + "（ツールの呼び出しを含む記録）", terms, show_time=True)
    # セッション記録が失われる（コンテナの作り直しなど）と、作り直した版から保存済みの発言が消える。
    # その場合は上書きしない（意図した置き換えなら、--allow-loss を付けて実行する）
    lost, missing, changed = [], [], False
    for path, new in ((REPO / "logs" / name, public), (PRIVATE / "logs" / name, full)):
        if path.exists():
            old = path.read_text(encoding="utf-8")
            lost += [f"{path.parent.parent.name}: {m}" for m in lost_messages(old, new)]
            missing += missing_messages(old, new)
            changed = changed or body_changed(old, new)
    if lost and not a.allow_loss:
        if not changed:
            print("作り直した版から、保存済みの発言が消える（セッション記録が失われた可能性がある）。上書きしない:",
                  file=sys.stderr)
        else:
            print("保存済みの発言の本文が変わる（伏せ字の語句の追加や要約への置き換えなど）。上書きしない。"
                  "意図した変更なら --allow-loss を付けて実行し、公開済みの履歴に直す前の版が残っていないか確かめること:",
                  file=sys.stderr)
        for m in lost[:20]:
            print(f"- {m}", file=sys.stderr)
        # 本文が変わった発言が一件でもあれば CHANGED（消えた発言と同時でも、次の回を始めない）
        return CHANGED if changed else LOSS
    (PRIVATE / "logs").mkdir(exist_ok=True)
    (PRIVATE / "logs" / name).write_text(full, encoding="utf-8")

    # 伏せ字の照合はログの全体で、疑いの検査は発言ごとに行う
    problems = [p for p in check(public, terms) if p.startswith("伏せ字")] + check_rows(rows, terms, overrides)
    if not any(export_log.is_output_user(d) or export_log.is_output_queued(d) for d in rows):
        problems.append("この回のユーザーの発言が一件も集まらない（記録のディレクトリかセッションの確認に問題がある"
                        "可能性がある。--since と、環境変数 CLAUDE_CODE_SESSION_ID を確かめる）")
    if broken:
        problems.append(f"セッション記録に読めない行がある（{', '.join(broken[:5])}）。記録が欠けたまま公開しない")
    if unconfirmed:
        ids = sorted({d["sessionId"] for d in unconfirmed})
        problems.append(f"確かめられていないセッションの発言が {len(unconfirmed)} 件ある（セッション {', '.join(ids)}）。"
                        "この研究の会話なら ID を、そうでなければ「!」を付けた ID を、非公開側の live-sessions.json に加える")
    if not sid:
        problems.append("今のセッションの ID が分からない（環境変数 CLAUDE_CODE_SESSION_ID がない）。"
                        "--session-id で明示すること")
    if untimed:
        problems.append(f"時刻かセッションのない発言が {len(untimed)} 件あり、どの回のものか判定できない"
                        f"（識別子 {', '.join(row_id(d) for d in untimed[:5])}）")
    # ファイル名と logs/live.json も公開するので、同じく照合する
    meta = name + "\n" + STATE.read_text(encoding="utf-8")
    if not SLUG.fullmatch(state["slug"]):
        problems.append("話題（slug）に英小文字・数字・ハイフン以外の文字がある")
    problems += [f"ファイル名か logs/live.json に{p}" for p in check(meta, terms, header_lines=-2)]
    problems += [f"タイトルに{p}" for p in check(state["title"], terms, header_lines=-2)]
    if problems:
        (PRIVATE / "held").mkdir(exist_ok=True)
        (PRIVATE / "held" / name).write_text(public, encoding="utf-8")
        print(f"公開を保留した（非公開リポジトリの held/{name}）。確認してから公開すること:", file=sys.stderr)
        for p in problems:
            print(f"- {p}", file=sys.stderr)
        if not a.no_push:
            print(commit_and_push(PRIVATE, [f"logs/{name}", f"held/{name}", *private_settings()],
                                  f"対話ログ（第 {state['number']:02d} 回）の保留"))
        return 1

    (REPO / "logs" / name).write_text(public, encoding="utf-8")
    print(f"wrote logs/{name}（{sum(1 for l in public.splitlines() if l.startswith('## '))} 件の発言、検査: 問題なし）")
    if a.no_push:
        return 0
    msg = f"対話ログ（第 {state['number']:02d} 回）の更新"
    # 非公開側を先に保存する（公開側だけが残ることを避ける）。どちらかが失敗したら、
    # 原因を直して sync をやり直せば、未 push のコミットも送られる
    # 伏せ字と置き換えの設定（redactions.txt、log-overrides.json）も、公開側より先に非公開側へ保存する。
    # 作業環境を失っても、リモートの設定で同じログを作り直せるようにするため
    print(commit_and_push(PRIVATE, [f"logs/{name}", *private_settings()], msg))
    print(commit_and_push(REPO, [f"logs/{name}", "logs/live.json"], msg, verify=history_problems(terms, {public})))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--projects", type=Path, default=PROJECTS, help="セッション記録のディレクトリ")
    p.add_argument("--no-push", action="store_true", help="書き出しと検査だけを行い、コミット・push しない")
    p.add_argument("--allow-loss", action="store_true", help="作り直した版から保存済みの発言が消えても上書きする")
    p.add_argument("--session-id", help="今のセッションの ID（環境変数 CLAUDE_CODE_SESSION_ID がないとき）")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start", help="回の情報を logs/live.json に書き、同期する")
    s.add_argument("--number", type=int, required=True)
    s.add_argument("--slug", required=True, help="ファイル名の話題（英小文字とハイフン）")
    s.add_argument("--title", required=True)
    s.add_argument("--since", required=True, help="その回の最初の発言の時刻（UTC、ISO 8601）")
    s.add_argument("--date", help="ファイル名の日付（省略時は since の日付）")
    s.set_defaults(func=cmd_start)
    sub.add_parser("sync", help="ログを作り直し、検査して push する").set_defaults(func=cmd_sync)
    a = p.parse_args()
    # 状態の読み取りから両リポジトリへの push の完了までを、作業ディレクトリに共通のロックで守る
    # （並行した二つの応答の sync が、古い収集結果で新しいログを上書きしないように）
    with exclusive_lock(LOCK):
        return a.func(a)


if __name__ == "__main__":
    raise SystemExit(main())
