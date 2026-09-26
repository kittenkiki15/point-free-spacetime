import Mathlib.Order.Lattice
import Mathlib.Order.BoundedOrder.Basic

/-!
# 平行性の不等式 (f±) と共役

heunen2026 の平行な順序付きロケールでは、局所的な錐 `↟`・`↡` が次の不等式 (f±) を満たす。

  `↟U ∧ V ≤ ↟(U ∧ ↡V)`、`↡U ∧ V ≤ ↡(U ∧ ↟V)`

ここから、Jónsson–Tarski の共役の条件 `↟U ∧ V = 0 ↔ U ∧ ↡V = 0` が出る。
この向きには補元も分配律も要らず、交わり半束で `f ⊥ = ⊥`・`g ⊥ = ⊥` だけを使う。
逆向きは一般のフレームでは成り立たない（結果 R-0005、`sim/tests/test_conjugate.py`）。

## 主な結果

* `PointFreeSpacetime.conjugate_of_fpm`：(f±) ならば共役（結果 R-0004）。
-/

namespace PointFreeSpacetime

variable {L : Type*} [SemilatticeInf L] [OrderBot L]

/-- **結果 R-0004**：`f ⊥ = ⊥`・`g ⊥ = ⊥` を満たす写像 `f`・`g` が不等式 (f±)

  `f U ⊓ V ≤ f (U ⊓ g V)`、`g V ⊓ U ≤ g (V ⊓ f U)`

を満たすなら、共役の条件 `f U ⊓ V = ⊥ ↔ U ⊓ g V = ⊥` が成り立つ。
heunen2026 の命題 3.10（平行性から `↟U ∧ V = ∅ ↔ U ∧ ↡V = ∅`）の抽象化にあたる。 -/
theorem conjugate_of_fpm (f g : L → L) (hf : f ⊥ = ⊥) (hg : g ⊥ = ⊥)
    (h₁ : ∀ U V, f U ⊓ V ≤ f (U ⊓ g V)) (h₂ : ∀ U V, g V ⊓ U ≤ g (V ⊓ f U))
    (U V : L) : f U ⊓ V = ⊥ ↔ U ⊓ g V = ⊥ := by
  constructor
  · intro h
    rw [eq_bot_iff, inf_comm, ← hg]
    refine (h₂ U V).trans (le_of_eq ?_)
    rw [inf_comm, h]
  · intro h
    rw [eq_bot_iff, ← hf]
    refine (h₁ U V).trans (le_of_eq ?_)
    rw [h]

end PointFreeSpacetime
