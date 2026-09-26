import Mathlib.Order.Basic
import Mathlib.Data.Set.Basic

/-!
# 識別の関係と、余白付きの包含の補間性

集合 `X` 上の関係 `T`（`T x y` は「`x` と `y` は区別できないほど近い」と読む）から、
部分集合の間の「余白付きの包含」`a ◁ b`（`a` の `T` 近傍が `b` に含まれる）を作る。
`T` が推移的であることと、`◁` が補間的（`a ◁ b` なら `a ◁ c ◁ b` となる `c` がある）で
あることは同値である。距離 `ℓ` 以内の関係のように推移的でない関係では、余白を二つに
分けられない。第 05 回の案 D（余白の下限）の出発点。
-/

namespace PointFreeSpacetime

variable {X : Type*}

/-- `T` による余白付きの包含：`a` の点と `T` で結ばれる点は、すべて `b` に属する。 -/
def MarginSub (T : X → X → Prop) (a b : Set X) : Prop :=
  ∀ x y, x ∈ a → T x y → y ∈ b

/-- 余白付きの包含が補間的であることと、`T` が推移的であることは同値である。
反射性などの仮定は要らない。 -/
theorem marginSub_interpolates_iff (T : X → X → Prop) :
    (∀ a b, MarginSub T a b → ∃ c, MarginSub T a c ∧ MarginSub T c b) ↔
      ∀ x y z, T x y → T y z → T x z := by
  constructor
  · intro h x y z hxy hyz
    obtain ⟨c, hac, hcb⟩ := h {x} {w | T x w} (by
      rintro x' w rfl hw
      exact hw)
    exact hcb y z (hac x y rfl hxy) hyz
  · intro htr a b hab
    refine ⟨{y | ∃ x ∈ a, T x y}, fun x y hx hxy => ⟨x, hx, hxy⟩, ?_⟩
    rintro y z ⟨x, hx, hxy⟩ hyz
    exact hab x z hx (htr x y z hxy hyz)

end PointFreeSpacetime
