import Mathlib.Topology.Order.Category.FrameAdjunction

/-!
# 完備ブール代数の点とアトム

完備ブール代数（をフレームとみなしたロケール）の点は、アトムと一対一に対応する。
[調査メモ 1 節](../../surveys/2026-09-25_02_pointfree-topology-basics.md) の証明の 4 段に沿って形式化する。

Mathlib では、フレーム `L` の点を、フレーム準同型 `L → Prop`（`Locale.PT L`）として定義している。
点 `x` に対して、集合 `{b | x b}` が完全素フィルターにあたる。

## 主な結果

* `PointFreeSpacetime.ptEquivPrime`：フレームの点と素元の一対一対応（1 段目）。
* `PointFreeSpacetime.IsPrimeElement.isCoatom`：完備ブール代数の素元は余アトム（2 段目）。
* `PointFreeSpacetime.ptEquivAtom`：完備ブール代数の点とアトムの一対一対応（3・4 段目）。
* `PointFreeSpacetime.isEmpty_pt_of_forall_not_isAtom`：アトムを持たない完備ブール代数は点を持たない。
-/

open Locale

namespace PointFreeSpacetime

variable {L : Type*}

/-- 素元（prime element）：`p ≠ 1` で、`a ∧ b ≤ p` ならば `a ≤ p` または `b ≤ p` となる元。 -/
def IsPrimeElement [Lattice L] [OrderTop L] (p : L) : Prop :=
  p ≠ ⊤ ∧ ∀ a b : L, a ⊓ b ≤ p → a ≤ p ∨ b ≤ p

/-! ### 1 段目：フレームの点と素元の対応 -/

section Frame

variable [Order.Frame L]

/-- 点 `x` に対応する素元：完全素フィルター `{b | x b}` の補集合の結び。 -/
def ptPrime (x : PT L) : L :=
  sSup {b | ¬ x b}

/-- 点 `x` は、対応する素元を含まない（完全素性による）。 -/
theorem not_apply_ptPrime (x : PT L) : ¬ x (ptPrime x) := by
  intro h
  rw [ptPrime, map_sSup] at h
  obtain ⟨_, ⟨b, hb, rfl⟩, hxb⟩ := h
  exact hb hxb

/-- 点 `x` が `b` を含むのは、`b` が対応する素元以下でないときである。
すなわち、完全素フィルターは素元の下集合の補集合になる。 -/
theorem apply_iff_not_le_ptPrime (x : PT L) (b : L) : x b ↔ ¬ b ≤ ptPrime x := by
  constructor
  · intro hb hle
    exact not_apply_ptPrime x (OrderHomClass.mono x hle hb)
  · intro hle
    by_contra hb
    exact hle (le_sSup hb)

/-- 点に対応する元は素元である。 -/
theorem isPrimeElement_ptPrime (x : PT L) : IsPrimeElement (ptPrime x) := by
  refine ⟨fun h => ?_, fun a b hab => ?_⟩
  · have : x ⊤ := by rw [map_top]; trivial
    exact not_apply_ptPrime x (h ▸ this)
  · by_contra h
    push Not at h
    rw [← apply_iff_not_le_ptPrime, ← apply_iff_not_le_ptPrime] at h
    have : x (a ⊓ b) := by rw [map_inf]; exact h
    exact (apply_iff_not_le_ptPrime x _).1 this hab

/-- 素元 `p` から作る点：`p` 以下でない元全体（完全素フィルター）。 -/
def primePt (p : L) (hp : IsPrimeElement p) : PT L where
  toFun b := ¬ b ≤ p
  map_inf' a b := by
    apply propext
    constructor
    · intro h
      exact ⟨fun ha => h (inf_le_left.trans ha), fun hb => h (inf_le_right.trans hb)⟩
    · rintro ⟨ha, hb⟩ hab
      exact (hp.2 a b hab).elim ha hb
  map_top' := by
    apply propext
    exact ⟨fun _ => trivial, fun _ h => hp.1 (top_le_iff.1 h)⟩
  map_sSup' s := by
    apply propext
    simp only [sSup_le_iff, not_forall, sSup_Prop_eq, Set.mem_image, exists_prop]
    constructor
    · rintro ⟨b, hb, hbp⟩
      exact ⟨_, ⟨b, hb, rfl⟩, hbp⟩
    · rintro ⟨_, ⟨b, hb, rfl⟩, hbp⟩
      exact ⟨b, hb, hbp⟩

@[simp]
theorem primePt_apply (p : L) (hp : IsPrimeElement p) (b : L) :
    primePt p hp b ↔ ¬ b ≤ p :=
  Iff.rfl

/-- **1 段目**：フレームの点（完全素フィルター）と素元は一対一に対応する。 -/
def ptEquivPrime : PT L ≃ {p : L // IsPrimeElement p} where
  toFun x := ⟨ptPrime x, isPrimeElement_ptPrime x⟩
  invFun p := primePt p.1 p.2
  left_inv x := by
    ext b
    exact (apply_iff_not_le_ptPrime x b).symm
  right_inv p := by
    apply Subtype.ext
    change sSup {b | ¬ ¬ b ≤ p.1} = p.1
    simp only [not_not]
    exact csSup_Iic

end Frame

/-! ### 2〜4 段目：完備ブール代数の場合 -/

section CompleteBooleanAlgebra

variable [CompleteBooleanAlgebra L]

/-- **2 段目**：完備ブール代数（一般にブール代数）の素元は余アトムである。
`p < q` なら、`q ∧ ¬q = 0 ≤ p` と素性から `¬q ≤ p < q` となり、`q = 1` を得る。 -/
theorem IsPrimeElement.isCoatom {p : L} (hp : IsPrimeElement p) : IsCoatom p := by
  refine ⟨hp.1, fun q hpq => ?_⟩
  rcases hp.2 q qᶜ (by simp) with hq | hq
  · exact absurd hq (not_le_of_gt hpq)
  · exact compl_le_self.1 (hq.trans hpq.le)

/-- 余アトム `p` について、`b ≤ p` でないことと `¬p ≤ b` は同値である（`¬p` はアトム）。 -/
theorem IsCoatom.not_le_iff_compl_le {p : L} (hp : IsCoatom p) (b : L) :
    ¬ b ≤ p ↔ pᶜ ≤ b := by
  rw [← hp.compl.not_disjoint_iff_le, disjoint_compl_left_iff]

/-- **4 段目**：アトム `a` から作る点 `↑a`。
任意の部分集合 `S` について `a ≤ ⋁ S` ならある `s ∈ S` で `a ≤ s` となる（`IsAtom.le_sSup`）ので、
`↑a` は完全素フィルターである。 -/
def atomPt (a : L) (ha : IsAtom a) : PT L where
  toFun b := a ≤ b
  map_inf' b c := propext le_inf_iff
  map_top' := propext ⟨fun _ => trivial, fun _ => le_top⟩
  map_sSup' s := by
    apply propext
    rw [ha.le_sSup]
    simp only [sSup_Prop_eq, Set.mem_image]
    constructor
    · rintro ⟨b, hb, hab⟩
      exact ⟨_, ⟨b, hb, rfl⟩, hab⟩
    · rintro ⟨_, ⟨b, hb, rfl⟩, hab⟩
      exact ⟨b, hb, hab⟩

@[simp]
theorem atomPt_apply (a : L) (ha : IsAtom a) (b : L) : atomPt a ha b ↔ a ≤ b :=
  Iff.rfl

/-- アトム `a` から作る点に対応する素元は `¬a` である。 -/
theorem ptPrime_atomPt (a : L) (ha : IsAtom a) : ptPrime (atomPt a ha) = aᶜ := by
  have : {b | ¬ atomPt a ha b} = Set.Iic aᶜ := by
    ext b
    simp [ha.not_le_iff_disjoint, le_compl_iff_disjoint_right, disjoint_comm]
  rw [ptPrime, this, csSup_Iic]

/-- **3・4 段目**：完備ブール代数の点とアトムは一対一に対応する。
点 `x` には、対応する素元（余アトム）の否定 `¬p` を対応させ、このとき完全素フィルターは `↑(¬p)` になる。
逆に、アトム `a` には点 `↑a` を対応させる。 -/
def ptEquivAtom : PT L ≃ {a : L // IsAtom a} where
  toFun x := ⟨(ptPrime x)ᶜ, (isPrimeElement_ptPrime x).isCoatom.compl⟩
  invFun a := atomPt a.1 a.2
  left_inv x := by
    ext b
    change (ptPrime x)ᶜ ≤ b ↔ x b
    rw [apply_iff_not_le_ptPrime,
      IsCoatom.not_le_iff_compl_le (isPrimeElement_ptPrime x).isCoatom b]
  right_inv a := by
    apply Subtype.ext
    simp [ptPrime_atomPt]

/-- 点 `x` が `b` を含むのは、`x` に対応するアトムが `b` 以下のときである。
すなわち、点に対応する完全素フィルターは `↑(¬p)` に等しい。 -/
theorem apply_iff_ptEquivAtom_le (x : PT L) (b : L) : x b ↔ (ptEquivAtom x : L) ≤ b := by
  conv_lhs => rw [← ptEquivAtom.symm_apply_apply x]
  rfl

/-- 系：アトムを持たない完備ブール代数は点を持たない。
非自明（`⊥ ≠ ⊤`）なら、自明でないのに点を持たないロケールを与える。 -/
theorem isEmpty_pt_of_forall_not_isAtom (h : ∀ a : L, ¬ IsAtom a) : IsEmpty (PT L) :=
  ⟨fun x => h _ (ptEquivAtom x).2⟩

end CompleteBooleanAlgebra

end PointFreeSpacetime
