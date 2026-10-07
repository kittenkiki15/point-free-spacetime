"""ID（定義・前提・予想・結果・タスク・未解決の点）の依存関係と参照箇所の索引を、ファイルから毎回作る。

索引は RDF のトリプル（主語・述語・目的語）として組み立て、そこから逆引き・JSON・Turtle を出力する
（第 31 回にユーザーと決めた。T-0025 の 4）。索引のファイルはコミットしない。

- 構造：各 ID のファイルの表（状態・層・依存する ID・目標の ID・参照する ID など。LITERAL_ROWS などの対応表に
  ある項目）と名前。「関係する予想・結果」は「依存する ID」の逆向きと一致することを test_framework.py で検査して
  いるので、取り込まない（pfs:dependsOn を逆にたどれば得られる）。
- 言及：Git の管理下のファイルと、無視の設定に当たらない未追跡のファイルのうち、`logs/` を除く Markdownと、`lean/`・`sim/` のコード（同じ条件）にある ID の言及。言及ごとに、
  言及元のファイル・節・行と、リンクかどうかを持つノード（pfs:Mention）を作る。
- 循環の検査に使う意味上の依存は「依存する ID」（pfs:dependsOn）だけで、参照・言及は使わない。

Markdown の読み取りは、このリポジトリで使っている書き方に限る（第 31 回にユーザーと決めた。PR #72 のレビュー）。
読むのは、インラインのリンク（タイトル付きを含む）、囲み型のコードブロック、インラインのコード、見出しである。
参照形式のリンク（使っていないことを検査する）、字下げ型のコードブロック、自動リンク（<https://…>）、HTML は
扱わない。構文解析器への置き換えは T-0026 の論点とする。

語彙（pfs:）の定義は tools/pfs.ttl にある。IRI の基底は公開リポジトリの main のファイルの URL で、
このファイルの BASE と、tools/pfs.ttl の @prefix pfs: の 2 か所にある。変えるときは両方を改める（食い違うと、
出力の語彙が pfs.ttl の定義と合わなくなり、test_id_index.py の語彙の検査が失敗する）。

使い方:
    python3 tools/id_index.py refs D-0002   # D-0002 を指す依存・参照と、言及の箇所を表示する
    python3 tools/id_index.py --json        # 索引を JSON で標準出力に書く
    python3 tools/id_index.py --ttl         # 索引を Turtle（RDF）で標準出力に書く
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deps_graph  # noqa: E402

ROOT = deps_graph.ROOT
BASE = "https://github.com/kittenkiki15/point-free-spacetime/blob/main/"
REPO_URL = "https://github.com/kittenkiki15/point-free-spacetime/"
PFS = BASE + "tools/pfs.ttl#"
PREFIXES = {
    "pfs": PFS,
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}
DIRS = {"D": "definitions", "A": "assumptions", "C": "conjectures", "R": "results", "T": "tasks", "Q": "questions"}
CLASSES = {"D": "Definition", "A": "Assumption", "C": "Conjecture", "R": "Result", "T": "Task", "Q": "Question"}
# ID の前後の境界は ASCII の英数字で判定する（\b は日本語の文字も単語の文字とみなし、「予想C-0001を」の
# ような日本語に接した ID を見落とすため。PR #72 のレビュー）
ANY_ID = re.compile(r"(?<![A-Za-z0-9_])([DACRTQ]-\d{4})(?![A-Za-z0-9_])")
# リンク先が ID のファイル（…/X-NNNN.md、節への印を含んでよい）であるか
TARGET_ID = re.compile(r"(?:^|/)([DACRTQ]-\d{4})\.md(?:#.*)?$")
# Markdown のリンク。リンク先の後の任意のタイトル（[文字](path "タイトル")）と、<path> の形も読む（PR #72 のレビュー）。
# タイトルは "…"・'…'・(…) のどれでもよい。読むのはインラインのリンクだけで、参照形式のリンク（[文字][名前] と [名前]: path）は使わない約束にする
# （logs/ を除く Markdown に参照形式のリンクの定義がないことを、tools/tests/test_id_index.py で検査する）
LINK = re.compile(r"""\[([^\]]*)\]\(<?([^)\s>]*)>?(?:\s+(?:"[^"]*"|'[^']*'|\([^)]*\)))?\)""")
FENCE = re.compile(r" {0,3}(`{3,}|~{3,})(.*)$")
CODE_DIRS = {"lean": "*.lean", "sim": "*.py"}

# 表の行 → 述語。値の読み方は、ID（依存の行と同じ読み方。裸の ID も読む）・リンクの ID（リンクと「〜」の範囲だけ）・
# 文字列・リンク先（Issue や初出のまとめ）のどれか
ID_ROWS = {"依存する ID": "dependsOn", "目標の ID": "targets", "参照する ID": "refersTo"}
# 「前提のタスク」は裸の ID（例：T-0004、T-0023）で書くので、依存の行と同じく裸の ID も読む
BARE_ID_ROWS = {"前提のタスク": "prerequisite"}
LINK_ID_ROWS = {"関係する ID": "concerns", "親の ID": "parent",
                "割り当てたタスク": "assignedTask", "関連する予想": "relatedConjecture"}
LITERAL_ROWS = {"状態": "status", "層": "layer", "体系": "system", "確度": "confidence", "重要度": "importance",
                "検証費用": "verificationCost", "優先度": "priority", "検証方法": "verificationMethod",
                "種類": "resultKind", "検証": "verification", "段階": "stage", "追加した回": "addedIn",
                "解決した回": "resolvedIn"}
LINK_ROWS = {"初出": "introducedIn", "Issue": "issue"}


@dataclass(frozen=True)
class Mention:
    target: str   # 言及された ID
    source: str   # 言及元のファイル（リポジトリからの相対パス）
    line: int
    section: str  # 直前の見出し（コードでは空）
    linked: bool  # ID を表示文字にしたリンクか


def id_path(i: str) -> str:
    return f"{DIRS[i[0]]}/{i}.md"


def id_files() -> dict[str, Path]:
    """ID → ファイル（定義・前提・予想・結果・タスク・未解決の点）。"""
    files = {}
    for kind, d in DIRS.items():
        for f in sorted((ROOT / d).glob(f"{kind}-[0-9][0-9][0-9][0-9].md")):
            files[f.stem] = f
    return files


def section_body(text: str, heading: str):
    """見出し heading の行の次から、コードブロックの外にある次の「## 」の見出しの前までを返す（なければ None）。
    コードブロックの中の「## 」の行では止まらない（PR #72 のレビュー）。"""
    lines, out, inside, fence = text.splitlines(), [], False, None
    for line in lines:
        m = FENCE.match(line)
        if fence is None and m:
            fence = (m.group(1)[0], len(m.group(1)))
        elif fence and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] and not m.group(2).strip():
            fence = None
        elif fence is None and line.startswith("## "):
            if inside:
                break
            inside = line.rstrip() == heading
            continue
        if inside:
            out.append(line)
    return "\n".join(out) if inside or out else None


def without_code_blocks(text: str) -> str:
    """コードブロック（囲みの行を含む）を除いた本文を返す。"""
    out, fence = [], None
    for line in text.splitlines():
        m = FENCE.match(line)
        if fence is None and m:
            fence = (m.group(1)[0], len(m.group(1)))
        elif fence and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] and not m.group(2).strip():
            fence = None
        elif fence is None:
            out.append(line)
    return "\n".join(out)


def link_target_id(target: str):
    """リンク先が ID のファイルなら、その ID を返す。絶対 URL は、このリポジトリの URL のときだけ認める
    （外部のサイトの同じ名前のファイルを、ID へのリンクとみなさない。PR #72 のレビュー）。"""
    # スキームのある URL と、スキームを省いた URL（//host/…）は外部とみなす（このリポジトリの URL を除く）
    if (re.match(r"[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("//")) and not target.startswith(REPO_URL):
        return None
    m = TARGET_ID.search(target)
    return m.group(1) if m else None


def link_ids(value) -> list[str]:
    """ID のリンクの ID を現れた順に返し、続けて、リンクどうしの「X〜Y」の範囲の中の ID を返す
    （重複は除く。範囲の中の ID は、範囲を書いた位置ではなく最後に並ぶ）。裸の ID は読まない。
    ID はリンク先のファイルから読む（表示文字に説明を含むリンク [C-0001 の主張](../conjectures/C-0001.md) も
    C-0001 と読む。PR #72 のレビュー）。"""
    ids = []
    for m in LINK.finditer(value or ""):
        # リンク先のファイルの ID を正とする（表示の ID とリンク先の一致は、test_framework.py のリンクの検査で
        # 確かめる）。リンク先が ID のファイルでなければ、ID への関係とはみなさない（PR #72 のレビュー）
        i = link_target_id(m.group(2))
        if i:
            ids.append(i)
    # 「〜」で続く二つのリンクは範囲として展開する。両端の ID も、リンク先のファイルから読む（PR #72 のレビュー）
    links = list(LINK.finditer(value or ""))
    for a, b in zip(links, links[1:]):
        if (value[a.end():b.start()].strip() == "〜"):
            start, end = link_target_id(a.group(2)), link_target_id(b.group(2))
            if start and end and start[0] == end[0] and int(start[2:]) <= int(end[2:]):
                ids += [f"{start[0]}-{n:04d}" for n in range(int(start[2:]), int(end[2:]) + 1)]
    return list(dict.fromkeys(ids))


def table_rows(path: Path) -> dict[str, str]:
    """先頭の表（「| 項目 | ... |」）の行を、項目 → 値で返す。"""
    rows, started = {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| 項目 |"):
            started = True
            continue
        if started:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and not set(cells[0]) <= set("- "):
                rows[cells[0]] = cells[1]
    return rows


def structure() -> list[tuple[str, str, object]]:
    """各 ID のファイルの表と名前から作るトリプル（主語の ID、述語、目的語）。

    目的語は、ID（str で ID の形）、リンク先（("link", 相対パスか URL)）、文字列（("literal", 値)）のどれか。
    """
    triples = []
    for i, f in id_files().items():
        triples.append((i, "rdf:type", ("class", CLASSES[i[0]])))
        triples.append((i, "rdfs:label", ("literal", deps_graph.title_of(f))))
        for key, value in table_rows(f).items():
            if value in ("なし", "—", ""):
                continue
            if key in ID_ROWS or key in BARE_ID_ROWS:
                # 自分自身への依存も残す（誤記を、SPARQL の循環の問い合わせと deps_graph の検査で検出する）
                pred = ID_ROWS.get(key) or BARE_ID_ROWS[key]
                objs = ANY_ID.findall(LINK.sub(lambda m: m.group(1), value))
                triples += [(i, "pfs:" + pred, x) for x in dict.fromkeys(objs)]
            elif key in LINK_ID_ROWS:
                triples += [(i, "pfs:" + LINK_ID_ROWS[key], x) for x in link_ids(value)]
            elif key in LINK_ROWS:
                if not LINK.search(value):
                    triples.append((i, "pfs:" + LINK_ROWS[key], ("literal", value)))
                for _, target in LINK.findall(value):
                    if target.startswith("http"):
                        triples.append((i, "pfs:" + LINK_ROWS[key], ("link", target)))
                    else:
                        rel = (f.parent / target.split("#")[0]).resolve().relative_to(ROOT).as_posix()
                        triples.append((i, "pfs:" + LINK_ROWS[key], ("link", rel)))
            elif key in LITERAL_ROWS:
                triples.append((i, "pfs:" + LITERAL_ROWS[key], ("literal", value)))
    return triples


def source_files() -> list[Path]:
    """索引が読むファイル。Git の管理下のファイルと、追加予定（無視の設定に当たらない未追跡）のファイルに限る
    （仮想環境などの中の Markdown が混ざらないように。PR #72 のレビュー）。logs/ は読まない。"""
    import subprocess
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                         capture_output=True, check=True).stdout.decode("utf-8")
    paths = sorted({ROOT / p for p in out.split("\0") if p})
    files = [p for p in paths if p.suffix == ".md" and p.parts[len(ROOT.parts)] != "logs" and p.is_file()]
    for d, pattern in CODE_DIRS.items():
        files += [p for p in paths if p.parts[len(ROOT.parts)] == d and p.match(pattern) and p.is_file()]
    return files


# インラインのコード。改行をまたいでよいが、空行（段落の区切り）はまたがない（PR #72 のレビュー）
# 開きと閉じは同じ長さのバッククォートの列（前後にバッククォートが続かない）にする（PR #72 のレビュー）
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)((?:(?!\n[ \t]*\n).)+?)(?<!`)\1(?!`)", re.S)


def without_inline_code(text: str) -> str:
    """インラインのコード（`…`）を除いた文字列を返す。改行は残す（行の番号を変えない）。"""
    return INLINE_CODE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def mentions_in(path: Path) -> list[Mention]:
    rel = path.relative_to(ROOT).as_posix()
    lines = path.read_text(encoding="utf-8").splitlines()
    if path.suffix != ".md":
        return [Mention(i, rel, n, "", False) for n, line in enumerate(lines, 1) for i in ANY_ID.findall(line)]
    # 行ごとの節と、コードブロックの中（と囲みの行）かどうか。囲みは、開いた囲みと同じ文字で、同じ長さ以上の行
    # だけが閉じる（入れ子の例を誤らない）
    sections, fenced, section, fence = [], [], "", None
    for line in lines:
        m = FENCE.match(line)
        if fence is None and m:
            fence = (m.group(1)[0], len(m.group(1)))
            fenced.append(True)
        elif fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] and not m.group(2).strip():
                fence = None
            fenced.append(True)
        else:
            if re.match(r"#{1,6} ", line):
                section = line.lstrip("#").strip()
            fenced.append(False)
        sections.append(section)
    # コードブロックとインラインのコード（改行をまたぐものを含む）の中のリンク記法はリンクではないので、その中の
    # ID はリンクのない言及として数える（PR #72 のレビュー）
    code = {n: [] for n in range(1, len(lines) + 1)}
    for n, line in enumerate(lines, 1):
        if fenced[n - 1]:
            code[n] += ANY_ID.findall(line)
    prose = "\n".join("" if f else line for line, f in zip(lines, fenced))
    for cm in INLINE_CODE.finditer(prose):
        for im in ANY_ID.finditer(cm.group(0)):
            code[prose.count("\n", 0, cm.start() + im.start()) + 1].append(im.group(1))
    found = []
    for n, line in enumerate(without_inline_code(prose).split("\n"), 1):
        sec = sections[n - 1] if n <= len(sections) else section
        found += [Mention(i, rel, n, sec, False) for i in code.get(n, [])]
        # ID のファイルへのリンクは、表示文字によらず、リンク先の ID への「リンク」として数える。表示文字の中の
        # その ID は数え直さず、表示文字のほかの ID はリンクのない言及として数える。リンク先のパスは読まない
        for lm in LINK.finditer(line):
            tid = link_target_id(lm.group(2))
            if tid:
                found.append(Mention(tid, rel, n, sec, True))
        line = LINK.sub(
            lambda lm: ANY_ID.sub(lambda x: "" if x.group(1) == link_target_id(lm.group(2)) else x.group(0),
                                  lm.group(1)), line)
        found += [Mention(i, rel, n, sec, False) for i in ANY_ID.findall(line)]
    return found


def mentions() -> list[Mention]:
    return [m for f in source_files() for m in mentions_in(f)]


# 出力

def iri(obj) -> str:
    if isinstance(obj, tuple):
        kind, value = obj
        if kind == "class":
            return f"pfs:{value}"
        if kind == "link":
            return f"<{value}>" if value.startswith("http") else f"<{BASE}{quote(value)}>"
        raise ValueError(obj)
    if obj.startswith(("pfs:", "rdf:", "rdfs:")):
        return obj
    return f"<{BASE}{quote(id_path(obj))}>"


def literal(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")
    return f'"{escaped}"@ja'


def term(obj) -> str:
    if isinstance(obj, tuple) and obj[0] == "literal":
        return literal(obj[1])
    return iri(obj)


def to_turtle(triples, ments) -> str:
    out = [f"@prefix {p}: <{u}> ." for p, u in PREFIXES.items()]
    out.append("")
    by_subject: dict[str, list] = {}
    for s, p, o in triples:
        by_subject.setdefault(s, []).append((p, o))
    for s, pos in by_subject.items():
        body = " ;\n    ".join(f"{p if p != 'rdf:type' else 'a'} {term(o)}" for p, o in pos)
        out.append(f"{iri(s)}\n    {body} .\n")
    for m in ments:
        out.append(f"[] a pfs:Mention ; pfs:mentions {iri(m.target)} ; "
                   f"pfs:source {iri(('link', m.source))} ; pfs:line {m.line} ; "
                   f"pfs:section {literal(m.section)} ; pfs:linked {'true' if m.linked else 'false'} .")
    return "\n".join(out) + "\n"


def to_json(triples, ments) -> str:
    def plain(o):
        return {"id": o} if isinstance(o, str) else {o[0]: o[1]}
    data = {
        "base": BASE,
        "triples": [{"s": s, "p": p, "o": plain(o)} for s, p, o in triples],
        "mentions": [m.__dict__ for m in ments],
    }
    return json.dumps(data, ensure_ascii=False, indent=1)


def refs(target: str, triples, ments) -> list[str]:
    lines = [f"{target} を目的語とする構造のトリプル："]
    lines += [f"  {s} {p} {target}" for s, p, o in triples if o == target] or ["  なし"]
    lines.append(f"{target} の言及（リンク {sum(m.linked for m in ments if m.target == target)} 件、"
                 f"リンクなし {sum(not m.linked for m in ments if m.target == target)} 件）：")
    for m in ments:
        if m.target == target:
            where = f" [{m.section}]" if m.section else ""
            lines.append(f"  {m.source}:{m.line}{where}{'（リンク）' if m.linked else ''}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", nargs="*", help="refs <ID>：その ID を指す依存・参照と言及を表示する")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--json", action="store_true", help="索引を JSON で書く")
    group.add_argument("--ttl", action="store_true", help="索引を Turtle（RDF）で書く")
    args = parser.parse_args()
    triples, ments = structure(), mentions()
    if args.json:
        print(to_json(triples, ments))
    elif args.ttl:
        print(to_turtle(triples, ments), end="")
    elif len(args.command) == 2 and args.command[0] == "refs" and ANY_ID.fullmatch(args.command[1]):
        print("\n".join(refs(args.command[1], triples, ments)))
    else:
        parser.print_help()
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
