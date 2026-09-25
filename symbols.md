# 記号一覧

本プロジェクトの文書と Lean のコードで使う記号です。分野ごとに、初出の順に並べます。
用語の説明は [用語一覧](glossary.md) を参照してください。数式の書き方は [数式の書き方](docs/math-guide.md) に従います。

- 「Lean」の列は、Lean 4 と Mathlib での対応する記法・名前です。空欄は、対応するものをまだ確認していないことを表します。
- 初出の列は、その記号を最初に使った文書です。

## 順序と束

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`a ≤ b`$ | a は b 以下 | 束・順序集合の順序。開集合では包含 $`⊆`$ | `a ≤ b` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`a ∧ b`$ | a と b の交わり（meet） | 二つの元の最大下界。開集合では共通部分 $`∩`$ | `a ⊓ b` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`a ∨ b`$ | a と b の結び（join） | 二つの元の最小上界。開集合では合併 $`∪`$ | `a ⊔ b` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`⋁ S`$、$`⋁_{i} b_i`$ | S の結び | 任意個の元の最小上界 | `sSup S`、`⨆ i, b i` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`⋀ S`$ | S の交わり | 任意個の元の最大下界 | `sInf S`、`⨅ i, b i` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`0`$、$`1`$ | 最小元、最大元 | 束の最小元・最大元。開集合では空集合と全体 | `⊥`、`⊤` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`a → b`$ | a ならば b | ハイティング代数の含意。$`⋁\{c : c ∧ a ≤ b\}`$ | `a ⇨ b` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`¬a`$ | a の否定（擬補元） | $`a → 0`$。開集合では補集合の内部 | `aᶜ` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`↑a`$ | a の上集合 | $`\{x : a ≤ x\}`$。a で生成される主フィルター | `Set.Ici a` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`↓a`$ | a の下集合 | $`\{x : x ≤ a\}`$。a で生成される主イデアル | `Set.Iic a` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`2`$ | 二元束 | $`\{0, 1\}`$。ロケール $`L`$ の点は、フレーム準同型 $`L → 2`$（ロケールとしては逆向きの射） | `Prop` または `Bool` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |

## 位相とロケール

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`𝒪(X)`$ | X の開集合フレーム | 位相空間 X の開集合全体のなすフレーム | `TopologicalSpace.Opens X` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`\mathrm{Frm}`$ | フレームの圏 | 対象はフレーム、射はフレーム準同型 | `Frm` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`\mathrm{Loc}`$ | ロケールの圏 | $`\mathrm{Frm}`$ の反対圏 | `Locale` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`\mathrm{Top}`$ | 位相空間の圏 | 対象は位相空間、射は連続写像 | `TopCat` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`\mathrm{pt}(L)`$ | L の点の空間 | ロケール L の点全体に位相を入れた空間 | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`f^{-1}`$ | f の逆像 | 連続写像 $`f : X → Y`$ から得られるフレーム準同型 $`𝒪(Y) → 𝒪(X)`$ | `Opens.comap f` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`j`$ | 核 | フレーム上の核（部分ロケールを定める） | `Nucleus` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |

## 圏論

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`F ⊣ G`$ | F は G の左随伴 | $`F(a) ≤ b ⟺ a ≤ G(b)`$（順序集合の場合） | `GaloisConnection F G`、`F ⊣ G` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`𝒞^{\mathrm{op}}`$ | 𝒞 の反対圏 | 射の向きを逆にした圏 | `𝒞ᵒᵖ` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |

## 様相論理・時制論理

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`□`$ | ボックス、必然 | 様相演算子。位相的な S4（すべての部分集合 $`𝒫(X)`$ 上の演算）では内部をとる操作 | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`◇`$ | ダイヤモンド、可能 | 様相演算子。$`𝒫(X)`$ 上の古典的な補集合 $`∖`$ を使って $`X ∖ □(X ∖ A)`$ と定め、閉包をとる操作になる。開集合フレームの擬補元 $`¬`$ とは別物で、開集合 $`U`$ の $`¬¬U`$ は閉包の内部 | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`○`$ | 遅延様相 | 核に対応する様相演算子 | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`P`$、$`F`$ | 過去の ◇、未来の ◇ | 「過去のどこかで」「未来のどこかで」成り立つ | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`H`$、$`G`$ | 過去の □、未来の □ | 「過去のすべてで」「未来のすべてで」成り立つ。$`P ⊣ G`$、$`F ⊣ H`$ | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |

## 時空の因果構造

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`I^+(S)`$ | S の時間的未来 | S のある点から未来向きの時間的曲線で到達できる点全体（開集合） | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`I^-(S)`$ | S の時間的過去 | $`I^+`$ の時間を反転したもの | | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
