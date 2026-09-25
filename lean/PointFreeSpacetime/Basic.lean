import Mathlib.Topology.Order.Category.FrameAdjunction

/-!
# 基本事項

点なし位相（point-free topology）の基本的な対象が Mathlib で使えることを確認する。
-/

namespace PointFreeSpacetime

/-- フレームでは、有限の交わりが結びに対して分配する。 -/
example {L : Type*} [Order.Frame L] (a b c : L) :
    a ⊓ (b ⊔ c) = (a ⊓ b) ⊔ (a ⊓ c) :=
  inf_sup_left a b c

end PointFreeSpacetime
