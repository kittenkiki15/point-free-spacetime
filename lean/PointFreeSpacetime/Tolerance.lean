import Mathlib.Order.GaloisConnection.Basic
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

/-! ### 点なしへの持ち上げ

順序集合（たとえばフレーム）`α` 上の単調な写像 `N`（膨張：領域を、操作的に区別できない
ところまで広げる）から、余白付きの包含を `N a ≤ b` と定める。上の点の場合は、
`N a` が `a` の `T` 近傍にあたる（`marginSub_iff_image_subset`）。 -/

/-- 点の場合の余白付きの包含は、`T` 近傍（`T` による像）の包含と同じである。 -/
theorem marginSub_iff_image_subset (T : X → X → Prop) (a b : Set X) :
    MarginSub T a b ↔ {y | ∃ x ∈ a, T x y} ⊆ b := by
  constructor
  · rintro h y ⟨x, hx, hxy⟩
    exact h x y hx hxy
  · intro h x y hx hxy
    exact h ⟨x, hx, hxy⟩

/-- 単調な `N` について、余白付きの包含 `N a ≤ b` が補間的であることと、
`N (N a) ≤ N a`（膨張を重ねても広がらない）は同値である。
点の場合の `marginSub_interpolates_iff` の点なし版にあたる。 -/
theorem margin_interpolates_iff {α : Type*} [Preorder α] (N : α → α) (hN : Monotone N) :
    (∀ a b, N a ≤ b → ∃ c, N a ≤ c ∧ N c ≤ b) ↔ ∀ a, N (N a) ≤ N a := by
  constructor
  · intro h a
    obtain ⟨c, hac, hcb⟩ := h a (N a) le_rfl
    exact (hN hac).trans hcb
  · intro h a b hab
    exact ⟨N a, le_rfl, (h a).trans hab⟩

/-- 膨張 `N` が右随伴（収縮 `E`）を持つとき、オープニング `N ∘ E`（型 I の「小さすぎる
部分を削る」操作）の不動点は、ちょうど `N` の像である。型 I と型 II は、同じ随伴 `N ⊣ E`
の二つの面になっている。 -/
theorem opening_fixed_iff_mem_range {α : Type*} [PartialOrder α] {N E : α → α}
    (gc : GaloisConnection N E) (b : α) : N (E b) = b ↔ b ∈ Set.range N := by
  constructor
  · intro h
    exact ⟨E b, h⟩
  · rintro ⟨a, rfl⟩
    exact gc.l_u_l_eq_l a

end PointFreeSpacetime
