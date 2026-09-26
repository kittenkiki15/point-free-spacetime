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
| $`F ⊣ G`$ | F は G の左随伴 | 順序集合の間の単調写像では $`F(a) ≤ b ⟺ a ≤ G(b)`$（ガロア接続）。圏の間の関手では、射の集合の自然な全単射 $`\mathrm{Hom}(F(a), b) ≅ \mathrm{Hom}(a, G(b))`$ | 順序集合の写像: `GaloisConnection F G`。関手: `F ⊣ G`（`CategoryTheory.Adjunction`） | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
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
| $`x ≼ y`$ | x は y の因果的過去にある | 時空の因果関係。x から y へ未来向きの因果曲線がある（前順序） | | [調査 03](surveys/2026-09-25_03_heunen2024.md) |
| $`x ≪ y`$ | x は y の時間的過去にある | 時空の時間的関係。x から y へ未来向きの時間的曲線がある | | [調査 03](surveys/2026-09-25_03_heunen2026.md) |
| $`J^+(S)`$、$`J^-(S)`$ | S の因果的未来・過去 | $`≼`$ についての上集合・下集合。滑らかな時空では、開集合 $`U`$ について $`J^±(U) = I^±(U)`$ | | [調査 03](surveys/2026-09-25_03_heunen2024.md) |
| $`↑A`$、$`↓A`$ | A の未来錐・過去錐 | 前順序付き集合の部分集合 $`A`$ の上集合 $`\{y : ∃ x ∈ A,\ x ≤ y\}`$ と下集合 | `upperClosure A`、`lowerClosure A` | [調査 03](surveys/2026-09-25_03_heunen2024.md) |
| $`A^◦`$ | A の内部 | 部分集合 $`A`$ に含まれる最大の開集合 | `interior A` | [調査 03](surveys/2026-09-25_03_heunen2024.md) |

## 順序付きロケールと因果被覆

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`U ⊑ V`$ | U は V に含まれる | ロケールの開集合フレームの順序（包含）。空間の点の順序 $`≤`$ と区別するために使う | `U ≤ V` | [調査 03](surveys/2026-09-25_03_heunen2024.md) |
| $`U ⊴ V`$ | U は V の因果的過去にある | 順序付きロケールの開集合の間の前順序。空間から作るときは Egli–Milner 順序（$`U ⊆ ↓V`$ かつ $`V ⊆ ↑U`$） | | [調査 03](surveys/2026-09-25_03_heunen2024.md) |
| $`↟U`$、$`↡U`$ | U の局所的な未来錐・過去錐 | $`⋁ \{V : U ⊴ V\}`$、$`⋁ \{W : W ⊴ U\}`$。滑らかな時空の開集合 $`U`$ では $`I^±(U)`$ に等しい | | [調査 03](surveys/2026-09-25_03_heunen2024.md) |
| $`\mathrm{Cov}^-_⊴(U)`$、$`\mathrm{Cov}^+_⊴(U)`$ | U の因果被覆 | U を下から（上から）覆う開集合全体 | | [調査 03](surveys/2026-09-25_03_heunen2026.md) |
| $`D^+(A)`$、$`D^-(A)`$ | A の未来・過去の依存領域 | A が下から（上から）覆う最大の開集合 | | [調査 03](surveys/2026-09-25_03_heunen2026.md) |
| $`L^+(U)`$、$`L^-(U)`$ | U の未来・過去の影響領域 | 抽象的な因果被覆から作る、結びを保つ閉包作用素。順序付きロケールから作ったときは $`↟`$・$`↡`$ に一致する | | [調査 03](surveys/2026-09-25_03_heunen2026.md) |

## 最小の尺度と余白付きの包含

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`T`$、$`T[a]`$ | 識別の関係、a の T 近傍 | 点の間の「区別できないほど近い」という関係（許容関係など）と、a の点と T で結ばれる点全体 | `T : X → X → Prop`、`{y \| ∃ x ∈ a, T x y}` | [調査 05](surveys/2026-09-26_05_subordination.md) |
| $`N`$、$`N_ℓ`$ | 膨張 | 領域を、操作的に区別できないところまで広げる写像。膨張は結びを保つ（右随伴 $`E`$ を持つ）写像を指すが、R-0006・R-0007 は単調性だけで成り立つ。$`ℓ`$ は尺度 | `N : α → α` | [調査 05](surveys/2026-09-26_05_subordination.md) |
| $`E`$ | 収縮 | 膨張 $`N`$ の右随伴（$`N\,a ≤ b \iff a ≤ E\,b`$） | `GaloisConnection N E` | [調査 05](surveys/2026-09-26_05_subordination.md) |
| $`a ◁ b`$ | a は b の中に余白を持って入っている | $`N\,a ≤ b`$。点の場合は $`T[a] ⊆ b`$ | `MarginSub T a b`、`N a ≤ b` | [調査 05](surveys/2026-09-26_05_subordination.md) |
| $`a ≺ b`$ | 劣位関係 | 劣位代数の関係（余白付きの包含の抽象化） | | [調査 05](surveys/2026-09-26_05_subordination.md) |
| $`λ_P`$ | プランク長 | $`\sqrt{G ℏ / c^3}`$ | | [調査 05](surveys/2026-09-26_05_subordination.md) |

## 測定と観測者の族

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`K`$ | 結合領域 | 系とプローブを相互作用させるコンパクトな時空の領域（Fewster–Verch） | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`ε_σ(B)`$ | 誘導される観測量 | プローブの初期状態 $`σ`$ とプローブの観測量 $`B`$ から誘導される系の観測量 | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`O`$ | 観測者側のデータ | 区別を行う側のデータ（結合領域、プローブの理論と結合、初期状態、観測量、使える資源、観測者の世界線の区間の両端の事象 $`p`$・$`q`$ など）。時間の向きを保つポアンカレ変換 $`g`$ で $`g\,O`$ に移る | | [NEXT.md](NEXT.md)（第 05 回の後）、[調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`T_O`$、$`N_O`$ | 観測者ごとの関係・膨張 | 観測者側のデータ $`O`$ を添字にした族。族の共変性は $`N_{gO}(g\,a) = g\,N_O\,a`$ | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`η`$ | ラピディティ | ブーストの大きさを表すパラメータ（ローレンツ因子は $`\cosh\,η`$） | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`ℓ`$、$`R_O`$ | 紫外の下限、赤外の上限 | 実現できる領域の最小の大きさと、観測者 $`O`$ が使える時空領域（有限な世界線の区間の両端の事象を頂点とする因果ダイヤモンド）の、両端を結ぶ時間的なベクトルの静止系での空間の半径。$`q - p`$ の固有時間（加速する世界線に沿う固有時間ではない）を $`τ_O`$ として $`R_O = τ_O/2`$ | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
