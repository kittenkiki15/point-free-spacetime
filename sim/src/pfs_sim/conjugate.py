"""有限の分配束の上で、共役の条件と不等式 (f±) の関係を総当たりで調べる。

heunen2026 の平行性の不等式 (f±)

    f(U) ∧ V ⊑ f(U ∧ g(V)),  g(V) ∧ U ⊑ g(V ∧ f(U))

と、Jónsson–Tarski の共役の条件

    f(U) ∧ V = 0  ⇔  U ∧ g(V) = 0

を比べる（第 04 回）。有限の分配束はフレームなので、フレーム一般での反例探しに使える。
ブール代数では両者は同値だが、フレームでは (f±) ⇒ 共役（結果 R-0004）だけが成り立つ
（逆の反例は結果 R-0005）。

束は、有限半順序集合の下集合全体（包含で順序付け）として作る。どの有限分配束もこの形で表せる
（Birkhoff の表現定理）。
"""

from __future__ import annotations

import itertools
from collections.abc import Callable, Iterable

Elem = frozenset[int]
Map = dict[Elem, Elem]


def downsets(n: int, less: Iterable[tuple[int, int]]) -> list[Elem]:
    """半順序集合 ({0, …, n-1}, less) の下集合全体を返す。less は i < j となる組 (i, j) の集合。"""
    rel = set(less)
    result = []
    for mask in range(1 << n):
        s = frozenset(i for i in range(n) if mask >> i & 1)
        if all(i in s for (i, j) in rel if j in s):
            result.append(s)
    return result


def join_preserving_closures(lattice: list[Elem]) -> list[Map]:
    """有限結び（空の結びを含む）を保つ閉包作用素（増大的で冪等な写像）をすべて返す。"""
    bottom = frozenset()
    maps = []
    for values in itertools.product(lattice, repeat=len(lattice)):
        f = dict(zip(lattice, values))
        if f[bottom] != bottom:
            continue
        if not all(f[x | y] == f[x] | f[y] for x in lattice for y in lattice):
            continue
        if all(x <= f[x] and f[f[x]] == f[x] for x in lattice):
            maps.append(f)
    return maps


def is_conjugate(lattice: list[Elem], f: Map, g: Map) -> bool:
    """共役の条件 f(x) ∧ y = 0 ⇔ x ∧ g(y) = 0 を調べる。"""
    return all(
        (not (f[x] & y)) == (not (x & g[y])) for x in lattice for y in lattice
    )


def satisfies_f_pm(lattice: list[Elem], f: Map, g: Map) -> bool:
    """不等式 (f±) を調べる。"""
    return all(
        (f[x] & y) <= f[x & g[y]] and (g[y] & x) <= g[y & f[x]]
        for x in lattice
        for y in lattice
    )


def compare(lattice: list[Elem]) -> tuple[int, int, list[tuple[Map, Map]]]:
    """閉包作用素の組 (f, g) を総当たりし、(共役の数, (f±) の数, 共役だが (f±) でない組) を返す。

    (f±) なのに共役でない組があれば AssertionError を送出する。
    """
    maps = join_preserving_closures(lattice)
    n_conj = n_fpm = 0
    counterexamples = []
    for f, g in itertools.product(maps, repeat=2):
        conj = is_conjugate(lattice, f, g)
        fpm = satisfies_f_pm(lattice, f, g)
        n_conj += conj
        n_fpm += fpm
        assert conj or not fpm, "(f±) なのに共役でない組がある"
        if conj and not fpm:
            counterexamples.append((f, g))
    return n_conj, n_fpm, counterexamples


# 調べる半順序集合（名前: (元の数, 狭義の順序)）
POSETS: dict[str, tuple[int, set[tuple[int, int]]]] = {
    "chain3": (2, {(0, 1)}),
    "chain4": (3, {(0, 1), (1, 2), (0, 2)}),
    "V": (3, {(0, 2), (1, 2)}),
    "Lambda": (3, {(0, 1), (0, 2)}),
    "2x3": (3, {(0, 1)}),
    "N": (4, {(0, 2), (1, 2), (1, 3)}),
}


def main(print_fn: Callable[[str], None] = print) -> None:
    for name, (n, less) in POSETS.items():
        lattice = downsets(n, less)
        n_conj, n_fpm, ces = compare(lattice)
        print_fn(
            f"{name}: 元 {len(lattice)} 個, 共役 {n_conj} 組, (f±) {n_fpm} 組, "
            f"共役だが (f±) でない {len(ces)} 組"
        )


if __name__ == "__main__":
    main()
