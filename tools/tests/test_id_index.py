"""tools/id_index.py（ID の依存関係と参照箇所の索引、RDF のトリプル）のテスト（第 31 回。T-0025 の 4）。"""

import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import deps_graph  # noqa: E402
import id_index  # noqa: E402

rdflib = pytest.importorskip("rdflib")
PFS = rdflib.Namespace(id_index.PFS)
# 参照形式のリンクの定義（[名前]: path。コロンの後の空白はなくてもよい）
REF_DEF = re.compile(r" {0,3}\[[^\]]+\]:")


@pytest.fixture(scope="module")
def index():
    return id_index.structure(), id_index.mentions()


@pytest.fixture(scope="module")
def graph(index):
    g = rdflib.Graph()
    g.parse(data=id_index.to_turtle(*index), format="turtle")
    return g


def test_turtle_parses_and_uses_only_defined_vocabulary(graph):
    vocab = rdflib.Graph().parse(Path(id_index.__file__).with_name("pfs.ttl"), format="turtle")
    defined = set(vocab.subjects())
    used = {p for p in graph.predicates() if str(p).startswith(id_index.PFS)}
    used |= {o for o in graph.objects(None, rdflib.RDF.type) if str(o).startswith(id_index.PFS)}
    assert used and used <= defined, sorted(used - defined)


def test_every_item_file_is_typed(graph):
    typed = {s for s in graph.subjects(rdflib.RDF.type, None) if (s, rdflib.RDF.type, PFS.Mention) not in graph}
    assert typed == {rdflib.URIRef(id_index.BASE + id_index.id_path(i)) for i in id_index.id_files()}


def test_dependencies_match_deps_graph(index):
    triples, _ = index
    from_index = {(s, o) for s, p, o in triples if p == "pfs:dependsOn"}
    # 自分自身への依存も除かない（誤記を検出するため。PR #72 のレビュー）
    expected = {(i, d) for i, ds in deps_graph.dependencies().items() for d in ds}
    assert from_index == expected


def test_prerequisite_tasks_written_as_bare_ids_are_read(index):
    # 「前提のタスク」は裸の ID で書く（PR #72 のレビュー）
    triples, _ = index
    prereq = {(s, o) for s, p, o in triples if p == "pfs:prerequisite"}
    assert ("T-0026", "T-0025") in prereq and ("T-0005", "T-0023") in prereq


def test_sparql_transitive_dependencies_match_python_and_have_no_cycle(graph):
    # SPARQL のプロパティパスで求めた推移的な依存が、Python で求めたものと一致し、循環がない
    deps = deps_graph.dependencies()

    def closure(i, seen):
        for d in deps.get(i, []):
            if d not in seen:
                seen.add(d)
                closure(d, seen)
        return seen

    python = {(i, d) for i in deps for d in closure(i, set())}
    rows = graph.query("SELECT ?x ?y WHERE { ?x pfs:dependsOn+ ?y }", initNs={"pfs": PFS})
    name = lambda u: str(u).rsplit("/", 1)[1].removesuffix(".md")
    assert {(name(x), name(y)) for x, y in rows} == python
    assert not graph.query("ASK { ?x pfs:dependsOn+ ?x }", initNs={"pfs": PFS}).askAnswer


def test_self_dependency_is_kept_and_detected_as_a_cycle(tmp_path, monkeypatch):
    for d in id_index.DIRS.values():
        (tmp_path / d).mkdir()
    (tmp_path / "definitions" / "D-0001.md").write_text(
        "# D-0001: d\n\n| 項目 | 値 |\n| --- | --- |\n| 依存する ID | [D-0001](D-0001.md) |\n", encoding="utf-8")
    monkeypatch.setattr(id_index, "ROOT", tmp_path)
    monkeypatch.setattr(deps_graph, "ROOT", tmp_path)
    triples = id_index.structure()
    assert ("D-0001", "pfs:dependsOn", "D-0001") in triples
    g = rdflib.Graph().parse(data=id_index.to_turtle(triples, []), format="turtle")
    assert g.query("ASK { ?x pfs:dependsOn+ ?x }", initNs={"pfs": PFS}).askAnswer


def test_sparql_detects_a_cycle():
    g = rdflib.Graph().parse(data=id_index.to_turtle([("D-0001", "pfs:dependsOn", "D-0002"),
                                                      ("D-0002", "pfs:dependsOn", "D-0001")], []),
                             format="turtle")
    assert g.query("ASK { ?x pfs:dependsOn+ ?x }", initNs={"pfs": PFS}).askAnswer


def test_mentions_distinguish_links_and_skip_link_targets(tmp_path, monkeypatch):
    monkeypatch.setattr(id_index, "ROOT", tmp_path)
    md = tmp_path / "x.md"
    md.write_text("# 見出し\n\n[D-0001](definitions/D-0001.md) と C-0002、[説明 A-0003](assumptions/A-0004.md)\n"
                  "[T-0027「リリース」](tasks/T-0027.md)、予想C-0005を検討する\n"
                  "```sh\n# コードの中の行は見出しではない T-0005\n```\n"
                  "````markdown\n```math\n# 入れ子の中も見出しではない\n```\n````\n", encoding="utf-8")
    found = id_index.mentions_in(md)
    assert [(m.target, m.line, m.section, m.linked) for m in found] == [
        # ID のファイルへのリンクは、表示文字によらずリンク先の ID で数え、表示文字のほかの ID はリンクのない言及
        ("D-0001", 3, "見出し", True), ("A-0004", 3, "見出し", True),
        ("C-0002", 3, "見出し", False), ("A-0003", 3, "見出し", False),
        # 表示文字に説明を含むリンクと、日本語に接した ID（PR #72 のレビュー）
        ("T-0027", 4, "見出し", True), ("C-0005", 4, "見出し", False),
        ("T-0005", 6, "見出し", False)]
    # コードブロックの中のリンク記法は、リンクのない言及として数える（PR #72 のレビュー）
    md.write_text("```markdown\n[D-0001](D-0001.md)\n```\n", encoding="utf-8")
    assert [(m.target, m.linked) for m in id_index.mentions_in(md)] == [("D-0001", False), ("D-0001", False)]
    # インラインのコードの中のリンク記法は、リンクのない言及として数える
    md.write_text("例：`[D-0002](D-0002.md)`\n", encoding="utf-8")
    assert [(m.target, m.linked) for m in id_index.mentions_in(md)] == [("D-0002", False), ("D-0002", False)]
    # 改行をまたぐインラインのコードの中のリンク記法も、リンクのない言及として数える
    md.write_text("例：`前半\n[D-0003](D-0003.md)` と [D-0004](D-0004.md)\n", encoding="utf-8")
    assert [(m.target, m.line, m.linked) for m in id_index.mentions_in(md)] == [
        ("D-0003", 2, False), ("D-0003", 2, False), ("D-0004", 2, True)]
    # 長さの違うバッククォートの列は、コードの閉じとみなさない（PR #72 のレビュー）
    md.write_text("`例 ``` [D-0001](D-0001.md) 終わり`\n", encoding="utf-8")
    assert [(m.target, m.linked) for m in id_index.mentions_in(md)] == [("D-0001", False), ("D-0001", False)]
    # 外部のサイトの同じ名前のファイルへのリンクは、ID へのリンクとみなさない
    md.write_text("[外部資料](https://example.org/D-0001.md)、[外部](//example.org/definitions/D-0003.md)、"
                  "[本リポジトリ](" + id_index.BASE + "definitions/D-0002.md)\n",
                  encoding="utf-8")
    assert [(m.target, m.linked) for m in id_index.mentions_in(md)] == [("D-0002", True)]
    # リンク先の後にタイトルを付けたリンク
    for title in ('"定義"', "'定義'", "(定義)"):
        md.write_text(f"[こちら](definitions/D-0001.md {title})\n", encoding="utf-8")
        assert [(m.target, m.linked) for m in id_index.mentions_in(md)] == [("D-0001", True)], title


def test_id_boundaries_exclude_adjacent_ascii_letters():
    # 英字・数字・下線に接した文字列は ID とみなさない。日本語に接した ID は ID とみなす（PR #72 のレビュー）
    assert id_index.ANY_ID.findall("D-0001abc D-0001_x xD-0002 D-00031 予想C-0005を（T-0004）") == ["C-0005", "T-0004"]


def test_no_reference_style_link_definitions():
    # 索引が読むのはインラインのリンクだけなので、参照形式のリンクの定義（[名前]: path）を使わない
    found = [f"{f.relative_to(id_index.ROOT)}:{n}" for f in id_index.source_files() if f.suffix == ".md"
             for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1)
             if REF_DEF.match(line)]
    assert found == []


def test_reference_definition_pattern_detects_forms_without_space():
    assert REF_DEF.match("[参照]:../definitions/D-0001.md") and REF_DEF.match("  [d]: D-0001.md")
    assert not REF_DEF.match("[D-0001](D-0001.md) の説明")


def test_link_ids_reads_links_and_ranges_only():
    value = "[C-0002](C-0002.md)〜[C-0004](C-0004.md)、[T-0001](../tasks/T-0001.md)。D-0001 は扱わない"
    assert id_index.link_ids(value) == ["C-0002", "C-0004", "T-0001", "C-0003"]
    # ID はリンク先のファイルから読み、ID のファイルでないリンク先は関係とみなさない（PR #72 のレビュー）
    assert id_index.link_ids("[C-0002](../conjectures/C-0003.md)、[C-0004](c.md)") == ["C-0003"]
    # 説明付きのリンクを両端にした範囲も展開する（PR #72 のレビュー）
    assert id_index.link_ids("[C-0009 の主張](C-0009.md)〜[C-0011 の主張](C-0011.md)") == ["C-0009", "C-0011", "C-0010"]
    # 表示文字に説明を含むリンクは、リンク先のファイルの ID を読む（PR #72 のレビュー）
    assert id_index.link_ids("[C-0001 の主張](../conjectures/C-0001.md)") == ["C-0001"]


def test_literal_escaping_round_trips():
    text = 'a "b" \\ c\nd'
    g = rdflib.Graph().parse(data=id_index.to_turtle([("D-0001", "pfs:status", ("literal", text))], []),
                             format="turtle")
    assert [str(o) for o in g.objects()] == [text]


def test_json_and_refs(index):
    data = json.loads(id_index.to_json(*index))
    assert len(data["triples"]) == len(index[0]) and len(data["mentions"]) == len(index[1])
    out = id_index.refs("D-0001", *index)
    assert any("pfs:dependsOn D-0001" in line for line in out)
    assert any(line.startswith("  definitions/D-0001.md:1") for line in out)


def test_code_mentions_include_result_ids(index):
    _, ments = index
    assert any(m.source.startswith("lean/") and m.target.startswith("R-") for m in ments)
