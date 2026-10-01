"""古典的な通信路の識別で、2 回の使用での非適応的な方式と適応的な方式の成功確率を厳密に数え上げる。

Harrow–Hassidim–Leung–Watrous (2010, arXiv:0909.0256v1) の 5 節の例 1 の検算に使う
（第 22 回の調査メモ surveys/2026-10-01_22_combs-and-composites.md の 2.6 節）。
事前確率は等しい（各 1/2）とし、判定は最尤（成功確率は 1/2 + (1/4)‖P0 − P1‖₁）とする。
"""

from fractions import Fraction
from itertools import product

# 通信路 a の確率行列 M[a][j][k] = Pr(出力 j | 入力 k)。原典の M0、M1（列が入力、行が出力）。
HHLW_EXAMPLE_1 = [
    [[Fraction(1, 3), Fraction(8, 9)], [Fraction(2, 3), Fraction(1, 9)]],
    [[Fraction(0), Fraction(1, 3)], [Fraction(1), Fraction(2, 3)]],
]


def success(p0, p1):
    """事前確率が等しい二つの分布（同じ添字の列）を最尤で判定したときの成功確率。"""
    return Fraction(1, 2) + Fraction(1, 4) * sum(abs(a - b) for a, b in zip(p0, p1))


def nonadaptive(m, k1, k2):
    """入力 (k1, k2) をあらかじめ固定した 2 回の使用の成功確率。"""
    n = len(m[0])
    dist = [[m[a][j1][k1] * m[a][j2][k2] for j1 in range(n) for j2 in range(n)] for a in range(2)]
    return success(*dist)


def adaptive(m, k, f):
    """1 回目の入力 k、1 回目の出力 j に応じて 2 回目の入力 f[j] を選ぶ方式の成功確率（原典の (5) 式の各項）。"""
    n = len(m[0])
    dist = [[m[a][j1][k] * m[a][j2][f[j1]] for j1 in range(n) for j2 in range(n)] for a in range(2)]
    return success(*dist)


def best(m):
    """非適応的な方式と適応的な方式（出力から入力への写像をすべて列挙）の最良の成功確率。"""
    n_in, n_out = len(m[0][0]), len(m[0])
    best_na = max(nonadaptive(m, k1, k2) for k1 in range(n_in) for k2 in range(n_in))
    best_ad = max(adaptive(m, k, f) for k in range(n_in) for f in product(range(n_in), repeat=n_out))
    return best_na, best_ad
