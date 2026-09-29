"""定義（definitions/）・前提（assumptions/）と framework.md の整合性を確かめる。"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import deps_graph  # noqa: E402

STATES = {"採用", "作業上", "未定", "廃止"}
LAYERS = {"実験", "観測量", "観測量の時空", "可能な実験", "可能な観測量", "点なし時空"}
ROWS = ["状態", "層", "依存する ID", "関係する予想・結果", "初出"]


def da_files():
    files = deps_graph.item_files()
    return {i: f for i, f in files.items() if i[0] in "DA"}


def test_each_file_has_title_and_rows():
    for i, f in da_files().items():
        assert deps_graph.title_of(f), (f, "1 行目が「# X-NNNN: 名前」でない")
        for key in ROWS:
            assert deps_graph.table_row(f, key) is not None, (f, key)
        assert deps_graph.table_row(f, "状態") in STATES, (f, "状態")
        assert deps_graph.table_row(f, "層") in LAYERS, (f, "層")


def test_readme_lists_every_file_with_same_name_layer_state():
    for directory in ["definitions", "assumptions"]:
        readme = (ROOT / directory / "README.md").read_text(encoding="utf-8")
        rows = re.findall(r"^\| \[([DA]-\d{4})\]\(\1\.md\) \| (.+?) \| (.+?) \| (.+?) \|$", readme, re.M)
        files = {i: f for i, f in da_files().items() if f.parent.name == directory}
        assert {r[0] for r in rows} == set(files), directory
        for i, name, layer, state in rows:
            f = files[i]
            assert name == deps_graph.title_of(f), (i, "名前")
            assert layer == deps_graph.table_row(f, "層"), (i, "層")
            assert state == deps_graph.table_row(f, "状態"), (i, "状態")


def test_referenced_ids_exist():
    files = deps_graph.item_files()
    for i, f in files.items():
        for key in ["依存する ID", "関係する予想・結果"]:
            for ref in deps_graph.ids_in(deps_graph.table_row(f, key), i):
                assert ref in files, (i, key, ref)


def test_no_dependency_cycles():
    deps = deps_graph.dependencies()
    state = {}

    def visit(i, path):
        if state.get(i) == "done":
            return
        assert state.get(i) != "active", ("依存関係が循環している", path + [i])
        state[i] = "active"
        for d in deps.get(i, []):
            visit(d, path + [i])
        state[i] = "done"

    for i in deps:
        visit(i, [])


def test_related_conjectures_match_dependencies():
    # 定義・前提の「関係する予想・結果」は、それに依存する予想・結果の集合と一致する
    deps = deps_graph.dependencies()
    for i, f in da_files().items():
        listed = set(deps_graph.ids_in(deps_graph.table_row(f, "関係する予想・結果"), i))
        expected = {c for c, ds in deps.items() if c[0] in "CR" and i in ds}
        assert listed == expected, (i, listed, expected)


def test_graph_is_up_to_date():
    text = deps_graph.FRAMEWORK.read_text(encoding="utf-8")
    assert deps_graph.render(text) == text, "python3 tools/deps_graph.py を実行して図を更新する"


def test_links_exist():
    targets = [deps_graph.FRAMEWORK, *da_files().values()]
    targets += [ROOT / d / "README.md" for d in ["definitions", "assumptions"]]
    for md in targets:
        for target in re.findall(r"\]\(([^)\s]+)\)", md.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            assert (md.parent / target.split("#")[0]).exists(), (md, target)
