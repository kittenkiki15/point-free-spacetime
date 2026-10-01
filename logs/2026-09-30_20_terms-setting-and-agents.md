# 2026-09-30 第 20 回: 設定への用語の統一と、主体・観測者・装置の使い分け

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> ツールの呼び出しは折りたたんで表示し、個人情報などは伏せ字にしています。

## ユーザー

次のセッションを開始してください。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git status | head -3 && git log --oneline -5 && cat NEXT.md
```

</details>

<details><summary>結果: Bash</summary>

```text
On branch claude/zealous-keller-o7r1sv
Your branch is up to date with 'origin/claude/zealous-keller-o7r1sv'.

7e05f52 第 6 回のクロスモデルレビューに対応：固定したプロトコルを Le Cam の実験として表せることと、族を比べられることを分けて書き、(a) の判定基準の論点を T-0019 に記録
f94ad9c 第 5 回のクロスモデルレビューに対応：「量子的な観測」の (b) を、読み出す前の量子的な出力を実験の対象に含める読み方と明記し、(a) と区別した
9798579 第 4 回のクロスモデルレビューに対応：まとめの T-0006 への移管に、ねじれ射の圏による読み替えの確認を加えた
5bd1a0a 第 3 回のクロスモデルレビューに対応：量子時計で較正が必ず確率的になるとの記述を弱め、核の入力の論点を D-0003 に記録
966f9b2 第 2 回のクロスモデルレビューに対応：検算済みの Δ 収束と未確認のねじれ射の圏の読み替えを分けて書き、詳細化の論点を記録
# 次のセッションでやること

最終更新: 2026-09-30（第 19 回セッションの後）

## 状況

- 第 01 回：リポジトリの運用ルールを決め、自動検証（Lean・Python・クロスモデルレビュー）を整えた。
- 第 02 回：点なし位相と論理・様相論理・因果・量子論のつながりを整理し、調査メモ・用語一覧・記号一覧・参考文献一覧を作った（[まとめ](summaries/2026-09-25_02_pointfree-logic.md)）。
- 第 03 回：Heunen–van der Schaaf の 2 本の論文メモを作り、「完備ブール代数の点はアトムと対応する」を Lean で形式化した（[まとめ](summaries/2026-09-25_03_ordered-locales.md)）。
- 第 04 回：第 03 回の結果をユーザーと確認し、論文メモを修正した。検証済みの主張を「結果」として管理する [`results/`](results/README.md) を作った（[まとめ](summaries/2026-09-25_04_review-and-results.md)）。
  - ユーザーの方針：予想の価値の主軸は、数学ではなく**物理学への寄与**（厳密な定義のない物理の概念や主張に数学的な定式化を与えることなど）に置く。
- 第 05 回：最小の長さと操作的な領域の構造について、おもちゃのモデルを多角的に検討した。最小の尺度の入れ方を型 I（小さい領域を捨てる）と型 II（余白に下限を置く）に分け、型 II を「膨張 $`N`$ による余白付きの包含が補間的でないこと」として点なしに表した。文献を調べ、数学の部分は既知と確認して結果 R-0006〜R-0008 に登録し、最初の予想 [C-0001](conjectures/C-0001.md)（優先度：高、[Issue #8](https://github.com/kittenkiki15/point-free-spacetime/issues/8)）を立てた（[まとめ](summaries/2026-09-26_05_minimal-scale.md)、[調査メモ](surveys/2026-09-26_05_subordination.md)）。
- 第 06 回
…（以下 8708 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
git fetch origin main -q && git log --oneline origin/main -3 && git log --oneline origin/main..HEAD | head && echo --- && git log --oneline HEAD..origin/main | head; cd ../point-free-spacetime-private && git status | head -2 && git fetch origin main -q && git log --oneline origin/main..HEAD | head
```

</details>

<details><summary>結果: Bash</summary>

```text
b6bea15 Merge pull request #36 from kittenkiki15/claude/zealous-keller-o7r1sv
7e05f52 第 6 回のクロスモデルレビューに対応：固定したプロトコルを Le Cam の実験として表せることと、族を比べられることを分けて書き、(a) の判定基準の論点を T-0019 に記録
f94ad9c 第 5 回のクロスモデルレビューに対応：「量子的な観測」の (b) を、読み出す前の量子的な出力を実験の対象に含める読み方と明記し、(a) と区別した
---
b6bea15 Merge pull request #36 from kittenkiki15/claude/zealous-keller-o7r1sv
On branch claude/zealous-keller-o7r1sv
Your branch is up to date with 'origin/claude/zealous-keller-o7r1sv'.
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git checkout -q -B claude/zealous-keller-o7r1sv origin/main && git log --oneline -1 && grep -n "T-0018" roadmap.md | head -20
```

</details>

<details><summary>ツール: Bash</summary>

```text
git log --oneline -1 && git log --oneline origin/main -1
```

</details>

<details><summary>結果: Bash</summary>

```text
b6bea15 Merge pull request #36 from kittenkiki15/claude/zealous-keller-o7r1sv
3:最終更新: 2026-09-30（第 19 回。T-0016 を閉じ、T-0018 の範囲を広げ、調査のタスク T-0019 を加えた）
11:- 順序は、第 11 回にユーザーと相談して決めた（2 節）。第 13 回に、ユーザーの提案で T-0015（D-0003 の未解決の点の解決）を T-0002 の前に加えた。第 15 回に、調査が不足している領域を洗い出し、Claude の提案にユーザーが賛成して、調査のタスク T-0016（段階 B の前）と T-0017（T-0008 の前）を加えた。第 19 回に、ユーザーの判断で、T-0018 の範囲を概念と用語の整理に広げ、調査のタスク T-0019（T-0018 の次、段階 B の前）を加えた。優先の順は、状況に応じてユーザーと相談して見直す。
18:\text{T-0001} \;→\; \text{T-0015} \;→\; \text{T-0002} \;→\; \text{T-0003} \;→\; \text{T-0016} \;→\; \text{T-0018} \;→\; \text{T-0019} \;→\; \text{段階 B（T-0004〜T-0007）} \;→\; \text{T-0017} \;→\; \text{T-0008} \;→\; \text{段階 C（T-0009）} \;→\; \text{段階 D（T-0010）}
25:| （用語） | 主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理 | T-0018 |
34:T-0015 は、番号は後から付けたが、順序は T-0001 の次である。T-0016 は T-0003 の次、T-0018 は T-0016 の次（第 16 回にユーザーと決めた）、T-0019 は T-0018 の次で段階 B の前（第 19 回にユーザーと決めた）、T-0017 は段階 B の次（T-0008 の前）である。
59:| T-0018 | 主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理（第 16 回に追加、第 19 回に範囲を拡大） | 用語 | なし | [A-0001](assumptions/A-0001.md)、[A-0007](assumptions/A-0007.md)、[A-0010](assumptions/A-0010.md)、[D-0001](definitions/D-0001.md)、[D-0003](definitions/D-0003.md)、[D-0005](definitions/D-0005.md)、[D-0011](definitions/D-0011.md) | 未着手 |
68:  T0016 --> T0018["T-0018 概念と用語の整理"]
243:### T-0018 主体・観測者・装置の使い分け（第 16 回に追加）
273:- 順序：T-0018 の次、段階 B の前（第 19 回にユーザーと決めた）。
```

</details>

<details><summary>結果: Bash</summary>

```text
b6bea15 Merge pull request #36 from kittenkiki15/claude/zealous-keller-o7r1sv
b6bea15 Merge pull request #36 from kittenkiki15/claude/zealous-keller-o7r1sv
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 243,275p roadmap.md
```

</details>

<details><summary>結果: Bash</summary>

```text
### T-0018 主体・観測者・装置の使い分け（第 16 回に追加）

第 16 回に、ユーザーの指摘で追加した。「主体」「観測者」「装置」などの語の、プロジェクト内での意味を決める。

- 今の使われ方（第 16 回に確認した範囲）：
  - **主体**：事前分布を持ち、データで信念を更新する者（[A-0007](assumptions/A-0007.md)、[D-0005](definitions/D-0005.md)）。[A-0001](assumptions/A-0001.md) の「実験の主体」は、実験をする者の意味（ユーザーによる）。
  - **観測者**：基準の時計と物差しを持ち、座標 $`M_O`$ を与える者（[D-0003](definitions/D-0003.md)、[A-0010](assumptions/A-0010.md)、[D-0011](definitions/D-0011.md)、[A-0008](assumptions/A-0008.md)、[C-0008](conjectures/C-0008.md)）。[D-0001](definitions/D-0001.md) では、実験をする者の意味（「実験を行う観測者の世界線」）で使っている。
  - **装置**：時空の中に領域を占める物理系（[D-0001](definitions/D-0001.md)、[D-0011](definitions/D-0011.md)、[C-0007](conjectures/C-0007.md)、[C-0008](conjectures/C-0008.md)）。
  - 「観測装置」「実験者」は使っていない。
- 論点：「観測者」の二つの意味（基準系と、実験をする者）。主体（信念を持つ者）と観測者（世界線や基準系を持つ者）と実験をする者が同じものか。装置と、観測者の時計・物差しの関係。第 07 回の「観測する側と観測される側の対称性」との関係。装置とそれ以外の境界の取り方と、実験の個別化（何を一つの実験として数えるか。[A-0001](assumptions/A-0001.md) の未解決の点。境界を連続的に動かすと主体が非可算になりうる、というユーザーの考察が A-0001 の背景にある。記録はアナログでもありうるので、必要がなければ記録の有限な記述は仮定しない、というユーザーの意見がある）。
- 手がかり（第 18 回）：Ludwig（*An Axiomatic Basis for Quantum Mechanics*, Vol. 1, 1985 の第 I 章）は、「測定装置」の語を避け、実験の配置を準備装置（preparation apparatus）と登録装置（registration apparatus）に分け、観測量や状態を基本領域に入れない。準備と登録への切り分けは一意でないが、二つの部分からなる構造は常にある、とする（9 ページの図 1。[第 18 回の調査メモ](surveys/2026-09-30_18_limit-topology.md)の 5.2 節）。
- 進め方：(1) 既存研究での使われ方の調査（記憶による候補：相対論の観測者と基準系、量子測定論の系・プローブ・装置（Fewster–Verch、Busch–Lahti–Mittelstaedt）、von Neumann の測定の連鎖とハイゼンベルクの切断（切断の位置の移動）、Wigner の友人、QBism と意思決定理論の agent、操
…（以下 2913 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cat definitions/D-0003.md && echo ======= && cat assumptions/A-0001.md && echo ===== && ls definitions assumptions conjectures && ls summaries | tail -3
```

</details>

<details><summary>結果: Bash</summary>

```text
# D-0003: 実験における時空

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)、[A-0004](../assumptions/A-0004.md)、[A-0010](../assumptions/A-0010.md) |
| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0004](../conjectures/C-0004.md)、[C-0008](../conjectures/C-0008.md) |
| 初出 | [2026-09-27 第 07 回](../summaries/2026-09-27_07_observation-and-experiment.md) |

## 定義

**実験における時空** $`X`$ は、可能な実験パラメータの組全体の空間である。次のように構成する。

1. **各プロトコルの設定の空間**：プロトコル $`π`$ の設定の空間 $`X_π`$ は、有限個の実数値のパラメータの組の集合 $`X_π ⊆ ℝ^{n_π}`$（[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)）で、部分空間の位相を入れる。資源の量（操作回数、時間、エネルギーなど）もパラメータに含める（[A-0004](../assumptions/A-0004.md)）。
2. **全体**：$`X := ⨆_π X_π`$（直和）とし、直和の位相を入れる。異なるプロトコルの設定のうち、時空の読みは下の換算の写像を通して比べる。その他の設定の比較方法は未定である（下の未解決の点）。
3. **時空の部分**：時空の読みにあたる設定値を持つプロトコル $`π`$（以下、時空の読みを持つプロトコル）について、$`X_π`$ のパラメータのうち、装置の中の時計や物差しの読みにあたるものを、観測者 $`O`$ の基準の時計と物差しとの較正によって、$`O`$ の座標に換算する（[A-0010](../assumptions/A-0010.md)）。この連続な写像を $`τ^O_π : X_π → M_O`$ とする（時空の読みを持たないプロトコルには定めない）。$`M_O := ℝ^{1+n}`$ を観測者 $`O`$ の**時空の部分**と呼ぶ。$`M_O`$ には座標の位相と、$`ℝ^{1+n}`$ の上のノルムから決まる座標の距離 $`d_O`$（例えば、$`O`$ の座標 $`(t, 𝐱)`$ で $`d_O = \max(c \left| Δt \right|, \left| Δ𝐱 \right|)`$）を入れる。有限次元なのでどのノルムも同値で、$`d_O`$ での有界性は通常の座標の上の有界性と一致する（$`\min(1, d)`$ のような、位相は同じでも全体が有界になる距離は採らない）。
4. **設定の部分**：時空の部分以外のパラメータ（磁場の強さ、初期状態の設定値など）。
5. **結果の読み**：結果の空間 $`Y_π`$（[D-0001](D-0001.md)）の座標のうち時計や物差しの読み
…（以下 5206 文字を省略）
```

</details>

## Claude

準備中です：`NEXT.md` とロードマップの T-0018、D-0003・A-0001 を読みました。D-0001 と D-0005 を確認してから、進め方をご相談します。

<details><summary>ツール: Bash</summary>

```text
sed -n 1,40p definitions/D-0001.md && echo ===== && grep -n "Θ" definitions/D-0005.md | head -20
```

</details>

<details><summary>結果: Bash</summary>

```text
# D-0001: 有限な実験

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md) |
| 関係する予想・結果 | [C-0003](../conjectures/C-0003.md) |
| 初出 | [2026-09-28 第 08 回](../summaries/2026-09-28_08_observation-as-limit.md) |

## 定義

**有限な実験**とは、一つの実験プロトコル $`π`$ に従い、有限回の操作と観測を行って、有限個の結果を読み出すものである。一つの有限な実験について、次を指定する。

- プロトコル $`π`$（有限の記述を持つ。[A-0002](../assumptions/A-0002.md)）
- 設定 $`x ∈ X_π`$：プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数値のパラメータの組（[A-0003](../assumptions/A-0003.md)）
- 結果の空間 $`Y_π`$ と、読み出した有限個の結果（実数値。[A-0003](../assumptions/A-0003.md)）

## 注意

- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める実験における時空の領域とは区別する。
- 設定の空間 $`X_π`$ と結果の空間 $`Y_π`$ は、プロトコルごとに異なりうる。
- 有限な実験に何を対応させるか（結果の統計）は [D-0004](D-0004.md) で定める。

## 未解決の点

- 各実験が占める領域の決め方（装置の準備や結果の読み出しを実験の領域に含めるか。設定値ごとの装置の占める領域 $`\mathrm{occ}`$ は [D-0011](D-0011.md) で導入した）と、実験が領域 $`R`$ に「収まる」ことの判定（[D-0008](D-0008.md) と共通）。
- 結果の空間 $`Y_π`$ の意味：個々の読みの空間か、実験 1 回分の全出力をまとめた空間か。同じ実験の中の結果どうしの同時分布と、実験を繰り返すときの同時分布を区別する（[D-0004](D-0004.md) と共通）。

## 履歴

- 第 08 回：「有限の期間に、有界な範囲で、有限回の操作を行い、有限個の結果を読み出すもの」として導入した。
- 第 09 回：プロトコル、実数値のパラメータと結果、プロトコルごとの設定の空間と結果の空間を加えた。
- 第 10 回：[第 08 回の調査メモ](../surveys/2026-09-28_08_observation-as-limit.md)（1.2・1.4 節）から移し、文章を整えた。
=====
32:  - 第 17 回の候補（[調査メモ](../surveys/2026-09-30_17_comparison-of-experiments.md)の 7.1・7.2 節。Claude の見立て）：Le Cam の不足度と距離 $`Δ`$ は、推定の対象の集合 $`Θ`$ が共通なら、結果の空間が異なる実験を比べられ、$`Δ = 0`$ で割った実験の型は距離空間になる。$`Θ`$ を推定の対象の空間と読むか、設定の空間と読むかは決ま
…（以下 1045 文字を省略）
```

</details>

## Claude

T-0018「主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理」の準備ができました。第 19 回の PR #36 はマージ済みです。作業ブランチ `claude/zealous-keller-o7r1sv` は、最新の `main` から作り直しました。

#### このタスクの中身（`roadmap.md` の T-0018 の節から）

大きく三つの部分があります。

**(A) D-0003 の再編と、較正の写像の一般化**（第 19 回に方針は合意済み）
- 今の D-0003 では「実験における時空」の語が、次の二つを指しています。
  - プロトコル全体の設定の空間 $`X = ⨆_π X_π`$
  - 観測者の座標 $`M_O`$
- $`τ^O_π`$ は、時空の読みだけを写す写像ではなく、$`X_π`$ 全体の上の写像にします（磁場による時計のずれなどの補正のため）。

**(B) 「実験パラメータ」を「設定」に統一**
- 書き換えるのは定義・前提・予想、`framework.md`、用語一覧、記号一覧です。過去のまとめとログは書き換えません。

**(C) 主体・観測者・装置の使い分け**
- 論点は次の三つです。
  - 「観測者」の二つの意味：基準系と、実験をする者
  - 「主体」（信念を持つ者）と「実験をする者」が同じものか
  - 装置の境界と、実験の個別化（A-0001）

#### 叩き台（Claude の提案。未決定）

**(A) の分け方**
- **D-0003「設定の空間」**：$`X_π`$ と $`X = ⨆_π X_π`$、直和の位相。
- **新しい定義 D-0012「観測者の実験における時空」**：$`M_O = ℝ^{1+n}`$ と距離 $`d_O`$。
- **新しい定義 D-0013「較正の写像」**：$`τ^O_π : X_π → M_O`$（$`X_π`$ 全体の上の写像）と、結果の読みの換算 $`σ^O_π`$。
- D-0012 と D-0013 を一つにまとめる案もあります。確率的な較正（核 $`K^O_π`$）にするかどうかは、T-0019 の後まで未決定のまま残します。

**(C) の使い分け**
- **主体**（agent）：実験を行い、記録を得て、事前分布から信念を更新する者。A-0001 の「実験の主体」と A-0007 の「主体」を一つにまとめます。
- **観測者**（observer）：基準の時計と物差しの組、つまり基準系だけを指します。D-0001 の「実験を行う観測者の世界線」は、「主体」か「装置」の語に改めます。
- **装置**（apparatus）：時空の中に領域を占める物理系です。準備と登録に分けるかは、Ludwig の分け方を参考に決めます。
- 「主体」と「観測者」を別の概念にすると、第 07 回の「観測する側と観測される側の対称性」は、装置と観測対象の間の関係として読み直すことになります。

#### ご相談したいこと

1. **順序**：次のどちらから始めますか？
   - (A)(B) の再編から始める。方針が決まっていて、作業が具体的なためです。
   - (C) の使い分けを先に決め、その後でまとめて書き換える。
2. **既存研究での使われ方の調査の深さ**：ロードマップにある文献の候補は記憶によるもので、未確認です。次のどちらにしますか？
   - arXiv などで原典を確かめ、短い調査メモを作る。
   - 今回は記憶による対応表にとどめ、「未確認」と明記する。
3. **(A) の分け方**：上の叩き台（D-0003 を「設定の空間」とし、D-0012・D-0013 を新しく作る）でよいですか？ D-0012 と D-0013 を一つにまとめる方がよいですか？

<details><summary>ツール: Bash</summary>

```text
git push -u origin claude/zealous-keller-o7r1sv 2>&1 | tail -2
```

</details>

<details><summary>結果: Bash</summary>

```text
* [new branch]      claude/zealous-keller-o7r1sv -> claude/zealous-keller-o7r1sv
branch 'claude/zealous-keller-o7r1sv' set up to track 'origin/claude/zealous-keller-o7r1sv'.
```

</details>

## Claude

作業ブランチ `claude/zealous-keller-o7r1sv` を push しました。前回の PR のマージ後にリモートのブランチが消えていたので、新しく作り直した形です。中身は最新の `main` と同じで、今回の変更はまだありません。

前のメッセージの三つのご相談（1. 始める順序、2. 既存研究の調査の深さ、3. D-0003 の分け方）へのお返事をお待ちしています。

<details><summary>ツール: ReadNotifications</summary>

```text
（入力の本文は省略。項目: ）
```

</details>

<details><summary>結果: ReadNotifications</summary>

```text
No queued notifications.
```

</details>

<details><summary>ツール: ToolSearch: select:mcp__github__pull_request_read</summary>

```text
（入力の本文は省略。項目: max_results, query）
```

</details>

<details><summary>結果: ToolSearch: select:mcp__github__pull_request_read</summary>

```text
[tool_reference]
```

</details>

<details><summary>ツール: mcp__github__pull_request_read</summary>

```text
（入力の本文は省略。項目: method, owner, pullNumber, repo）
```

</details>

<details><summary>結果: mcp__github__pull_request_read</summary>

```text
{"number":36,"title":"第 19 回：量子・古典の実験の要件と、設定・時空の用語の整理（T-0016 を閉じる）","body":"## 概要\n\nロードマップの T-0016「実験の族の位相と極限の先行研究の調査」の続きとして、第 17 回・第 18 回の調査メモについてユーザーと対話しました。ユーザーの判断で T-0016 を閉じ、次のタスクを整理しました。新しく読んだ文献はありません。\n\n## 決定事項（ユーザーの判断）\n\n- **要件**：量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えるようにする（量子重力理論への寄与という目的による）。\n- **T-0016 を閉じる**：残りは次のように移しました。\n  - 一般化確率論 → 新しい T-0019\n  - 弱い併合 → T-0005\n  - 第 17 回・第 18 回の検算の、証明の形での確認と、ねじれ射の圏による模倣の読み替えの、式での確認 → T-0006\n- **T-0018 の範囲を広げる**：「主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理」とし、次の方針に合意しました（実施は T-0018 で行います）。\n  - D-0003 の再編：設定の空間 $`X`$ と、観測者の実験における時空 $`M_O`$ を分けます。\n  - 較正の写像 $`τ^O_π`$ を、射影ではなく、設定全体の上の写像とします。\n  - 「実験パラメータ」を「設定」に統一します。\n- **T-0019 を加える**：「量子・古典・混成の実験の扱いの先行研究の調査」です。調べる対象は、一般化確率論、Le Cam の理論の量子版、量子参照系・量子時計です。\n- **順序**：T-0018 → T-0019 → 段階 B とします。\n- **「量子的な観測」の読み方は T-0019 の後に判断する**：次の二つのどちらを採るかは、T-0019 の調査結果を踏まえてユーザーが判断します。\n  - (a) 量子系を測った古典的な記録（今の立場）。量子的な時計は、装置のモデルとして扱えます。\n  - (b) 出力が量子系のまま残る実験を含める。時計を含む量子系を、古典的な記録へ読み出す前の量子的な出力として、実験の対象に含めます。\n\n## 変更したファイル\n\n- `logs/2026-09-30_19_quantum-classical-and-terms.md`：対話ログ\n- `summaries/2026-09-30_19_quantum-classical-and-terms.md`：まとめ\n- `roadmap.md`：T-0016 を完了にし、T-0018 の範囲を広げ、T-0019 を追加し、順序の式・段階の表・図を更新しました。弱い併合を T-0005 に、検算の確認を T-0006 に移しました。\n- `definitions/D-0003.md`：未解決の点に、再編の方針を記録しました。\n- `definitions/D-0005.md`：未解決の点に、$`Θ`$ の読み方の候補（Claude の提案。未決定）を記録しました。\n- `framework.md`：6 節に、要件と用語の再編の方針を加えました。\n- `glossary.md`：「設定（setting）」を追加しました。\n- `NEXT.md`：第 19 回の状況を加え、次のタスクを T-0018 にしました。\
…（以下 1108 文字を省略）
```

</details>

## Claude

Merged. Delete the pending check-in.

<details><summary>ツール: mcp__Claude_Code_Remote__delete_trigger</summary>

```text
（入力の本文は省略。項目: trigger_id）
```

</details>

<details><summary>結果（エラー）: mcp__Claude_Code_Remote__delete_trigger</summary>

```text
failed to delete trigger: the requested resource was not found
```

</details>

<details><summary>ツール: mcp__Claude_Code_Remote__list_triggers</summary>

```text
（入力の本文は省略。項目: enabled）
```

</details>

<details><summary>結果: mcp__Claude_Code_Remote__list_triggers</summary>

```text
{"data":[],"has_more":false}
```

</details>

## Claude

[PR #36](https://github.com/kittenkiki15/point-free-spacetime/pull/36) がマージされたことを確認しました。非公開リポジトリには変更がなかったので、PR はこれ 1 件だけです。PR の状態を確かめる予約は、もう一件も残っていません。

これで第 19 回のセッションは終わりです。`/clear` でコンテキストを初期化してから、次のセッションを始めてください。次回は、`NEXT.md` に書いたとおり T-0018「主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理」を扱います。

## ユーザー

「1. 順序」 ですが、依存関係でいうと、(C) は 「既存研究での使われ方の調査」に依存し、(A) は「観測者」の概念を含むので (C) に依存します。(B) → 調査 → (C) → (A) の順でお願いします。

「2. 既存研究での使われ方の調査の深さ」 は「arXiv などで原典を確かめ、短い調査メモを作る」でお願いします。

「3. (A) の分け方」は、(A) を実施するときに再検討したいです。「観測者」の概念と、「D-0001: 有限な実験」「D-0002: 実際の実験と可能な実験」との間の関係が気になっています。その点を明らかにしたうえで、(A) の定義内容も含めて再検討したいです。

<details><summary>ツール: Bash</summary>

```text
cd /root/.claude/projects/-home-user/ && ls -t *.jsonl | head -3; python3 - <<'EOF'
import json,glob,os
fs=sorted(glob.glob('/root/.claude/projects/-home-user/*.jsonl'),key=os.path.getmtime)[-3:]
for f in fs:
    for line in open(f):
        d=json.loads(line)
        if d.get('type')=='assistant':
            for c in d['message'].get('content',[]):
                if isinstance(c,dict) and c.get('type')=='text' and '(A) の分け方' in c.get('text',''):
                    print(f, d['timestamp']); print(c['text'][:3000]); print('----')
EOF
```

</details>

<details><summary>結果: Bash</summary>

```text
[ID].jsonl
[ID].jsonl
[ID].jsonl
/root/.claude/projects/-home-user/[ID].jsonl 2026-09-30T17:22:34.097Z
T-0018「主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理」の準備ができました。第 19 回の PR #36 はマージ済みです。作業ブランチ `claude/zealous-keller-o7r1sv` は、最新の `main` から作り直しました。

## このタスクの中身（`roadmap.md` の T-0018 の節から）

大きく三つの部分があります。

**(A) D-0003 の再編と、較正の写像の一般化**（第 19 回に方針は合意済み）
- 今の D-0003 では「実験における時空」の語が、次の二つを指しています。
  - プロトコル全体の設定の空間 $`X = ⨆_π X_π`$
  - 観測者の座標 $`M_O`$
- $`τ^O_π`$ は、時空の読みだけを写す写像ではなく、$`X_π`$ 全体の上の写像にします（磁場による時計のずれなどの補正のため）。

**(B) 「実験パラメータ」を「設定」に統一**
- 書き換えるのは定義・前提・予想、`framework.md`、用語一覧、記号一覧です。過去のまとめとログは書き換えません。

**(C) 主体・観測者・装置の使い分け**
- 論点は次の三つです。
  - 「観測者」の二つの意味：基準系と、実験をする者
  - 「主体」（信念を持つ者）と「実験をする者」が同じものか
  - 装置の境界と、実験の個別化（A-0001）

## 叩き台（Claude の提案。未決定）

**(A) の分け方**
- **D-0003「設定の空間」**：$`X_π`$ と $`X = ⨆_π X_π`$、直和の位相。
- **新しい定義 D-0012「観測者の実験における時空」**：$`M_O = ℝ^{1+n}`$ と距離 $`d_O`$。
- **新しい定義 D-0013「較正の写像」**：$`τ^O_π : X_π → M_O`$（$`X_π`$ 全体の上の写像）と、結果の読みの換算 $`σ^O_π`$。
- D-0012 と D-0013 を一つにまとめる案もあります。確率的な較正（核 $`K^O_π`$）にするかどうかは、T-0019 の後まで未決定のまま残します。

**(C) の使い分け**
- **主体**（agent）：実験を行い、記録を得て、事前分布から信念を更新する者。A-0001 の「実験の主体」と A-0007 の「主体」を一つにまとめます。
- **観測者**（observer）：基準の時計と物差しの組、つまり基準系だけを指します。D-0001 の「実験を行う観測者の世界線」は、「主体」か「装置」の語に改めます。
- **装置**（apparatus）：時空の中に領域を占める物理系です。準備と登録に分けるかは、Ludwig の分け方を参考に決めます。
- 「主体」と「観測者」を別の概念にすると、第 07 回の「観測する側と観測される側の対称性」は、装置と観測対象の間の関係として
…（以下 2140 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git status -sb | head -3 && git log --oneline -2 && grep -rn "実験パラメータ\|パラメータ" --include=*.md definitions assumptions conjectures results framework.md glossary.md symbols.md README.md 2>/dev/null | grep -v "_template" | cut -c1-220
```

</details>

<details><summary>結果: Bash</summary>

```text
## claude/zealous-keller-o7r1sv...origin/claude/zealous-keller-o7r1sv
b6bea15 Merge pull request #36 from kittenkiki15/claude/zealous-keller-o7r1sv
7e05f52 第 6 回のクロスモデルレビューに対応：固定したプロトコルを Le Cam の実験として表せることと、族を比べられることを分けて書き、(a) の判定基準の論点を T-0019 に記録
definitions/D-0005.md:27:- 極限の位相。コーシー性を使う場合の一様構造、すべてのコーシー列が収束するための完備性、極限を一つに定めるための分離性（ハウスドル�
definitions/D-0005.md:32:  - 第 17 回の候補（[調査メモ](../surveys/2026-09-30_17_comparison-of-experiments.md)の 7.1・7.2 節。Claude の見立て）：Le Cam の不足度と距離 $`Δ`$ は、推定の対�
definitions/D-0001.md:16:- 設定 $`x ∈ X_π`$：プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数値のパラメータの組（[A-0003](../assumption
definitions/D-0001.md:33:- 第 09 回：プロトコル、実数値のパラメータと結果、プロトコルごとの設定の空間と結果の空間を加えた。
definitions/D-0003.md:13:**実験における時空** $`X`$ は、可能な実験パラメータの組全体の空間である。次のように構成する。
definitions/D-0003.md:15:1. **各プロトコルの設定の空間**：プロトコル $`π`$ の設定の空間 $`X_π`$ は、有限個の実数値のパラメータの組の集合 $`X_π ⊆ ℝ^{n_π}`$（[A-0002](..
definitions/D-0003.md:17:3. **時空の部分**：時空の読みにあたる設定値を持つプロトコル $`π`$（以下、時空の読みを持つプロトコル）について、$`X_π`$ のパラメータのう�
definitions/D-0003.md:18:4. **設定の部分**：時空の部分以外のパラメータ（磁場の強さ、初期状態の設定値など）。
definitions/D-0003.md:23:- 第 07 回のユーザーの構想の用語で、「実験装置の中の時計や物差しで測った実験パラメータを記述する数学的なモデル」である。観測における
definitions/D-0003.md:26:- パラメータの尺度の取り方には任意性がある。取り替えを同等とみなす場合は、同相写像による取り替えに限る。
definitions/D-0003.md:31:- **用語と構成の再編**（第 19 回。ユーザーの提案に合意し、[T-0018](../roadmap.md) で行う）：この定義では「実験における時空」が、設定全体の空�
definitions/D-0003.md:38:- どのパラメータを時計や物差しの読みとみなすかの判定。時空の読みを持たないプロトコルには $`τ^O_π`$ を定めない（PR #28 のレビューを受け�
definitions/D-0003.md:45:- 第 09 回：
…（以下 4401 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
for f in definitions/D-0001.md definitions/D-0003.md definitions/D-0011.md assumptions/A-0001.md assumptions/A-0002.md assumptions/A-0003.md assumptions/A-0004.md assumptions/A-0005.md assumptions/A-0006.md conjectures/C-0004.md conjectures/C-0007.md; do echo "=== $f"; grep -n "パラメータ" $f; done; grep -n "パラメータ" symbols.md glossary.md framework.md | grep -v "パラメータの集合\|パラメータが有限\|ラピディティ\|集中するパラメータ\|データを生んだ"
```

</details>

<details><summary>結果: Bash</summary>

```text
=== definitions/D-0001.md
16:- 設定 $`x ∈ X_π`$：プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数値のパラメータの組（[A-0003](../assumptions/A-0003.md)）
33:- 第 09 回：プロトコル、実数値のパラメータと結果、プロトコルごとの設定の空間と結果の空間を加えた。
=== definitions/D-0003.md
13:**実験における時空** $`X`$ は、可能な実験パラメータの組全体の空間である。次のように構成する。
15:1. **各プロトコルの設定の空間**：プロトコル $`π`$ の設定の空間 $`X_π`$ は、有限個の実数値のパラメータの組の集合 $`X_π ⊆ ℝ^{n_π}`$（[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)）で、部分空間の位相を入れる。資源の量（操作回数、時間、エネルギーなど）もパラメータに含める（[A-0004](../assumptions/A-0004.md)）。
17:3. **時空の部分**：時空の読みにあたる設定値を持つプロトコル $`π`$（以下、時空の読みを持つプロトコル）について、$`X_π`$ のパラメータのうち、装置の中の時計や物差しの読みにあたるものを、観測者 $`O`$ の基準の時計と物差しとの較正によって、$`O`$ の座標に換算する（[A-0010](../assumptions/A-0010.md)）。この連続な写像を $`τ^O_π : X_π → M_O`$ とする（時空の読みを持たないプロトコルには定めない）。$`M_O := ℝ^{1+n}`$ を観測者 $`O`$ の**時空の部分**と呼ぶ。$`M_O`$ には座標の位相と、$`ℝ^{1+n}`$ の上のノルムから決まる座標の距離 $`d_O`$（例えば、$`O`$ の座標 $`(t, 𝐱)`$ で $`d_O = \max(c \left| Δt \right|, \left| Δ𝐱 \right|)`$）を入れる。有限次元なのでどのノルムも同値で、$`d_O`$ での有界性は通常の座標の上の有界性と一致する（$`\min(1, d)`$ のような、位相は同じでも全体が有界になる距離は採らない）。
18:4. **設定の部分**：時空の部分以外のパラメータ（磁場の強さ、初期状態の設定値など）。
23:- 第 07 回のユーザーの構想の用語で、「実験装置の中の時計や物差しで測った実験パラメータを記述する数学的なモデル」である。観測における時空（[D-0007](D-0007.md)）とは区別する。
26:- パラメータの尺度の取り方には任意性がある。取り替えを同等とみなす場合は、同相写像による取り替えに限る。
31:- **用語と構成の再編**（第 19 回。ユーザーの提案に合意し、[T-0018](../roadmap.md) で行う）：この定義では「実験における時空」が、設定全体の空間 $`X`$ と観測者の座標 $`M_O`$ の二つの意味に使われている。$`X_π`$ を「プロトコル $`π`$ の設定の空間」、$`X`$ を「プロトコル全体の設定の空間」とし、$`M_O`$ を「観測者 $`O`$ の実験における時空」とする。また、時空の部分と設定の部分を単純に分けず、$`τ^O_π`$ 
…（以下 5538 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
R = {
'definitions/D-0001.md':[
 ('初期状態の条件と測定の条件を定める実数値のパラメータの組','初期状態の条件と測定の条件を定める実数の組')],
'definitions/D-0003.md':[
 ('$`X`$ は、可能な実験パラメータの組全体の空間である。','$`X`$ は、可能な設定全体の空間である。'),
 ('有限個の実数値のパラメータの組の集合 $`X_π ⊆ ℝ^{n_π}`$','有限個の実数の組の集合 $`X_π ⊆ ℝ^{n_π}`$'),
 ('もパラメータに含める（[A-0004]','も設定に含める（[A-0004]'),
 ('$`X_π`$ のパラメータのうち、装置の中の','$`X_π`$ の座標のうち、装置の中の'),
 ('時空の部分以外のパラメータ（磁場の強さ','時空の部分以外の座標（磁場の強さ'),
 ('測った実験パラメータを記述する数学的なモデル」である。','測った実験パラメータを記述する数学的なモデル」である（「実験パラメータ」は第 20 回に「設定」に改めた語）。'),
 ('- パラメータの尺度の取り方には任意性がある。','- 設定の座標の尺度の取り方には任意性がある。'),
 ('- どのパラメータを時計や物差しの読みとみなすかの判定。','- どの座標を時計や物差しの読みとみなすかの判定。'),
 ('「実験パラメータ」の語も「設定」に統一する。','「実験パラメータ」の語も「設定」に統一する（第 20 回に実施した）。')],
'definitions/D-0011.md':[('時空の部分以外のパラメータ','時空の部分以外の座標')],
'assumptions/A-0001.md':[('（プロトコルと実数値のパラメータの組）','（プロトコルと、実数の組である設定の組）')],
'assumptions/A-0002.md':[('実数値のパラメータ（[A-0003](A-0003.md)）を含む','実数値の設定（[A-0003](A-0003.md)）を含む')],
'assumptions/A-0003.md':[
 ('# A-0003: 実験パラメータと結果は実数値','# A-0003: 設定と結果は実数値'),
 ('各観測の実験パラメータ（少なくとも初期状態の条件と測定の条件を設定するもの）','各観測の設定（少なくとも初期状態の条件と測定の条件を定めるもの）'),
 ('実際に得られるパラメータと結果の値','実際に得られる設定と結果の値')],
'assumptions/A-0004.md':[
 ('# A-0004: 資源の量を実験パラメータに含める','# A-0004: 資源の量を設定に含める'),
 ('も、実験パラメータの一部として記録する。','も、設定の一部として記録する。'),
 ('資源の量をパラメータとして記録しておけば','資源の量を設定として記録しておけば'),
 ('この前提の下で、実験パラメータの組から作る）','この前提の下で、設定から作る）'),
 ('パラメータの値域の条件（[A-0005](A-0005.md)）だけで、資源を許容されるパラメータ全体で','設定の値域の条件（[A-0005](A-0005.md)）だけで、資源を許容される設定全体で'),
 ('この前提は実験パラメータについて述べ、$`X`$ は D-0003 でそのパラメータ
…（以下 2329 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
definitions/D-0003.md:23:- 第 07 回のユーザーの構想の用語で、「実験装置の中の時計や物差し�
definitions/D-0003.md:31:- **用語と構成の再編**（第 19 回。ユーザーの提案に合意し、[T-0018](../r
definitions/D-0003.md:45:- 第 09 回：可能な実験パラメータの組全体の空間とし、時空の部分と�
assumptions/A-0005.md:17:資源の条件を「特に限定せず、実験パラメータの値域とする」という�
assumptions/A-0005.md:35:- 第 09 回：ユーザーの提案で、資源の条件を実験パラメータの値域と�
assumptions/A-0006.md:17:ユーザーの提案は、「同一の実験プロトコルと実験パラメータの組で�
framework.md:203:- 用語と構成の再編（第 19 回に方針に合意。ロードマップの T-0018）。D-0003 �
glossary.md:28:| experimental spacetime | 実験における時空 | 本プロジェクトの用語（第 07 回、ユ�
glossary.md:79:| setting | 設定 | 実験の条件を定める値（初期状態の条件と測定の条件など）。
symbols.md:105:| $`X`$ | 実験における時空 | 可能な設定全体の空間（第 09 回の改訂案。第 20 回
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
fs=['definitions/D-0001.md','definitions/D-0003.md','definitions/D-0011.md','assumptions/A-0001.md','assumptions/A-0002.md','assumptions/A-0003.md','assumptions/A-0004.md','assumptions/A-0005.md','assumptions/A-0006.md','conjectures/C-0004.md','conjectures/C-0007.md']
line='- 第 20 回：「実験パラメータ」（とその意味での「パラメータ」）の語を「設定」に改めた（[T-0018](../roadmap.md)。用語だけの変更で、内容は変えていない）。'
for p in fs:
    s=open(p).read().rstrip('\n')
    i=s.rfind('\n## ')
    assert s[i+1:].startswith('## 履歴'),(p,s[i+1:i+20])
    open(p,'w').write(s+'\n'+line+'\n')
EOF
python3 -m pytest -q tools/tests 2>&1 | tail -1; git diff --stat | tail -1
```

</details>

<details><summary>結果: Bash</summary>

```text
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
AssertionError: ('conjectures/C-0004.md', '## 結果\n\n（未着手）')
33 passed in 0.50s
 15 files changed, 48 insertions(+), 39 deletions(-)
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "^## " conjectures/C-0004.md conjectures/C-0007.md; cat conjectures/_template.md | grep -n "^## \|履歴"
```

</details>

<details><summary>結果: Bash</summary>

```text
conjectures/C-0004.md:16:## 主張
conjectures/C-0004.md:20:## 注意
conjectures/C-0004.md:28:## 詳細化の論点
conjectures/C-0004.md:33:## 背景
conjectures/C-0004.md:39:## 評価の根拠
conjectures/C-0004.md:45:## 検証の方針
conjectures/C-0004.md:49:## 結果
conjectures/C-0007.md:16:## 主張
conjectures/C-0007.md:20:## 注意
conjectures/C-0007.md:26:## 詳細化の論点
conjectures/C-0007.md:36:## 背景
conjectures/C-0007.md:41:## 物理学的な新規性（見立て）
conjectures/C-0007.md:45:## 評価の根拠
conjectures/C-0007.md:51:## 検証の方針
conjectures/C-0007.md:57:## 結果
16:## 主張
20:## 詳細化の論点
24:## 背景
28:## 評価の根拠
34:## 検証の方針
38:## 結果
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -lc "第 20 回：「実験パラメータ」" definitions/*.md assumptions/*.md conjectures/*.md; python3 -m pytest -q tools/tests 2>&1 | tail -1
```

</details>

<details><summary>結果: Bash</summary>

```text
definitions/D-0001.md
definitions/D-0003.md
definitions/D-0011.md
assumptions/A-0001.md
assumptions/A-0002.md
assumptions/A-0003.md
assumptions/A-0004.md
assumptions/A-0005.md
assumptions/A-0006.md
33 passed in 0.17s
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "実験パラメータ" roadmap.md NEXT.md | cut -c1-150
```

</details>

<details><summary>結果: Bash</summary>

```text
roadmap.md:45:| T-0004 | 実験パラメータの空間と、結果の統計の空間の位相 | B | なし | [D-0001](definitions/D-0001.md)、[D-000
roadmap.md:122:### T-0004 実験パラメータの空間と、結果の統計の空間の位相
roadmap.md:259:  - **「実験パラメータ」から「設定」への統一**：既存研究（統計学、Le Cam）では「パラメータ」は�
roadmap.md:260:  - 影響の範囲：「実験における時空」「時空の部分」「実験パラメータ」を使う定義・前提・予想�
NEXT.md:16:    1. 「実験における時空」は、実験装置の中の時計や物差しで測った「実験パラメータ」を記述する数
NEXT.md:43:- 第 19 回：ロードマップの T-0016 の続きとして、第 17 回・第 18 回の調査メモについてユーザーと対話し
NEXT.md:50:- 第 19 回に合意した方針（D-0003 の再編、$`τ^O_π`$ の一般化、「実験パラメータ」から「設定」への統一
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -i 's/| T-0004 | 実験パラメータの空間と、結果の統計の空間の位相 |/| T-0004 | 設定の空間と、結果の統計の空間の位相 |/; s/^### T-0004 実験パラメータの空間と、結果の統計の空間の位相$/### T-0004 設定の空間と、結果の統計の空間の位相/' roadmap.md && grep -n "T-0004 " roadmap.md | head -3 | cut -c1-60; grep -n "T-0004" framework.md | cut -c1-100 | head
```

</details>

<details><summary>結果: Bash</summary>

```text
45:| T-0004 | 設定の空間と、結果の統計の空間�
46:| T-0005 | 尤度と同時分布、主体の間で共有�
48:| T-0007 | 局在の詳細化 | B | T-0004 | [D-0001](def
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "### T-0004" roadmap.md; git add -A && git commit -qm "第 20 回：「実験パラメータ」の語を「設定」に統一した（定義・前提・予想・用語一覧・記号一覧・framework・ロードマップ）

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: https://claude.ai/code/[伏せ字]" && git push -q && git log -1 --format=%h
```

</details>

<details><summary>結果: Bash</summary>

```text
122:### T-0004 設定の空間と、結果の統計の空間の位相
231bd99
```

</details>

## Claude

(B)「実験パラメータ」→「設定」の統一を終え、231bd99 として push しました。次の既存研究の調査のために、arXiv にアクセスできるか確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp && curl -sS -m 30 -o /dev/null -w "%{http_code}\n" https://arxiv.org/abs/1810.06512; curl -sS -m 30 -o /dev/null -w "%{http_code}\n" https://export.arxiv.org/api/query?id_list=1810.06512; which pdftotext
```

</details>

<details><summary>結果: Bash</summary>

```text
200
200
/usr/bin/pdftotext
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Bash</summary>

```text
D=/tmp/claude-0/-home-user/[ID]/scratchpad/t18; mkdir -p $D && cd $D && for id in 1810.06512 quant-ph/0101012 0908.1583 1311.5253 1804.00749 quant-ph/9609002 gr-qc/0110035 1712.07207 1303.2849; do f=$(echo $id | tr / _); curl -sSL -m 120 -A "Mozilla/5.0" -o $f.pdf https://arxiv.org/pdf/$id && pdftotext -layout $f.pdf $f.txt; echo "$id $(wc -l < $f.txt 2>/dev/null)"; done
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && grep -n -i "probe\b\|system of interest\|apparatus\|experimenter\|observer" 1810.06512.txt | head -40
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 112,120p 1810.06512.txt; sed -n 398,412p 1810.06512.txt; grep -n -i "Heisenberg cut\|cut\b\|chain" 1810.06512.txt | head
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

## Claude

Now Hardy and Chiribella et al.

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && grep -n -i "knob\|preparation device\|measurement apparatus\|transformation device" quant-ph_0101012.txt | head -20; echo ----; grep -n -i "\bsetting\|test\b.*outcome\|agent\|observer\|apparatus" 0908.1583.txt | head -25
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 140,165p quant-ph_0101012.txt; echo ----; grep -n -i "physical device\|laboratory\|circuit\|operational-probabilistic\|\"test\"\|a test\b" 0908.1583.txt | head -15
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 146,200p 0908.1583.txt | cut -c60-130
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && grep -n -i "agent\|user's manual\|decision" 1311.5253.txt | head -20; echo ----; grep -n -i "observer\|agent\|wigner" 1804.00749.txt | head -20
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 30,62p 1311.5253.txt; echo ----; sed -n 95,125p 1804.00749.txt
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && grep -n -i "observer" quant-ph_9609002.txt | head -25
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 143,172p quant-ph_9609002.txt | cut -c1-70; echo -----; grep -n -i "partial observable\|complete observable\|clock\|observer" gr-qc_0110035.txt | head -25
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 60,110p gr-qc_0110035.txt
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 110,150p gr-qc_0110035.txt; echo ----; grep -n -i "reference frame\|observer\|laboratory" 1712.07207.txt | head -20
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 72,100p 1712.07207.txt | cut -c1-200; echo ----; grep -n -i "measurement setting\|setting x\|inputs\b\|choice of measurement" 1303.2849.txt | head -12
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/t18 && sed -n 203,232p quant-ph_9609002.txt | cut -c1-70; grep -n -i "coupling region\|compact" 1810.06512.txt | head -5
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_20_agent-observer-apparatus.md を参照）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && grep -n "^@" references.bib | grep -i "fewster\|hardy\|chiribella\|fuchs\|brukner\|rovelli\|giacomini\|brunner\|ludwig" ; ls surveys | tail -3; head -30 surveys/2026-09-30_18_limit-topology.md | sed -n 1,12p
```

</details>

<details><summary>結果: Bash</summary>

```text
348:@article{fewster2020,
456:@misc{fewster2016,
569:@article{fewster2015,
735:@inproceedings{fuchs2009priors,
749:@article{fuchs2013,
916:@article{ludwig1968,
926:@book{ludwig1985,
2026-09-30_17_comparison-of-experiments.md
2026-09-30_18_limit-topology.md
README.md
# 実験の族の極限の位相：Le Cam の弱位相

- 作成：[2026-09-30 第 18 回](../summaries/2026-09-30_18_limit-topology.md)（[T-0016](../roadmap.md)）
- 重点：T-0016 の残りのうち、D-0005 の「極限の位相」に直結する二つ（Le Cam の実験の弱収束と、Ludwig の一様構造）に絞る（Claude の提案に、ユーザーが賛成）。深さは、本文で定義と定理の仮定と結論まで確かめる。
- 2〜5 節は原典で確かめた内容である（要約。他者の文章の長い引用はしない）。6 節は原典に書かれていない、プロジェクトへのつながりの候補（Claude の見立てと検算）である。両者を区別して読むこと。

## 1. 読んだ文献

`ludwig1985` 以外の PDF は非公開リポジトリの `papers/<引用キー>.pdf` にある。4 件とも、第 18 回にユーザーが入手した出版社版である。`ludwig1985` は書籍で、ユーザーが電子版を入手し、該当するページのスクリーンショットを見せてもらって確かめた（PDF は置いていない）。

| 引用キー | 文献 | 読んだ範囲 | 役割 |
| --- | --- | --- | --- |
```

</details>

## Claude

arXiv から 9 本の論文を取得し、本文で用語の使われ方を確かめました。いまは調査メモと参考文献を書いています。

<details><summary>ツール: Bash</summary>

```text
sed -n 348,360p references.bib; sed -n 749,760p references.bib; grep -n "^@.*fewster2020\|title" references.bib | sed -n '/fewster2020/,+2p' | head; grep -n "1810.06512\|0908.1583\|1311.5253" references.bib
```

</details>

<details><summary>結果: Bash</summary>

```text
@article{fewster2020,
  author  = {Fewster, Christopher J. and Verch, Rainer},
  title   = {Quantum fields and local measurements},
  journal = {Communications in Mathematical Physics},
  volume  = {378},
  pages   = {851},
  year    = {2020},
  eprint  = {1810.06512},
}

@article{bostelmann2021,
  author  = {Bostelmann, Henning and Fewster, Christopher J. and Ruep, Maximilian H.},
  title   = {Impossible measurements require impossible apparatus},
@article{fuchs2013,
  author  = {Fuchs, Christopher A. and Schack, R\"{u}diger},
  title   = {Quantum-{B}ayesian coherence},
  journal = {Reviews of Modern Physics},
  volume  = {85},
  pages   = {1693--1715},
  year    = {2013},
  doi     = {10.1103/RevModPhys.85.1693},
  eprint  = {0906.2187},
}

@article{blackwell1962,
348:@article{fewster2020,
350:  title   = {Quantum fields and local measurements},
360:  title   = {Impossible measurements require impossible apparatus},
355:  eprint  = {1810.06512},
```

</details>

<details><summary>ツール: Bash</summary>

```text
curl -sS -m 60 "https://export.arxiv.org/api/query?id_list=quant-ph/0101012,0908.1583,1311.5253,1804.00749,quant-ph/9609002,gr-qc/0110035,1712.07207,1303.2849&max_results=10" | python3 -c "
import sys,re
t=sys.stdin.read()
for e in t.split('<entry>')[1:]:
    g=lambda k: (re.search('<'+k+'[^>]*>(.*?)</'+k+'>',e,re.S) or [None,''])[1].strip().replace('\n',' ')
    au=re.findall('<name>(.*?)</name>',e)
    print(g('id'),'|',g('title'),'|',', '.join(au),'|',g('arxiv:journal_ref'),'|',g('arxiv:doi'))
"
```

</details>

<details><summary>結果: Bash</summary>

```text
http://arxiv.org/abs/0908.1583v5 | Probabilistic theories with purification | G. Chiribella, G. M. D'Ariano, P. Perinotti | Phys. Rev. A 81, 062348 (2010) | 10.1103/PhysRevA.81.062348
http://arxiv.org/abs/1712.07207v2 | Quantum mechanics and the covariance of physical laws in quantum reference frames | Flaminia Giacomini, Esteban Castro-Ruiz, Časlav Brukner | Nat. Commun. 10, 494 (2019) | 10.1038/s41467-018-08155-0
http://arxiv.org/abs/quant-ph/0101012v4 | Quantum Theory From Five Reasonable Axioms | Lucien Hardy |  | 
http://arxiv.org/abs/gr-qc/0110035v3 | Partial observables | Carlo Rovelli | Phys.Rev.D65:124013,2002 | 10.1103/PhysRevD.65.124013
http://arxiv.org/abs/1804.00749v1 | A no-go theorem for observer-independent facts | Caslav Brukner | Entropy 20, 350, (2018) | 10.3390/e20050350
http://arxiv.org/abs/1303.2849v3 | Bell nonlocality | Nicolas Brunner, Daniel Cavalcanti, Stefano Pironio, Valerio Scarani, Stephanie Wehner | Rev. Mod. Phys. 86, 419 (2014) | 10.1103/RevModPhys.86.419
http://arxiv.org/abs/quant-ph/9609002v2 | Relational Quantum Mechanics | Carlo Rovelli | Int. J. of Theor. Phys. 35 (1996) 1637 | 10.1007/BF02302261
http://arxiv.org/abs/1311.5253v1 | An Introduction to QBism with an Application to the Locality of Quantum Mechanics | Christopher A. Fuchs, N. David Mermin, Ruediger Schack | Am. J. Phys., Vol. 82, No. 8, August 2014, 749-754 | 10.1119/1.4874855
```

</details>

<details><summary>ツール: Write: /home/user/point-free-spacetime/surveys/2026-09-30_20_agent-observer-apparatus.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/surveys/2026-09-30_20_agent-observer-apparatus.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/surveys/2026-09-30_20_agent-observer-apparatus.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash</summary>

```text
cat >> references.bib <<'EOF'

@misc{hardy2001,
  author  = {Hardy, Lucien},
  title   = {Quantum theory from five reasonable axioms},
  year    = {2001},
  eprint  = {quant-ph/0101012},
}

@article{chiribella2010,
  author  = {Chiribella, Giulio and D'Ariano, Giacomo Mauro and Perinotti, Paolo},
  title   = {Probabilistic theories with purification},
  journal = {Physical Review A},
  volume  = {81},
  pages   = {062348},
  year    = {2010},
  doi     = {10.1103/PhysRevA.81.062348},
  eprint  = {0908.1583},
}

@article{brunner2014,
  author  = {Brunner, Nicolas and Cavalcanti, Daniel and Pironio, Stefano and Scarani, Valerio and Wehner, Stephanie},
  title   = {Bell nonlocality},
  journal = {Reviews of Modern Physics},
  volume  = {86},
  pages   = {419},
  year    = {2014},
  doi     = {10.1103/RevModPhys.86.419},
  eprint  = {1303.2849},
}

@article{fuchs2014,
  author  = {Fuchs, Christopher A. and Mermin, N. David and Schack, R\"{u}diger},
  title   = {An introduction to {QB}ism with an application to the locality of quantum mechanics},
  journal = {American Journal of Physics},
  volume  = {82},
  pages   = {749--754},
  year    = {2014},
  doi     = {10.1119/1.4874855},
  eprint  = {1311.5253},
}

@article{brukner2018,
  author  = {Brukner, \v{C}aslav},
  title   = {A no-go theorem for observer-independent facts},
  journal = {Entropy},
  volume  = {20},
  pages   = {350},
  year    = {2018},
  doi     = {10.3390/e20050350},
  eprint  = {1804.00749},
}

@article{rovell
…（以下 1005 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

````text
92
33 passed in 0.13s
# 参考文献の調査メモ

時系列で調査の経過を追えるよう、ファイル名の先頭に、作成したセッションの日付と番号を付けます（[`summaries/`](../summaries/) と同じ形式）。

- 論文ごとのメモ: `YYYY-MM-DD_NN_<引用キー>.md`（例: `2026-09-25_02_heunen2024.md`）
- テーマごとのメモ: `YYYY-MM-DD_NN_<テーマ>.md`（例: `2026-09-25_02_pointfree-topology-basics.md`）

引用キーは [`references.bib`](../references.bib) と揃えます。
同じ論文やテーマを後のセッションで読み直したときは、既存のメモを更新し、冒頭に更新したセッションを追記します。

## 論文メモの書式

```markdown
# <引用キー>: <タイトル>

- 書誌情報: 著者、タイトル、掲載誌・出版社、年、DOI・arXiv ID
- 入手状況: 非公開リポジトリに PDF あり・なし

## 要旨（自分の言葉で）
## 本プロジェクトとの関係
````

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime-private && git status -sb | head -2 && sed -n 1,15p papers/README.md && ls papers | wc -l && ls papers | head -40
```

</details>

<details><summary>結果: Bash</summary>

```text
## claude/zealous-keller-o7r1sv...origin/claude/zealous-keller-o7r1sv
# 論文の PDF

ファイル名は `<引用キー>.pdf` とします。引用キーは公開リポジトリの `references.bib` と揃えます。

| ファイル | 文献 | 版 |
| --- | --- | --- |
| `halvorson2001.pdf` | Halvorson, On the nature of continuous physical quantities in classical and quantum mechanics (2001) | arXiv:quant-ph/0003074v1（2000-03-17）。出版社版との違いは未確認 |
| `doplicher1995.pdf` | Doplicher–Fredenhagen–Roberts, The quantum structure of spacetime at the Planck scale and quantum fields (1995) | arXiv:hep-th/0303037v1（2003-03-05 に公開された版。Commun. Math. Phys. 172, 187–220） |
| `heijmans1990.pdf` | Heijmans–Ronse, The algebraic basis of mathematical morphology I: dilations and erosions (1990) | 出版社版（Computer Vision, Graphics, and Image Processing 50） |
| `heunen2009.pdf` | Heunen–Landsman–Spitters, A topos for algebraic quantum theory (2009) | 出版社版 |
| `arntzenius2003.pdf` | Arntzenius, Is quantum mechanics pointless? (2003) | 著者最終稿（出版社版ではない） |
| `heunen2024.pdf` | Heunen–van der Schaaf, Ordered locales (2024) | 出版社版 |
| `heunen2026.pdf` | Heunen–van der Schaaf, Causal coverage in ordered locales and spacetimes (2026) | 出版社版（J. Math. Phys. 67, 083506、2026-08-25 公開） |
| `heunen2026_arxiv-v1.pdf` | 同上 | arXiv:2510.17417v1（2025-10-20）。第 03 回の論文メモの節・定理番号はこの版による |
| `hossenfelder2013.pdf` | Hossenfelder, Minimal length scale scenarios for quantum gravity (2013) | 出版社版（Living Rev. Relativity 16, 2） |
57
README.md
amelinocamelia2011.pdf
arntzenius2003.pdf
blackwell1951.pdf
blackwell1953.
…（以下 616 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
git fetch -q origin main && git log --oneline -1 origin/main && git checkout -q -B claude/zealous-keller-o7r1sv origin/main && S=/tmp/claude-0/-home-user/[ID]/scratchpad/t18 && cp $S/quant-ph_0101012.pdf papers/hardy2001.pdf && cp $S/0908.1583.pdf papers/chiribella2010.pdf && cp $S/1303.2849.pdf papers/brunner2014.pdf && cp $S/1311.5253.pdf papers/fuchs2014.pdf && cp $S/1804.00749.pdf papers/brukner2018.pdf && cp $S/quant-ph_9609002.pdf papers/rovelli1996.pdf && cp $S/gr-qc_0110035.pdf papers/rovelli2002.pdf && cp $S/1712.07207.pdf papers/giacomini2019.pdf && cat >> papers/README.md <<'EOF'
| `hardy2001.pdf` | Hardy, Quantum theory from five reasonable axioms (2001) | arXiv:quant-ph/0101012v4（第 20 回に取得） |
| `chiribella2010.pdf` | Chiribella–D'Ariano–Perinotti, Probabilistic theories with purification (2010) | arXiv:0908.1583v5（第 20 回に取得。Phys. Rev. A 81, 062348） |
| `brunner2014.pdf` | Brunner ほか, Bell nonlocality (2014) | arXiv:1303.2849v3（第 20 回に取得。Rev. Mod. Phys. 86, 419） |
| `fuchs2014.pdf` | Fuchs–Mermin–Schack, An introduction to QBism with an application to the locality of quantum mechanics (2014) | arXiv:1311.5253v1（第 20 回に取得。Am. J. Phys. 82, 749） |
| `brukner2018.pdf` | Brukner, A no-go theorem for observer-independent facts (2018) | arXiv:1804.00749v1（第 20 回に取得。Entropy 20, 350） |
| `rovelli1996.pdf` | Rovelli, Relational quantum mechanics (1996) | arXiv:quant-ph/9609002v2（第 20 回に取得。Int. J. Theor. Phys. 35, 1637） |
| `rovelli2002.pdf` |
…（以下 363 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
edea906 Merge pull request #11 from kittenkiki15/claude/zealous-keller-o7r1sv
| `lecam1972.pdf` | Le Cam, Limits of experiments (1972) | 出版社版（Project Euclid。Proc. Sixth Berkeley Symp. Math. Statist. Probab., Vol. 1, 245–261。ユーザーが入手） |
| `vandervaart2002.pdf` | van der Vaart, The statistical work of Lucien Le Cam (2002) | 出版社版（Project Euclid。Ann. Statist. 30, 631–682。ユーザーが入手） |
| `torgersen1970.pdf` | Torgersen, Comparison of experiments when the parameter space is finite (1970) | 出版社版（Springer。Z. Wahrsch. verw. Geb. 16, 219–249。ユーザーが入手） |
| `ludwig1968.pdf` | Ludwig, Attempt of an axiomatic foundation of quantum mechanics and more general theories. III (1968) | 出版社版（Project Euclid。Commun. Math. Phys. 9, 1–12。ユーザーが入手） |
 M papers/README.md
?? papers/brukner2018.pdf
?? papers/brunner2014.pdf
?? papers/chiribella2010.pdf
?? papers/fuchs2014.pdf
?? papers/giacomini2019.pdf
?? papers/hardy2001.pdf
?? papers/rovelli1996.pdf
?? papers/rovelli2002.pdf
```

</details>

## Claude

調査メモを書き終え、参考文献を 8 件追加しました。いまは、取得した PDF を非公開リポジトリに置き、両方のリポジトリでコミットしています。

<details><summary>ツール: Bash</summary>

```text
git add -A && git commit -qm "第 20 回：主体・観測者・装置の用語の調査で読んだ arXiv 版の論文 8 件を追加

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: https://claude.ai/code/[伏せ字]" && git push -q -u origin claude/zealous-keller-o7r1sv 2>&1 | grep -v "^remote:" ; cd ../point-free-spacetime && git add -A && git commit -qm "第 20 回：主体・観測者・装置・設定の既存研究での使われ方の調査メモと、参考文献 8 件を追加

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: https://claude.ai/code/[伏せ字]" && git push -q && git log -1 --format=%h
```

</details>

<details><summary>結果: Bash</summary>

```text
0fb96d4
```

</details>

## Claude

(B) の書き換えと、既存研究の調査が終わりました。どちらも push 済みです。

#### 済んだこと

**(B) 「実験パラメータ」を「設定」に統一**（231bd99）
- 書き換えたのは、定義 3 件、前提 6 件、予想 2 件、`framework.md`、用語一覧、記号一覧、ロードマップの T-0004 の名前です。A-0003 の名前は「設定と結果は実数値」に、A-0004 の名前は「資源の量を設定に含める」になりました。
- 統計学の意味の「パラメータ」（Le Cam の $`Θ`$ など）は、そのまま残しました。
- ユーザーの発言を引用した箇所と、履歴の記録は書き換えていません。そうした箇所には「第 20 回に『設定』に改めた語」と注記しています。
- 定義と前提のファイルの履歴には、用語だけの変更であることを書きました。

**既存研究の調査**（[調査メモ](surveys/2026-09-30_20_agent-observer-apparatus.md)、0fb96d4）
- arXiv の原典 9 件で、語の使われ方を確かめました。Fewster–Verch、Hardy、Chiribella ほか、ベル非局所性のレビュー、QBism、Wigner の友人（Brukner）、関係的量子力学、部分観測量（Rovelli）、量子参照系です。
- 新しく登録した 8 件は、`references.bib` に加え、PDF を非公開リポジトリに置きました。非公開リポジトリにも同じ名前のブランチで push してあり、PR はセッションの終わりに作ります。
- 分かったことは次の四点です。
  - **「観測者」は既存研究でも二つの意味で使われています。** 一つは基準系（相対論、Rovelli 1996、量子参照系）、もう一つは結果を知覚する者（Wigner の友人）です。
  - **「実験を行い、信念を更新する者」には、QBism の agent が当たります。** agent は「行為する者」の意味です。
  - **「設定」は、Hardy の「つまみの設定」、ベル実験の「測定の設定」と同じ役割です。**
  - **Rovelli（2002）は時計の読みを部分観測量とし、一般相対論的な文脈では、時刻とほかの量の区別がなくなるとしています。** 時計の読みを設定と結果のどちらに置くかという D-0003 の論点に参考になり、(A) で使えます。

#### (C) の使い分けの案（Claude の提案。未決定）

| 語 | 意味 | 既存研究との対応 | 今の用法からの変更 |
| --- | --- | --- | --- |
| **主体**（agent） | 事前分布を持ち、実験の記録から信念を更新する者。実験を行う（設定を選び、結果を得る）こともある | QBism の agent、Hardy の experimentalist | A-0001 の「実験の主体」と A-0007 の「主体」を、この一つの語にまとめる |
| **観測者**（observer） | 基準の時計と物差しを持つ基準系。時間と空間を比べる基準 | 相対論の観測者、Rovelli 1996、参照系 | D-0001 の「実験を行う観測者の世界線」は「実験を行う主体の世界線」に改める |
| **装置**（apparatus） | 時空の中に領域を占める物理系。準備と登録に分けてもよい | Hardy の準備・変換・測定の装置、Ludwig の準備装置と登録装置、Fewster–Verch のプローブ | 変更なし |

この案には、次の三つの帰結があります。

- **定義として登録するか**：主体はプロジェクトの中心になる概念なので、定義（D-0012）として登録することを提案します。観測者は、ご指摘の D-0001・D-0002 との関係を明らかにしたうえで、(A) の $`M_O`$ と合わせて決めるのがよいと思います。装置は、用語一覧の説明にとどめます。
- **観測者が物理系かどうか**：量子参照系の文献は、参照系を物理系として扱います。本プロジェクトの観測者も、実際の実験の中の物理系（装置の一種）とみるのか、可能な実験を記述するための理想化とみるのかという問いが残ります。これは (A) で扱います（調査メモの 4 節に記録しました）。
- **第 07 回の「観測する側と観測される側の対称性」の読み直し**：主体と観測者を分けると、この対称性は主体どうしの関係ではなく、装置と観測される系の間の関係として読むことになります。

#### ご相談

1. 上の三つの語の使い分けでよいでしょうか。
2. 「主体」の意味に「実験を行うこともある」を含めてよいでしょうか。これは、実験を行わずにデータだけを受け取る主体（A-0007 の、主体の間で共有するデータ）も許すためです。
3. 定義として登録する範囲は、主体だけを今回登録し、観測者は (A) で決める、という形でよいでしょうか。

## ユーザー

「1. 上の三つの語の使い分けでよいでしょうか」について、三つの語ともに、「実際の～」と「可能な～」に概念を分けたいです。例えば、 A-0001 の「主体」 は「実際の実験」の主体で、高々可算です。これを「実際の主体」と呼ぶことにします。一方、「可能な主体」は「可能な実験」の主体で、非可算であることを許します。A-0007 の「主体」は、「実際の観測量の推定」においては「実際の主体」ですが、「可能な観測量の推定」においては「可能な主体」と解釈します。「実際の～」と「可能な～」で A-0007 の主張を分けた方が、仮定が最小化されてよいかもしれません。「観測者」や「装置」も、「実際の実験」と「可能な実験」とに応じて、それぞれ「実際の～」と「可能な～」に分けておいた方がよいと思います。

また、「観測者」の世界線は実験ごとに異なるはずなので、「観測者」も実験ごとに異なるはずです。一般に、同一の存在が異なる世界線を持つことはできないからです。同様に、「装置」も実験ごとに異なります。「観測者」と「装置」は実験に 1 対 1 対応する概念になると考えられます。一方、「主体」は複数の実験を行うことができます。したがって、「主体」は「観測者」とも「装置」とも別の概念になると考えます。

『2. 「主体」の意味に「実験を行うこともある」を含めてよいでしょうか」について、含めてよいと考えます。A-0001 の「各主体が行う実験も高々可算個」には、0 個 (実験をしない) の場合も含むという解釈です。

『3. 定義として登録する範囲』は、上記の議論を踏まえて、いっしょに再検討したいです。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && sed -n '/^## 主張/,/^## 注意/p' assumptions/A-0007.md; grep -n "主体\|観測者" definitions/D-0001.md definitions/D-0002.md definitions/D-0005.md | cut -c1-160
```

</details>

<details><summary>結果: Bash</summary>

```text
## 主張

異なる主体の事前分布から決まる、無限のデータ列の上の予測分布どうしは、互いに絶対連続である。

条件を課すのは予測分布であって、事前分布そのものではない。例えば、互いに特異な二つの事前分布でも、それぞれが集中するパラメータが同じデータの分布を与えるなら、予測分布は一致する。

## 採用の理由

実際の観測量（[D-0005](../definitions/D-0005.md)）の推定で、主体の事前分布への依存を抑えるため、Blackwell–Dubins の意見の一致を要請する。この前提はその前提条件である（Claude の提案に、ユーザーが賛成した。第 09 回）。

## 注意
definitions/D-0001.md:21:- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める実験における時空の領域�
definitions/D-0005.md:23:- 先行例：QBism の量子状態の断層撮影の読み替え（Caves–Fuchs–Schack 2002 など）では、情報的に完全な
```

</details>

## Claude

三点とも、議論の土台になる大事な整理だと思います。順に、私の見立てを述べます。

#### 1. 「実際の～」と「可能な～」に分けること

賛成です。D-0002 の「実際の実験と可能な実験」の区別を、三つの語すべてに通すことになり、構成が揃います。

- **主体**：「実際の主体」は実際の実験の主体で、A-0001 により高々可算です。「可能な主体」は可能な実験の主体で、非可算も許します。
- **A-0007 を分ける効果**：分けると、実際の観測量の推定（段階 B・C）に必要な仮定が小さくなります。
  - 実際の版が制約するのは、実際にいる主体の事前分布だけです。
  - 可能な版は、「許される事前分布の全体」を制限する、ずっと強い仮定になります。すべての可能な主体の予測分布が、互いに絶対連続でなければならないからです。予測分布が零集合を共有する範囲に、事前分布を限ることにあたります。
  - この差は、主体の個数が可算か非可算かによるものではありません。互いに絶対連続という関係は同値関係なので、個数が非可算でも、どれか一つの予測分布と零集合が一致すれば足ります。差は「実際にいる主体の事前分布」と「考えうる事前分布の全体」の違いから来ます。

#### 2. 観測者・装置は実験と 1 対 1 に対応する、という点

「主体は複数の実験を行えるので、観測者とも装置とも別の概念になる」という結論に賛成です。装置を「その実験で占める領域 $`\mathrm{occ}(e)`$ を持つ物理系」と読むなら、装置が実験と 1 対 1 に対応するのも自然です。同じ物理的な機器を別の実験で使い回すことはありますが、それは別の装置として数えることになります。

観測者については、一点確かめたいことがあります。同じ実験室で順に行う二つの実験は、同じ世界線の異なる区間を使うことがありえます。D-0001 の注意にも「実験を行う観測者の世界線の区間（実験の期間）」とあります。そのため、1 対 1 に対応するのは「観測者の世界線の区間」だと考えられます。観測者を世界線全体と読むと、複数の実験が一つの観測者を共有しうることになります。

この違いは (A) に効きます。

- A-0010 の観測者の役割は、異なるプロトコルの設定を一つの座標 $`M_O`$ で比べることでした。
- 観測者が実験ごとに異なるとすると、異なる実験を比べるには、必ず観測者の取り替え $`M_O → M_{O'}`$ を通ることになります。
- その場合、観測者の取り替えは、今は T-0009 の整合条件の一部にすぎませんが、フレームワークの中心的な構造になります。

どちらの読み方を採るかは、(A) で D-0001・D-0002 との関係を明らかにするときに決めるのがよいと思います。候補は次の二つです。

- (i) 観測者を、実験ごとの世界線の区間とする（実験と 1 対 1）。
- (ii) 観測者を世界線とし、実験はその区間を使う（一つの観測者が複数の実験を持ちうる）。

#### 3. 定義として登録する範囲（再検討の案）

1・2 の議論を踏まえ、次の形を提案します。

- **観測者と装置は、実験の構成要素として D-0001 に含める。** 実験と 1 対 1 に対応するなら、有限な実験が指定するもの（プロトコル、設定、結果）に、「装置」と「観測者（の区間）」を加える形が自然です。こうすると、「実際の観測者・装置」と「可能な観測者・装置」は、D-0002 の区別からそのまま決まり、別に定義する必要がなくなります。
- **主体は、独立した定義にする（D-0012）。** 主体は複数の実験にまたがる概念なので、実験の構成要素にはできません。D-0012 に「実際の主体」（実際の実験を行うか、その記録から信念を更新する者。高々可算個）と「可能な主体」（非可算も許す）を並べて定めます。実験を 0 個しか行わない主体も含めます。
- **前提の書き換え**：
  - A-0001 は、「実際の主体」が高々可算で、各実際の主体が行う実験は高々可算個（0 個を含む）である、と書き直します。
  - A-0007 は、実際の主体の版と可能な主体の版に分けます。分け方には、同じファイルの中で二つの主張にする方法と、別の前提に分ける方法があります。

#### ご相談

1. 観測者は、2 の (i)・(ii) のどちらの読み方にしますか。(A) で決める形でもかまいません。
2. 観測者と装置を D-0001 の構成要素として含め、主体を D-0012 として独立させる、という登録の形でよいでしょうか。
3. A-0007 の分け方は、同じファイルの中で二つの主張にするか、別の前提に分けるか、どちらがよいでしょうか。

## ユーザー

『(i) 観測者を、実験ごとの世界線の区間とする（実験と 1 対 1）』に賛成です。その方がより正確です。「一つの観測者が複数の実験を持ちうる」は避けたいです。

「3. 定義として登録する範囲（再検討の案）」に賛成です。観測者と装置を D-0001 の構成要素として含め、主体を D-0012 として独立させてください。

A-0007 の分け方は、「別の前提に分ける」でお願いします。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && cat definitions/D-0001.md definitions/D-0002.md assumptions/A-0007.md definitions/_template.md; cat definitions/README.md | sed -n 1,40p
```

</details>

<details><summary>結果: Bash</summary>

```text
# D-0001: 有限な実験

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md) |
| 関係する予想・結果 | [C-0003](../conjectures/C-0003.md) |
| 初出 | [2026-09-28 第 08 回](../summaries/2026-09-28_08_observation-as-limit.md) |

## 定義

**有限な実験**とは、一つの実験プロトコル $`π`$ に従い、有限回の操作と観測を行って、有限個の結果を読み出すものである。一つの有限な実験について、次を指定する。

- プロトコル $`π`$（有限の記述を持つ。[A-0002](../assumptions/A-0002.md)）
- 設定 $`x ∈ X_π`$：プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数の組（[A-0003](../assumptions/A-0003.md)）
- 結果の空間 $`Y_π`$ と、読み出した有限個の結果（実数値。[A-0003](../assumptions/A-0003.md)）

## 注意

- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める実験における時空の領域とは区別する。
- 設定の空間 $`X_π`$ と結果の空間 $`Y_π`$ は、プロトコルごとに異なりうる。
- 有限な実験に何を対応させるか（結果の統計）は [D-0004](D-0004.md) で定める。

## 未解決の点

- 各実験が占める領域の決め方（装置の準備や結果の読み出しを実験の領域に含めるか。設定値ごとの装置の占める領域 $`\mathrm{occ}`$ は [D-0011](D-0011.md) で導入した）と、実験が領域 $`R`$ に「収まる」ことの判定（[D-0008](D-0008.md) と共通）。
- 結果の空間 $`Y_π`$ の意味：個々の読みの空間か、実験 1 回分の全出力をまとめた空間か。同じ実験の中の結果どうしの同時分布と、実験を繰り返すときの同時分布を区別する（[D-0004](D-0004.md) と共通）。

## 履歴

- 第 08 回：「有限の期間に、有界な範囲で、有限回の操作を行い、有限個の結果を読み出すもの」として導入した。
- 第 09 回：プロトコル、実数値のパラメータと結果、プロトコルごとの設定の空間と結果の空間を加えた。
- 第 10 回：[第 08 回の調査メモ](../surveys/2026-09-28_08_observation-as-limit.md)（1.2・1.4 節）から移し、文章を整えた。
- 第 20 回：「実験パラメータ」（とその意味での「パラメータ」）の語を「設定」に改めた（[T-0018](../roadmap.md)。用語だけの変更で、内容は変えていない）。
# D-0002: 実際の実験と可能な実験

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0001](../assumptions/A-
…（以下 6013 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "def test" tools/tests/test_framework.py; grep -n "A-0001\|A-0007" definitions/*.md assumptions/*.md conjectures/*.md | grep "依存する ID\|関係する予想" | cut -c1-200
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -rn "A-0007" --include=*.md definitions assumptions conjectures framework.md glossary.md roadmap.md | grep -v "^assumptions/A-0007" | cut -c1-140
```

</details>

<details><summary>結果: Bash</summary>

```text
definitions/D-0005.md:7:| 依存する ID | [D-0002](../definitions/D-0002.md)、[D-0004](../definitions/D-0004.md)、[A-0007](../assumption
definitions/D-0005.md:22:- 事前分布から決まる予測分布どうしの相互絶対連続性（[A-0007](../assumptions/A-0007.md)）�
assumptions/README.md:36:| [A-0007](A-0007.md) | 事前分布から決まる予測分布どうしの相互絶対連続性 | 観測量 | 採�
framework.md:37:| 2. 観測量 | 実際の実験の族の極限としての観測量と、その局在 | [D-0004](definitions/D-0004.md) 応
framework.md:71:  A_0007(["A-0007: 事前分布から決まる予測分布どうしの相互絶対連続性"])
framework.md:160:- **層 1〜2：マルコフ圏**。応答関数（D-0004）はマルコフ核（$`\mathsf{Stoch}`$ の射）で、一つ�
framework.md:167:層 2 の推定（D-0005）と主体の間の一致（A-0007）を、QBism の量子 de Finetti 定理による一致と比
framework.md:170:- 本プロジェクトは、交換可能性を課さず、予測分布の相互絶対連続性（A-0007）から将来の�
framework.md:171:- Fuchs–Schack 2009 が一致しない例として挙げるものは、どれも予測分布が互いに絶対連続で�
framework.md:173:第 16 回に、Blackwell–Dubins 1962 と Diaconis–Freedman 1986 の原典を確かめた（[第 16 回の調査メモ]
glossary.md:54:| merging of opinions | 意見の一致 | 異なる事前分布を持つ主体による、過去のデータで条件付け�
roadmap.md:44:| T-0003 | QBism の先行研究の調査（第 15 回） | 調査 | なし | [D-0005](definitions/D-0005.md)、[A-0007](assum
roadmap.md:46:| T-0005 | 尤度と同時分布、主体の間で共有するデータの空間 | B | T-0004 | [D-0001](definitions/D-0001.md
roadmap.md:47:| T-0006 | 極限と事後分布の集中 | B | T-0004、T-0005 | [D-0005](definitions/D-0005.md)、[D-0006](definitions/D-000
roadmap.md:57:| T-0016 | 実験の族の位相と極限の先行研究の調査（第 15〜19 回） | 調査 | なし | [D-0001](definition
roadmap.md:59:| T-0018 | 主体・観測者・装置の使い分けと、設定・時空・パラメータの概念と用語の整理（第 
roadmap.md:119:  - [A-0007](assumptions/A-0007.md) と [D-0005](definitions/D-0005.md) の「注意」に比較の結果を加え、一致�
r
…（以下 681 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
23:def test_each_file_has_title_and_rows():
32:def test_readme_lists_every_file_with_same_name_layer_state():
46:def test_referenced_ids_exist():
54:def test_id_links_point_to_matching_files():
62:def test_link_mismatch_is_detected():
73:def test_targets_are_assumptions_not_dependencies():
91:def test_only_conjectures_have_targets():
101:def test_roadmap_task_states_are_valid():
111:def test_no_self_dependency():
116:def test_no_dependency_cycles():
133:def test_related_conjectures_match_dependencies():
142:def test_graph_is_up_to_date():
147:def test_links_exist():
157:def test_roadmap_task_ids_are_unique_and_described():
definitions/D-0002.md:7:| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0001](../assumptions/A-0001.md) |
definitions/D-0005.md:7:| 依存する ID | [D-0002](../definitions/D-0002.md)、[D-0004](../definitions/D-0004.md)、[A-0007](../assumptions/A-0007.md) |
definitions/D-0011.md:7:| 依存する ID | [D-0001](D-0001.md)、[D-0002](D-0002.md)、[D-0003](D-0003.md)、[D-0009](D-0009.md)、[D-0010](D-0010.md)、[A-0001](../assumptions/A-0001.md)、[A-0008](
conjectures/C-0005.md:12:| 依存する ID | [D-0005](../definitions/D-0005.md)、[D-0006](../definitions/D-0006.md)、[A-0001](../assumptions/A-0001.md) |
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 1,30p definitions/D-0006.md; cat assumptions/A-0001.md | sed -n 1,12p; ls assumptions
```

</details>

<details><summary>結果: Bash</summary>

```text
# D-0006: 可能な観測量

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 可能な観測量 |
| 依存する ID | [D-0002](../definitions/D-0002.md)、[D-0004](../definitions/D-0004.md)、[D-0005](../definitions/D-0005.md)、[D-0007](../definitions/D-0007.md) |
| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0005](../conjectures/C-0005.md) |
| 初出 | [2026-09-29 第 09 回](../summaries/2026-09-29_09_actual-and-possible-observables.md) |

## 定義

**可能な観測量**は、可能な実験（[D-0002](D-0002.md)）の族の極限として得られる観測量である。

## 注意

- 構成の順序：実際の観測量から観測量の時空（[D-0007](D-0007.md)）を再構成し、その中で物理的にモデル化した装置（時計や物差しなど）を使って可能な実験を記述し直してから、可能な観測量を定める。その記述ができることは予想である（[C-0002](../conjectures/C-0002.md)）。

## 未解決の点

- 極限の取り方。可能な実験は設定 $`(π, x)`$ だけで結果の記録を含まないので、実際の観測量（[D-0005](D-0005.md)）と同じ形（データで更新した事後分布の極限）にはできない。可能な実験に、観測量の時空の中のモデルが与える結果の統計（応答関数 [D-0004](D-0004.md) の値）を対応させ、その族の極限として定める案がある（見立て）。
- 実際の観測量との関係（可能な観測量が実際の観測量を含むか、一致するか、真に大きいか）。
- 可能な観測量から時空を再構成し直しても同じ時空が得られる、という不動点の条件を要請するか（見立て）。
- この定義は、可能な実験を観測量の時空の中で記述し直せること（[C-0002](../conjectures/C-0002.md)）を前提に使う一方、C-0002 はこの定義に依存する。この依存が「結論を得てから使う定義」への参照か、証明の前提かを区別する。
- 上の循環は、D-0006 の依存する ID から C-0002 を省くだけでは解消しない（依存関係の図が非循環になるだけである）。解消するには、C-0002 を述べるのに必要な D-0006 の部分を C-0002 に依存しない形で切り出すか、条件付きの構成と、その条件を導く予想を分ける（PR #28 のレビュー）。

## 履歴

- 第 09 回：ユーザーの提案で、可能な実験の族の極限を「可能な観測量」とした。
- 第 10 回：[第 08 回の調査メモ](../surveys/2026-09-28_08_observation-as-limit.md)（1.2・1.4 節）から移し、文章を整えた。
# A-0001: 実際の実験の可算性

| 項目 | 値 |
| --- | --- |
| 状態 | 採用 |
| 層 | 実験 |
| 依存する ID | なし |
| 関係する予想・結果 | [C-0005](../conjectures/C-000
…（以下 230 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='definitions/D-0001.md'
rep(p,'- 結果の空間 $`Y_π`$ と、読み出した有限個の結果（実数値。[A-0003](../assumptions/A-0003.md)）\n',
'''- 結果の空間 $`Y_π`$ と、読み出した有限個の結果（実数値。[A-0003](../assumptions/A-0003.md)）
- **装置**：その実験で、準備から結果の読み出しまでに使う物理系
- **観測者**：その実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うもの（[A-0010](../assumptions/A-0010.md) の基準の時計と物差し）

装置と観測者は、実験ごとに一つずつ定まる（実験と 1 対 1 に対応する）。
''')
rep(p,'- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める実験における時空の領域とは区別する。\n',
'''- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める実験における時空の領域とは区別する。
- 装置と観測者が実験と 1 対 1 に対応するのは、同一の存在が異なる世界線を持つことはできず、実験ごとに世界線の区間が異なるからである（ユーザーの説明。第 20 回）。同じ機器や同じ実験室を別の実験で使っても、別の装置・別の観測者として数える。一つの観測者が複数の実験を持つ扱いはしない（ユーザーの判断）。
- 実験を行う者は**主体**（[D-0012](D-0012.md)）とよび、観測者・装置とは別の概念とする。一つの主体は複数の実験を行える。
- 実際の実験の装置・観測者を「実際の装置」「実際の観測者」、可能な実験の装置・観測者を「可能な装置」「可能な観測者」とよぶ（[D-0002](D-0002.md)）。
- 既存研究での装置・観測者の語の使われ方は、[第 20 回の調査メモ](../surveys/2026-09-30_20_agent-observer-apparatus.md)にある（装置：Hardy の準備・変換・測定の装置、Ludwig の準備装置と登録装置、Fewster–Verch のプローブ。観測者：相対論や関係的量子力学の、基準系としての観測者）。
''')
rep(p,'| 依存する ID | [A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md) |',
'| 依存する ID | [A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)、[A-0010](../assumptions/A-0010.md) |')
rep(p,'## 履歴\n','''- 観測者が実験と 1 対 1 に対応することと、[A-0010](../assumptions/A-0010.md)・[D-0003](D-0003.md) の観測者 $`O`$ の座標 $`M_O`$（異なるプロトコルの設定を一つの座標で比べる）との関係。観測者が実験ごとに異なるので、異なる実験を比べるには観測者の取り替え $`M_O →
…（以下 362 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
11:## 定義
23:## 注意
33:## 未解決の点
41:## 履歴
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "依存する ID" assumptions/A-0010.md assumptions/A-0002.md assumptions/A-0003.md definitions/D-0003.md
```

</details>

<details><summary>結果: Bash</summary>

```text
assumptions/A-0010.md:7:| 依存する ID | [D-0001](../definitions/D-0001.md) |
assumptions/A-0002.md:7:| 依存する ID | なし |
assumptions/A-0003.md:7:| 依存する ID | なし |
definitions/D-0003.md:7:| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)、[A-0004](../assumptions/A-0004.md)、[A-0010](../assumptions/A-0010.md) |
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='definitions/D-0001.md'
rep(p,'、[A-0010](../assumptions/A-0010.md) |','|'.join(['',''])[:0]+' |')
rep(p,'基準の時計と物差しを伴うもの（[A-0010](../assumptions/A-0010.md) の基準の時計と物差し）','基準の時計と物差しを伴うもの')
rep(p,'- 実験を行う者は**主体**','- 観測者の基準の時計と物差しで装置の読みを座標に換算できることは、前提 [A-0010](../assumptions/A-0010.md) で置く（この定義は A-0010 に依存しない）。\n- 実験を行う者は**主体**')
EOF
sed -n 1,10p definitions/D-0001.md | grep 依存
```

</details>

<details><summary>結果: Bash</summary>

```text
| 依存する ID | [A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md) |
```

</details>

## Claude

Now D-0002 and D-0012.

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='definitions/D-0002.md'
rep(p,'| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0001](../assumptions/A-0001.md) |','| 依存する ID | [D-0001](../definitions/D-0001.md) |')
rep(p,'- **実際の実験**：実際に行われた有限な実験（[D-0001](D-0001.md)）。行ったときの組 $`(π, x)`$ と、得た結果の記録からなる。[A-0001](../assumptions/A-0001.md) により、実際の実験の全体は高々可算である。\n',
'''- **実際の実験**：実際に行われた有限な実験（[D-0001](D-0001.md)）。行ったときの組 $`(π, x)`$ と、得た結果の記録からなる。
- 実際の実験の装置と観測者（[D-0001](D-0001.md)）を**実際の装置**・**実際の観測者**、可能な実験の装置と観測者を**可能な装置**・**可能な観測者**とよぶ。可能な装置・可能な観測者は、可能な実験の記述（[C-0002](../conjectures/C-0002.md) の観測量の時空の中のモデル）で与える。
''')
rep(p,'## 注意\n\n','''## 注意

- 実際の実験の全体が高々可算であることは、前提 [A-0001](../assumptions/A-0001.md) で置く（この定義は A-0001 に依存しない。第 20 回に、A-0001 が実際の主体（[D-0012](D-0012.md)）を通してこの定義に依存するようになったので、依存の向きを整理した）。
- 実際の実験・可能な実験を行う者を、それぞれ実際の主体・可能な主体とよぶ（[D-0012](D-0012.md)）。
''')
s=open(p).read().rstrip('\n')+'\n- 第 20 回：実際の装置・観測者と可能な装置・観測者を加えた（ユーザーの判断）。A-0001 への依存を外し、実際の実験の可算性は A-0001 の側に置いた（依存の循環を避けるため。内容は変えていない）。\n'
open(p,'w').write(s)
EOF
cat > definitions/D-0012.md <<'EOF'
# D-0012: 主体

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[D-0002](../definitions/D-0002.md) |
| 関係する予想・結果 | なし |
| 初出 | [2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md) |

## 定義

**主体**（agent）とは、事前分布を持ち、実験の記録から信念を更新する者である。主体は実験を行う（設定を選び、結果の記録を得る）こともある。主体が行う実験の個数は 0 個で
…（以下 1012 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
ok
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='assumptions/A-0001.md'
rep(p,'| 依存する ID | なし |','| 依存する ID | [D-0002](../definitions/D-0002.md)、[D-0012](../definitions/D-0012.md) |')
rep(p,'実験の主体は高々可算個で、各主体が行う実験も高々可算個である。したがって、**実際に行われた**有限な実験の全体は高々可算である。',
'実際の主体（[D-0012](../definitions/D-0012.md)）は高々可算個で、各実際の主体が行う実験も高々可算個（0 個を含む）である。各実際の実験は、いずれかの実際の主体が行う。したがって、**実際に行われた**有限な実験（実際の実験。[D-0002](../definitions/D-0002.md)）の全体は高々可算である。')
rep(p,'「実験の主体」は、実験をする者の意味である。主体が高々可算個であることを仮定する背景は',
'「主体」は、第 16 回の時点では「実験の主体」（実験をする者）の意味で、第 20 回に D-0012 の実際の主体に改めた。主体が高々可算個であることを仮定する背景は')
rep(p,'- 対象は実際の実験である。','- 対象は実際の実験と実際の主体である。可能な主体（[D-0012](../definitions/D-0012.md)）は、非可算個あることも許す。')
s=open(p).read().rstrip('\n')+'\n- 第 20 回：ユーザーの判断で、主語を「実際の主体」（D-0012）に改め、各主体が行う実験に 0 個を含むことと、各実際の実験をいずれかの実際の主体が行うことを明記した（可算性の主張は変えていない）。\n'
open(p,'w').write(s)
EOF
sed -n '/^## 主張/,/^## 注意/p' assumptions/A-0001.md; sed -n '/^## 注意/,/^## 未解決/p' assumptions/A-0001.md | head -5
```

</details>

<details><summary>結果: Bash</summary>

```text
## 主張

実際の主体（[D-0012](../definitions/D-0012.md)）は高々可算個で、各実際の主体が行う実験も高々可算個（0 個を含む）である。各実際の実験は、いずれかの実際の主体が行う。したがって、**実際に行われた**有限な実験（実際の実験。[D-0002](../definitions/D-0002.md)）の全体は高々可算である。

## 採用の理由

有限な主体が有限な時間に行える実験の数え方として、ユーザーが提案した（第 09 回）。観測量を「有限な実験の族の極限」として定義する動機の一つである（高々可算個の実験から非可算個の観測量を近似する）。極限を使うのはこのフレームワークで選んだ構成方法で、可算性からの論理的な帰結ではない。

「主体」は、第 16 回の時点では「実験の主体」（実験をする者）の意味で、第 20 回に D-0012 の実際の主体に改めた。主体が高々可算個であることを仮定する背景は、次の考察である（ユーザーの説明。第 16 回）。実験の装置を主体とみなし、装置とそれ以外を分ける境界を連続的に変えると、非可算個の装置（主体）が得られる、という立場がありうる。この立場では、主体ごとの実験が 1 個でも、実験の全体は非可算になりうる。この仮定は、その立場を除くためのものである。

## 注意
## 注意

- 対象は実際の実験と実際の主体である。可能な主体（[D-0012](../definitions/D-0012.md)）は、非可算個あることも許す。可能な実験（プロトコルと、実数の組である設定の組）は、一般に非可算である（[D-0002](../definitions/D-0002.md)）。
- 可算性だけからは、観測量の空間の可分性は従わない（[C-0005](../conjectures/C-0005.md)）。
- 先例：Ludwig（*An Axiomatic Basis for Quantum Mechanics*, Vol. 1, 1985 の第 III 章 §3）は、「物理の有限性（finiteness of physics）」を理由に、物理系・準備の手続き・登録の手続きの集合を可算と仮定し、そこからアンサンブルと効果の集合の可算性と、アンサンブルを埋め込むバナッハ空間 $`ℬ`$ の可分性を得ている（効果を埋め込む双対 $`ℬ'`$ の可分性は従わない）。この前提が実際に行われた実験について述べるのに対し、Ludwig は手続きの種類について述べる点が異なる（[第 18 回の調査メモ](../surveys/2026-09-30_18_limit-topology.md)の 5.2 節・6.4 節）。
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='assumptions/A-0007.md'
rep(p,'# A-0007: 事前分布から決まる予測分布どうしの相互絶対連続性','# A-0007: 実際の主体の予測分布どうしの相互絶対連続性')
rep(p,'| 依存する ID | [D-0004](../definitions/D-0004.md) |','| 依存する ID | [D-0004](../definitions/D-0004.md)、[D-0012](../definitions/D-0012.md) |')
rep(p,'異なる主体の事前分布から決まる、無限のデータ列の上の予測分布どうしは、互いに絶対連続である。',
'異なる実際の主体（[D-0012](../definitions/D-0012.md)）の事前分布から決まる、無限のデータ列の上の予測分布どうしは、互いに絶対連続である。')
rep(p,'## 注意\n\n','''## 注意

- 第 20 回に、ユーザーの判断で、実際の主体についての前提（この前提）と、可能な主体についての前提（[A-0011](A-0011.md)）に分けた。実際の観測量（[D-0005](../definitions/D-0005.md)）の推定に要るのはこの前提だけで、制約するのは実際にいる主体の事前分布に限られる。可能な主体についての版は、許される事前分布の全体を制限する、より強い仮定になる（Claude の補足）。
''')
s=open(p).read().rstrip('\n')+'\n- 第 20 回：ユーザーの判断で、対象を実際の主体（D-0012）に限り、可能な主体についての主張を [A-0011](A-0011.md) に分けた。名前を「実際の主体の予測分布どうしの相互絶対連続性」に改めた。\n'
open(p,'w').write(s)
EOF
cat assumptions/_template.md | head -12
```

</details>

<details><summary>結果: Bash</summary>

```text
# A-NNNN: 前提の短い名前

| 項目 | 値 |
| --- | --- |
| 状態 | 採用・作業上・未定・廃止 |
| 層 | 実験・観測量・観測量の時空・可能な実験・可能な観測量・点なし時空 |
| 依存する ID | この前提が使う定義・前提の ID（例：[D-NNNN](../definitions/D-NNNN.md)、[A-NNNN](A-NNNN.md)）。なければ「なし」 |
| 関係する予想・結果 | この前提に依存する予想・結果の ID。なければ「なし」 |
| 初出 | [YYYY-MM-DD 第 NN 回](../summaries/YYYY-MM-DD_NN_topic.md) |

## 主張
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 12,30p assumptions/_template.md; cat > assumptions/A-0011.md <<'EOF'
# A-0011: 可能な主体の予測分布どうしの相互絶対連続性

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 可能な観測量 |
| 依存する ID | [D-0004](../definitions/D-0004.md)、[D-0012](../definitions/D-0012.md) |
| 関係する予想・結果 | なし |
| 初出 | [2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md) |

## 主張

異なる可能な主体（[D-0012](../definitions/D-0012.md)）の事前分布から決まる、無限のデータ列の上の予測分布どうしは、互いに絶対連続である。

## 採用の理由

可能な観測量（[D-0006](../definitions/D-0006.md)）の推定で、主体の事前分布への依存を抑えるため。第 20 回に、ユーザーの判断で、[A-0007](A-0007.md)（第 09 回に採用）を実際の主体についての前提と、可能な主体についての前提（この前提）に分けた。分けることで、実際の観測量の推定に要る仮定を最小にする（ユーザーの説明）。

## 注意

- 実際の主体についての [A-0007](A-0007.md) より強い仮定である。可能な主体は非可算個あることも許すので、この前提は、許される事前分布の全体を、予測分布が零集合を共有するものに制限することにあたる（Claude の補足）。差は個数によるものではない。相互の絶対連続性は同値関係なので、非可算個でも、どれか一つの予測分布と零集合が一致すれば足りる。
- 定理の形（Blackwell–Dubins の意見の一致）と一致の段階についての注意は、[A-0007](A-0007.md) の「注意」と同じである。

## 未解決の点

- 可能な観測量（[D-0006](../definitions/D-0006.md)）の構成で、事前分布と事後分布を使うか。D-0006 の未解決の点にあるとおり、可能な実験は結果の記録を含まないので、実際の観測量と同じ形の推定にはできない。この前提が必要になるかは、D-0006 の極限の取り方による。
- [A-0007](A-0007.md) の未解決の点（同時分布と尤度、相互か片側か、一致の段階、適用範囲、共有するデータの空間）は、この前提にも共通する。

## 履歴

- 第 20 回：ユーザーの判断で、A-0007 から可能な主体についての主張を分けて導入した（[T-0018](../roadmap.md)）。
EOF
python3 - <<'EOF'
p='/home/user/point-free-spacetime/assumptions/README.md'
s=open(p).read()
a='| [A-0007](A-0007.md) | 事前分布から決まる予測分布どうしの相互絶対連続性 |'
assert a in s
s=s.replace(a,'| [A-0007](A-0007.md) | 実際の主体の予測分布どうしの相互絶対連続性 |')
lines=s.split('\n')
i=max(k 
…（以下 462 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
（前提として採用する主張）

## 採用の理由

（なぜこの前提を置くか。誰の提案か）

## 注意

（前提から従わないこと、ほかの前提との区別）

## 未解決の点

（まだ決まっていない指定。なければ「なし」）

## 履歴

- 第 NN 回：（導入・改訂の要旨を 1 行で）

tools/tests/test_framework.py:154: AssertionError
=========================== short test summary info ============================
FAILED tools/tests/test_framework.py::test_links_exist - AssertionError: (Pos...
1 failed, 32 passed in 0.18s
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 -m pytest -q tools/tests -k links_exist 2>&1 | grep -o "AssertionError.*" | head -3
```

</details>

<details><summary>結果: Bash</summary>

```text
AssertionError: (PosixPath('/home/user/point-free-spacetime/definitions/D-0012.md'), '../summaries/2026-09-30_20_terms-setting-and-agents.md')
AssertionError
AssertionError: (Pos...
```

</details>

<details><summary>ツール: Bash</summary>

```text
printf '# 2026-09-30 第 20 回: 設定への用語の統一と、主体・観測者・装置の使い分け\n\n（セッションの終わりに書く）\n' > summaries/2026-09-30_20_terms-setting-and-agents.md && python3 -m pytest -q tools/tests 2>&1 | tail -1
```

</details>

<details><summary>結果: Bash</summary>

```text
33 passed in 0.14s
```

</details>

## Claude

主体（D-0012）を新しく定義し、A-0011 を加え、A-0001・A-0007 を改めました。テストが通ったので、続けて用語一覧を更新してからコミットします。

<details><summary>ツール: Bash</summary>

```text
cut -c1-60 glossary.md | grep -n "^| a[g-z]\|^| ap\|^| ob\|^| ag" 
```

</details>

<details><summary>結果: Bash</summary>

```text
8:| atom | アトム | 束で、0 のすぐ上にある元（0
58:| observational spacetime | 観測における時空 | 本�
59:| observer independence | 観測者非依存性 | 最小の�
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='glossary.md'
L=open(p).read().split('\n')
S='[第 20 回の調査メモ](surveys/2026-09-30_20_agent-observer-apparatus.md)'
def ins(before_prefix,row):
    i=next(k for k,l in enumerate(L) if l.startswith(before_prefix))
    L.insert(i,row)
ins('| atom |','| agent | 主体 | 事前分布を持ち、実験の記録から信念を更新する者。実験を行う（設定を選び、結果の記録を得る）こともある（0 個でもよい）。QBism の agent（行為する者）に合わせた語。一つの主体は複数の実験を行えるので、実験と 1 対 1 に対応する観測者・装置とは別の概念。実際の主体（高々可算。A-0001）と可能な主体（非可算も許す）に分ける。本プロジェクトの定義は [D-0012](definitions/D-0012.md)。 | '+S+' |')
ins('| atom |','| apparatus | 装置 | 実験で、準備から結果の読み出しまでに使う物理系。本プロジェクトでは実験と 1 対 1 に対応し、同じ機器を別の実験で使っても別の装置として数える（[D-0001](definitions/D-0001.md)）。既存研究では、Hardy の準備・変換・測定の装置、Ludwig の準備装置と登録装置、Fewster–Verch のプローブなどに当たる。 | '+S+' |')
ins('| observer independence |','| observer | 観測者 | 本プロジェクトでは、実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うもの。実験と 1 対 1 に対応する（[D-0001](definitions/D-0001.md)）。既存研究では、基準系の意味（相対論、関係的量子力学）と、結果を知覚する者の意味（Wigner の友人）があり、本プロジェクトは前者に当たる。後者の「実験を行う者」は主体とよぶ。 | '+S+' |')
open(p,'w').write('\n'.join(L))
EOF
cut -c1-30 glossary.md | sed -n 6,12p; python3 -m pytest -q tools/tests 2>&1 | tail -1
```

</details>

<details><summary>結果: Bash</summary>

```text
| --- | --- | --- | --- |
| actual observable | 実際�
| agent | 主体 | 事前分�
| apparatus | 装置 | 実験�
| atom | アトム | 束で、
| Bayesian inversion | ベイ�
| causal coverage | 因果被�
33 passed in 0.15s
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='framework.md'
s=open(p).read()
a='[D-0010](definitions/D-0010.md) 余白付きの包含（作業上） |'
assert s.count(a)==1
s=s.replace(a,'[D-0010](definitions/D-0010.md) 余白付きの包含（作業上）<br>[D-0012](definitions/D-0012.md) 主体（作業上） |')
a='[A-0007](assumptions/A-0007.md) 事前分布から決まる予測分布どうしの相互絶対連続性（採用）'
print(s.count(a))
s=s.replace(a,'[A-0007](assumptions/A-0007.md) 実際の主体の予測分布どうしの相互絶対連続性（採用）')
open(p,'w').write(s)
EOF
grep -n "^| 5. 可能な観測量\|^| 5\." framework.md | cut -c1-300
```

</details>

<details><summary>結果: Bash</summary>

```text
1
40:| 5. 可能な観測量 | 可能な実験の族の極限としての観測量 | [D-0006](definitions/D-0006.md) 可能な観測量（作業上） | （未定） | |
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -i 's/^| 5. 可能な観測量 | 可能な実験の族の極限としての観測量 | \[D-0006\](definitions\/D-0006.md) 可能な観測量（作業上） | （未定） | |$/| 5. 可能な観測量 | 可能な実験の族の極限としての観測量 | [D-0006](definitions\/D-0006.md) 可能な観測量（作業上） | [A-0011](assumptions\/A-0011.md) 可能な主体の予測分布どうしの相互絶対連続性（作業上） | |/' framework.md && sed -n 40p framework.md && python3 tools/deps_graph.py >/dev/null && python3 -m pytest -q tools/tests 2>&1 | tail -1 && python3 - <<'EOF'
p='/home/user/point-free-spacetime/assumptions/A-0010.md'
s=open(p).read()
i=s.index('## 未解決の点\n')+len('## 未解決の点\n')
s=s[:i]+'\n- 観測者が実験と 1 対 1 に対応すること（第 20 回。[D-0001](../definitions/D-0001.md)）との関係。この前提は、一人の観測者 $`O`$ が複数のプロトコルの設定を自分の座標に換算する形で書かれている。観測者が実験ごとに異なるなら、この前提を、各実験の観測者の座標への換算と、観測者の取り替え $`M_O → M_{O\'}`$ に書き直す必要がある。[T-0018](../roadmap.md) の (A)（D-0003 の再編）で扱う。'+s[i:]
open(p,'w').write(s)
EOF
sed -n '/^## 未解決の点/,/^## 履歴/p' assumptions/A-0010.md | head -6
```

</details>

<details><summary>結果: Bash</summary>

```text
| 5. 可能な観測量 | 可能な実験の族の極限としての観測量 | [D-0006](definitions/D-0006.md) 可能な観測量（作業上） | [A-0011](assumptions/A-0011.md) 可能な主体の予測分布どうしの相互絶対連続性（作業上） | |
33 passed in 0.14s
## 未解決の点

- 観測者が実験と 1 対 1 に対応すること（第 20 回。[D-0001](../definitions/D-0001.md)）との関係。この前提は、一人の観測者 $`O`$ が複数のプロトコルの設定を自分の座標に換算する形で書かれている。観測者が実験ごとに異なるなら、この前提を、各実験の観測者の座標への換算と、観測者の取り替え $`M_O → M_{O'}`$ に書き直す必要がある。[T-0018](../roadmap.md) の (A)（D-0003 の再編）で扱う。
- 空間の次元 $`n`$ を前提として固定するか、較正から決まるものとするか。
- 較正の約束の選び方と、その取り替えの扱い。
- 観測者が使える範囲の有限性（到達できる範囲 $`R_O`$）を、$`M_O`$ の部分集合として扱うか（[C-0008](../conjectures/C-0008.md) の詳細化の論点）。
```

</details>

<details><summary>ツール: Bash</summary>

```text
git add -A && git commit -qm "第 20 回：主体（D-0012）を定義し、観測者と装置を有限な実験（D-0001）の構成要素に加え、A-0007 から可能な主体の前提 A-0011 を分けた

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: https://claude.ai/code/[伏せ字]" && git push -q && git log -1 --format=%h
```

</details>

<details><summary>結果: Bash</summary>

```text
c134e58
```

</details>

## Claude

(C) で合意した内容を定義と前提に反映し、c134e58 で push しました。依存関係の検査（テスト 33 件）は通っています。

#### 変更した点

- **D-0001（有限な実験）**：実験が指定するものに「装置」と「観測者」を加えました。
  - 装置は、その実験で準備から読み出しまでに使う物理系です。観測者は、実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うものです。
  - どちらも実験と 1 対 1 に対応することと、その理由（同一の存在は異なる世界線を持てない）を書きました。
  - 同じ機器や実験室を別の実験で使っても、別の装置・別の観測者として数えます。
- **D-0002（実際の実験と可能な実験）**：「実際の装置・観測者」と「可能な装置・観測者」を加えました。
- **D-0012（主体、新規）**：事前分布を持ち、実験の記録から信念を更新する者です。実験を行うこともあり、行う実験は 0 個でもかまいません。
  - 実際の主体と可能な主体に分けました。可能な主体は、非可算個あることも許します。
  - 主体は複数の実験を行えるので、観測者・装置とは別の概念だと書きました。
- **A-0001**：主語を「実際の主体」に改め、「0 個を含む」を明記しました。
  - 前提の主張の中に、「各実際の実験は、いずれかの実際の主体が行う」という一文を加えました。これは可算性の結論を導くのに必要で、これまでは暗黙だったものです。前提の主張に一文が加わったことになるので、ご確認ください。
- **A-0007 と A-0011（新規）**：別の前提に分けました。
  - A-0007 は「実際の主体の予測分布どうしの相互絶対連続性」で、状態は採用のままです。
  - A-0011 は「可能な主体の予測分布どうしの相互絶対連続性」で、層は可能な観測量です。
- **依存の循環の解消**：A-0001 が D-0012 を通して D-0002 に依存するようになり、依存が循環しました。そこで、D-0002 から A-0001 への依存を外しました。実際の実験の可算性は、もともと A-0001 の主張にあります。同じ理由で、D-0001 も A-0010 に依存させず、注意で参照する形にしました。
- **A-0010**：未解決の点に、観測者が実験ごとに異なることとの関係を加えました。今の A-0010 は、一人の観測者が複数のプロトコルの設定を換算する形で書かれているので、(A) で書き直します。
- **用語一覧と `framework.md`**：用語一覧に「主体」「装置」「観測者」を加え、`framework.md` の表と依存関係の図を更新しました。

#### ご確認いただきたいこと

1. **D-0012 と A-0011 の状態**：どちらも「作業上」にしてあります。内容は今回合意したとおりなので、「採用」にしてよければお知らせください。A-0011 には、次の点を未解決の点として書いてあります。
   - D-0006 の可能な観測量は、結果の記録を使わない構成になる見込みです。その場合、A-0011 自体が要らなくなる可能性があります。
2. **A-0001 の主張に加えた一文**：「各実際の実験は、いずれかの実際の主体が行う」でよいでしょうか。

これで (B)・調査・(C) が終わり、残るのは (A) の D-0003 の再編です。ご指摘の「観測者と D-0001・D-0002 の関係」は、観測者を D-0001 の構成要素にしたことで、半分は整理できたと考えています。残りの論点は二つです。

- 実験ごとに異なる観測者の座標 $`M_O`$ を、どう比べるか。
- 較正の写像 $`τ^O_π`$ を、プロトコルごとではなく実験ごとの写像として書き直すか。

今回のセッションで (A) に進むか、ここで区切るか、ご判断ください。

## ユーザー

「1. D-0012 と A-0011 の状態」は、少なくともこのセッションのレビューが完了するまでは「作業上」でよいです。

「2. A-0001 の主張に加えた一文」は、ご提案の通りで問題ありません。

現状だとクロスモデルレビューの指摘が収束しなさそうなので、「今回のセッションで (A) に進む」でお願いします。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && grep -rln "M_O\|τ^O" --include=*.md definitions assumptions conjectures | sort; sed -n '/^## 主張/,/^## 採用/p' assumptions/A-0008.md
```

</details>

<details><summary>結果: Bash</summary>

```text
assumptions/A-0008.md
assumptions/A-0009.md
assumptions/A-0010.md
conjectures/C-0008.md
definitions/D-0001.md
definitions/D-0003.md
definitions/D-0011.md
## 主張

実験における時空（[D-0003](../definitions/D-0003.md)）の領域と、その包含・有界性は、再構成の対象である観測の局在を使わずに、独立に与えられる。具体的には、観測者 $`O`$ の時空の部分 $`M_O`$ の開集合を領域とし、包含は集合の包含、有界性は距離 $`d_O`$ での有界性とする。

## 採用の理由
```

</details>

## Claude

(A) に進みます。書き換えの前に、構成の案を示してご相談します。(C) で「観測者は実験ごとの世界線の区間」と決めたので、D-0003 の再編はそれに合わせた形になります。

#### (A) の構成案（Claude の提案。未決定）

##### 1. D-0003 を「設定の空間」にする
- 中身は、$`X_π ⊆ ℝ^{n_π}`$（プロトコル $`π`$ の設定の空間）、$`X = ⨆_π X_π`$（プロトコル全体の設定の空間）、直和の位相です。
- 「時空の部分」と「設定の部分」への分割（今の 3・4 項）はなくします。時空の読みは、2 の較正の写像の側で扱います。
- 「実験における時空」の語は、D-0003 からなくなります。

##### 2. 新しい定義 D-0013「観測者の実験における時空と較正」
- **観測者の実験における時空**：実験 $`e`$ の観測者 $`O_e`$（D-0001）の基準の時計と物差しで決まる座標 $`M_{O_e} = ℝ^{1+n}`$ と、その上の距離 $`d_{O_e}`$ です。
- **較正の規則はプロトコルが与え、座標は観測者が与える**、と分けることを提案します。
  - プロトコル $`π`$ は、装置の時計や物差しの読みを基準の時計と物差しの座標に換算する規則 $`τ_π : X_π → ℝ^{1+n}`$ を含みます。この規則は、設定全体の連続写像です。磁場による原子時計のずれのような補正も、この規則に入ります。
  - 実験 $`e = (π, x, …)`$ では、この規則を $`x`$ に当てはめた点 $`τ_π(x)`$ を、観測者 $`O_e`$ の座標 $`M_{O_e}`$ の点と読みます。
  - こうすると、$`τ`$ は「設定全体の上の写像」（第 19 回の合意）のまま、観測者が実験ごとに異なること（第 20 回の合意）とも両立します。
- 結果の読みの換算 $`σ`$ も、同じ形（プロトコルが規則を与え、観測者が座標を与える）にします。
- $`M_O = ℝ^{1+n}`$ 全体は理想化で、実際に較正で意味を持つのは、観測者の世界線の区間の近くだけです。この点は注意に書きます。

##### 3. 異なる観測者の比べ方（ここが一番の論点です）
観測者が実験ごとに異なるので、二つの実験を比べるには、観測者の取り替え $`M_O → M_{O'}`$ が要ります。その与え方の候補は三つあります。

- **(a) 実験で与える**：二つの観測者の時計合わせや物差しの比較そのものを、実際の実験（比較の実験）とみなします。取り替えの写像は、その実験の結果から決まります。この立場では、取り替えを前提として仮定しません。取り替えどうしの整合性（三つの観測者を経由しても同じになるか）や、ポアンカレ変換になるかは、観測における時空との整合条件（T-0009）と T-0017（レーダー座標など）で扱います。
- **(b) 前提で与える**：取り替えの写像が存在することを、前提として置きます（A-0010 を書き直す）。
- **(c) 今は決めない**：取り替えが要ることだけを未解決の点に書きます。

私は **(a)** を勧めます。理由は二つあります。

- 「観測結果から時空を再構成する」という目的に最も忠実です。
- 基準の時計と物差しの比較も実験であり、その結果は高々可算個の実数の記録である、という (C) の整理と一貫します。

ただし、(a) でも中身はすぐには決まらず、当面は未解決の点として記録することになります。

##### 4. 影響を受けるファイル
- **A-0010**：「一人の観測者が複数のプロトコルの設定を換算する」形から、2 の形に書き直します。各実験の観測者が、プロトコルの較正の規則で、自分の座標に換算する形です。
- **A-0008・A-0009・C-0008・D-0011**：一人の観測者の座標 $`M_O`$ の上で述べています。これらは「ある観測者の座標の上で述べた主張」と読み直します。ほかの観測者の実験のデータは、3 の取り替えで持ち込みます。主張の中身は変えず、注意と未解決の点に記録します。
- **用語一覧・記号一覧・`framework.md`**：「実験における時空」の項目を、新しい意味（観測者の実験における時空）に改めます。

#### ご相談

1. **D-0003 の分け方**：D-0003 を「設定の空間」にし、$`M_O`$ と較正を一つの新しい定義 D-0013 にまとめる形でよいでしょうか。$`M_O`$ と較正を別々の定義にする案もあります。
2. **較正の規則**：「較正の規則はプロトコルが与え、座標は観測者が与える」という分け方でよいでしょうか。
3. **観測者の取り替え**：(a)・(b)・(c) のどれにしますか。

## ユーザー

その前に、「D-0001: 有限な実験」をもう一度見直したいです。有限の実験 e に対して、「観測の回数 N_e ∈ ℕ」 を明示的に含めるようにしたいです。また、「設定 x ∈ X_π」と「結果 y ∈ Y_π」を、それぞれ「設定の族 {x_i} (x_i ∈ X_π,  i = 1, ... , N_e)」と「結果の族 {y_i}  (y_i ∈ Y_π,  i = 1, ... , N_e)」 に置き換えたいです。いかがでしょうか？

「較正の規則はプロトコルが与え、座標は観測者が与える」について確認です。「装置の時計や物差しの読みを基準の時計と物差しの座標に換算する規則は、実験プロトコルのみに依存し、装置および観測者に依らない」という意図でしょうか？ そもそも 「装置の時計や物差しの読み」は装置に、「基準の時計と物差しの座標」は観測者に、それぞれ依存しているので、もしその意図であれば、非自明な主張であるように思います。なので、新規の仮定として登録した方がよいと思いますが、いかがでしょうか？ また、仮定として登録する場合、その仮定からどのような予想が導かれますか？

次に、点 τ_π(x) の解釈です。これは、装置が置かれた場所の座標でしょうか？観測者がいる場所の座標でしょうか？ それとも、装置が観測を行った場所の座標でしょうか？ 「装置の時計や物差しの読み」が何を表しているかによると思うのですが、その意味が与えられていないように思います。結果の読みの換算 σ についても同様です。もし、意味が未解決でこれから与えるのであれば、有限の実験 e で複数回の観測を行う場合を想定して、設定の族から得られる族 {τ_π(x_i)} と、結果の族から得られる {σ_π(x_i, y_i)} との組が、物理実験的な何らかの意味を持つようにしたいです。

「3. 異なる観測者の比べ方」について、「(a) 実験で与える」と「(b) 前提で与える」の立場をとったとき、物理としてどのような違いが生じるかに興味があります。フレームワークとしては、両者を比較できるようにしたいです。

## Claude

四点とも、定義の根本に関わる大事な指摘です。順に見立てを述べ、最後にご相談をまとめます。

#### 1. D-0001 に観測の回数と、設定・結果の族を入れること

賛成です。一つの実験 $`e`$ を、次の組とします。

```math
e = \bigl(π,\ N_e,\ (x_i)_{i=1}^{N_e},\ (y_i)_{i=1}^{N_e},\ \text{装置},\ \text{観測者}\bigr), \quad x_i ∈ X_π,\ y_i ∈ Y_π
```

これで、D-0001 の未解決の点「$`Y_π`$ は個々の読みの空間か、1 回分の全出力の空間か」が解決します。$`Y_π`$ は 1 回の観測の読みの空間になります。D-0004 の「同じ実験の中の同時分布」も、$`(y_i)`$ の同時分布として述べられるようになります。

決めておきたい細部が三つあります。

- **$`N_e ≥ 1`$ とするか。** 観測を 1 回もしない実験は除くのが自然だと思います。
- **添字 $`i`$ の意味。** 実行の順序とすることを提案します。3 節の時空の点の読み方とつながります。
- **$`x_i`$ を前の結果 $`y_1, …, y_{i-1}`$ に応じて選んでよいか（適応的な設定）。** D-0005 に未解決の点として記録してあります。D-0001 では許し、選び方の規則も実験の記録に含める、という形を提案します。

この変更に合わせて、D-0002 の可能な実験も $`(π, N, (x_i))`$ に改めます。

#### 2. 「較正の規則はプロトコルが与える」は非自明な主張か

ご指摘のとおりで、意図していたのはその主張です。「装置の読みを基準の座標に換算する規則は、プロトコルと設定だけで決まり、どの装置・どの観測者かには依らない」という主張は、明らかに非自明です。新しい前提として登録すべきだと思います。名前の候補は「較正の普遍性」です。

この前提の物理的な意味は、相対性原理の一つの形だと考えます。同じ手順（プロトコル）で測れば、どの観測者も自分の座標で同じ値を得る、という主張だからです。ご指摘の補正（磁場、温度、重力ポテンシャル）は設定に含めるので、残る主張は「装置や観測者の個体にはそれ以上依存しない」ということです。これは、一般相対論の等価原理（アインシュタインの等価原理）のうち、局所位置不変性と局所ローレンツ不変性に近い内容です（記憶による）。プロジェクトの A-0006（実験の等価原理）とは別物です。

この前提から導かれそうな予想の候補を二つ挙げます（Claude の見立て。文献は記憶による）。

- **観測者の取り替えの形**：較正の普遍性（相対性原理）に、取り替えが群をなすこと、一様性・等方性、連続性を加えると、取り替えはローレンツ変換かガリレイ変換に限られる、という古典的な定理があります（Ignatowski 1910、Lévy-Leblond 1976 など）。不変な速さ $`c`$ の値は、実験から決まります。本プロジェクトでは、C-0008 がポアンカレ変換を仮定していますが、その仮定を「較正の普遍性からの帰結」に置き換えられる可能性があります。
- **普遍性の破れの検出**：同じプロトコル・同じ設定の実験を別の観測者が行い、取り替えで持ち込んだ値が一致しなければ、普遍性が破れていることになります。原理的に、実験で検証できる主張になります。

#### 3. 点 $`τ_π(x)`$ と $`σ_π(x, y)`$ の意味

ご指摘のとおり、「装置の時計や物差しの読み」が何を表すかを決めていませんでした。観測を $`N_e`$ 回行う形に合わせて、次の読み方を提案します。

- **$`τ_π(x_i)`$：$`i`$ 回目の観測の準備の事象**。設定で指定した、準備（放出、開始など）を行う時刻と場所を、観測者の座標で表したものです。
- **$`σ_π(x_i, y_i)`$：$`i`$ 回目の観測の登録の事象**。結果として装置が記録した、登録（検出など）の時刻と場所を、観測者の座標で表したものです。

この読み方には、次の利点があります。

- 組 $`(τ_π(x_i), σ_π(x_i, y_i))`$ は、「準備の事象から登録の事象へ」という、1 回の観測の時空の上の端点の組になります。これは Ludwig の準備装置と登録装置の区別に対応します。
- 族 $`\{(τ_i, σ_i)\}_{i=1}^{N_e}`$ は、例えば次のような物理的なデータになります。
  - レーダーなら、放出と受信の時刻の組です。
  - 飛行時間の測定なら、出発と到着の組です。
  - 粒子の検出なら、線源と検出の位置・時刻の組です。
- 予想の候補が一つ自然に出てきます。登録の事象は、準備の事象の（観測者の座標での）因果的な未来にある、つまり光速を超えてつながらない、という主張です。これは、因果構造の再構成（T-0017。Malament など）の入力になりえます。
- D-0011 の装置の占める領域 $`\mathrm{occ}`$ は、これらの事象を含む領域と読めます。

一つの観測に準備も登録もない読み（時計の読みを持たないプロトコル）は、今と同じく部分写像として扱います。

#### 4. (a) 実験で与える と (b) 前提で与える の物理的な違い

両者を比べられるようにすることに賛成です。私の見立てでは、違いは次の三点に出ます。

| | (a) 比較の実験で与える | (b) 前提で与える |
| --- | --- | --- |
| 取り替えの身分 | 実際の比較の実験の結果（有限精度、高々可算個、統計的） | 仮定（例えば、ポアンカレ群） |
| 取り替えの形（ローレンツかガリレイか、$`c`$ の値） | データと、2 節の予想から導く | 入力として与える |
| 経路への依存 | 比較を経由する経路によって結果が変わりうる | 全体で一つの群なので、経路によらない |

三つ目の違いが、物理として最も重要だと考えます。

- (a) では、観測者 A → B → C → A と比較を一周したとき、取り替えの合成が恒等写像に戻るとは限りません。この一周のずれ（ホロノミー）は、曲率、つまり重力の効果の候補になります。
- (b) で全体に一つの群を仮定すると、一周のずれは常に 0 で、平坦な特殊相対論の状況に限られます。
- 予想の候補：(a) で一周のずれがすべて 0 になる、という条件を加えると (b) が得られる。

フレームワークとしては、(a) と (b) を二つの前提にして、どちらを採るかで体系を分けることを提案します。第 08 回の方針（前提を変えて得られる体系を比べる）に沿う形です。

#### ご相談

1. **D-0001 の細部**：1 節の三点（$`N_e ≥ 1`$、$`i`$ は実行の順序、適応的な設定を許す）でよいでしょうか。
2. **較正の普遍性**：2 節の内容で前提として登録し、2 節の二つを予想の候補として記録してよいでしょうか。予想として登録するか、候補として記録するにとどめるかもご判断ください。
3. **$`τ`$ と $`σ`$ の意味**：3 節の「準備の事象」「登録の事象」という読み方でよいでしょうか。
4. **(a) と (b)**：二つの前提に分けて、体系を比べる形にしてよいでしょうか。一周のずれの予想も、候補として記録しますか。

## ユーザー

「1. D-0001 の細部」について、圏論的に意味があるのであれば、N_e = 0 も許可したいです。「i は実行の順序」と「適応的な設定を許す」には賛成します。あと、「N_e ≧ 1 であるような実際の実験 e に対して、N_e - 1 回目までの観測に制限した実験 e' も実際の実験である」という仮定を新規に儲けたいです。

「2. 較正の普遍性」について、2 節の二つを予想として記録したいです。クロスモデルレビューにより「詳細化の論点」が追加されていくので、その方が有用と考えます。

「3. τ と σ の意味」は、物理的なデータとしての例が明確なので、ご提案の 3 節の「準備の事象」「登録の事象」という読み方でよいです。

「4. (a) と (b)」について、二つの前提に分けて、体系を比べる形にしてください。一周のずれの予想は、上記と同様に、予想として登録してください。

*（ユーザーがツールの実行を中断）*

## ユーザー

「1. D-0001 の細部」について、圏論的に意味があるのであれば、N_e = 0 も許可したいです。「i は実行の順序」と「適応的な設定を許す」には賛成します。あと、「N_e ≧ 1 であるような実際の実験 e に対して、N_e - 1 回目までの観測に制限した実験 e' も実際の実験である」という仮定を新規に設けたいです。

「2. 較正の普遍性」について、2 節の二つを予想として記録したいです。クロスモデルレビューにより「詳細化の論点」が追加されていくので、その方が有用と考えます。

「3. τ と σ の意味」は、物理的なデータとしての例が明確なので、ご提案の 3 節の「準備の事象」「登録の事象」という読み方でよいです。

「4. (a) と (b)」について、二つの前提に分けて、体系を比べる形にしてください。一周のずれの予想は、上記と同様に、予想として登録してください。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && cat conjectures/_template.md; sed -n 1,40p conjectures/README.md; grep -ln "D-0003" definitions/*.md assumptions/*.md conjectures/*.md | xargs grep -n "依存する ID" | grep D-0003 | cut -c1-80
```

</details>

<details><summary>結果: Bash</summary>

```text
# C-NNNN: 予想の短い名前

| 項目 | 値 |
| --- | --- |
| 確度 | 高・中・低 |
| 重要度 | 高・中・低 |
| 検証費用 | 高・中・低 |
| 優先度 | 高・中・低（対話で決定） |
| 検証方法 | Lean・数値実験・文献調査 |
| 状態 | 未着手・検証中・証明済み・反証済み・数値的に支持・保留 |
| Issue | #NN |
| 依存する ID | 予想の記述・証明に用いる定義と、仮定する前提の ID（例：[D-NNNN](../definitions/D-NNNN.md)）。なければ「なし」 |
| 目標の ID | 予想が定理として導こうとする前提の ID（前提の主張を結論とする予想の場合。定義は命題ではないので書かない）。なければ「なし」 |
| 初出 | [YYYY-MM-DD 第 NN 回](../summaries/YYYY-MM-DD_NN_topic.md) |

## 主張

（自然言語による主張。数式は docs/math-guide.md に従う）

## 詳細化の論点

（主張をさらに詳しくするための条件や問い。クロスモデルレビューの「詳細化の論点」もここに記録する。なければ「なし」）

## 背景

（どのような議論から出てきたか）

## 評価の根拠

- 確度:
- 重要度:
- 検証費用:

## 検証の方針

（Lean で形式化する、数値実験で反例を探す、文献を調べる など）

## 結果

（検証が終わったら、結果の要旨と、登録した結果の ID（[`results/`](../results/) の `R-NNNN`）を書く）
# 予想の一覧

対話の中で出てきた未検証の主張を「予想」として管理します。
1 件 1 ファイル（`C-NNNN.md`）で、書式は [`_template.md`](_template.md) のとおりです。

## 評価の段階

| 項目 | 高 | 中 | 低 |
| --- | --- | --- | --- |
| 確度 | 成り立つと強く見込まれる | どちらともいえない | 成り立たない見込みが強い |
| 重要度 | 成り立てば考察全体の方向を左右する | 個別の論点に効く | 補助的・興味本位 |
| 検証費用 | 数日以上、または新しい道具が必要 | 数時間〜1 日程度 | 1 セッション内で済む |

優先度（高・中・低）は、上の評価をもとに対話の中で決めます。

## 状態

`未着手` → `検証中` → `証明済み`・`反証済み`・`数値的に支持`・`保留`

- `証明済み`：数学的な証明がある場合に限る（Lean による形式証明、または対話・文献中の証明）。
- `反証済み`：反例がある場合（数値実験で見つけた反例を含む）。
- `数値的に支持`：数値実験などで支持されているが、証明はない場合。証明済みとは区別する。

## 一覧

優先度の高い順に並べます。

| ID | 予想 | 確度 | 重要度 | 検証費用 | 優先度 | 状態 | Issue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [C-0007](C-0007.md) | 局在の限界から、装置の占める領域の上下限が導かれる | 中 | 高 | 高 | 高 | 未着手 | [#25](https://github.com/kittenkiki15/point-fr
…（以下 1948 文字を省略）
```

</details>

## Claude

D-0001 から順に書き換えます。まず D-0001 の今の全文を確認します。

<details><summary>ツール: Bash</summary>

```text
cat definitions/D-0001.md | sed -n 11,45p
```

</details>

<details><summary>結果: Bash</summary>

```text
## 定義

**有限な実験**とは、一つの実験プロトコル $`π`$ に従い、有限回の操作と観測を行って、有限個の結果を読み出すものである。一つの有限な実験について、次を指定する。

- プロトコル $`π`$（有限の記述を持つ。[A-0002](../assumptions/A-0002.md)）
- 設定 $`x ∈ X_π`$：プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数の組（[A-0003](../assumptions/A-0003.md)）
- 結果の空間 $`Y_π`$ と、読み出した有限個の結果（実数値。[A-0003](../assumptions/A-0003.md)）
- **装置**：その実験で、準備から結果の読み出しまでに使う物理系
- **観測者**：その実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うもの

装置と観測者は、実験ごとに一つずつ定まる（実験と 1 対 1 に対応する）。

## 注意

- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める実験における時空の領域とは区別する。
- 装置と観測者が実験と 1 対 1 に対応するのは、同一の存在が異なる世界線を持つことはできず、実験ごとに世界線の区間が異なるからである（ユーザーの説明。第 20 回）。同じ機器や同じ実験室を別の実験で使っても、別の装置・別の観測者として数える。一つの観測者が複数の実験を持つ扱いはしない（ユーザーの判断）。
- 観測者の基準の時計と物差しで装置の読みを座標に換算できることは、前提 [A-0010](../assumptions/A-0010.md) で置く（この定義は A-0010 に依存しない）。
- 実験を行う者は**主体**（[D-0012](D-0012.md)）とよび、観測者・装置とは別の概念とする。一つの主体は複数の実験を行える。
- 実際の実験の装置・観測者を「実際の装置」「実際の観測者」、可能な実験の装置・観測者を「可能な装置」「可能な観測者」とよぶ（[D-0002](D-0002.md)）。
- 既存研究での装置・観測者の語の使われ方は、[第 20 回の調査メモ](../surveys/2026-09-30_20_agent-observer-apparatus.md)にある（装置：Hardy の準備・変換・測定の装置、Ludwig の準備装置と登録装置、Fewster–Verch のプローブ。観測者：相対論や関係的量子力学の、基準系としての観測者）。
- 設定の空間 $`X_π`$ と結果の空間 $`Y_π`$ は、プロトコルごとに異なりうる。
- 有限な実験に何を対応させるか（結果の統計）は [D-0004](D-0004.md) で定める。

## 未解決の点

- 各実験が占める領域の決め方（装置の準備や結果の読み出しを実験の領域に含めるか。設定値ごとの装置の占める領域 $`\mathrm{occ}`$ は [D-0011](D-0011.md) で導入した）と、実験が領域 $`R`$ に「収まる」ことの判定（[D-0008](D-0008.md) と共通）。
- 結果の空間 $`Y_π`$ の意味：個々の読みの空間か、実験 1 回分の全出力をまとめた空間か。同じ実験の中の結果どうしの同時分布と、実験を繰り返すときの同時分布を区別する（[D-0004](D-0004.md) と共通）。

- 観測者が実験と 1 対 1 に
…（以下 426 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='definitions/D-0001.md'
s=open(p).read()
i=s.index('## 定義'); j=s.index('## 履歴')
new='''## 定義

**有限な実験**とは、一つの実験プロトコル $`π`$ に従い、有限回の観測を行って、観測ごとに結果を読み出すものである。一つの有限な実験 $`e`$ について、次を指定する。

- プロトコル $`π`$（有限の記述を持つ。[A-0002](../assumptions/A-0002.md)）
- 観測の回数 $`N_e ∈ ℕ`$（$`N_e = 0`$ も許す）
- 設定の族 $`(x_i)_{i=1}^{N_e}`$：$`x_i`$ は $`i`$ 回目の観測の設定で、プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数の組（[A-0003](../assumptions/A-0003.md)）
- 結果の族 $`(y_i)_{i=1}^{N_e}`$：$`y_i`$ は $`i`$ 回目の観測の結果で、結果の空間 $`Y_π`$ の元（実数の組。[A-0003](../assumptions/A-0003.md)）
- **装置**：その実験で、準備から結果の読み出しまでに使う物理系
- **観測者**：その実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うもの

添字 $`i`$ は観測を実行した順序を表す。設定 $`x_i`$ は、それまでの結果 $`y_1, …, y_{i-1}`$ に応じて選んでもよい（適応的な設定）。その場合は、選び方の規則もプロトコルの記述に含める。装置と観測者は、実験ごとに一つずつ定まる（実験と 1 対 1 に対応する）。

## 注意

- $`N_e = 0`$ の実験は、観測を 1 回も行わない、情報を与えない実験である。統計的実験の比較（Blackwell の順序、Le Cam の不足度）では、どの実験からも後処理で模倣できる最小の実験にあたり、実験を順につなぐ操作の単位元にあたる（Claude の補足）。実験の最初の何回かの観測への制限（[A-0012](../assumptions/A-0012.md)）を繰り返したときの行き着く先でもある。
- $`Y_π`$ は 1 回の観測の結果の空間である。同じ実験の中の結果どうしの同時分布は、結果の族 $`(y_i)`$ の同時分布として述べる（[D-0004](D-0004.md) の未解決の点）。
- 実験を行う観測者の世界線の区間（実験の期間）と、装置と操作が占める領域とは区別する。
- 装置と観測者が実験と 1 対 1 に対応するのは、同一の存在が異なる世界線を持つことはできず、実験ごとに世界線の区間が異なるからである（ユーザーの説明。第 20 回）。同じ機器や同じ実験室を別の実験で使っても、別の装置・別の観測者として数える。一つの観測者が複数の実験を持つ扱いはしない（ユーザーの判断）。
- 観測者の基準の時計と物差しで装置の読みを座標に換算できることは、前提 [A-0010](../assumptions/A-0010.md) で置き、換算の写像と座標は [D-0013](D-0013.md) で定める（この定義は A-0010 と D-0013 に依存しない）。
- 実験を行う者は**主体**（[D-0012](D-0012.md)）とよび、観測者・装置とは別
…（以下 975 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
ok
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "可能な実験\*\*\|実際の実験\*\*" definitions/D-0002.md && python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='definitions/D-0002.md'
rep(p,'- **可能な実験**：プロトコル $`π`$ と設定 $`x ∈ X_π`$ の組 $`(π, x)`$。一般に非可算個ある。',
'- **可能な実験**：プロトコル $`π`$、観測の回数 $`N`$、設定の族 $`(x_i)_{i=1}^{N}`$（$`x_i ∈ X_π`$）の組 $`(π, N, (x_i))`$。適応的な設定（[D-0001](D-0001.md)）の場合は、設定の族の代わりに、それまでの結果から設定を選ぶ規則を指定する。一般に非可算個ある。')
rep(p,'行ったときの組 $`(π, x)`$ と、得た結果の記録からなる。','行ったときのプロトコル、観測の回数、設定の族と、得た結果の族の記録からなる。')
s=open(p).read().rstrip('\n')+'\n- 第 20 回：D-0001 に観測の回数と設定・結果の族を入れたのに合わせて、可能な実験を $`(π, N, (x_i))`$ に改めた（ユーザーの判断）。\n'
open(p,'w').write(s)
EOF
grep -rn "(π, x)" --include=*.md definitions assumptions conjectures framework.md glossary.md symbols.md | cut -c1-140
```

</details>

<details><summary>結果: Bash</summary>

```text
13:- **可能な実験**：プロトコル $`π`$ と設定 $`x ∈ X_π`$ の組 $`(π, x)`$。一般に非可算個ある。
14:- **実際の実験**：実際に行われた有限な実験（[D-0001](D-0001.md)）。行ったときの組 $`(π, x)`$ と、得た結果の記録からなる。
definitions/D-0006.md:21:- 極限の取り方。可能な実験は設定 $`(π, x)`$ だけで結果の記録を含まないので、実際�
definitions/D-0004.md:19:その族 $`(π, x) ↦ p_π(\,\cdot \mid x)`$ を**応答関数**（統計の関数）と呼ぶ。$`\mathrm{Prob}(
definitions/D-0011.md:16:2. **可能な実験の占める領域**：可能な実験（[D-0002](D-0002.md)）$`e = (π, x)`$ について、�
conjectures/C-0003.md:18:有限な実験に対応させる確率分布の台を、$`X`$ の上の統計の関数（プロトコル $`π`$ �
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 12,30p definitions/D-0011.md
```

</details>

<details><summary>結果: Bash</summary>

````text
観測者 $`O`$ の時空の部分 $`M_O`$（[D-0003](D-0003.md)）の上で考える。扱うのは、時空の読みを持つプロトコルの実験だけである。実験 $`e`$ の時空の部分の設定値を $`x_e := τ^O_π(x) ∈ M_O`$ と書く（$`e`$ のプロトコルが $`π`$、設定が $`x`$ のとき）。

1. **実際の実験の記録された占める領域**：実際の実験（[D-0002](D-0002.md)）$`e`$ について、その装置が準備から結果の読み出しまでに占めた点がすべてその中にあることを、記録が保証する範囲（外側の範囲）を $`\mathrm{occ}_{\mathrm{rec}}(e) ⊆ M_O`$ とする。有限の記録から占めた点の全体を特定できるとは限らないので、実際に占めた点の全体ではなく、記録が保証する外側の範囲をとる。
2. **可能な実験の占める領域**：可能な実験（[D-0002](D-0002.md)）$`e = (π, x)`$ について、可能な実験を観測量の時空の中でモデル化できること（[C-0002](../conjectures/C-0002.md)）を前提として、そのモデルの装置が占める点の全体を $`M_O`$ に写したものを $`\mathrm{occ}_{\mathrm{mod}}(e) ⊆ M_O`$ とする（観測における時空から $`M_O`$ への写し方は、[D-0003](D-0003.md) の整合条件による。したがってこの定義は、C-0002 のモデル化とその写し方の両方を与えた場合の条件付きの構成である）。実際の実験は可能な実験でもあるので、実際の実験 $`e`$ には $`\mathrm{occ}_{\mathrm{rec}}(e)`$ と $`\mathrm{occ}_{\mathrm{mod}}(e)`$ の二つがありうる。両者の関係（例えば $`\mathrm{occ}_{\mathrm{rec}}(e) ⊆ \mathrm{occ}_{\mathrm{mod}}(e)`$）は、別の整合条件とする。
3. どちらの場合も、$`x_e ∈ \mathrm{occ}_{\mathrm{rec}}(e)`$、$`x_e ∈ \mathrm{occ}_{\mathrm{mod}}(e)`$（装置は、自分の設定値の点を占める）を課す。
4. **設定値ごとの合併**：$`M_O`$ の各点 $`y`$ について、**装置の占める領域** $`\mathrm{occ}(y) ⊆ M_O`$ を、設定値が $`y`$ の可能な実験のモデルの占める領域の合併 $`\mathrm{occ}(y) := ⋃_{x_e = y} \mathrm{occ}_{\mathrm{mod}}(e)`$ と定める。次を課す。
   - すべての $`y ∈ M_O`$ について、設定値が $`y`$ の可能な実験がある。これがないと、実験のない点で $`\mathrm{occ}(y) = ∅`$ となり、下の $`N_{\mathrm{occ}}`$ は増大的でない。実際の実験は高々可算個（[A-0001](../assumptions/A-0001.md)）なので、この条件は可能な実験でしか課せない。
   - $`\mathrm{occ}(y)`$ は $`M_O`$ の領域（開集合）である。

このとき、$`M_O`$ の領域 $`R`$ について

```math
N_{\mat
…（以下 293 文字を省略）
````

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 1,12p definitions/D-0003.md; sed -n '/^## 未解決の点/,$p' definitions/D-0003.md
```

</details>

<details><summary>結果: Bash</summary>

```text
# D-0003: 実験における時空

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)、[A-0004](../assumptions/A-0004.md)、[A-0010](../assumptions/A-0010.md) |
| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0004](../conjectures/C-0004.md)、[C-0008](../conjectures/C-0008.md) |
| 初出 | [2026-09-27 第 07 回](../summaries/2026-09-27_07_observation-and-experiment.md) |

## 定義

## 未解決の点

- **用語と構成の再編**（第 19 回。ユーザーの提案に合意し、[T-0018](../roadmap.md) で行う）：この定義では「実験における時空」が、設定全体の空間 $`X`$ と観測者の座標 $`M_O`$ の二つの意味に使われている。$`X_π`$ を「プロトコル $`π`$ の設定の空間」、$`X`$ を「プロトコル全体の設定の空間」とし、$`M_O`$ を「観測者 $`O`$ の実験における時空」とする。また、時空の部分と設定の部分を単純に分けず、$`τ^O_π`$ を $`X_π`$ 全体の上の写像とする。時空の読み以外の設定の値によって、較正に補正が要る場合があるため（ユーザーの指摘。例えば、磁場の中の原子時計の周波数のずれ。例は Claude の補足）。「実験パラメータ」の語も「設定」に統一する（第 20 回に実施した）。
  - 較正が確率的になる場合（時計が量子系である場合など。[T-0019](../roadmap.md) の Claude の見立て）の扱い：確率的な較正を別の核 $`K^O_π : X_π ⇝ M_O`$ として入れるか、$`τ^O_π`$ そのものを一般化するか。時計の記録された読みを、設定 $`X_π`$ と結果 $`Y_π`$ のどちらに置くか（結果に置く場合は、$`σ^O_π`$ の側の問いになる）。核を使う場合、時計の状態と読み取り方が設定 $`x`$ から決まるか。未知の状態に依存するなら、$`x`$ だけを入力とする核では足りないので、状態を設定に含めるか、推定の対象ごとの核を使うかも決める。T-0018・T-0019 で決める（PR #36 のレビューの論点）。
- **整合条件**：時計や物差しも観測の対象である。観測における時空で測った時間・空間が、実験における時空の時間・空間と矛盾しないことの定式化。見立て：[C-0002](../conjectures/C-0002.md) の下で、観測における時空のモデルは基準の時計と物差しの読みを予測する。その予測が較正の写像 $`τ^O`$ と一致することを、再構成の不動点の条件とする。次もこの条件の一部と見なす（ロードマップの T-0009）。
  - 観測者の取り替え（較正の取り替え）$`M_O → M_{O'}`$ がどんな写像になるか（ポアンカレ変換になるか）。
  - 実際の
…（以下 1095 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='definitions/D-0003.md'
s=open(p).read()
hist=s[s.index('## 履歴'):].rstrip('\n')
head='''# D-0003: 設定の空間

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)、[A-0004](../assumptions/A-0004.md) |
| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0004](../conjectures/C-0004.md)、[C-0008](../conjectures/C-0008.md) |
| 初出 | [2026-09-27 第 07 回](../summaries/2026-09-27_07_observation-and-experiment.md) |

## 定義

1. **プロトコル $`π`$ の設定の空間**：$`X_π`$ は、1 回の観測の設定（[D-0001](D-0001.md)）全体の集合で、有限個の実数の組の集合 $`X_π ⊆ ℝ^{n_π}`$（[A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md)）とし、部分空間の位相を入れる。資源の量（操作回数、時間、エネルギーなど）も設定に含める（[A-0004](../assumptions/A-0004.md)）。
2. **プロトコル全体の設定の空間**：$`X := ⨆_π X_π`$（直和）とし、直和の位相を入れる。

## 注意

- 第 19 回までは、この定義を「実験における時空」とよび、$`X_π`$ の座標を「時空の部分」（時計や物差しの読み）と「設定の部分」に分けていた。第 20 回に、ユーザーの提案で、この定義を設定の空間とし、時空の読みの扱いは、観測者の実験における時空と較正（[D-0013](D-0013.md)）に移した。較正の写像は設定全体に依存してよいので、座標を時空の部分と設定の部分に分けることはしない（時空の読み以外の設定の値で較正に補正が要る場合があるため。ユーザーの指摘。例えば、磁場の中の原子時計の周波数のずれ）。
- 設定の座標の尺度の取り方には任意性がある。取り替えを同等とみなす場合は、同相写像による取り替えに限る。
- 直和の位相では、連続性（[A-0006](../assumptions/A-0006.md)）は各プロトコルの中だけで意味を持つ。
- 設定の空間は 1 回の観測の設定の空間である。$`N`$ 回の観測からなる実験の設定の族は $`X_π^N`$ の元になる（[D-0001](D-0001.md)）。

## 未解決の点

- 時空の読み以外の設定（磁場の強さなど）を、異なるプロトコルの間でどう比べるか（PR #28 のレビュー）。
- 結果の空間のうち、時計や物差しの読みでない座標を共通の空間に写す方法（[A-0006](../assumptions/A-0006.md) の未解決の点）。

'''
hist+='\n- 第 20 
…（以下 192 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
done
```

</details>

<details><summary>ツール: Write: /home/user/point-free-spacetime/definitions/D-0013.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/definitions/D-0013.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/definitions/D-0013.md (file state is current in your context — no need to Read it back)
```

</details>

## Claude

Now A-0010 rewrite and look at its current content.

<details><summary>ツール: Bash</summary>

```text
cat assumptions/A-0010.md | sed -n 1,40p
```

</details>

<details><summary>結果: Bash</summary>

```text
# A-0010: 観測者の基準の時計と物差しによる座標づけ

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md) |
| 関係する予想・結果 | なし |
| 初出 | [2026-09-29 第 13 回](../summaries/2026-09-29_13_experimental-spacetime.md) |

## 主張

観測者 $`O`$ は、基準の時計と物差しを持つ。時空の読みにあたる設定値を持つ各プロトコル $`π`$ について、その設定の空間 $`X_π`$（[D-0001](../definitions/D-0001.md)）のパラメータのうち、装置の中の時計や物差しの読みにあたるものは、基準の時計と物差しとの較正（時計合わせと物差しの比較）によって、$`O`$ の座標 $`(t, 𝐱) ∈ ℝ^{1+n}`$ に連続に換算できる。

## 採用の理由

- 実験における時空（[D-0003](../definitions/D-0003.md)）の時空の部分を、異なるプロトコルの間で比べる共通の空間が要る（第 10 回からの D-0003 の未解決の点）。第 13 回に、ユーザーの提案で D-0003 の未解決の点を先に解決することにし、その共通の空間を観測者の座標として与えた。
- 領域と有界性を観測の局在を使わずに与えるため（[A-0008](A-0008.md)）と、距離を使う前提・予想（[A-0009](A-0009.md)、[C-0001](../conjectures/C-0001.md)、[C-0008](../conjectures/C-0008.md)）が意味を持つために要る。

## 注意

- 較正には約束が入る（例えば、離れた時計の時計合わせ）。この前提は、約束を一つ決めれば換算が定まることだけを述べ、どの約束が物理的に自然かは述べない。
- 座標が $`ℝ^{1+n}`$ に値を取ることは、時空の幾何（計量や、観測者の取り替えの形）について何も主張しない。それらは、観測における時空との整合条件（[D-0003](../definitions/D-0003.md) の未解決の点）の側の問いである。
- 換算は観測者 $`O`$ に依存する。観測者を添字にした族として扱う（[C-0008](../conjectures/C-0008.md) の観測者ごとの族と同じ添字）。

## 未解決の点

- 観測者が実験と 1 対 1 に対応すること（第 20 回。[D-0001](../definitions/D-0001.md)）との関係。この前提は、一人の観測者 $`O`$ が複数のプロトコルの設定を自分の座標に換算する形で書かれている。観測者が実験ごとに異なるなら、この前提を、各実験の観測者の座標への換算と、観測者の取り替え $`M_O → M_{O'}`$ に書き直す必要がある。[T-0018](../roadmap.md) の (A)（D-0003 の再編）で扱う。
- 空間の次元 $`n`$ を前提として固定するか、較正から決まるものとするか。
- 較正の約束の選び方と、その取り替えの扱い。
- 観測者が使える範囲の有限性（到達できる範囲 $`R_O`$）を、$`M_O`$ の部分集合として扱うか（[C-0008](../conjectures/C-0008
…（以下 83 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='assumptions/A-0010.md'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
rep('| 依存する ID | [D-0001](../definitions/D-0001.md) |','| 依存する ID | [D-0001](../definitions/D-0001.md)、[D-0003](../definitions/D-0003.md) |')
rep(s[s.index('## 主張'):s.index('## 採用の理由')],'''## 主張

各有限な実験 $`e`$（[D-0001](../definitions/D-0001.md)）の観測者 $`O_e`$ は、基準の時計と物差しを持つ。時空の読みを持つプロトコル $`π`$ の実験 $`e`$ では、装置の時計や物差しの読み（設定の読みと結果の読み）は、$`O_e`$ の基準の時計と物差しとの較正（時計合わせと物差しの比較）によって、$`O_e`$ の座標 $`(t, 𝐱) ∈ ℝ^{1+n}`$ に連続に換算できる。換算は、設定全体（[D-0003](../definitions/D-0003.md)）と結果に依存してよい。

''')
rep('- 実験における時空（[D-0003](../definitions/D-0003.md)）の時空の部分を、異なるプロトコルの間で比べる共通の空間が要る（第 10 回からの D-0003 の未解決の点）。第 13 回に、ユーザーの提案で D-0003 の未解決の点を先に解決することにし、その共通の空間を観測者の座標として与えた。',
'- 装置の読みを、時空の点として比べられる座標に移す必要がある（第 10 回からの D-0003 の未解決の点）。第 13 回に、ユーザーの提案で、その座標を観測者の座標として与えた。第 20 回に、観測者が実験ごとに異なること（[D-0001](../definitions/D-0001.md)）に合わせて、各実験の観測者の座標への換算に改めた。換算の写像（準備の事象と登録の事象）は [D-0013](../definitions/D-0013.md) で定める。')
rep('それらは、観測における時空との整合条件（[D-0003](../definitions/D-0003.md) の未解決の点）の側の問いである。','それらは、観測における時空との整合条件（[D-0013](../definitions/D-0013.md) の未解決の点）と、観測者の取り替えの前提（[A-0014](A-0014.md)・[A-0015](A-0015.md)）の側の問いである。')
rep('- 換算は観測者 $`O`$ に依存する。観測者を添字にした族として扱う（[C-0008](../conjectures/C-0008.md) の観測者ごとの族と同じ添字）。',
'- 換算は実験（装置と観測者）に依存しうる。プロトコルだけで決まることは、別の前提 [A-0013](A-0013.md)（較正の普遍性）で置く。\n- 異なる実験の観測者の座標の比べ方は、この前提に含めない（[A-0014](A-0014.md)・[A-0015](A-0015.md)）。')
rep('- 観測者が実験と 1 対 1 に対応す
…（以下 414 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
ok
```

</details>

<details><summary>ツール: Bash</summary>

```text
S='[2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md)' && cat > assumptions/A-0012.md <<EOF
# A-0012: 実際の実験の最初の観測への制限

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[D-0002](../definitions/D-0002.md) |
| 関係する予想・結果 | なし |
| 初出 | $S |

## 主張

\$\`N_e ≥ 1\`\$ の実際の実験 \$\`e\`\$（[D-0002](../definitions/D-0002.md)）について、最初の \$\`N_e − 1\`\$ 回の観測に制限した実験 \$\`e'\`\$ も、実際の実験である。ここで \$\`e'\`\$ は、\$\`e\`\$ と同じプロトコルで、設定の族と結果の族を \$\`(x_i)_{i=1}^{N_e − 1}\`\$、\$\`(y_i)_{i=1}^{N_e − 1}\`\$ に制限したものである。

## 採用の理由

ユーザーの提案（第 20 回）。実験の途中までの記録も、それ自体が実際の実験の記録として使えることを保証する。

## 注意

- 繰り返し使うと、実際の実験のすべての最初の \$\`k\`\$ 回への制限（\$\`k = 0, 1, …, N_e\`\$）が実際の実験になる。行き着く先は \$\`N_e = 0\`\$ の実験である（[D-0001](../definitions/D-0001.md) の注意）。
- 各実際の実験の制限は有限個（\$\`N_e + 1\`\$ 個）なので、実際の実験の全体が高々可算であること（[A-0001](A-0001.md)）とは両立する（Claude の補足）。
- 装置と観測者は実験と 1 対 1 に対応する（[D-0001](../definitions/D-0001.md)）ので、\$\`e'\`\$ の観測者は、\$\`e\`\$ の観測者の世界線の区間を、\$\`N_e − 1\`\$ 回目までの観測の期間に縮めたものになる（Claude の補足）。
- 適応的な設定（[D-0001](../definitions/D-0001.md)）でも、\$\`i\`\$ 回目の設定は \$\`i − 1\`\$ 回目までの結果だけで決まるので、制限した実験の記録は矛盾しない。

## 未解決の点

- 制限した実験 \$\`e'\`\$ の装置と観測者の定め方（世界線の区間の端をどこに取るか）。
- 実験の族の極限（[D-0005](../definitions/D-0005.md)）で、制限の列（入れ子の観測。第 17 回の調査メモの 7.2 節）をどう使うか。
- 可能な実験についても同じ閉性を課すか。

## 履歴

- 第 20 回：ユーザーの提案で導入した（[T-0018](../roadmap.md)）。
EOF
cat > assumptions/A-0013.md <<EOF
# A-0013: 較正の普遍性

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0013](../de
…（以下 3929 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
13:$`ℝ^{1+n}`$ に作用する群 $`G`$ があり、任意の二つの観測者 $`O`$、$`O'`$ について、取り替え $`φ_{O'O} : M_O → M_{O'}`$（[D-0013](../definitions/D-0013.md)）が $`G`$ の元として定まり、$`φ_{OO} = \mathrm{id}`$、$`φ_{O''O'} ∘ φ_{O'O} = φ_{O''O}`$ を満たす（取り替えは比較の経路に依らない）。
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 13p assumptions/A-0012.md; sed -n 13p assumptions/A-0013.md | cut -c1-120
```

</details>

<details><summary>結果: Bash</summary>

```text
$`N_e ≥ 1`$ の実際の実験 $`e`$（[D-0002](../definitions/D-0002.md)）について、最初の $`N_e − 1`$ 回の観測に制限した実験 $`e'`$ も、実際の実験である。ここで $`e'`$ は、$`e`$ と同じプロトコルで、設定の族と結果の族を $`(x_i)_{i=1}^{N_e − 1}`$、$`(y_i)_{i=1}^{N_e − 1}`$ に制限したものである。
時空の読みを持つ各プロトコル $`π`$ について、部分写像 $`τ_π : X_π ⇀ ℝ^{1+n}`$ と $`σ_π
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 1,15p conjectures/C-0008.md
```

</details>

<details><summary>結果: Bash</summary>

```text
# C-0008: ポアンカレ共変な装置の占める領域は有界にできない

| 項目 | 値 |
| --- | --- |
| 確度 | 高 |
| 重要度 | 中 |
| 検証費用 | 中 |
| 優先度 | 中（第 12 回にユーザーと相談して決定） |
| 検証方法 | 自然言語の証明・Lean |
| 状態 | 未着手 |
| Issue | [#26](https://github.com/kittenkiki15/point-free-spacetime/issues/26) |
| 依存する ID | [D-0003](../definitions/D-0003.md)、[D-0009](../definitions/D-0009.md)、[D-0011](../definitions/D-0011.md) |
| 目標の ID | なし |
| 初出 | [2026-09-26 第 05 回](../summaries/2026-09-26_05_minimal-scale.md)（C-0001 の旧主張 4。第 12 回に分割） |
```

</details>

<details><summary>ツール: Bash</summary>

```text
S='[2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md)' && cat > conjectures/C-0009.md <<EOF
# C-0009: 較正の普遍性から、観測者の取り替えはローレンツ変換かガリレイ変換になる

| 項目 | 値 |
| --- | --- |
| 確度 | 高 |
| 重要度 | 高 |
| 検証費用 | 中 |
| 優先度 | 未定（対話で決定） |
| 検証方法 | 文献調査・自然言語の証明 |
| 状態 | 未着手 |
| Issue | 未作成 |
| 依存する ID | [D-0013](../definitions/D-0013.md)、[A-0013](../assumptions/A-0013.md)、[A-0015](../assumptions/A-0015.md) |
| 目標の ID | なし |
| 初出 | $S |

## 主張

較正の普遍性（[A-0013](../assumptions/A-0013.md)）と、観測者の取り替えが群をなすこと（[A-0015](../assumptions/A-0015.md)）に、取り替えの一様性・等方性・連続性などの条件を加えると、群 \$\`G\`\$ の線形部分は、ある不変な速さ \$\`c\`\$ についてのローレンツ変換の群か、ガリレイ変換の群（\$\`c = ∞\`\$）に限られる。\$\`c\`\$ の値は実験から決まる。

## 詳細化の論点

- 加える条件（一様性、等方性、連続性、因果の向きを保つことなど）の正確な形と、それぞれを較正の普遍性からどこまで導けるか。
- 較正の普遍性（同じ手順で測れば、どの観測者も自分の座標で同じ値を得る）を、群 \$\`G\`\$ についての条件（相対性原理）として定式化する方法。
- 比較の実験で取り替えを与える体系（[A-0014](../assumptions/A-0014.md)）での対応する主張。
- [C-0008](C-0008.md)（ポアンカレ共変性を仮定する予想）との関係。この予想が成り立てば、C-0008 の仮定を較正の普遍性からの帰結に置き換えられる可能性がある。

## 背景

第 20 回に、較正の普遍性を前提として登録するときに、その前提から導かれる予想としてユーザーと記録した。相対性原理と一様性・等方性などから、光速の不変性を仮定せずにローレンツ変換かガリレイ変換を導く古典的な結果がある（Ignatowski 1910、Lévy-Leblond 1976 など。記憶による。未確認）。

## 評価の根拠

- 確度: 高。条件を適切に加えれば、古典的な結果と同じ型の主張になる見込み。ただし、較正の普遍性からその条件を得られるかは確かめていない。
- 重要度: 高。観測者の取り替えの形（時空の幾何）を、実験の手順についての前提から導く道筋になる。
- 検証費用: 中。古典的な結果の原典を確かめ、本プロジェクトの前提に読み替える。

## 検証の方針

原典（Ignatowski、Lévy-Leblond、その後の文献）を確かめ、仮定を本プロジェクトの前提（A-0013・A-0015）に読み替える。必要なら Lean で形式化する。

## 結果

（未着手）
EOF
cat > conjectures/C-0010.md <<EOF
# C-0010: 比較の実
…（以下 2333 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
ok
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
import re
def addrows(p,after_prefix,rows):
    L=open(p).read().split('\n')
    i=max(k for k,l in enumerate(L) if l.startswith(after_prefix))
    for r in reversed(rows): L.insert(i+1,r)
    open(p,'w').write('\n'.join(L))
addrows('assumptions/README.md','| [A-0011]',[
'| [A-0012](A-0012.md) | 実際の実験の最初の観測への制限 | 実験 | 作業上 |',
'| [A-0013](A-0013.md) | 較正の普遍性 | 実験 | 作業上 |',
'| [A-0014](A-0014.md) | 観測者の取り替えを比較の実験で与える | 実験 | 作業上 |',
'| [A-0015](A-0015.md) | 観測者の取り替えの群 | 実験 | 作業上 |'])
addrows('definitions/README.md','| [D-0012]',['| [D-0013](D-0013.md) | 観測者の実験における時空と較正 | 実験 | 作業上 |'])
p='definitions/README.md'; s=open(p).read(); s=s.replace('| [D-0003](D-0003.md) | 実験における時空 |','| [D-0003](D-0003.md) | 設定の空間 |'); open(p,'w').write(s)
addrows('conjectures/README.md','| [C-0006]',[
'| [C-0009](C-0009.md) | 較正の普遍性から、観測者の取り替えはローレンツ変換かガリレイ変換になる | 高 | 高 | 中 | 未定 | 未着手 | 未作成 |',
'| [C-0010](C-0010.md) | 比較の実験で取り替えを与える体系では、較正の普遍性は検証できる条件に言い換えられる | 中 | 中 | 中 | 未定 | 未着手 | 未作成 |',
'| [C-0011](C-0011.md) | 比較の一周のずれがすべて自明なら、観測者の取り替えは群をなす | 中 | 高 | 高 | 未定 | 未着手 | 未作成 |'])
EOF
python3 tools/deps_graph.py >/dev/null; python3 -m pytest -q tools/tests 2>&1 | grep -E "passed|failed|Error" | head
```

</details>

<details><summary>結果: Bash</summary>

```text
33 passed in 0.41s
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -rn "実験における時空\|時空の部分\|τ^O\|σ^O" --include=*.md definitions assumptions conjectures framework.md glossary.md symbols.md | grep -v "^definitions/D-0013\|^definitions/D-0003" | cut -c1-170
```

</details>

<details><summary>結果: Bash</summary>

```text
definitions/D-0008.md:13:実験における時空（[D-0003](D-0003.md)）の有界な領域 $`R`$ について、次のように定める。
definitions/D-0008.md:23:- 添字 $`R`$ は実験における時空の領域で、観測における時空の領域ではない。循環を避けるには、$`R`$ とそ�
definitions/README.md:41:| [D-0013](D-0013.md) | 観測者の実験における時空と較正 | 実験 | 作業上 |
definitions/D-0009.md:13:完備束 $`L`$（典型的には、実験における時空の領域のフレーム）の上の写像 $`N : L → L`$ が**膨張**（dilation�
definitions/D-0009.md:28:- $`L`$ として何を取るか。実験における時空の領域の束は、[D-0003](D-0003.md) の $`X`$ の位相、または [A-0008](../a
definitions/D-0007.md:18:- 第 07 回のユーザーの構想の 2 に当たる。実験における時空（[D-0003](D-0003.md)）とは区別する。
definitions/D-0007.md:24:- 実験における時空との整合条件（[D-0003](D-0003.md) の未解決の点）。
definitions/D-0011.md:13:観測者 $`O`$ の時空の部分 $`M_O`$（[D-0003](D-0003.md)）の上で考える。扱うのは、時空の読みを持つプロトコルの
definitions/D-0011.md:58:- 設定の部分（時空の部分以外の座標）が $`\mathrm{occ}`$ にどう効くか。
definitions/D-0011.md:65:- 第 12 回：C-0001 の「区別」を、実験における時空の言葉で書き直す候補 A として導入した（ユーザーの判断
definitions/D-0011.md:66:- 第 13 回：可能な実験についての定義であることを明記し、層を「実験」から「可能な実験」に改めた。実�
assumptions/A-0008.md:1:# A-0008: 実験における時空の領域を独立に与える
assumptions/A-0008.md:13:実験における時空（[D-0003](../definitions/D-0003.md)）の領域と、その包含・有界性は、再構成の対象である観測の
assumptions/A-0008.md:17:局在（[D-0008](../definitions/D-0008.md)）を実験における時空の領域で添字づけるとき、循環を避けるために要る（
assumptions/A-0005.md:13:実験の有限性は、実験における時空 $`X`$（[D-0003](../definitions/D-0003.md)）の各座標の値域が、ℝ の通常の位相�
assumptions/README.md:37:| [A-0008](A-0008.md) | 実験における時空の領域を独立に与える | 実験 | 作業上 |
assumptions/A-0010.md:35:- 第 13 回：D-0003 の未解決の点（共通の時空の部分と比べる写像）を解決するために導入した（ユーザーの判
assumptions/A-0009.md:13:観測者 $`O`$ の時空の部分 $`M_O`$
…（以下 1559 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
for f in definitions/D-0007.md definitions/D-0008.md definitions/D-0009.md definitions/D-0011.md assumptions/A-0008.md assumptions/A-0009.md conjectures/C-0008.md conjectures/C-0002.md; do grep -n "依存する ID" $f | cut -c1-200; done; sed -n 37p conjectures/C-0002.md; sed -n 42p conjectures/C-0002.md; sed -n 28p definitions/D-0009.md; sed -n 18p conjectures/C-0008.md; sed -n 13p assumptions/A-0009.md
```

</details>

<details><summary>結果: Bash</summary>

```text
7:| 依存する ID | [D-0005](../definitions/D-0005.md) |
7:| 依存する ID | [D-0003](../definitions/D-0003.md)、[D-0005](../definitions/D-0005.md)、[A-0008](../assumptions/A-0008.md) |
7:| 依存する ID | なし |
7:| 依存する ID | [D-0001](D-0001.md)、[D-0002](D-0002.md)、[D-0003](D-0003.md)、[D-0009](D-0009.md)、[D-0010](D-0010.md)、[A-0001](../assumptions/A-0001.md)、[A-0008](../assumptions/A-0008.
51:- この定義は [C-0002](../conjectures/C-0002.md) に依存するが、C-0002 はこの定義に依存しないので、D-0011 と C-0002 の間には循環はない。一方、可能な観測�
66:- 第 13 回：可能な実験についての定義であることを明記し、層を「実験」から「可能な実験」に改めた。実際の実験の記録された占める領域と、�
7:| 依存する ID | [D-0003](../definitions/D-0003.md) |
7:| 依存する ID | [D-0003](../definitions/D-0003.md)、[D-0011](../definitions/D-0011.md) |
12:| 依存する ID | [D-0003](../definitions/D-0003.md)、[D-0009](../definitions/D-0009.md)、[D-0011](../definitions/D-0011.md) |
12:| 依存する ID | [D-0003](../definitions/D-0003.md)、[D-0005](../definitions/D-0005.md)、[D-0006](../definitions/D-0006.md)、[D-0007](../definitions/D-0007.md) |
31:- [D-0006](../definitions/D-0006.md) との依存の意味：D-0006 は、この予想の結論（可能な実験を記述し直せること）を前提に使う。この予想の「依存する ID
Claude の補足（見立て）：可能な観測量は実際の観測量を含み、可能な観測量から時空を再構成し直しても同じ時空が得られる、という不動点の条件を要請するのが自然である。これは、時計と物差しで測った時空がもとの実験における時空と矛盾しないという整合条件を、再構成の不動点の条件として述べ直したものになる。
- 重要度：高。成り立てば、本プロジェクトの構想（観測量の代数から時空を再構成し、実験における時空との対応を与える）の中心の主張になる。
- $`L`$ として何を取るか。実験における時空の領域の束は、[D-0003](D-0003.md) の $`X`$ の位相、または [A-0008](../assumptions/A-0008.md) で与える領域から作る（どちらもまだ決まっていない）。
観測者 $`O`$ の時空の部分 $`M_O = ℝ^{1+n}`$（[D-0003](../definitions/D-0003.md)。$`n ≥ 
…（以下 211 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b,cnt=1):
    s=open(p).read(); assert s.count(a)==cnt,(p,a,s.count(a)); open(p,'w').write(s.replace(a,b))
D13='[D-0013](D-0013.md)'; D13u='[D-0013](../definitions/D-0013.md)'
rep('definitions/D-0008.md','| 依存する ID | [D-0003](../definitions/D-0003.md)、','| 依存する ID | [D-0013](../definitions/D-0013.md)、')
rep('definitions/D-0008.md','実験における時空（[D-0003](D-0003.md)）の有界な領域','観測者の実験における時空（'+D13+'）の有界な領域')
rep('definitions/D-0008.md','- 添字 $`R`$ は実験における時空の領域','- 添字 $`R`$ は観測者の実験における時空の領域')
rep('definitions/D-0009.md','（典型的には、実験における時空の領域のフレーム）','（典型的には、観測者の実験における時空の領域のフレーム）')
rep('definitions/D-0009.md','- $`L`$ として何を取るか。実験における時空の領域の束は、[D-0003](D-0003.md) の $`X`$ の位相、または [A-0008](../assumptions/A-0008.md) で与える領域から作る（どちらもまだ決まっていない）。',
 '- $`L`$ として何を取るか。観測者の実験における時空の領域の束は、'+D13+' の $`M_O`$ の位相（[A-0008](../assumptions/A-0008.md) で与える領域）から作る。第 19 回までは、[D-0003](D-0003.md) の $`X`$ の位相も候補だったが、第 20 回に $`X`$ は設定の空間になった。')
rep('definitions/D-0007.md','実験における時空（[D-0003](D-0003.md)）とは区別する。','観測者の実験における時空（'+D13+'）とは区別する。')
rep('definitions/D-0007.md','- 実験における時空との整合条件（[D-0003](D-0003.md) の未解決の点）。','- 観測者の実験における時空との整合条件（'+D13+' の未解決の点）。')
rep('assumptions/A-0008.md','# A-0008: 実験における時空の領域を独立に与える','# A-0008: 観測者の実験における時空の領域を独立に与える')
rep('assumptions/A-0008.md','| 依存する ID | [D-0003](../definitions/D-0003.md) |','| 依存する ID | '+D13u+' |')
rep('assumptions/A-0008.md','実験における時空（[D-0003](../definitions/D-0003.md)）の領域と、その包含・有界性は','観測者の実験における時空（'+D13u+'）の領域と、その包含・有界性は')
rep('a
…（以下 1472 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
assumptions/A-0008.md:1:# A-0008: 観測者の実験における時空の領域を独立に与える
assumptions/A-0008.md:13:観測者の実験における時空（[D-0013](../definitions/D-0013.md)）の領域と、その包含・有界性は、再�
assumptions/A-0008.md:17:局在（[D-0008](../definitions/D-0008.md)）を観測者の実験における時空の領域で添字づけるとき、循�
assumptions/A-0009.md:13:観測者 $`O`$ の実験における時空 $`M_O`$ と、その座標の距離 $`d_O`$（[D-0013](../definitions/D-0013.md)�
conjectures/C-0008.md:18:観測者 $`O`$ の実験における時空 $`M_O = ℝ^{1+n}`$（[D-0013](../definitions/D-0013.md)。$`n ≥ 1`$）の上�
definitions/D-0011.md:13:観測者 $`O`$ の時空の部分 $`M_O`$（[D-0003](D-0003.md)）の上で考える。扱うのは、時空の読みを持�
definitions/D-0011.md:58:- 設定の部分（時空の部分以外の座標）が $`\mathrm{occ}`$ にどう効くか。
definitions/D-0011.md:65:- 第 12 回：C-0001 の「区別」を、実験における時空の言葉で書き直す候補 A として導入した（�
definitions/D-0011.md:66:- 第 13 回：可能な実験についての定義であることを明記し、層を「実験」から「可能な実験�
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 13p definitions/D-0011.md && python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='definitions/D-0011.md'
s=open(p).read()
line=s.split('\n')[12]
new='観測者 $`O`$ の実験における時空 $`M_O`$（[D-0013](D-0013.md)）の上で考える。扱うのは、時空の読みを持つプロトコルの、1 回の観測からなる実験（$`N_e = 1`$。[D-0001](D-0001.md)）だけである。実験 $`e`$ の 1 回の観測の準備の事象（[D-0013](D-0013.md)）を $`x_e ∈ M_O`$ と書き、$`e`$ の設定値とよぶ。異なる観測者の実験は、観測者の取り替え（[A-0014](../assumptions/A-0014.md) または [A-0015](../assumptions/A-0015.md)）で $`O`$ の座標に持ち込んだものとして扱う。'
s=s.replace(line,new)
s=s.replace('可能な実験（[D-0002](D-0002.md)）$`e = (π, x)`$ について','可能な実験（[D-0002](D-0002.md)）$`e = (π, 1, (x_1))`$ について')
s=s.replace('- 設定の部分（時空の部分以外の座標）が $`\\mathrm{occ}`$ にどう効くか。','- 時空の読み以外の設定が $`\\mathrm{occ}`$ にどう効くか。\n- 第 20 回の再編（観測者が実験ごとに異なること、準備の事象と登録の事象。[D-0013](D-0013.md)）に合わせた、2 回以上の観測からなる実験と、登録の事象の扱い。今の定義は、1 回の観測の準備の事象だけを使う。')
s=s.replace('| 依存する ID | [D-0001](D-0001.md)、[D-0002](D-0002.md)、[D-0003](D-0003.md)、','| 依存する ID | [D-0001](D-0001.md)、[D-0002](D-0002.md)、[D-0013](D-0013.md)、')
s=s.rstrip('\n')+'\n- 第 20 回：D-0003 の再編に合わせて、$`M_O`$ を観測者の実験における時空（D-0013）とし、設定値 $`x_e`$ を 1 回の観測の準備の事象と読み直した（内容は変えていない）。\n'
open(p,'w').write(s)
EOF
grep -n "依存する ID\|D-0003\|x_e :=" definitions/D-0011.md | cut -c1-120; python3 tools/deps_graph.py >/dev/null; python3 -m pytest -q tools/tests 2>&1 | grep -oE "[0-9]+ (passed|failed)|AssertionError.*" | head
```

</details>

<details><summary>結果: Bash</summary>

```text
観測者 $`O`$ の時空の部分 $`M_O`$（[D-0003](D-0003.md)）の上で考える。扱うのは、時空の読みを持つプロトコルの実験だけである。実験 $`e`$ の時空の部分の設定値を $`x_e := τ^O_π(x) ∈ M_O`$ と書く（$`e`$ のプロトコルが $`π`$、設定が $`x`$ のとき）。
7:| 依存する ID | [D-0001](D-0001.md)、[D-0002](D-0002.md)、[D-0013](D-0013.md)、[D-0009](D-0009.md)、[D-0010](D
16:2. **可能な実験の占める領域**：可能な実験（[D-0002](D-0002.md)）$`e = (π, 1, (x_1))`$ につい�
51:- この定義は [C-0002](../conjectures/C-0002.md) に依存するが、C-0002 はこの定義に依存しないの
61:- 記録とモデルの占める領域の関係 $`\mathrm{occ}_{\mathrm{rec}}(e)`$ と $`\mathrm{occ}_{\mathrm{mod}}(
67:- 第 13 回：可能な実験についての定義であることを明記し、層を「実験」から「可能な
69:- 第 20 回：D-0003 の再編に合わせて、$`M_O`$ を観測者の実験における時空（D-0013）とし、
AssertionError: ('A-0008', '名前')
AssertionError
AssertionError: ('D-0003', {'C-0002', 'C-0004', 'C-0008'}, {'C-0002', 'C-0004'})
AssertionError
2 failed
31 passed
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
rep('assumptions/README.md','| [A-0008](A-0008.md) | 実験における時空の領域を独立に与える |','| [A-0008](A-0008.md) | 観測者の実験における時空の領域を独立に与える |')
rep('definitions/D-0003.md','| [C-0002](../conjectures/C-0002.md)、[C-0004](../conjectures/C-0004.md)、[C-0008](../conjectures/C-0008.md) |','| [C-0002](../conjectures/C-0002.md)、[C-0004](../conjectures/C-0004.md) |')
rep('definitions/D-0013.md','| 関係する予想・結果 | [C-0009]','| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0008](../conjectures/C-0008.md)、[C-0009]')
rep('definitions/D-0011.md','異なる観測者の実験は、観測者の取り替え（[A-0014](../assumptions/A-0014.md) または [A-0015](../assumptions/A-0015.md)）で $`O`$ の座標に持ち込んだものとして扱う。','異なる観測者の実験は、観測者の取り替え（[D-0013](D-0013.md) の注意）で $`O`$ の座標に持ち込んだものとして扱う。')
EOF
sed -i 's/  A_0008(\["A-0008: 実験における時空の領域を独立に与える"\])/  A_0008(["A-0008: 観測者の実験における時空の領域を独立に与える"])/' framework.md
python3 tools/deps_graph.py >/dev/null; python3 -m pytest -q tools/tests 2>&1 | grep -oE "[0-9]+ (passed|failed)|AssertionError.*" | head
```

</details>

<details><summary>結果: Bash</summary>

```text
33 passed
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 12p framework.md; sed -n 36p framework.md; sed -n 43p framework.md | cut -c1-200; sed -n 232,240p framework.md
```

</details>

<details><summary>結果: Bash</summary>

```text
- 実験装置の時計や物差しで測った「実験における時空」（[D-0003](definitions/D-0003.md)）と、観測量から再構成する「観測における時空」（[D-0007](definitions/D-0007.md)）を分ける。
| 1. 実験 | 実際に行われる有限な実験と、その設定の空間 | [D-0001](definitions/D-0001.md) 有限な実験（作業上）<br>[D-0002](definitions/D-0002.md) 実際の実験と可能な実験（作業上）<br>[D-0003](definitions/D-0003.md) 実験における時空（作業上）<br>[D-0009](definitions/D-0009.md) 膨張（作業上）<br>[D-0010](definitions/D-0010.md) 余白付きの包含（作業上）<br>[D-0012](definitions/D-0012.md) 主体（作業上） | [A-0001](assumptions/A-0001.md) 実際の実験の可算性（採用）<br>[A-0002](assumptions/A-0002.md) プロトコルの有限な記述（採用）<br>[A-0003](assumptions/A-0003.md) 設定と結果は実数値（採用）<br>[A-0004](assumptions/A-0004.md) 資源の量を設定に含める（採用）<br>[A-0005](assumptions/A-0005.md) 実験の有限性を値域のコンパクト性で表す（作業上）<br>[A-0006](assumptions/A-0006.md) 実験の等価原理（採用）<br>[A-0008](assumptions/A-0008.md) 実験における時空の領域を独立に与える（作業上）<br>[A-0010](assumptions/A-0010.md) 観測者の基準の時計と物差しによる座標づけ（作業上） | [C-0004](conjectures/C-0004.md) 等価原理は計算可能性から従う |
第 12 回に、C-0001 の「区別」を、実験における時空の言葉（装置の占める領域 $`\mathrm{occ}`$ による膨張。[D-0011](definitions/D-0011.md)）で書き直し、C-0001 �
各ファイルの「未解決の点」のうち、フレームワーク全体に関わるものです。

- 極限の位相と、事後分布を置く空間（[D-0005](definitions/D-0005.md)）。
- 実験における時空 $`X`$ の位相と、観測における時空との整合条件（[D-0003](definitions/D-0003.md)）。
- 観測における時空を再構成するときの入力と一意性（[D-0007](definitions/D-0007.md)）。
- 層 4・6 の定義と前提。
- 量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えること（第 19 回のユーザーの方針。量子重力理論への寄与という目的による）。今の定義では、結果は実数値の記録で（[A-0003](assumptions/A-0003.md)）、量子の測定は応答関数の形として入る（[D-0004](definitions/D-0004.md)）。「量子的な観測」を量子系を測った古典的な記録と読むか、時計を含む量子系を、古典的な記録へ読み出す前の量子的な出力として実験の対象に
…（以下 204 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
p='framework.md'
rep(p,'- 実験装置の時計や物差しで測った「実験における時空」（[D-0003](definitions/D-0003.md)）と、','- 観測者の基準の時計と物差しで装置の読みを換算した「観測者の実験における時空」（[D-0013](definitions/D-0013.md)）と、')
rep(p,'[D-0003](definitions/D-0003.md) 実験における時空（作業上）','[D-0003](definitions/D-0003.md) 設定の空間（作業上）')
rep(p,'[D-0012](definitions/D-0012.md) 主体（作業上） |','[D-0012](definitions/D-0012.md) 主体（作業上）<br>[D-0013](definitions/D-0013.md) 観測者の実験における時空と較正（作業上） |')
rep(p,'[A-0008](assumptions/A-0008.md) 実験における時空の領域を独立に与える（作業上）<br>[A-0010](assumptions/A-0010.md) 観測者の基準の時計と物差しによる座標づけ（作業上） | [C-0004](conjectures/C-0004.md) 等価原理は計算可能性から従う |',
'[A-0008](assumptions/A-0008.md) 観測者の実験における時空の領域を独立に与える（作業上）<br>[A-0010](assumptions/A-0010.md) 観測者の基準の時計と物差しによる座標づけ（作業上）<br>[A-0012](assumptions/A-0012.md) 実際の実験の最初の観測への制限（作業上）<br>[A-0013](assumptions/A-0013.md) 較正の普遍性（作業上）<br>[A-0014](assumptions/A-0014.md) 観測者の取り替えを比較の実験で与える（作業上。A-0015 と二者択一）<br>[A-0015](assumptions/A-0015.md) 観測者の取り替えの群（作業上。A-0014 と二者択一） | [C-0004](conjectures/C-0004.md) 等価原理は計算可能性から従う<br>[C-0009](conjectures/C-0009.md) 較正の普遍性から、観測者の取り替えはローレンツ変換かガリレイ変換になる<br>[C-0010](conjectures/C-0010.md) 比較の実験で取り替えを与える体系では、較正の普遍性は検証できる条件に言い換えられる<br>[C-0011](conjectures/C-0011.md) 比較の一周のずれがすべて自明なら、観測者の取り替えは群をなす |')
rep(p,'C-0001 の「区別」を、実験における時空の言葉','C-0001 の「区別」を、実験における時空（第 20 回からは観測者の実験における時空）の言葉')
rep(p,'- 実験における時空 $`X`$ の位相と、観測における時空との整合条件（[D-0003](definitions/D-0003.m
…（以下 626 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
36:| 1. 実験 | 実際に行われる有限な実験と、その設定の空間
3:最終更新: 2026-09-30（第 19 回。要件（量子・古典・混成の実験）と、D-0003 の用語の再編の方針を 6 節に加えた）
220:第 18 回に、D-0005 の「極限の位相」について、Le Cam（1972）の実験の弱位相と Ludwig（1985）の構成を原典で確かめた（[第 18 回の調査メモ](surveys/2026-09-30_18_limit-topology.md)）。次は候補である（Claude の見立て）。
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 30p glossary.md; sed -n 85p symbols.md; sed -n 105p symbols.md; sed -n 1,8p symbols.md
```

</details>

<details><summary>結果: Bash</summary>

```text
| experimental spacetime | 実験における時空 | 本プロジェクトの用語（第 07 回、ユーザーの構想による）。実験装置の中の時計や物差しで測った「実験パラメータ」（第 20 回に「設定」に改めた語）を記述する数学的なモデル。観測量の代数から再構成する「観測における時空」とは分けて考える。実験の有限性に含まれる局所性は、この時空についての前提である。本プロジェクトの定義は [D-0003](definitions/D-0003.md)。 | [第 07 回のまとめ](summaries/2026-09-27_07_observation-and-experiment.md) |
| $`M_O`$、$`d_O`$、$`τ^O_π`$ | 観測者の時空の部分、その距離、換算の写像 | 観測者 $`O`$ の基準の時計と物差しによる座標の空間 $`ℝ^{1+n}`$、その座標の距離、プロトコル $`π`$ の設定の時計・物差しの読みを $`M_O`$ に換算する写像（[D-0003](definitions/D-0003.md)、[A-0010](assumptions/A-0010.md)） | — | [第 13 回](summaries/2026-09-29_13_experimental-spacetime.md) |
| $`X`$ | 実験における時空 | 可能な設定全体の空間（第 09 回の改訂案。第 20 回に「実験パラメータ」の語を「設定」に改めた）。時空の部分と、それ以外の設定の部分からなる | | [調査 08](surveys/2026-09-28_08_observation-as-limit.md)（1.4 節） |
# 記号一覧

本プロジェクトの文書と Lean のコードで使う記号です。分野ごとに、初出の順に並べます。
用語の説明は [用語一覧](glossary.md) を参照してください。数式の書き方は [数式の書き方](docs/math-guide.md) に従います。

- 「Lean」の列は、Lean 4 と Mathlib での対応する記法・名前です。空欄は、対応するものをまだ確認していないことを表します。
- 初出の列は、その記号を最初に使った文書です。
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
rep('glossary.md','実験の有限性に含まれる局所性は、この時空についての前提である。本プロジェクトの定義は [D-0003](definitions/D-0003.md)。 |',
'実験の有限性に含まれる局所性は、この時空についての前提である。第 20 回に、設定全体の空間（設定の空間。[D-0003](definitions/D-0003.md)）と分け、観測者ごとの座標 $`M_O`$ と較正の写像を「観測者の実験における時空」とした（観測者は実験ごとに異なる）。本プロジェクトの定義は [D-0013](definitions/D-0013.md)。 |')
rep('symbols.md','| $`M_O`$、$`d_O`$、$`τ^O_π`$ | 観測者の時空の部分、その距離、換算の写像 | 観測者 $`O`$ の基準の時計と物差しによる座標の空間 $`ℝ^{1+n}`$、その座標の距離、プロトコル $`π`$ の設定の時計・物差しの読みを $`M_O`$ に換算する写像（[D-0003](definitions/D-0003.md)、[A-0010](assumptions/A-0010.md)） | — |',
'| $`M_O`$、$`d_O`$、$`τ^O_π`$ | 観測者の実験における時空、その距離、換算の写像 | 観測者 $`O`$ の基準の時計と物差しによる座標の空間 $`ℝ^{1+n}`$、その座標の距離、設定の時計・物差しの読みを $`M_O`$ に換算する写像（第 13 回は「観測者の時空の部分」とよび、[D-0003](definitions/D-0003.md) で定めた。第 20 回に [D-0013](definitions/D-0013.md) に移し、換算の写像は実験ごとの $`τ_e`$・$`σ_e`$ に改めた） | — |')
rep('symbols.md','| $`X`$ | 実験における時空 | 可能な設定全体の空間（第 09 回の改訂案。第 20 回に「実験パラメータ」の語を「設定」に改めた）。時空の部分と、それ以外の設定の部分からなる |',
'| $`X`$ | 設定の空間 | プロトコル全体の設定の空間 $`⨆_π X_π`$（[D-0003](definitions/D-0003.md)）。第 09 回の改訂案では「実験における時空」とよび、時空の部分と設定の部分に分けていたが、第 20 回に設定の空間とし、分割をやめた |')
L=open('symbols.md').read().split('\n')
i=next(k for k,l in enumerate(L) if l.startswith('| $`M_O`$、$`d_O`$'))
L.insert(i+1,'| $`N_e`$、$`(x_i)`$、$`(y_i)`$ | 観測の回数、設定の族、結果の族 | 有限な実験 $`e`$ の観測の回数（0 も許す）と、$`i`$ 回目（実行の順序）の観測の設定 $`x_i ∈ X_π`$・結果 $`y_i ∈ Y_π`$（[D-0001](definitions/D-0001.md)） | — | [第 20 回](sum
…（以下 1073 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
33 passed in 0.14s
7d073b4
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -i 's/可能な実験は設定 \$`(π, x)`\$ だけで結果の記録を含まないので/可能な実験はプロトコルと設定の族 $`(π, N, (x_i))`$ だけで結果の記録を含まないので/' definitions/D-0006.md && grep -c "(π, N, (x_i))" definitions/D-0006.md && python3 -m pytest -q tools/tests 2>&1 | tail -1 && git commit -qam "第 20 回：D-0006 の可能な実験の記法を D-0002 に合わせた

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: https://claude.ai/code/[伏せ字]" && git push -q && git log -1 --format=%h
```

</details>

<details><summary>結果: Bash</summary>

```text
1
33 passed in 0.13s
beb0b26
```

</details>

## Claude

(A) の書き換えを終え、7d073b4 と beb0b26 で push しました。依存関係の検査（テスト 33 件）は通っています。新しく加えた定義・前提は、合意どおりすべて「作業上」にしました。

#### 変更した点

**定義**
- **D-0001（有限な実験）**：一つの実験を、プロトコル、観測の回数 $`N_e`$（0 も許す）、設定の族 $`(x_i)`$、結果の族 $`(y_i)`$、装置、観測者の組にしました。添字 $`i`$ は実行の順序で、設定をそれまでの結果に応じて選んでもよい（適応的な設定）としました。
  - $`N_e = 0`$ の実験は、どの実験からも模倣できる、情報を与えない最小の実験です。実験を順につなぐ操作の単位元にもあたります。注意に書きました（Claude の補足）。
  - 未解決だった「$`Y_π`$ は何の空間か」は、1 回の観測の結果の空間、として解消しました。
- **D-0002**：可能な実験を $`(π, N, (x_i))`$ に改めました。適応的な設定の場合は、設定の族の代わりに、設定を選ぶ規則を指定します。
- **D-0003**：名前を「設定の空間」に改め、時空の部分と設定の部分への分割をやめました。
- **D-0013（新規）「観測者の実験における時空と較正」**
  - 観測者ごとの座標 $`M_O`$ と距離 $`d_O`$ を定めました。
  - 実験ごとの較正の写像を二つ置きました。$`τ_e`$ は準備の事象、$`σ_e`$ は登録の事象を、観測者の座標で表します。
  - 各観測の (準備の事象, 登録の事象) の組を、「観測の事象の族」としました。レーダーなどの例を注意に書いています。
  - 旧 D-0003 の未解決の点（整合条件など）は、ここに移しました。
  - 因果的な順序（登録の事象は準備の事象の未来にある）は、予想の候補として未解決の点に書くにとどめました。予想として登録してほしいというご指示はなかったためです。

**前提（新規）**
- **A-0012**：実際の実験の最初の $`N_e − 1`$ 回への制限も、実際の実験である。ご提案の前提です。
- **A-0013（較正の普遍性）**：較正の規則は、プロトコルと設定・結果だけで決まり、装置や観測者に依らない。今は実際の実験に限って課しています。
- **A-0014**：観測者の取り替えを、比較の実験で与える。
- **A-0015**：観測者の取り替えは、比較の経路に依らない群をなす。A-0014 と二者択一で、どちらを採るかで体系を分けます。

**予想（新規）**
- **C-0009**：較正の普遍性と群（A-0015）、一様性・等方性などから、観測者の取り替えはローレンツ変換かガリレイ変換になる。
- **C-0010**：A-0014 の体系では、較正の普遍性を検証できる条件に言い換えられる。目標の ID は A-0013 です。
- **C-0011**：比較の一周のずれがすべて自明なら、取り替えは群をなす。目標の ID は A-0015 です。自明でないずれは、曲率の候補になります。

**ほかのファイル**
- A-0010 は、各実験の観測者の座標への換算に書き直しました。
- A-0008・A-0009・C-0008・D-0007〜D-0009・D-0011 の参照を、D-0013 に付け替えました。
- 用語一覧、記号一覧（$`N_e`$、$`τ_e`$、$`σ_e`$、$`φ_{O'O}`$ を追加）、`framework.md` も更新しました。

#### ご相談

1. **予想 C-0009〜C-0011 の優先度**：私の評価（確度・重要度・検証費用）は次のとおりです。
   - C-0009：高・高・中
   - C-0010：中・中・中
   - C-0011：中・高・高

   今は優先度を「未定」、Issue を「未作成」にしています。優先度を決めていただければ、Issue を `[C-NNNN] …` の形で作り、優先度のラベルを付けて、ファイルに番号を書きます。
2. **A-0013 の範囲**：実際の実験に限って課しました。可能な実験にも課すかは、未解決の点に残しています。この形でよいでしょうか。

これで T-0018 の (A)・(B)・(C) が一通り終わりました。優先度が決まって Issue を作ったら、対話を終えてセッションの終え方に進むか、ご判断ください。

## ユーザー

「因果的な順序（登録の事象は準備の事象の未来にある）」について、「可能な実験は因果的な順序を破らない」は予想として登録した方がよいと思います。一方、「実際の実験で因果的な順序を破る実験は存在しない」は、他のどの仮定からも導けないと思うので、新規の仮定として新設した方がよいと思います。いかがでしょうか？

「1. 予想 C-0009〜C-0011 の優先度」について、いったん優先度「低」に設定して、予想の検証に着手したら、棚卸を行いましょう。

「2. A-0013 の範囲」について、これも「実際の実験」についてはご提案の A-0013 のように仮定にし、「可能な実験」については予想として登録するのがよいと思います。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && S='[2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md)' && cat > assumptions/A-0016.md <<EOF
# A-0016: 実際の実験は因果的な順序を破らない

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0002](../definitions/D-0002.md)、[D-0013](../definitions/D-0013.md) |
| 関係する予想・結果 | なし |
| 初出 | $S |

## 主張

実際の実験 \$\`e\`\$（[D-0002](../definitions/D-0002.md)）の各観測 \$\`i\`\$ について、準備の事象 \$\`τ_e(x_i)\`\$ と登録の事象 \$\`σ_e(x_i, y_i)\`\$（[D-0013](../definitions/D-0013.md)）がともに定まるなら、観測者 \$\`O_e\`\$ の時刻の座標で、登録の事象は準備の事象より前にない：\$\`t\\bigl(σ_e(x_i, y_i)\\bigr) ≥ t\\bigl(τ_e(x_i)\\bigr)\`\$。

## 採用の理由

ユーザーの提案（第 20 回）。実際の実験で因果的な順序を破るものがないことは、ほかのどの定義・前提からも導けないので、前提として置く。可能な実験について同じことが成り立つかは、予想 [C-0012](../conjectures/C-0012.md) とする。

## 注意

- ここで述べるのは、観測者の時刻の座標での順序だけである（最も弱い形。Claude の提案）。\$\`M_O\`\$ にはまだ因果構造（光円錐）を入れていないので（[D-0013](../definitions/D-0013.md) の注意）、「ある不変な速さを超えてつながらない」という強い形は、観測者の取り替えの形（[C-0009](../conjectures/C-0009.md)）が決まった後に述べる。
- 一つの観測の中の順序だけを述べ、異なる観測の間や異なる実験の間の順序は述べない。

## 未解決の点

- 強い形（登録の事象が準備の事象の因果的な未来にある）への置き換えと、そのために要る \$\`M_O\`\$ の因果構造。
- 時刻の座標の精度（有限精度の記録で、\$\`t(σ) ≥ t(τ)\`\$ をどう判定するか）。
- 因果構造の再構成（ロードマップの T-0017）の入力としての使い方。

## 履歴

- 第 20 回：ユーザーの提案で導入した（[T-0018](../roadmap.md) の (A)）。
EOF
cat > conjectures/C-0012.md <<EOF
# C-0012: 可能な実験は因果的な順序を破らない

| 項目 | 値 |
| --- | --- |
| 確度 | 高 |
| 重要度 | 中 |
| 検証費用 | 中 |
| 優先度 | 低（第 20 回にユーザーと決定。検証に着手したら見直す） |
| 検証方法 | 自然言語の証明 |
| 状態 | 未着手 |
| Issue | 未作成 |
| 依存する ID | [D-0002](../def
…（以下 4023 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
AssertionError: ('D-0002', set(), {'C-0012', 'C-0013'})
AssertionError
1 failed
32 passed
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rep(p,a,b):
    s=open(p).read(); assert s.count(a)==1,(p,a); open(p,'w').write(s.replace(a,b))
rep('definitions/D-0002.md','| 関係する予想・結果 | なし |','| 関係する予想・結果 | [C-0012](../conjectures/C-0012.md)、[C-0013](../conjectures/C-0013.md) |')
rep('assumptions/A-0016.md','| 関係する予想・結果 | なし |','| 関係する予想・結果 | [C-0012](../conjectures/C-0012.md) |')
EOF
python3 -m pytest -q tools/tests 2>&1 | grep -oE "[0-9]+ (passed|failed)|AssertionError.*" | head
```

</details>

<details><summary>結果: Bash</summary>

```text
33 passed
```

</details>

## Claude

Now create Issues for C-0009〜C-0013.

<details><summary>ツール: ToolSearch: select:mcp__github__issue_write,mcp__github__list_issues</summary>

```text
（入力の本文は省略。項目: max_results, query）
```

</details>

<details><summary>結果: ToolSearch: select:mcp__github__issue_write,mcp__github__list_issues</summary>

```text
[tool_reference]
[tool_reference]
```

</details>

<details><summary>ツール: mcp__github__list_issues</summary>

```text
（入力の本文は省略。項目: fields, labels, owner, perPage, repo）
```

</details>

<details><summary>結果: mcp__github__list_issues</summary>

```text
{"issues":[{"body":"## 予想\n\n- ファイル: [conjectures/C-0006.md](https://github.com/kittenkiki15/point-free-spacetime/blob/claude/zealous-keller-o7r1sv/conjectures/C-0006.md)（第 09 回の PR がマージされるまでは作業ブランチにある）\n- 優先度: 低（第 09 回にユーザーと相談して決定。ほかの予想の証明に必要になった場合に上げる）\n\n主張の概要：等価原理を課しても、有限な実験の族の事後分布が一点に収束しない場合がある。そのような族の極限は、点なしの空間でしか表せない観測になりうる。\n\n**予想の詳細化（主張の正確な定式化）は今後のタスクとする。** 第 09 回の最初の試みでの検討（保存用のブランチ `archive/session-09-attempt-1`）を、詳細化の参考にする。\n\n## 作業の計画\n\n- [ ] 予想を詳細化する（収束の位相、事前分布、確定性などの条件）\n\n## 進み具合・議論\n\n- 第 09 回（2026-09-29）：予想を登録。","labels":["priority:low","conjecture"],"number":20,"title":"[C-0006] 等価原理の下でも、事後分布が点に収束しない場合がある"},{"body":"## 予想\n\n- ファイル: [conjectures/C-0005.md](https://github.com/kittenkiki15/point-free-spacetime/blob/claude/zealous-keller-o7r1sv/conjectures/C-0005.md)（第 09 回の PR がマージされるまでは作業ブランチにある）\n- 優先度: 低（第 09 回にユーザーと相談して決定。ほかの予想の証明に必要になった場合に上げる）\n\n主張の概要：実際の実験は高々可算個なので、その族の極限で観測量を近似するなら、観測量の空間は（適切な位相で）可分である。点なしの言い方では、可算な基底を持つ。\n\n**予想の詳細化（主張の正確な定式化）は今後のタスクとする。**\n\n## 作業の計画\n\n- [ ] 予想を詳細化する（位相と近似の意味）\n\n## 進み具合・議論\n\n- 第 09 回（2026-09-29）：予想を登録。","labels":["priority:low","conjecture"],"number":19,"title":"[C-0005] 実験から得る可算集合の閉包が、観測量の全体を含む物理的に自然な条件がある"}],"pageInfo":{"hasNextPage":true,"hasPreviousPage":false,"startCursor":"Y3Vyc29yOnYyOpK0MjAyNi0wOS0yOVQwMTo0ODozN1rPAAAAAU80iW8=","endCursor":"Y3Vyc29yOnYyOpK0MjAyNi0wOS0yOVQwMTo0ODozM1rPAAAAAU80h30="},"totalCount":5}
```

</details>

<details><summary>ツール: mcp__github__issue_write</summary>

```text
（入力の本文は省略。項目: body, labels, method, owner, repo, title）
```

</details>

<details><summary>結果: mcp__github__issue_write</summary>

```text
{"id":"5657078006","url":"https://github.com/kittenkiki15/point-free-spacetime/issues/37"}
```

</details>

<details><summary>ツール: mcp__github__issue_write</summary>

```text
（入力の本文は省略。項目: body, labels, method, owner, repo, title）
```

</details>

<details><summary>結果: mcp__github__issue_write</summary>

```text
{"id":"5657078535","url":"https://github.com/kittenkiki15/point-free-spacetime/issues/38"}
```

</details>

<details><summary>ツール: mcp__github__issue_write</summary>

```text
（入力の本文は省略。項目: body, labels, method, owner, repo, title）
```

</details>

<details><summary>結果: mcp__github__issue_write</summary>

```text
{"id":"5657079073","url":"https://github.com/kittenkiki15/point-free-spacetime/issues/39"}
```

</details>

<details><summary>ツール: mcp__github__issue_write</summary>

```text
（入力の本文は省略。項目: body, labels, method, owner, repo, title）
```

</details>

<details><summary>結果: mcp__github__issue_write</summary>

```text
{"id":"5657079564","url":"https://github.com/kittenkiki15/point-free-spacetime/issues/40"}
```

</details>

<details><summary>ツール: mcp__github__issue_write</summary>

```text
（入力の本文は省略。項目: body, labels, method, owner, repo, title）
```

</details>

<details><summary>結果: mcp__github__issue_write</summary>

```text
{"id":"5657080036","url":"https://github.com/kittenkiki15/point-free-spacetime/issues/41"}
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
U='https://github.com/kittenkiki15/point-free-spacetime/issues/'
m={'C-0009':37,'C-0010':38,'C-0011':39,'C-0012':40,'C-0013':41}
p='conjectures/README.md'; s=open(p).read()
for c,n in m.items():
    f=f'conjectures/{c}.md'; t=open(f).read()
    assert '| Issue | 未作成 |' in t
    open(f,'w').write(t.replace('| Issue | 未作成 |',f'| Issue | [#{n}]({U}{n}) |'))
    L=s.split('\n')
    for k,l in enumerate(L):
        if l.startswith(f'| [{c}]'):
            assert l.endswith('| 未作成 |'); L[k]=l[:-len('未作成 |')]+f'[#{n}]({U}{n}) |'
    s='\n'.join(L)
open(p,'w').write(s)
EOF
grep -c "未作成" conjectures/*.md | grep -v ":0"; python3 -m pytest -q tools/tests 2>&1 | tail -1; git add -A; git commit -qm "第 20 回：前提 A-0016（実際の実験は因果的な順序を破らない）と、予想 C-0012・C-0013（可能な実験の因果的な順序と較正の普遍性）を加え、C-0009〜C-0013 の優先度を低にして Issue を作った

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: https://claude.ai/code/[伏せ字]" && git push -q && git log -1 --format=%h
```

</details>

<details><summary>結果: Bash</summary>

```text
33 passed in 0.16s
49c2d9d
```

</details>

## Claude

3 点とも賛成で、その形で登録しました。49c2d9d で push してあり、依存関係の検査（33 件）も通っています。

#### 因果的な順序

**前提 A-0016「実際の実験は因果的な順序を破らない」（作業上）**
- 主張は、各観測で、観測者の時刻の座標の上で、登録の事象が準備の事象より前にない（$`t(σ_e(x_i, y_i)) ≥ t(τ_e(x_i))`$）というものです。
- これは最も弱い形に絞っています。今の $`M_O`$ にはまだ因果構造（光円錐）を入れていないためです。
- 強い形（ある不変な速さを超えてつながらない）は、観測者の取り替えの形（C-0009）が決まった後に述べることにし、未解決の点に記録しました。
- 弱い形にとどめたのは私の判断です。最初から強い形にしたい場合は、お知らせください。

**予想 C-0012「可能な実験は因果的な順序を破らない」**
- A-0016 と同じ形の順序が、可能な実験についても成り立つという予想です。

#### 較正の普遍性
- **A-0013** は、実際の実験についての前提のままにしました。
- **予想 C-0013「可能な実験でも較正の普遍性が成り立つ」** を加え、A-0013 の未解決の点からこの予想を参照するようにしました。

#### 優先度と Issue
C-0009〜C-0013 の優先度をすべて「低」にしました。検証に着手したら、棚卸しして見直します。Issue を作り、`priority:low` と `conjecture` のラベルを付けて、予想ファイルと一覧表に番号を書きました。

| 予想 | Issue |
| --- | --- |
| C-0009 較正の普遍性から、観測者の取り替えはローレンツ変換かガリレイ変換になる | [kittenkiki15/point-free-spacetime#37](https://github.com/kittenkiki15/point-free-spacetime/issues/37) |
| C-0010 比較の実験で取り替えを与える体系では、較正の普遍性は検証できる条件に言い換えられる | [kittenkiki15/point-free-spacetime#38](https://github.com/kittenkiki15/point-free-spacetime/issues/38) |
| C-0011 比較の一周のずれがすべて自明なら、観測者の取り替えは群をなす | [kittenkiki15/point-free-spacetime#39](https://github.com/kittenkiki15/point-free-spacetime/issues/39) |
| C-0012 可能な実験は因果的な順序を破らない | [kittenkiki15/point-free-spacetime#40](https://github.com/kittenkiki15/point-free-spacetime/issues/40) |
| C-0013 可能な実験でも較正の普遍性が成り立つ | [kittenkiki15/point-free-spacetime#41](https://github.com/kittenkiki15/point-free-spacetime/issues/41) |

これで、T-0018 の (A)・(B)・(C) と、今回の追加の論点への対応が一通り終わりました。対話を終えてセッションの終え方に進んでよいか、ご判断ください。

## ユーザー

対話を終えてセッションの終え方に進んでください。

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
import json
f='/root/.claude/projects/-home-user/[ID].jsonl'
for line in open(f):
    d=json.loads(line)
    if d.get('type')=='user' and d.get('timestamp','')>'2026-09-30T17:00' and d.get('timestamp','')<'2026-09-30T17:30':
        c=d['message']['content']
        t=c if isinstance(c,str) else ' '.join(x.get('text','') for x in c if isinstance(x,dict))
        print(d['timestamp'], repr(t[:150]))
EOF
```

</details>

<details><summary>結果: Bash</summary>

```text
2026-09-30T17:20:29.523Z '<task-notification>\n<task-type>queued-remote-notifications</task-type>\n<status>pending</status>\n<summary>1 unread notification (GitHub activity on a s'
2026-09-30T17:20:33.519Z ''
2026-09-30T17:20:37.528Z ''
2026-09-30T17:21:32.712Z "<local-command-caveat>The command below was run directly in Claude Code, not sent to you as a request, and its output goes straight to the user. It's "
2026-09-30T17:21:32.699Z '<command-name>/clear</command-name>\n            <command-message>clear</command-message>\n            <command-args></command-args>'
2026-09-30T17:21:50.350Z '次のセッションを開始してください。'
2026-09-30T17:21:54.105Z ''
2026-09-30T17:22:00.705Z ''
2026-09-30T17:22:04.863Z ''
2026-09-30T17:22:04.948Z ''
2026-09-30T17:22:07.897Z ''
2026-09-30T17:22:10.468Z ''
2026-09-30T17:22:14.035Z ''
2026-09-30T17:22:34.161Z "Stop hook feedback:\n[~/.claude/stop-hook-git-check.sh]: There are 1 unpushed commit(s) on branch 'claude/zealous-keller-o7r1sv'. Please push these cha"
2026-09-30T17:22:40.097Z ''
```

</details>

<details><summary>ツール: Bash</summary>

```text
L=logs/2026-09-30_20_terms-setting-and-agents.md && python3 tools/export_log.py /root/.claude/projects/-home-user/[ID].jsonl $L --title "2026-09-30 第 20 回: 設定への用語の統一と、主体・観測者・装置の使い分け" --redact-file ../point-free-spacetime-private/redactions.txt --since 2026-09-30T17:21:50.350Z && wc -l $L && grep -v -e '^#' -e '^$' ../point-free-spacetime-private/redactions.txt | grep -iFcf - $L; grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[a-z]{2,}|sk-[A-Za-z0-9]{10,}' $L | head -3; grep -n "^## ユーザー" $L | head -3
```

</details>
