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


def test_cited_lean_names_exist():
    lean = "\n".join(p.read_text(encoding="utf-8") for p in SOURCES if p.suffix == ".lean")
    for f in result_files():
        for name in re.findall(r"`PointFreeSpacetime\.([\w.]+)`", f.read_text(encoding="utf-8")):
            last = name.split(".")[-1]
            assert re.search(rf"^(theorem|def|lemma) ({re.escape(name)}|{re.escape(last)})\b", lean, re.M), (f, name)


def test_cited_test_functions_exist():
    tests = "\n".join(p.read_text(encoding="utf-8") for p in SOURCES if p.name.startswith("test_"))
    for f in result_files():
        for name in re.findall(r"`(test_\w+)`", f.read_text(encoding="utf-8")):
            assert re.search(rf"^def {name}\(", tests, re.M), (f, name)


def test_ids_in_sources_have_files():
    ids = {f.stem for f in result_files()}
    for p in SOURCES:
        for rid in re.findall(r"R-\d{4}", p.read_text(encoding="utf-8")):
            assert rid in ids, (p, rid)
