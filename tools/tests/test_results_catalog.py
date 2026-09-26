"""results/（検証済みの結果の一覧）と、Lean・テストの成果物の対応を確かめる。"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "results"
SOURCES = sorted((ROOT / "lean" / "PointFreeSpacetime").glob("*.lean")) + sorted(
    (ROOT / "sim").glob("**/*.py")
)


def result_files():
    return sorted(RESULTS.glob("R-[0-9][0-9][0-9][0-9].md"))


def test_readme_lists_every_result():
    readme = (RESULTS / "README.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"^\| \[(R-\d{4})\]\((R-\d{4})\.md\)", readme, re.M))
    assert all(a == b for a, b in listed)
    assert {a for a, _ in listed} == {f.stem for f in result_files()}


def test_each_file_has_matching_title():
    for f in result_files():
        first = f.read_text(encoding="utf-8").splitlines()[0]
        assert first.startswith(f"# {f.stem}: "), f


def linked_files(md: Path, text: str | None = None) -> list[Path]:
    """Markdown のリンクのうち、リポジトリ内のファイルを指すものを解決して返す。"""
    text = md.read_text(encoding="utf-8") if text is None else text
    paths = []
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        paths.append((md.parent / target.split("#")[0]).resolve())
    return paths


def lean_doc(lean: str, name: str):
    """宣言 name（名前空間の接頭辞を除いた最後の部分でもよい）の直前の文書コメントを返す。なければ None。"""
    last = name.split(".")[-1]
    pat = re.compile(
        r"/--((?:(?!-/).)*?)-/\s*(?:@\[[^\]]*\]\s*)?(?:theorem|def|lemma) "
        rf"(?:{re.escape(name)}|{re.escape(last)})\b",
        re.S,
    )
    m = pat.search(lean)
    return m.group(1) if m else None


def docstring_of_test(tests: str, name: str):
    """テスト関数 name の docstring を返す。なければ None。"""
    m = re.search(rf'^def {name}\([^)]*\):\n    """(.*?)"""', tests, re.M | re.S)
    return m.group(1) if m else None


def read_linked(paths: list[Path], pred) -> str:
    return "\n".join(p.read_text(encoding="utf-8") for p in paths if pred(p))


def test_links_exist():
    for md in [RESULTS / "README.md", *result_files()]:
        for path in linked_files(md):
            assert path.exists(), (md, path)


def test_cited_lean_names_exist_in_linked_files_and_carry_id():
    for f in result_files():
        lean = read_linked(linked_files(f), lambda p: p.suffix == ".lean")
        for name in re.findall(r"`PointFreeSpacetime\.([\w.]+)`", f.read_text(encoding="utf-8")):
            doc = lean_doc(lean, name)
            assert doc is not None, (f, name, "リンク先の Lean ファイルに宣言か文書コメントがない")
            assert f.stem in doc, (f, name, "文書コメントに R-ID がない")


def test_cited_test_functions_exist_in_linked_files_and_carry_id():
    for f in result_files():
        tests = read_linked(linked_files(f), lambda p: p.name.startswith("test_"))
        for name in re.findall(r"`(test_\w+)`", f.read_text(encoding="utf-8")):
            doc = docstring_of_test(tests, name)
            assert doc is not None, (f, name, "リンク先のテストファイルに関数か docstring がない")
            assert f.stem in doc, (f, name, "docstring に R-ID がない")


def test_readme_rows_match_linked_files():
    # 列：ID、結果、種類、検証、成果物、初出。検証の欄に応じて、成果物の欄を検査する
    readme = RESULTS / "README.md"
    for row in readme.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| \[(R-\d{4})\]", row)
        if not m:
            continue
        rid = m.group(1)
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        verification, artifacts = cells[3], cells[4]
        paths = linked_files(readme, artifacts)
        assert paths, (rid, "成果物の欄にリンクがない")
        names = re.findall(r"\)：`(\w+)`", artifacts)
        lean = read_linked(paths, lambda p: p.suffix == ".lean")
        tests = read_linked(paths, lambda p: p.name.startswith("test_"))
        if "Lean" in verification:
            lean_names = [n for n in names if not n.startswith("test_")]
            assert lean_names, (rid, "Lean の宣言名がない")
            for name in lean_names:
                doc = lean_doc(lean, name)
                assert doc is not None and rid in doc, (rid, name)
        if "テスト" in verification:
            test_names = [n for n in names if n.startswith("test_")]
            assert test_names, (rid, "テスト関数名がない")
            for name in test_names:
                doc = docstring_of_test(tests, name)
                assert doc is not None and rid in doc, (rid, name)
        # 自然言語の証明・数値実験のスクリプトなどは、リンク先の存在（test_links_exist）だけを確かめる


def test_ids_in_sources_have_files():
    ids = {f.stem for f in result_files()}
    for p in SOURCES:
        for rid in re.findall(r"R-\d{4}", p.read_text(encoding="utf-8")):
            assert rid in ids, (p, rid)
