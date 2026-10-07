"""定義（definitions/）・前提（assumptions/）と framework.md の整合性を確かめる。"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import deps_graph  # noqa: E402
import id_index  # noqa: E402

ROADMAP = ROOT / "roadmap.md"
STATES = {"採用", "作業上", "未定", "廃止"}
LAYERS = {"実験", "観測量", "観測量の時空", "可能な実験", "可能な観測量", "点なし時空"}
ROWS = ["状態", "層", "依存する ID", "関係する予想・結果", "初出"]


def heading_matches_file(f):
    """1 行目が「# <ファイル名の ID>: 名前」であるか（ID の取り違えを検出する。第 30 回）。"""
    lines = f.read_text(encoding="utf-8").splitlines()
    return bool(lines) and re.fullmatch(rf"# {re.escape(f.stem)}: \S.*", lines[0]) is not None


def test_heading_with_wrong_id_is_detected(tmp_path):
    good, bad = tmp_path / "T-0001.md", tmp_path / "Q-0001.md"
    good.write_text("# T-0001: タスク\n", encoding="utf-8")
    bad.write_text("# Q-9999: 論点\n", encoding="utf-8")
    assert heading_matches_file(good)
    assert not heading_matches_file(bad) and deps_graph.title_of(bad) == ""


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
        for key in ["依存する ID", "関係する予想・結果", "目標の ID", "参照する ID"]:
            for ref in deps_graph.ids_in(deps_graph.table_row(f, key), i):
                assert ref in files, (i, key, ref)


def test_id_links_point_to_matching_files():
    # 依存欄だけでなく本文も含めて、表示文字が ID のリンクがその ID のファイルを指すことを検査する
    targets = [deps_graph.FRAMEWORK, ROADMAP, *deps_graph.item_files().values()]
    targets += [ROOT / d / "README.md" for d in ["definitions", "assumptions", "conjectures", "results", "tasks", "questions"]]
    targets += [*task_files().values(), *sorted(QUESTIONS.glob("Q-[0-9][0-9][0-9][0-9].md"))]
    for md in targets:
        text = md.read_text(encoding="utf-8")
        assert deps_graph.link_mismatches(text, md.parent) == [], md
        # タスクと Q の ID のリンクは、すべての Markdown のファイルで tq_link_problems が検査する


def body_link_problems(f):
    """「## 定義」「## 主張」の節の本文にある ID のリンクが、「依存する ID」「目標の ID」「参照する ID」の
    どれかの行にあるか（第 31 回にユーザーと決めた。T-0025 の 4）。参照する ID は依存とは重ならない。
    循環の検査に使うのは「依存する ID」だけで、参照は使わない。"""
    text = f.read_text(encoding="utf-8")
    # タスク・Q の ID（参照する ID にだけ置ける）も読む（PR #72 のレビュー）
    row = lambda k: set(re.findall(r"\b[DACRTQ]-\d{4}\b", deps_graph.LINK_RE.sub(
        lambda m: m.group(1), deps_graph.table_row(f, k) or ""))) - {f.stem}
    deps, refs = row("依存する ID"), row("参照する ID")
    targets = row("目標の ID")
    # 依存（仮定する）・目標（仮定せずに導く）・参照（依存ではない）は、互いに重ならない（PR #72 のレビュー）
    problems = [f"{f.stem}: {x} が「{a}」と「{b}」の両方にある"
                for a, b, xs in (("依存する ID", "参照する ID", deps & refs), ("依存する ID", "目標の ID", deps & targets),
                                 ("目標の ID", "参照する ID", targets & refs))
                for x in sorted(xs)]
    # 「## 定義」と「## 主張」の両方の節を検査する。節の見出しは、コードブロックの外のものだけを読み、末尾の空白は
    # 除いて比べる（section_body）。コードの中のリンク記法はリンクではないので、検査から外す（PR #72 のレビュー）
    section = "\n".join(id_index.without_inline_code(id_index.without_code_blocks(body))
                         for body in (id_index.section_body(text, h) for h in ("## 定義", "## 主張")) if body)
    listed = deps | refs | targets
    # リンクの読み取りは索引と同じ正規表現（タイトル付きのリンクも読む）にする（PR #72 のレビュー）
    for shown, target in id_index.LINK.findall(section):
        # 表示文字が ID のリンクに加えて、表示文字に説明を含むリンク（例：[D-0003 の 3](../definitions/D-0003.md)）も、
        # リンク先の ID で数える（PR #72 のレビュー）
        # リンク先の判定は索引と同じ（外部の URL は ID へのリンクとみなさない。PR #72 のレビュー）
        tid = id_index.link_target_id(target)
        external = re.match(r"([a-z][a-z0-9+.-]*:|//)", target, re.I)
        linked = tid or (None if external else (shown if re.fullmatch(r"[DACRTQ]-\d{4}", shown) else None))
        if linked and linked != f.stem and linked not in listed:
            problems.append(f"{f.stem}: 本文の {linked} へのリンクが、依存・目標・参照のどの行にもない")
    return list(dict.fromkeys(problems))


def test_dependency_rows_link_with_id_text():
    # 依存・目標・参照の行のリンクは、表示文字を ID にする（索引と deps_graph は ID を表示文字から読むため。
    # PR #72 のレビュー）
    bad = []
    for i, f in deps_graph.item_files().items():
        for key in ("依存する ID", "目標の ID", "参照する ID"):
            for shown, _ in deps_graph.LINK_RE.findall(deps_graph.table_row(f, key) or ""):
                if not re.fullmatch(r"[DACRTQ]-\d{4}", shown):
                    bad.append((i, key, shown))
    assert bad == []


def test_body_links_are_dependencies_or_references():
    assert [p for f in deps_graph.item_files().values() for p in body_link_problems(f)] == []


def test_body_link_problems_detects_unlisted_links(tmp_path):
    f = tmp_path / "D-0001.md"
    head = "# D-0001: d\n\n| 項目 | 値 |\n| --- | --- |\n| 依存する ID | [D-0002](D-0002.md) |\n"
    f.write_text(head + "\n## 定義\n\n[D-0002](D-0002.md) と [D-0003](D-0003.md)。\n\n## 注意\n\n[D-0004](D-0004.md)\n",
                 encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の D-0003 へのリンクが、依存・目標・参照のどの行にもない"]
    # 表示文字に説明を含むリンクも、リンク先の ID で数える
    # コードブロックの中の「## 」の行で、節の終わりとみなさない（PR #72 のレビュー）
    f.write_text(head + "\n## 定義\n\n```\n## 例\n```\n\n[D-0006](D-0006.md)\n\n## 注意\n", encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の D-0006 へのリンクが、依存・目標・参照のどの行にもない"]
    f.write_text(head + "\n## 定義\n\n```markdown\n[D-0007](D-0007.md)\n```\n", encoding="utf-8")
    assert body_link_problems(f) == []
    # インラインのコードの中のリンク記法も外し、末尾に空白のある見出しも節とみなす
    f.write_text(head + "\n## 定義 \n\n`[D-0007](D-0007.md)` と [D-0008](D-0008.md)、`改行を\nまたぐ [D-0009](D-0009.md)`\n",
                 encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の D-0008 へのリンクが、依存・目標・参照のどの行にもない"]
    f.write_text(head + "\n## 定義\n\n[D-0005「名前」](D-0005.md)\n", encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の D-0005 へのリンクが、依存・目標・参照のどの行にもない"]
    # 外部の URL（スキームを省いたものを含む）は、ID へのリンクとみなさない
    f.write_text(head + "\n## 定義\n\n[外部](//example.org/definitions/D-0011.md)、[外部](https://example.org/D-0012.md)\n",
                 encoding="utf-8")
    assert body_link_problems(f) == []
    # 両方の節を検査し、コードブロックの中の見出しの例は節とみなさない
    f.write_text(head + "\n```\n## 定義\n```\n\n## 定義\n\nなし\n\n## 主張\n\n[D-0013](D-0013.md)\n", encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の D-0013 へのリンクが、依存・目標・参照のどの行にもない"]
    # タイトル付きのリンクも検査する
    f.write_text(head + '\n## 定義\n\n[D-0010](D-0010.md "説明")\n', encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の D-0010 へのリンクが、依存・目標・参照のどの行にもない"]
    # タスクと Q へのリンクも検査し、参照する ID に書けば通る
    f.write_text(head + "\n## 定義\n\n[T-0027「リリース」](../tasks/T-0027.md)\n", encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: 本文の T-0027 へのリンクが、依存・目標・参照のどの行にもない"]
    f.write_text(head + "| 参照する ID | [T-0027](../tasks/T-0027.md) |\n\n## 定義\n\n[T-0027「リリース」](../tasks/T-0027.md)\n",
                 encoding="utf-8")
    assert body_link_problems(f) == []
    f.write_text(head + "| 参照する ID | [D-0002](D-0002.md)、[D-0003](D-0003.md) |\n\n## 定義\n\n[D-0003](D-0003.md)\n",
                 encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: D-0002 が「依存する ID」と「参照する ID」の両方にある"]
    f.write_text("# C-0001: c\n\n| 項目 | 値 |\n| --- | --- |\n| 依存する ID | [A-0001](A-0001.md) |\n"
                 "| 目標の ID | [A-0001](A-0001.md) |\n\n## 主張\n\nなし\n", encoding="utf-8")
    assert body_link_problems(f) == ["D-0001: A-0001 が「依存する ID」と「目標の ID」の両方にある"]


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


TASKS = ROOT / "tasks"
QUESTIONS = ROOT / "questions"
TASK_STATES = {"未着手", "進行中", "完了", "保留"}
TASK_ROW = re.compile(r"^\| \[(T-\d{4})\]\(tasks/\1\.md\) \|(.*)\|$", re.M)


def table_data_rows(text, header_start):
    """header_start で始まる見出しの行を持つ表の、データの行（区切りの行の後、表が終わるまで）をすべて返す。"""
    lines = text.splitlines()
    start = next((k for k, line in enumerate(lines) if line.startswith(header_start)), None)
    assert start is not None, (header_start, "表の見出しがない")
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        rows.append(line)
    return rows


def roadmap_rows(text=None):
    # roadmap.md の一覧表：タスクの ID → [名前, 段階, 前提のタスク, 関係する ID, 状態, Issue]。
    # 表のデータの行をすべて読み、形式（ID のリンク）を確かめてから集める（形式の誤った行を取りこぼさない）
    text = ROADMAP.read_text(encoding="utf-8") if text is None else text
    rows = {}
    for line in table_data_rows(text, "| ID | タスク |"):
        m = TASK_ROW.match(line)
        assert m, (line[:60], "一覧表の行の形式が正しくない（1 列目は [T-NNNN](tasks/T-NNNN.md)）")
        tid, rest = m.groups()
        assert tid not in rows, (tid, "一覧表で ID が重複している")
        rows[tid] = [c.strip() for c in rest.split("|")]
    return rows


def test_roadmap_rows_rejects_malformed_and_duplicate_rows():
    head = "| ID | タスク | 段階 | 前提のタスク | 関係する ID | 状態 | Issue |\n| --- | --- | --- | --- | --- | --- | --- |\n"
    good = "| [T-0001](tasks/T-0001.md) | a | A | なし | — | 完了 | なし |\n"
    assert set(roadmap_rows(head + good)) == {"T-0001"}
    for extra in ("| T-0001 | a | A | なし | — | 完了 | なし |\n", good):
        try:
            roadmap_rows(head + good + extra)
        except AssertionError:
            continue
        raise AssertionError(extra)


def task_files(directory=TASKS):
    return {f.stem: f for f in sorted(directory.glob("T-[0-9][0-9][0-9][0-9].md"))}


def task_fields(f):
    return {k: deps_graph.table_row(f, k) for k in ("段階", "前提のタスク", "関係する ID", "状態", "Issue", "追加した回")}


def test_roadmap_task_states_are_valid():
    rows = roadmap_rows()
    assert rows, "タスクの表がない"
    for tid, cells in rows.items():
        assert len(cells) == 6, (tid, "列の数が表の見出しと合わない")
        assert cells[4] in TASK_STATES, (tid, cells[4])


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
    targets += [ROOT / d / "README.md" for d in ["definitions", "assumptions", "tasks", "questions"]]
    targets += [*task_files().values(), *sorted(QUESTIONS.glob("Q-[0-9][0-9][0-9][0-9].md"))]
    for md in targets:
        for target in re.findall(r"\]\(([^)\s]+)\)", md.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            assert (md.parent / target.split("#")[0]).exists(), (md, target)


def test_roadmap_task_ids_are_unique_and_described():
    # 一覧表のタスクと tasks/ のファイルが一対一で、表の各列がファイルの表と一致する（第 30 回。T-0025 の 2）
    text = ROADMAP.read_text(encoding="utf-8")
    rows, files = roadmap_rows(text), task_files()
    assert rows, "タスクの表がない"
    assert set(rows) == set(files), ("一覧表とファイルのタスクが一致しない", set(rows) ^ set(files))
    for tid, (name, stage, prereq, related, state, issue) in rows.items():
        f = files[tid]
        fields = task_fields(f)
        assert heading_matches_file(f), (tid, "1 行目の ID がファイル名と一致しない")
        assert deps_graph.title_of(f) == name, (tid, "名前が一致しない")
        assert fields["段階"] == stage and fields["前提のタスク"] == prereq, (tid, "段階か前提のタスクが一致しない")
        assert fields["状態"] == state, (tid, "状態が一致しない")
        assert fields["Issue"] == issue, (tid, "Issue が一致しない")
        # ID だけでなく、ID でない関係先（framework.md など）も含めて、リンク先の相対パスをそろえて比べる
        assert fields["関係する ID"].replace("](../", "](") == related, (tid, "関係する ID が一致しない")
        assert fields["追加した回"], (tid, "追加した回がない")
        for heading in ("## 内容", "## 履歴"):
            assert heading in f.read_text(encoding="utf-8"), (tid, heading)
    # 本文から参照するタスクの ID は、表にあるものに限る
    assert set(re.findall(r"\bT-\d{4}\b", text)) <= set(rows)


ISSUE_CELL = re.compile(r"\[#(\d+)\]\(https://github\.com/kittenkiki15/point-free-spacetime/issues/(\d+)\)")


def issue_number(cell):
    """Issue の欄の番号。形が正しくないか、表示の番号とリンク先の番号が違えば None。"""
    m = ISSUE_CELL.fullmatch(cell or "")
    return int(m.group(1)) if m and m.group(1) == m.group(2) else None


def issue_problems(conjectures, others):
    """Issue の欄の検査。conjectures は予想のファイル、others はタスクと Q のファイル。

    未完了のタスクと Q には Issue があり、表示とリンク先の番号が一致し、予想・タスク・Q の間で
    同じ Issue を使わない（第 30 回。PR #68 のレビュー）。
    """
    problems, used = [], {}
    for f in conjectures:
        cell = deps_graph.table_row(f, "Issue")
        n = issue_number(cell)
        if n is None:
            # 予想にはすべて Issue がある（CLAUDE.md の「予想の管理」）。読めない欄は飛ばさずに知らせる
            problems.append(f"{f.stem} の Issue の欄の形が正しくないか、表示とリンク先の番号が違う: {cell}")
            continue
        if n in used:
            problems.append(f"{f.stem} と {used[n]} が同じ Issue #{n} を使っている")
        used[n] = f.stem
    for f in others:
        cell = deps_graph.table_row(f, "Issue")
        if cell in (None, "なし"):
            # 「なし」は、第 30 回の時点で完了していたタスクだけに許す。Issue を作ってから完了したタスクは、
            # 閉じた Issue へのリンクを残す（PR #68 のレビュー）
            if f.stem not in TASKS_DONE_BEFORE_ISSUES:
                problems.append(f"{f.stem} に Issue がない")
            continue
        if OLD_REPO_ISSUE.fullmatch(cell):
            # 旧リポジトリ（非公開）で閉じた Issue。新しい公開用リポジトリへは移していない（第 32 回）
            if task_fields(f).get("状態") != "完了":
                problems.append(f"{f.stem} は完了していないのに、Issue が旧リポジトリのものになっている")
            continue
        n = issue_number(cell)
        if n is None:
            problems.append(f"{f.stem} の Issue の欄の形が正しくないか、表示とリンク先の番号が違う: {cell}")
            continue
        if n in used:
            problems.append(f"{f.stem} と {used[n]} が同じ Issue #{n} を使っている")
        used[n] = f.stem
    return problems


# 第 30 回にタスクの Issue を作った時点で、すでに完了していたタスク（Issue なし。tasks/README.md）
OLD_REPO_ISSUE = re.compile(r"旧リポジトリ（非公開）の Issue #\d+")
TASKS_DONE_BEFORE_ISSUES = {"T-0001", "T-0002", "T-0003", "T-0015", "T-0016",
                            "T-0018", "T-0019", "T-0020", "T-0021", "T-0022"}


def test_tasks_done_before_issues_are_done():
    files = task_files()
    assert all(task_fields(files[t])["状態"] == "完了" for t in TASKS_DONE_BEFORE_ISSUES)


def test_issue_problems_rejects_dropping_issue_of_task_done_later(tmp_path):
    task = tmp_path / "T-0004.md"
    task.write_text("# T-0004: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 完了 |\n| Issue | なし |\n", encoding="utf-8")
    assert issue_problems([], [task]) == ["T-0004 に Issue がない"]
    done = tmp_path / "T-0001.md"
    done.write_text("# T-0001: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 完了 |\n| Issue | なし |\n", encoding="utf-8")
    assert issue_problems([], [done]) == []


def test_open_tasks_have_issues():
    conjectures = [f for i, f in deps_graph.item_files().items() if i[0] == "C"]
    others = [*task_files().values(), *sorted(QUESTIONS.glob("Q-[0-9][0-9][0-9][0-9].md"))]
    assert issue_problems(conjectures, others) == []


def test_issue_problems_detects_duplicates_between_conjectures(tmp_path):
    url = "https://github.com/kittenkiki15/point-free-spacetime/issues/"
    for name, n in (("C-0001", 8), ("C-0002", 8)):
        (tmp_path / f"{name}.md").write_text(f"# {name}: c\n\n| 項目 | 内容 |\n| --- | --- |\n| Issue | [#{n}]({url}{n}) |\n",
                                             encoding="utf-8")
    assert issue_problems(sorted(tmp_path.glob("C-*.md")), [])
    # 予想とタスクが同じ番号を使う場合と、予想の欄が読めない場合
    (tmp_path / "C-0002.md").write_text(f"# C-0002: c\n\n| 項目 | 内容 |\n| --- | --- |\n| Issue | [#53]({url}53#x) |\n",
                                       encoding="utf-8")
    task = tmp_path / "T-0004.md"
    task.write_text(f"# T-0004: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 未着手 |\n| Issue | [#8]({url}8) |\n",
                    encoding="utf-8")
    probs = issue_problems(sorted(tmp_path.glob("C-*.md")), [task])
    assert any("C-0002" in p and "形" in p for p in probs) and any("T-0004" in p and "#8" in p for p in probs)


def test_issue_number_checks_display_and_url():
    url = "https://github.com/kittenkiki15/point-free-spacetime/issues/"
    assert issue_number(f"[#53]({url}53)") == 53
    assert issue_number(f"[#53]({url}54)") is None
    assert issue_number("なし") is None


def related_ids(related):
    # 「関係する ID」の文字列に挙がった ID の集合。数えるのはリンク [X-NNNN](...) の表示の ID と、リンクどうしの
    # 「X〜Y」の範囲だけで、リンクでない裸の ID（「D-0001 は扱わない」などの注記）は数えない（PR #68 のレビュー）。
    # リンク先のパスの ID は読まない（表示とリンク先の一致は test_id_links_point_to_matching_files で検査する）
    ids = {m.group(1) for m in deps_graph.LINK_RE.finditer(related or "")
           if re.fullmatch(r"[DACRQ]-\d{4}", m.group(1))}
    for kind, start, end_kind, end in re.findall(r"\[([DACR])-(\d{4})\]\([^)]*\)〜\[([DACR])-(\d{4})\]", related or ""):
        assert kind == end_kind and int(start) <= int(end), (related, "ID の範囲の始点と終点の種類が違うか、順序が逆")
        ids |= {f"{kind}-{n:04d}" for n in range(int(start), int(end) + 1)}
    return ids


def open_task_ids(directory=TASKS):
    # 未完了（状態が「完了」でない）タスクのファイルの「関係する ID」に挙がった ID の集合（第 30 回からファイルを読む）
    ids = set()
    for f in task_files(directory).values():
        fields = task_fields(f)
        if fields["状態"] != "完了":
            ids |= related_ids(fields["関係する ID"])
    return ids


def open_points(path):
    # 定義・前提の「未解決の点」と予想の「詳細化の論点」の箇条（「なし」を除く）
    heading = "## 詳細化の論点" if path.name.startswith("C-") else "## 未解決の点"
    text = path.read_text(encoding="utf-8")
    if heading not in text:
        return []
    body = text.split(heading, 1)[1].split("\n## ", 1)[0]
    # 箇条書きに限らず、空行と「なし」以外の行があれば論点があるとみなす
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    lines = [line for line in lines if not re.match(r"^(- )?なし(。|（|$)", line)]

    def resolved_question(line):
        # 解決・取り下げにした Q へのリンクの行は、論点として数えない（第 30 回。PR #68 のレビュー）
        # 行が「Q へのリンク」と「：Q の名前」だけからなる場合に限る（ほかの問いが書き足された行は数える）
        m = re.fullmatch(r"- \[(Q-\d{4})\]\(\.\./questions/\1\.md\)：(.+)", line)
        qf = path.parents[1] / "questions" / f"{m.group(1)}.md" if m else None
        return bool(qf and qf.exists() and m.group(2).strip() == deps_graph.title_of(qf)
                    and deps_graph.table_row(qf, "状態") in {"解決", "取り下げ"})

    return [line for line in lines if not resolved_question(line)]


def test_open_points_are_assigned_to_open_tasks():
    """未解決の点・詳細化の論点を持つ定義・前提・予想は、どれかの未完了のタスクの「関係する ID」にある（roadmap.md の使い方。第 27 回）。

    ファイルの掲載漏れの検査で、論点ごとの割り当ては検査しない（各タスクの節の記述で確かめる）。
    """
    covered = open_task_ids()
    missing = [i for i, f in deps_graph.item_files().items() if i[0] in "DAC" and open_points(Path(f)) and i not in covered]
    assert not missing, ("どの未完了のタスクにも割り当てていない論点がある", sorted(missing))


def test_open_points_detects_paragraphs_and_none(tmp_path):
    with_paragraph = tmp_path / "D-9998.md"
    with_paragraph.write_text("# D\n\n## 未解決の点\n\n箇条書きでない論点。\n\n## 履歴\n", encoding="utf-8")
    assert open_points(with_paragraph)
    none = tmp_path / "C-9999.md"
    none.write_text("# C\n\n## 詳細化の論点\n\nなし。\n\n## 背景\n", encoding="utf-8")
    assert not open_points(none)
    none_with_note = tmp_path / "D-9997.md"
    none_with_note.write_text("# D\n\n## 未解決の点\n\n- なし（別の項目で扱う）。\n\n## 履歴\n", encoding="utf-8")
    assert not open_points(none_with_note)


def test_open_task_ids_handles_states_and_ranges(tmp_path):
    def task(tid, related, state):
        (tmp_path / f"{tid}.md").write_text(
            f"# {tid}: x\n\n| 項目 | 内容 |\n| --- | --- |\n| 関係する ID | {related} |\n| 状態 | {state} |\n",
            encoding="utf-8")
    task("T-0001", "[D-0001](d.md)", "完了")
    task("T-0002", "[C-0002](c.md)〜[C-0004](c.md)、[A-0001](a.md)", "未着手")
    assert open_task_ids(tmp_path) == {"C-0002", "C-0003", "C-0004", "A-0001"}
    try:
        related_ids("[C-0002](c.md)〜[A-0004](a.md)")
    except AssertionError:
        pass
    else:
        raise AssertionError("種類の異なる ID の範囲を検出できない")


def question_problems(q, root=ROOT):
    """questions/Q-NNNN.md の検査（第 30 回。T-0025 の 5）。問題の一覧を返す。"""
    problems = []
    title = deps_graph.title_of(q)
    if not heading_matches_file(q):
        problems.append("1 行目が「# Q-NNNN: 名前」でない（ID はファイル名と一致させる）")
    row = lambda k: deps_graph.table_row(q, k)
    parents = deps_graph.ids_in(row("親の ID"))
    if len(parents) != 1 or parents[0][0] not in "DAC":
        return problems + ["親の ID は、定義・前提・予想のどれか一つ"]
    parent = parents[0]
    kinds = {"D": "definitions", "A": "assumptions", "C": "conjectures"}
    if row("親の ID") != f"[{parent}](../{kinds[parent[0]]}/{parent}.md)":
        problems.append(f"親の ID は、親のファイルへのリンク（[{parent}](../{kinds[parent[0]]}/{parent}.md)）一つにする")
    pf = root / kinds[parent[0]] / f"{parent}.md"
    if not pf.exists():
        return problems + [f"親のファイル {parent} がない"]
    heading = "## 詳細化の論点" if parent[0] == "C" else "## 未解決の点"
    section = pf.read_text(encoding="utf-8").split(heading, 1)[-1].split("\n## ", 1)[0] if heading in pf.read_text(encoding="utf-8") else ""
    # 親の節には、論点の箇条を置き換えた所定の行（Q へのリンクと「：Q の名前」だけの行）がある
    item = f"- [{q.stem}](../questions/{q.stem}.md)：{title}"
    if item not in [line.strip() for line in section.splitlines()]:
        problems.append(f"親のファイル {parent} の節に、{q.stem} への所定の箇条の行（{item}）がない")
    state = row("状態")
    if state not in {"未解決", "解決", "取り下げ"}:
        problems.append(f"状態が正しくない: {state}")
    if issue_number(row("Issue")) is None:
        problems.append("Issue がない（か、表示とリンク先の番号が違う）")
    # 割り当てたタスクの形式と、タスクのファイルがあることは、状態によらず検査する
    cell = row("割り当てたタスク") or ""
    tasks = list(dict.fromkeys(re.findall(r"T-\d{4}", cell)))
    if len(tasks) != 1:
        return problems + [f"割り当てたタスクは一つにする（{len(tasks)} 件ある）"]
    if cell != f"[{tasks[0]}](../tasks/{tasks[0]}.md)":
        problems.append("割り当てたタスクは、タスクのファイルへのリンク（[T-NNNN](../tasks/T-NNNN.md)）一つにする")
    tf = root / "tasks" / f"{tasks[0]}.md"
    if not tf.exists():
        return problems + ["割り当てたタスクがない"]
    # 未完了であること、親の ID が「関係する ID」にあることは、未解決の Q に求める
    if state == "未解決":
        fields = task_fields(tf)
        if fields["状態"] == "完了":
            problems.append(f"割り当てたタスク {tasks[0]} が完了している")
        if parent not in related_ids(fields["関係する ID"]):
            problems.append(f"割り当てたタスク {tasks[0]} の「関係する ID」に親の {parent} がない")
    return problems


def test_questions_are_consistent():
    files = sorted(QUESTIONS.glob("Q-[0-9][0-9][0-9][0-9].md"))
    for q in files:
        assert not question_problems(q), (q.name, question_problems(q))
    assert not question_list_problems(QUESTIONS / "README.md", files)
    # 親のファイルから Q へのリンクは、ある Q だけを指し、その Q の「親の ID」はリンク元のファイルである
    # （同じ Q を二つの親の論点として載せない）
    for i, f in deps_graph.item_files().items():
        text = f.read_text(encoding="utf-8")
        for qid in re.findall(r"\[(Q-\d{4})\]\(\.\./questions/", text):
            assert (QUESTIONS / f"{qid}.md").exists(), (f.name, qid)
        # 親子の関係は、論点の節の Q の箇条だけで見る（ほかの節からの参照は、ふつうの相互参照として許す）
        for qid in question_items(f):
            qf = QUESTIONS / f"{qid}.md"
            assert deps_graph.ids_in(deps_graph.table_row(qf, "親の ID")) == [i], (f.name, qid, "Q の親の ID がリンク元と違う")


def question_items(f):
    """定義・前提・予想のファイルの論点の節（「未解決の点」、予想は「詳細化の論点」）にある、Q の箇条の ID。"""
    heading = "## 詳細化の論点" if f.name.startswith("C-") else "## 未解決の点"
    text = f.read_text(encoding="utf-8")
    if heading not in text:
        return []
    section = text.split(heading, 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^- \[(Q-\d{4})\]\(\.\./questions/\1\.md\)", section, re.M)


def test_question_items_reads_only_the_open_points_section(tmp_path):
    d = tmp_path / "D-0002.md"
    d.write_text("# D-0002: d\n\n## 注意\n\n- [Q-0001](../questions/Q-0001.md) を参照（相互参照）\n\n"
                 "## 未解決の点\n\n- [Q-0002](../questions/Q-0002.md)：論点\n\n## 履歴\n", encoding="utf-8")
    assert question_items(d) == ["Q-0002"]


def question_list_problems(readme, files):
    """questions/README.md の一覧の各行（ID・論点・親の ID・割り当てたタスク・状態・Issue）と、Q のファイルの一致。"""
    problems = []
    rows = {}
    text = readme.read_text(encoding="utf-8")
    # 一覧表の見出しがなければ失敗にする（Q が 0 件のときに一覧表を消しても通らないように。PR #68 のレビュー）
    header = "| ID | 論点 | 親の ID | 割り当てたタスク | 状態 | Issue |"
    if header not in [line.strip() for line in text.splitlines()]:
        return [f"一覧表の見出し（{header}）がない"]
    data = table_data_rows(text, "| ID | 論点 |")
    for line in data:
        m = re.match(r"^\| \[(Q-\d{4})\]\(\1\.md\) \|(.*)\|$", line)
        if not m:
            problems.append(f"一覧の行の形式が正しくない: {line[:60]}")
            continue
        qid, rest = m.groups()
        if qid in rows:
            problems.append(f"{qid} が一覧で重複している")
        rows[qid] = [c.strip() for c in rest.split("|")]
    if set(rows) != {q.stem for q in files}:
        problems.append(f"一覧とファイルの Q が一致しない: {sorted(set(rows) ^ {q.stem for q in files})}")
    for q in files:
        if q.stem not in rows:
            continue
        cells = rows[q.stem]
        want = [deps_graph.title_of(q)] + [deps_graph.table_row(q, k) for k in ("親の ID", "割り当てたタスク", "状態", "Issue")]
        if cells != want:
            problems.append(f"{q.stem} の一覧の行がファイルと一致しない: {cells} ≠ {want}")
    return problems


def test_question_list_problems_detects_mismatch(tmp_path):
    q = tmp_path / "Q-0001.md"
    q.write_text("# Q-0001: 論点\n\n| 項目 | 内容 |\n| --- | --- |\n| 親の ID | [D-0001](../definitions/D-0001.md) |\n"
                 "| 割り当てたタスク | [T-0001](../tasks/T-0001.md) |\n| 状態 | 未解決 |\n| Issue | [#1](u) |\n", encoding="utf-8")
    row = ("| ID | 論点 | 親の ID | 割り当てたタスク | 状態 | Issue |\n| --- | --- | --- | --- | --- | --- |\n"
           "| [Q-0001](Q-0001.md) | 論点 | [D-0001](../definitions/D-0001.md) | [T-0001](../tasks/T-0001.md) | {} | [#1](u) |\n")
    readme = tmp_path / "README.md"
    readme.write_text(row.format("未解決"), encoding="utf-8")
    assert question_list_problems(readme, [q]) == []
    readme.write_text(row.format("解決"), encoding="utf-8")
    assert question_list_problems(readme, [q])
    readme.write_text("", encoding="utf-8")
    assert question_list_problems(readme, [q])
    readme.write_text(row.format("未解決") + "| Q-0001 | 論点 | x | y | 未解決 | z |\n", encoding="utf-8")
    assert any("形式" in p for p in question_list_problems(readme, [q]))
    # Q が 0 件でも、一覧表（見出しだけ）がなければ失敗する
    header_only = row.split("| [Q-0001]")[0]
    readme.write_text(header_only, encoding="utf-8")
    assert question_list_problems(readme, []) == []
    readme.write_text("# 未解決の点\n", encoding="utf-8")
    assert any("見出し" in p for p in question_list_problems(readme, []))


def test_resolved_question_links_are_not_open_points(tmp_path):
    (tmp_path / "definitions").mkdir()
    (tmp_path / "questions").mkdir()
    d = tmp_path / "definitions" / "D-0001.md"
    d.write_text("# D-0001: d\n\n## 未解決の点\n\n- [Q-0001](../questions/Q-0001.md)：論点\n\n## 履歴\n", encoding="utf-8")
    q = tmp_path / "questions" / "Q-0001.md"
    q.write_text("# Q-0001: 論点\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 未解決 |\n", encoding="utf-8")
    assert open_points(d)
    q.write_text("# Q-0001: 論点\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 解決 |\n", encoding="utf-8")
    assert not open_points(d)
    # リンクの後に別の問いが書き足された行は、論点として数える
    d.write_text("# D-0001: d\n\n## 未解決の点\n\n- [Q-0001](../questions/Q-0001.md)：論点。別の問いもある\n", encoding="utf-8")
    assert open_points(d)


def test_question_problems_detects_errors(tmp_path):
    for d in ("definitions", "tasks", "questions"):
        (tmp_path / d).mkdir()
    (tmp_path / "definitions" / "D-0001.md").write_text(
        "# D-0001: d\n\n## 未解決の点\n\n- [Q-0001](../questions/Q-0001.md)：論点\n\n## 履歴\n", encoding="utf-8")
    (tmp_path / "tasks" / "T-0001.md").write_text(
        "# T-0001: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 関係する ID | [D-0001](../definitions/D-0001.md) |\n| 状態 | 未着手 |\n",
        encoding="utf-8")
    good = ("# Q-0001: 論点\n\n| 項目 | 内容 |\n| --- | --- |\n| 親の ID | [D-0001](../definitions/D-0001.md) |\n"
            "| 割り当てたタスク | [T-0001](../tasks/T-0001.md) |\n| 状態 | 未解決 |\n"
            "| Issue | [#1](https://github.com/kittenkiki15/point-free-spacetime/issues/1) |\n")
    q = tmp_path / "questions" / "Q-0001.md"
    q.write_text(good, encoding="utf-8")
    assert question_problems(q, tmp_path) == []
    q.write_text(good.replace("| 親の ID | [D-0001](../definitions/D-0001.md) |", "| 親の ID | D-0001 |"), encoding="utf-8")
    assert any("親のファイルへのリンク" in p for p in question_problems(q, tmp_path))
    q.write_text(good.replace("# Q-0001:", "# Q-9999:"), encoding="utf-8")
    assert any("ファイル名と一致" in p for p in question_problems(q, tmp_path))
    q.write_text(good.replace("issues/1)", "issues/2)"), encoding="utf-8")
    assert any(p.startswith("Issue がない") for p in question_problems(q, tmp_path))
    (tmp_path / "definitions" / "D-0001.md").write_text("# D-0001: d\n\n## 未解決の点\n\n- 別の論点\n", encoding="utf-8")
    q.write_text(good, encoding="utf-8")
    assert any("所定の箇条" in p for p in question_problems(q, tmp_path))
    # 元の論点の文の末尾にリンクを添えただけの行は、所定の行とみなさない
    (tmp_path / "definitions" / "D-0001.md").write_text(
        "# D-0001: d\n\n## 未解決の点\n\n- 元の論点の文。[Q-0001](../questions/Q-0001.md)\n", encoding="utf-8")
    assert any("所定の箇条" in p for p in question_problems(q, tmp_path))
    (tmp_path / "definitions" / "D-0001.md").write_text(
        "# D-0001: d\n\n## 未解決の点\n\n- [Q-0001](../questions/Q-0001.md)：論点\n\n## 履歴\n", encoding="utf-8")
    (tmp_path / "tasks" / "T-0001.md").write_text(
        "# T-0001: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 関係する ID | なし |\n| 状態 | 完了 |\n", encoding="utf-8")
    probs = question_problems(q, tmp_path)
    assert any("完了している" in p for p in probs) and any("「関係する ID」に親" in p for p in probs)
    q.write_text(good.replace("| 割り当てたタスク | [T-0001](../tasks/T-0001.md) |",
                              "| 割り当てたタスク | [T-0001](../tasks/T-0001.md)、[T-0002](../tasks/T-0002.md) |"), encoding="utf-8")
    assert any("一つにする" in p for p in question_problems(q, tmp_path))
    q.write_text(good.replace("| 割り当てたタスク | [T-0001](../tasks/T-0001.md) |", "| 割り当てたタスク | T-0001 |"), encoding="utf-8")
    assert any("リンク" in p for p in question_problems(q, tmp_path))
    # 解決した Q でも、割り当てたタスクの欄は検査する
    q.write_text(good.replace("| 状態 | 未解決 |", "| 状態 | 解決 |").replace(
        "| 割り当てたタスク | [T-0001](../tasks/T-0001.md) |", "| 割り当てたタスク | なし |"), encoding="utf-8")
    assert any("一つにする" in p for p in question_problems(q, tmp_path))


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


def tq_link_problems(root):
    """logs/ を除くすべての Markdown のファイルで、タスクと Q の ID のリンクが、その ID の実在するファイル
    （tasks/T-NNNN.md・questions/Q-NNNN.md）を指すか（第 30 回。PR #68 のレビューと、その後のリンクの付け替え）。"""
    problems = []
    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root).parts
        if rel[0] in ("logs", ".git") or "node_modules" in rel:
            continue
        for shown, target in deps_graph.LINK_RE.findall(md.read_text(encoding="utf-8")):
            if not re.fullmatch(r"[TQ]-\d{4}", shown):
                continue
            expected = (root / ("tasks" if shown[0] == "T" else "questions") / f"{shown}.md").resolve()
            resolved = (md.parent / target.split("#")[0]).resolve()
            if resolved != expected:
                problems.append(f"{md.relative_to(root)}: {shown} のリンク先が違う（{target}）")
            elif not expected.is_file():
                problems.append(f"{md.relative_to(root)}: {shown} のファイルがない")
    return problems


def test_task_and_q_links_in_all_markdown_files():
    assert tq_link_problems(ROOT) == []


def test_tq_link_problems_detects_wrong_targets_and_missing_files(tmp_path):
    for d in ("questions", "tasks", "logs", "definitions"):
        (tmp_path / d).mkdir()
    (tmp_path / "tasks" / "T-0001.md").write_text("# T-0001: t\n", encoding="utf-8")
    (tmp_path / "NEXT.md").write_text("[Q-9999](questions/Q-9999.md)、[T-0001](tasks/T-0001.md)\n", encoding="utf-8")
    # 4 節を移す前の roadmap.md を指すタスクのリンク
    (tmp_path / "definitions" / "D-0001.md").write_text("[T-0001](../roadmap.md)\n", encoding="utf-8")
    (tmp_path / "logs" / "x.md").write_text("[Q-9998](../questions/Q-9998.md)\n", encoding="utf-8")  # logs/ は除く
    assert tq_link_problems(tmp_path) == ["NEXT.md: Q-9999 のファイルがない",
                                          "definitions/D-0001.md: T-0001 のリンク先が違う（../roadmap.md）"]


def test_related_ids_reads_shown_ids_only():
    assert related_ids("[D-0002](../definitions/D-0001.md)") == {"D-0002"}
    # リンクでない裸の ID は、割り当てとして数えない
    assert related_ids("[C-0002](c.md)。D-0001 は扱わない") == {"C-0002"}
    assert related_ids("[C-0002](c.md)〜[C-0004](c.md)") == {"C-0002", "C-0003", "C-0004"}


def test_issue_problems_accepts_old_repo_issue_only_for_done_tasks(tmp_path):
    # 旧リポジトリ（非公開）で閉じた Issue は、完了したタスクにだけ許す（第 32 回）
    done = tmp_path / "T-0025.md"
    done.write_text("# T-0025: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 完了 |\n"
                    "| Issue | 旧リポジトリ（非公開）の Issue #67 |\n", encoding="utf-8")
    assert issue_problems([], [done]) == []
    open_task = tmp_path / "T-0004.md"
    open_task.write_text("# T-0004: t\n\n| 項目 | 内容 |\n| --- | --- |\n| 状態 | 未着手 |\n"
                         "| Issue | 旧リポジトリ（非公開）の Issue #53 |\n", encoding="utf-8")
    assert issue_problems([], [open_task])
