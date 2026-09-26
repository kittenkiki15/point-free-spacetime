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


def test_cited_lean_names_exist_and_carry_id():
    lean = "\n".join(p.read_text(encoding="utf-8") for p in SOURCES if p.suffix == ".lean")
    for f in result_files():
        for name in re.findall(r"`PointFreeSpacetime\.([\w.]+)`", f.read_text(encoding="utf-8")):
            doc = lean_doc(lean, name)
            assert doc is not None, (f, name, "宣言か文書コメントがない")
            assert f.stem in doc, (f, name, "文書コメントに R-ID がない")


def test_cited_test_functions_exist_and_carry_id():
    tests = "\n".join(p.read_text(encoding="utf-8") for p in SOURCES if p.name.startswith("test_"))
    for f in result_files():
        for name in re.findall(r"`(test_\w+)`", f.read_text(encoding="utf-8")):
            doc = docstring_of_test(tests, name)
            assert doc is not None, (f, name, "テスト関数か docstring がない")
            assert f.stem in doc, (f, name, "docstring に R-ID がない")


def test_ids_in_sources_have_files():
    ids = {f.stem for f in result_files()}
    for p in SOURCES:
        for rid in re.findall(r"R-\d{4}", p.read_text(encoding="utf-8")):
            assert rid in ids, (p, rid)
