from pfs_sim.conjugate import (
    POSETS,
    compare,
    downsets,
    join_preserving_closures,
    join_preserving_closures_naive,
    is_conjugate,
    satisfies_f_pm,
)


def _key(f):
    return tuple(sorted((tuple(sorted(k)), tuple(sorted(v))) for k, v in f.items()))


def test_enumeration_matches_naive():
    # 結び既約元での値による列挙が、全写像の総当たりと一致する（元が 6 個以下の束）
    for n, less in POSETS.values():
        lattice = downsets(n, less)
        if len(lattice) > 6:
            continue
        fast = sorted(map(_key, join_preserving_closures(lattice)))
        naive = sorted(map(_key, join_preserving_closures_naive(lattice)))
        assert fast == naive


def test_f_pm_implies_conjugate_on_small_lattices():
    """結果 R-0004 の、小さい有限分配束の上での確認（証明は Lean の conjugate_of_fpm）。"""
    # compare は (f±) なのに共役でない組があると AssertionError を送出する
    for n, less in POSETS.values():
        compare(downsets(n, less))


def test_no_counterexample_on_some_lattices():
    # これらの束では、閉包作用素の組について両者が一致する
    for name in ["chain3", "chain4", "V", "2x3"]:
        n, less = POSETS[name]
        n_conj, n_fpm, ces = compare(downsets(n, less))
        assert n_conj == n_fpm and not ces


def test_five_element_counterexample():
    """結果 R-0005：フレームでは、共役ならば (f±) とは限らない。"""
    # 0 < a < b, c < 1 の 5 元の束（0 でない元はすべて a 以上）
    lattice = downsets(*POSETS["Lambda"])
    assert len(lattice) == 5
    bot, a, b, c, top = (
        frozenset(),
        frozenset({0}),
        frozenset({0, 1}),
        frozenset({0, 2}),
        frozenset({0, 1, 2}),
    )
    assert set(lattice) == {bot, a, b, c, top}
    f = {x: x for x in lattice}
    g = {bot: bot, a: a, b: b, c: top, top: top}
    closures = join_preserving_closures(lattice)
    assert f in closures and g in closures
    assert is_conjugate(lattice, f, g)
    assert not satisfies_f_pm(lattice, f, g)
    # 破れる箇所：g(c) ∧ b = b だが g(c ∧ f(b)) = g(a) = a
    assert (g[c] & b) == b and g[c & f[b]] == a
