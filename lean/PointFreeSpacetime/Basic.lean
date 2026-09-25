import Mathlib.Topology.Order.Category.FrameAdjunction

/-!
# 基本事項

点なし位相（point-free topology）の基本的な対象が Mathlib で使えることを確認する。
-/

namespace PointFreeSpacetime

/-- フレームでは、有限の交わりが任意の結びに対して分配する（添字付きの結び）。
これがフレームを特徴づける分配律である。 -/
example {L : Type*} [Order.Frame L] {ι : Type*} (a : L) (f : ι → L) :
    a ⊓ ⨆ i, f i = ⨆ i, a ⊓ f i :=
  inf_iSup_eq a f

/-- 同じ分配律を、部分集合の上限で述べたもの。 -/
example {L : Type*} [Order.Frame L] (a : L) (s : Set L) :
    a ⊓ sSup s = ⨆ b ∈ s, a ⊓ b :=
  inf_sSup_eq

/-- 特に、二項の結びに対する分配律が成り立つ。 -/
example {L : Type*} [Order.Frame L] (a b c : L) :
    a ⊓ (b ⊔ c) = (a ⊓ b) ⊔ (a ⊓ c) :=
  inf_sup_left a b c

end PointFreeSpacetime
