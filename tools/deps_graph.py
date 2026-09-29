"""定義・前提・予想・結果の依存関係を読み、framework.md の依存関係の図（Mermaid）を生成する。

各ファイル（definitions/D-NNNN.md、assumptions/A-NNNN.md、conjectures/C-NNNN.md、
results/R-NNNN.md）の表にある「依存する ID」の行を読む。行がないファイルは、依存なしとして扱う。

使い方:
    python3 tools/deps_graph.py          # framework.md の図を書き直す
    python3 tools/deps_graph.py --check  # 図が最新でなければ 1 を返す（CI 用）
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {
    "D": ROOT / "definitions",
    "A": ROOT / "assumptions",
    "C": ROOT / "conjectures",
    "R": ROOT / "results",
}
FRAMEWORK = ROOT / "framework.md"
START = "<!-- deps-graph:start（tools/deps_graph.py が生成する。手で書き換えない） -->"
END = "<!-- deps-graph:end -->"
ID_RE = re.compile(r"\b([DACR]-\d{4})\b")


def item_files():
    """ID → ファイルのパス。"""
    files = {}
    for prefix, directory in KINDS.items():
        for f in sorted(directory.glob(f"{prefix}-[0-9][0-9][0-9][0-9].md")):
            files[f.stem] = f
    return files


def title_of(path: Path) -> str:
    """1 行目の「# X-NNNN: 名前」から名前を返す。"""
    first = path.read_text(encoding="utf-8").splitlines()[0]
    m = re.match(rf"# {re.escape(path.stem)}: (.+)", first)
    return m.group(1).strip() if m else ""


def table_row(path: Path, key: str):
    """表の「| key | 値 |」の値を返す。行がなければ None。"""
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] == key:
            return cells[1]
    return None


def ids_in(value, exclude: str = "") -> list[str]:
    """文字列に現れる ID を、重複を除いて現れた順に返す（リンクの文字とパスの両方に現れるため）。"""
    return [i for i in dict.fromkeys(ID_RE.findall(value or "")) if i != exclude]


def dependencies():
    """ID → 依存する ID のリスト。自分自身への参照も残す（テストで循環として検出する）。"""
    return {i: ids_in(table_row(f, "依存する ID")) for i, f in item_files().items()}


def graph_text() -> str:
    files = item_files()
    deps = dependencies()
    # 図に載せるのは、定義・前提・予想のすべてと、依存の辺を持つ結果
    shown = {i for i in files if i[0] in "DAC"}
    for i, ds in deps.items():
        if ds:
            shown.add(i)
            shown.update(ds)
    shape = {"D": ('["', '"]'), "A": ('(["', '"])'), "C": ('{{"', '"}}'), "R": ('[["', '"]]')}
    lines = ["```mermaid", "flowchart TD"]
    for i in sorted(shown, key=lambda s: ("DACR".index(s[0]), s)):
        left, right = shape[i[0]]
        name = title_of(files[i]).replace('"', "'") if i in files else "（ファイルなし）"
        lines.append(f"  {i.replace('-', '_')}{left}{i}: {name}{right}")
    for i in sorted(deps):
        for d in deps[i]:
            lines.append(f"  {d.replace('-', '_')} --> {i.replace('-', '_')}")
    lines.append("```")
    return "\n".join(lines)


def render(text: str) -> str:
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    return f"{before}{START}\n{graph_text()}\n{END}{after}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="図が最新か確かめるだけで、書き換えない")
    args = parser.parse_args()
    text = FRAMEWORK.read_text(encoding="utf-8")
    new = render(text)
    if args.check:
        if new != text:
            print("framework.md の依存関係の図が最新ではありません。python3 tools/deps_graph.py を実行してください。")
            return 1
        return 0
    FRAMEWORK.write_text(new, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
