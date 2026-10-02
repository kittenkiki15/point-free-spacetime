"""定義（definitions/）・前提（assumptions/）と framework.md の整合性を確かめる。"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import deps_graph  # noqa: E402

ROADMAP = ROOT / "roadmap.md"
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
        assert len(rows) == len(files), (directory, "一覧に同じ ID の行が重複している")
        for i, name, layer, state in rows:
            f = files[i]
            assert name == deps_graph.title_of(f), (i, "名前")
            assert layer == deps_graph.table_row(f, "層"), (i, "層")
            assert state == deps_graph.table_row(f, "状態"), (i, "状態")


def test_referenced_ids_exist():
    files = deps_graph.item_files()
    for i, f in files.items():
        for key in ["依存する ID", "関係する予想・結果", "目標の ID"]:
            for ref in deps_graph.ids_in(deps_graph.table_row(f, key), i):
                assert ref in files, (i, key, ref)


def test_id_links_point_to_matching_files():
    # 依存欄だけでなく本文も含めて、表示文字が ID のリンクがその ID のファイルを指すことを検査する
    targets = [deps_graph.FRAMEWORK, ROADMAP, *deps_graph.item_files().values()]
    targets += [ROOT / d / "README.md" for d in ["definitions", "assumptions", "conjectures", "results"]]
    for md in targets:
        assert deps_graph.link_mismatches(md.read_text(encoding="utf-8"), md.parent) == [], md


def test_link_mismatch_is_detected():
    conj = deps_graph.KINDS["C"]
    value = "[D-0001](../definitions/D-0002.md)、[A-0001](../assumptions/A-0001.md)"
    assert deps_graph.ids_in(value) == ["D-0001", "A-0001"]
    assert deps_graph.link_mismatches(value, conj) == [("D-0001", "../definitions/D-0002.md")]
    # 予想のファイルから同じディレクトリのつもりで書くと、存在しないファイルを指す
    assert deps_graph.link_mismatches("[D-0001](D-0001.md)", conj) != []
    assert deps_graph.link_mismatches("[D-0001](D-0001.md)", deps_graph.KINDS["D"]) == []
    assert deps_graph.link_mismatches("[D-0001](../assumptions/D-0001.md)", conj) != []


def test_targets_are_assumptions_not_dependencies():
    # 目標の ID は前提に限り（定義は命題ではない）、依存をたどって（間接的にも）仮定しない（結論を仮定しない）
    deps = deps_graph.dependencies()

    def ancestors(i, seen):
        for d in deps.get(i, []):
            if d not in seen:
                seen.add(d)
                ancestors(d, seen)
        return seen

    for i, ts in deps_graph.targets().items():
        used = ancestors(i, set())
        for t in ts:
            assert t[0] == "A", (i, t, "目標の ID は前提に限る")
            assert t not in used, (i, t, "目標を直接または間接に仮定している")


def test_only_conjectures_have_targets():
    # 目標の ID は予想の欄で、すべての予想に置く（目標がなければ「なし」）
    for i, f in deps_graph.item_files().items():
        row = deps_graph.table_row(f, "目標の ID")
        if i[0] == "C":
            assert row is not None, (i, "目標の ID の行がない")
        else:
            assert row is None, (i, "目標の ID は予想の欄")


def test_roadmap_task_states_are_valid():
    text = ROADMAP.read_text(encoding="utf-8")
    rows = [line for line in text.splitlines() if re.match(r"\| T-\d{4} \|", line)]
    assert rows, "タスクの表がない"
    for line in rows:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        assert len(cells) == 6, (line, "列の数が表の見出しと合わない")
        assert cells[-1] in {"未着手", "進行中", "完了", "保留"}, (cells[0], cells[-1])


def test_no_self_dependency():
    for i, ds in deps_graph.dependencies().items():
        assert i not in ds, (i, "自分自身に依存している")


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
    targets = [deps_graph.FRAMEWORK, ROADMAP, *deps_graph.item_files().values()]
    targets += [ROOT / d / "README.md" for d in ["definitions", "assumptions"]]
    for md in targets:
        for target in re.findall(r"\]\(([^)\s]+)\)", md.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            assert (md.parent / target.split("#")[0]).exists(), (md, target)


def test_roadmap_task_ids_are_unique_and_described():
    text = ROADMAP.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (T-\d{4}) \|", text, re.M)
    assert rows, "タスクの表がない"
    assert len(rows) == len(set(rows)), "タスクの ID が重複している"
    headings = re.findall(r"^### (T-\d{4}) ", text, re.M)
    assert headings == rows, "表のタスクと「各タスクの内容」の見出しが一致しない"
    # 本文から参照するタスクの ID は、表にあるものに限る
    assert set(re.findall(r"\bT-\d{4}\b", text)) <= set(rows)



def open_task_ids(text):
    # 未完了（状態が「完了」でない）タスクの「関係する ID」に挙がった ID の集合。「X〜Y」の範囲も展開する
    ids = set()
    for line in re.findall(r"^\| T-\d{4} \|.*$", text, re.M):
        cells = [c.strip() for c in line.strip("|").split("|")]
        related, state = cells[4], cells[5]
        if state == "完了":
            continue
        ids |= set(re.findall(r"[DACR]-\d{4}", related))
        for kind, start, end in re.findall(r"\[([DACR])-(\d{4})\]\([^)]*\)〜\[[DACR]-(\d{4})\]", related):
            ids |= {f"{kind}-{n:04d}" for n in range(int(start), int(end) + 1)}
    return ids


def open_points(path):
    # 定義・前提の「未解決の点」と予想の「詳細化の論点」の箇条（「なし」を除く）
    heading = "## 詳細化の論点" if path.name.startswith("C-") else "## 未解決の点"
    text = path.read_text(encoding="utf-8")
    if heading not in text:
        return []
    body = text.split(heading, 1)[1].split("\n## ", 1)[0]
    return [line for line in body.splitlines() if line.startswith("- ") and not line.startswith("- なし")]


def test_open_points_are_assigned_to_open_tasks():
    """未解決の点・詳細化の論点を持つ定義・前提・予想は、どれかの未完了のタスクの「関係する ID」にある（roadmap.md の使い方。第 27 回）。

    ファイルの掲載漏れの検査で、論点ごとの割り当ては検査しない（各タスクの節の記述で確かめる）。
    """
    covered = open_task_ids(ROADMAP.read_text(encoding="utf-8"))
    missing = [i for i, f in deps_graph.item_files().items() if i[0] in "DAC" and open_points(Path(f)) and i not in covered]
    assert not missing, ("どの未完了のタスクにも割り当てていない論点がある", sorted(missing))


def test_open_task_ids_handles_states_and_ranges():
    text = (
        "| T-0001 | a | B | なし | [D-0001](d.md) | 完了 |\n"
        "| T-0002 | b | B | なし | [C-0002](c.md)〜[C-0004](c.md)、[A-0001](a.md) | 未着手 |\n"
    )
    assert open_task_ids(text) == {"C-0002", "C-0003", "C-0004", "A-0001"}

def choice_pairs():
    # assumptions/README.md の「択一の組と体系」の表：前提の ID → (組, 体系)。表の全データ行の書式を検査する
    readme = (ROOT / "assumptions" / "README.md").read_text(encoding="utf-8")
    section = readme.split("## 択一の組と体系", 1)[1].split("\n## ", 1)[0]
    lines = [line for line in section.splitlines() if line.startswith("|")]
    assert lines[0].startswith("| 組 |") and set(lines[1]) <= set("|- "), "表の見出しがない"
    pattern = re.compile(r"^\| (\d+) \| ([A-Z]) \| \[(A-\d{4})\]\(\3\.md\) \| [^|]+ \|$")
    result = {}
    for line in lines[2:]:
        m = pattern.match(line)
        assert m, (line, "択一の組の表の行の書式が正しくない（体系の記号は英大文字 1 文字）")
        pair, system, a = m.groups()
        assert a not in result, (a, "同じ前提が二度登録されている")
        assert a in deps_graph.item_files(), (a, "登録した前提のファイルがない")
        result[a] = (pair, system)
    return result


def systems_of(f):
    # 「体系」の行の、括弧の前の記号（複数の組に依存する場合は「・」で区切る）。各記号は英大文字 1 文字で、重複しない
    row = deps_graph.table_row(f, "体系")
    if row is None:
        return None
    labels = [s.strip() for s in row.split("（")[0].split("・")]
    assert all(re.fullmatch(r"[A-Z]", s) for s in labels), (f, "体系の記号は英大文字 1 文字")
    assert len(labels) == len(set(labels)), (f, "「体系」の行に同じ記号が重複している")
    return set(labels)


def test_choice_groups_have_two_or_more_members_with_distinct_systems():
    pairs = choice_pairs()
    assert pairs, "択一の組の表がない"
    labels = [s for _, s in pairs.values()]
    assert len(labels) == len(set(labels)), "体系の記号が重複している"
    for pair in {p for p, _ in pairs.values()}:
        assert sum(1 for p, _ in pairs.values() if p == pair) >= 2, (pair, "組の前提が二つ以上でない")


def test_choice_pairs_and_systems_are_consistent():
    # 同じ組の二つの前提に（間接的にも）依存しない。組の前提とそれに依存する項目は、「体系」の行が依存と一致する
    pairs = choice_pairs()
    deps = deps_graph.dependencies()

    def ancestors(i, seen):
        for d in deps.get(i, []):
            if d not in seen:
                seen.add(d)
                ancestors(d, seen)
        return seen

    for i, f in deps_graph.item_files().items():
        used = ancestors(i, set()) | ({i} if i in pairs else set())
        by_pair = {}
        for a in used:
            if a in pairs:
                pair, system = pairs[a]
                by_pair.setdefault(pair, set()).add(system)
        for pair, systems in by_pair.items():
            assert len(systems) == 1, (i, pair, "同じ組の二つの前提に依存している")
        systems = {s for ss in by_pair.values() for s in ss}
        if systems:
            assert systems_of(f) == systems, (i, "「体系」の行が依存と一致しない")
        else:
            assert systems_of(f) is None, (i, "組の前提に依存しないのに「体系」の行がある")
