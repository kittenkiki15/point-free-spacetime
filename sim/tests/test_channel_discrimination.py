from fractions import Fraction

from pfs_sim.channel_discrimination import HHLW_EXAMPLE_1, adaptive, best, nonadaptive


def test_hhlw_example_1_recomputed():
    """Harrow ほか 2010 の例 1 の検算（第 22 回の調査メモの 2.6 節）。

    原典が最良とする非適応的な方式（両方の入力を 1 番目）は 7/9 を与えるが、両方を 2 番目にすると 68/81 になる。
    原典が最良とする適応的な方式（k = 2、f(1) = 2、f(2) = 1）は、原典の (5) 式で 139/162 を与える（原典の値は 65/81）。
    """
    m = HHLW_EXAMPLE_1
    assert nonadaptive(m, 0, 0) == Fraction(7, 9)
    assert nonadaptive(m, 1, 1) == Fraction(68, 81)
    assert adaptive(m, 1, (1, 0)) == Fraction(139, 162)
    assert best(m) == (Fraction(68, 81), Fraction(139, 162))
    assert best(m)[1] > best(m)[0]
