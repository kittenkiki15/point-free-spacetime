#!/usr/bin/env python3
"""Claude Code のセッション記録（JSONL）を、公開用の Markdown に変換する。

使い方:
    python3 tools/export_log.py <セッション.jsonl> <出力.md> [--title タイトル] [--redact-file ファイル] [--since 時刻] [--until 時刻]

- ユーザーの発言と Claude の返答を本文として出力する。
- ツールの呼び出しと結果は、折りたたみ（<details>）にして要点だけ残す。
  入力はシェルのコマンドだけを残し、ファイルへの書き込み内容などの本文は省く。
  結果は先頭の一部だけを残す。
- システムが付加した情報（環境情報、システムプロンプトなど）は出力しない。
- メールアドレス、組織 ID、API キーらしき文字列などは伏せ字にする。
- --redact-file で指定したファイル（1 行 1 語句）の語句も伏せ字にする。
  個人情報の断片など、公開リポジトリに書けない語句は非公開リポジトリの
  redactions.txt に置き、それを指定する。
  変換後も必ず目視で確認すること。
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ツール結果として残す最大文字数
MAX_RESULT_CHARS = 1500

REDACTIONS = [
    # メールアドレス
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[メールアドレス]"),
    # 秘密鍵
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S), "[秘密情報]"),
    # API キー・トークンらしき文字列
    # （OpenAI・Anthropic、GitHub、AWS のアクセスキー ID、Google、Slack）
    (re.compile(
        r"\b(sk-[A-Za-z0-9_-]{16,}"
        r"|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"
        r"|(?:AKIA|ASIA)[0-9A-Z]{16}"
        r"|AIza[0-9A-Za-z_-]{35}"
        r"|xox[abprs]-[A-Za-z0-9-]{10,})"
    ), "[秘密情報]"),
    # AWS のシークレットアクセスキー（キー名に続く 40 文字）
    (re.compile(r"(?i)(aws_secret_access_key\s*[=:]\s*)[\"']?[A-Za-z0-9/+=]{40}[\"']?"), r"\1[秘密情報]"),
    # UUID（組織 ID やセッション ID など）
    (re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.IGNORECASE), "[ID]"),
    # セッション URL
    (re.compile(r"https://claude\.ai/code/session_[A-Za-z0-9]+"), "[セッション URL]"),
]


def load_terms(path: Path | None) -> list[str]:
    if path is None:
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    terms = [t.strip() for t in lines if t.strip() and not t.startswith("#")]
    return sorted(terms, key=len, reverse=True)  # 長い語句から置き換える


def redact(text: str, terms: list[str] = ()) -> str:
    for term in terms:
        text = re.sub(re.escape(term), "[伏せ字]", text, flags=re.IGNORECASE)
    for pattern, repl in REDACTIONS:
        text = pattern.sub(repl, text)
    return text


def truncate(text: str, limit: int = MAX_RESULT_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n…（以下 {len(text) - limit} 文字を省略）"


def fence(text: str) -> str:
    """中身に含まれるバッククォートより長いフェンスで囲む。"""
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    ticks = "`" * max(3, longest + 1)
    return f"{ticks}text\n{text}\n{ticks}"


# Claude Code がユーザーの発言として記録する、システム由来の文字列
SYSTEM_MESSAGE = re.compile(
    r"^<(command-name|command-message|command-args|local-command-stdout|local-command-stderr"
    r"|local-command-caveat|system-reminder|task-notification|bash-input|bash-stdout|bash-stderr)>"
)
SYSTEM_REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)


def user_text(text: str) -> str | None:
    """ユーザーの発言を返す。システム由来の文字列なら None を返す。"""
    text = SYSTEM_REMINDER.sub("", text).strip()
    if not text or SYSTEM_MESSAGE.match(text):
        return None
    return text


def demote_headings(text: str) -> str:
    """発言者の見出し（##）と区別するため、本文中の見出しを 2 段下げる（コードブロック内は除く）。"""
    lines, in_code = [], False
    for line in text.splitlines():
        if re.match(r"\s*(```|~~~)", line):
            in_code = not in_code
        elif not in_code and re.match(r"#{1,4} ", line):
            line = "##" + line
        lines.append(line)
    return "\n".join(lines)


def result_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for c in content:
            if c.get("type") == "text":
                parts.append(c.get("text", ""))
            else:
                parts.append(f"[{c.get('type')}]")
        return "\n".join(parts)
    return str(content)


def tool_summary(block: dict) -> str:
    name = block.get("name", "?")
    inp = block.get("input", {}) or {}
    desc = inp.get("description") or inp.get("query") or inp.get("url") or inp.get("file_path") or ""
    return f"{name}: {desc}".rstrip(": ")


def tool_detail(block: dict) -> str:
    """ツール入力のうち、公開してよい要点だけを返す。

    シェルのコマンドは再現のために残す（長いものは切り詰める）。
    ファイルへの書き込み内容など、それ以外の入力の本文は出力しない。
    """
    inp = block.get("input", {}) or {}
    if "command" in inp:
        return truncate(inp["command"])
    keys = ", ".join(sorted(inp))
    return f"（入力の本文は省略。項目: {keys}）"


def parse_time(text: str) -> datetime:
    """ISO 8601 の時刻を、タイムゾーン付きの日時として解析する。

    小数秒の有無や末尾の Z・+00:00 の違いによらず比較できるようにする。
    タイムゾーンのない時刻は UTC とみなす。
    """
    dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def convert(jsonl_path: Path, title: str, terms: list[str] = (), since: str | None = None,
            until: str | None = None) -> str:
    """since・until（ISO 8601 の時刻、例: 2026-09-25T11:02:28Z）で出力する期間を絞る。

    since 以上、until 未満の記録だけを出力する。期間を指定したときは、時刻のない発言は
    どの回のものか判定できないので出力せず、標準エラーに警告を出す。
    """
    out = [f"# {title}", "", "> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。",
           "> ツールの呼び出しは折りたたんで表示し、個人情報などは伏せ字にしています。", ""]
    pending = {}  # tool_use_id -> 見出し
    since_dt = parse_time(since) if since else None
    until_dt = parse_time(until) if until else None

    untimed = []  # 期間を指定したのに時刻がなく、除外した記録の行番号

    for lineno, line in enumerate(jsonl_path.read_text(encoding="utf-8").splitlines(), 1):
        d = json.loads(line)
        kind = d.get("type")
        msg = d.get("message")
        if kind not in ("user", "assistant") or not isinstance(msg, dict) or d.get("isSidechain") or d.get("isMeta"):
            continue
        if since_dt or until_dt:
            # 時刻がない記録は、どの回のものか判定できないので出力しない（警告する）
            if not d.get("timestamp"):
                untimed.append(lineno)
                continue
            ts = parse_time(d["timestamp"])
            # since 以上、until 未満の記録だけを出力する
            if (since_dt and ts < since_dt) or (until_dt and ts >= until_dt):
                continue
        content = msg.get("content")

        if kind == "user":
            if isinstance(content, str):
                text = user_text(content)
                if text:
                    out += ["## ユーザー", "", demote_headings(text), ""]
                continue
            for c in content:
                if c.get("type") == "text":
                    text = user_text(c.get("text", ""))
                    if text and text.startswith("[Request interrupted"):
                        out += ["*（ユーザーがツールの実行を中断）*", ""]
                    elif text:
                        out += ["## ユーザー", "", demote_headings(text), ""]
                elif c.get("type") == "tool_result":
                    head = pending.pop(c.get("tool_use_id"), "ツール")
                    body = truncate(result_text(c.get("content")).strip())
                    status = "（エラー）" if c.get("is_error") else ""
                    out += [f"<details><summary>結果{status}: {head}</summary>", "", fence(body), "", "</details>", ""]
        else:
            for c in content or []:
                t = c.get("type")
                if t == "text" and c.get("text", "").strip():
                    out += ["## Claude", "", demote_headings(c["text"].strip()), ""]
                elif t == "tool_use":
                    head = tool_summary(c)
                    pending[c.get("id")] = head
                    out += [f"<details><summary>ツール: {head}</summary>", "", fence(tool_detail(c)), "", "</details>", ""]
    if untimed:
        print(f"警告: 時刻（timestamp）のない発言が {len(untimed)} 件あり、--since・--until で期間を判定できないため"
              f"出力しませんでした（{jsonl_path} の {', '.join(map(str, untimed))} 行目）。"
              "必要なら内容を確認してください。", file=sys.stderr)
    return redact("\n".join(out).rstrip() + "\n", terms)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("jsonl", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--title", default="対話ログ")
    p.add_argument("--redact-file", type=Path, help="伏せ字にする語句のファイル（1 行 1 語句）")
    p.add_argument("--since", help="この時刻（ISO 8601）以降の記録だけを出力する。同じセッション記録を複数回に分けて書き出すときに使う")
    p.add_argument("--until", help="この時刻（ISO 8601）より前の記録だけを出力する。次の回の最初の発言の時刻を指定する")
    a = p.parse_args()
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(convert(a.jsonl, a.title, load_terms(a.redact_file), a.since, a.until), encoding="utf-8")
    print(f"wrote {a.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
