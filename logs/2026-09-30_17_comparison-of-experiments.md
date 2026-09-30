# 2026-09-30 第 17 回: 実験の比較と Le Cam の不足度

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> ツールの呼び出しは折りたたんで表示し、個人情報などは伏せ字にしています。

## ユーザー

次のセッションを開始してください。

<details><summary>ツール: Bash: Check repo state and read NEXT.md</summary>

```text
cd /home/user/point-free-spacetime && git status | head -5 && git log --oneline -5 && cat NEXT.md
```

</details>

<details><summary>結果: Bash: Check repo state and read NEXT.md</summary>

```text
On branch claude/zealous-keller-o7r1sv
Your branch is up to date with 'origin/claude/zealous-keller-o7r1sv'.

nothing to commit, working tree clean
09cdc22 PR #33 の第 2 回のレビューに対応：実験の比較の原典 5 件を references.bib に登録し、ほかの手がかりの未確認の注意を戻す
72d447c PR #33 のレビューに対応：実験の比較の原典の書誌情報を roadmap.md の T-0016 の節に移し、NEXT.md からは参照する
ea39a9b 次のセッションを T-0016 の残りから始めることと、実験の比較の原典の入手を NEXT.md に記録する
7578c7c Merge pull request #32 from kittenkiki15/claude/zealous-keller-o7r1sv
5d97ed9 PR #32 のレビューの論点に対応：非公開リポジトリの PR もマージされたらセッションを終える、と手順 6 に明記する
# 次のセッションでやること

最終更新: 2026-09-30（第 16 回セッションの後）

## 状況

- 第 01 回：リポジトリの運用ルールを決め、自動検証（Lean・Python・クロスモデルレビュー）を整えた。
- 第 02 回：点なし位相と論理・様相論理・因果・量子論のつながりを整理し、調査メモ・用語一覧・記号一覧・参考文献一覧を作った（[まとめ](summaries/2026-09-25_02_pointfree-logic.md)）。
- 第 03 回：Heunen–van der Schaaf の 2 本の論文メモを作り、「完備ブール代数の点はアトムと対応する」を Lean で形式化した（[まとめ](summaries/2026-09-25_03_ordered-locales.md)）。
- 第 04 回：第 03 回の結果をユーザーと確認し、論文メモを修正した。検証済みの主張を「結果」として管理する [`results/`](results/README.md) を作った（[まとめ](summaries/2026-09-25_04_review-and-results.md)）。
  - ユーザーの方針：予想の価値の主軸は、数学ではなく**物理学への寄与**（厳密な定義のない物理の概念や主張に数学的な定式化を与えることなど）に置く。
- 第 05 回：最小の長さと操作的な領域の構造について、おもちゃのモデルを多角的に検討した。最小の尺度の入れ方を型 I（小さい領域を捨てる）と型 II（余白に下限を置く）に分け、型 II を「膨張 $`N`$ による余白付きの包含が補間的でないこと」として点なしに表した。文献を調べ、数学の部分は既知と確認して結果 R-0006〜R-0008 に登録し、最初の予想 [C-0001](conjectures/C-0001.md)（優先度：高、[Issue #8](https://github.com/kittenkiki15/point-free-spacetime/issues/8)）を立てた（[まとめ](summaries/2026-09-26_05_minimal-scale.md)、[調査メモ](surveys/2026-09-26_05_subordinat
…（以下 7309 文字を省略）
```

</details>

<details><summary>ツール: Bash: Compare branches with main in both repos</summary>

```text
git fetch -q origin main && git log --oneline -3 origin/main && git merge-base --is-ancestor HEAD origin/main && echo HEAD_IN_MAIN; cd ../point-free-spacetime-private && git status | head -3 && git fetch -q origin main && git log --oneline -3 origin/main && ls papers/
```

</details>

<details><summary>結果: Bash: Compare branches with main in both repos</summary>

```text
41c85e6 Merge pull request #33 from kittenkiki15/claude/zealous-keller-o7r1sv
09cdc22 PR #33 の第 2 回のレビューに対応：実験の比較の原典 5 件を references.bib に登録し、ほかの手がかりの未確認の注意を戻す
72d447c PR #33 のレビューに対応：実験の比較の原典の書誌情報を roadmap.md の T-0016 の節に移し、NEXT.md からは参照する
HEAD_IN_MAIN
On branch claude/zealous-keller-o7r1sv
Your branch is up to date with 'origin/claude/zealous-keller-o7r1sv'.

41db798 Merge pull request #10 from kittenkiki15/claude/zealous-keller-o7r1sv
6a79126 T-0016 の続きのために、実験の比較の文献の PDF を追加する（ユーザーが入手）
5a6b404 Merge pull request #9 from kittenkiki15/claude/zealous-keller-o7r1sv
README.md
amelinocamelia2011.pdf
arntzenius2003.pdf
blackwell1951.pdf
blackwell1953.pdf
blackwell1962.pdf
bombelli2009.pdf
bostelmann2021.pdf
buchholz2001.pdf
casini2002.pdf
caves2002bayes.pdf
caves2002definetti.pdf
choi2008.pdf
connes2021.pdf
connes2022.pdf
dantoni1987.pdf
derudder2020.pdf
diaconis1986.pdf
doplicher1995.pdf
dowker2004.pdf
fewster2016.pdf
fewster2020.pdf
fuchs2009priors.pdf
fuchs2013.pdf
halvorson2001.pdf
halvorson2001rs.pdf
halvorson2001rs_arxiv-v1.pdf
halvorson2002.pdf
heijmans1990.pdf
heunen2009.pdf
heunen2024.pdf
heunen2026.pdf
heunen2026_arxiv-v1.pdf
hossenfelder2006.pdf
hossenfelder2013.pdf
isham1998.pdf
johnstone1983.pdf
jonsson1951.pdf
kleijn2019.pdf
landsman2005.pdf
lecam1964.pdf
miller2018.pdf
morinelli2018.pdf
naaijkens2012.pdf
pomatto2014.pdf
raginsky2011.pdf
schack2001bayes.pdf
shannon1958.pdf
sorkin1993.pdf
sorkin2007.pdf
spitters2014.pdf
vanderschaaf2024.pdf
vovk2023.pdf
```

</details>

## Claude

Both branches are already contained in main. I'll bring the working branches up to date with the latest main.

<details><summary>ツール: Bash: Reset branches to main and read the T-0016 section</summary>

```text
cd /home/user/point-free-spacetime && git checkout -q -B claude/zealous-keller-o7r1sv origin/main && git log --oneline -1; cd ../point-free-spacetime-private && git checkout -q -B claude/zealous-keller-o7r1sv origin/main && git log --oneline -1; cd ../point-free-spacetime && awk '/^### T-0016/,/^### T-0017/' roadmap.md
```

</details>

<details><summary>結果: Bash: Reset branches to main and read the T-0016 section</summary>

```text
41c85e6 Merge pull request #33 from kittenkiki15/claude/zealous-keller-o7r1sv
41db798 Merge pull request #10 from kittenkiki15/claude/zealous-keller-o7r1sv
### T-0016 実験の族の位相と極限の先行研究の調査（第 15 回に追加）

第 15 回に、調査が不足している領域のうち、段階 B（T-0004〜T-0006）の位相と極限に直結するものを一つの調査にまとめた（文献は記憶による。未確認）。

- 統計的実験の比較と収束の理論：Le Cam の不足度と距離、Blackwell の実験の比較、Torgersen。実験の族の極限の位相と距離の候補。第 14 回の概観の「模倣」の順序との対応（[調査メモ](surveys/2026-09-29_14_categorical-overview.md)の 6 節）。
- 操作的な確率論の枠組み：一般化確率論（Hardy、Barrett、Chiribella–D'Ariano–Perinotti）と Ludwig の公理的な量子力学。実験から統計への対応（[D-0001](definitions/D-0001.md)〜[D-0004](definitions/D-0004.md)）の先行研究、状態空間の再構成、有限な実験からの一様構造による完備化（[D-0005](definitions/D-0005.md) の極限の位相）。[C-0003](conjectures/C-0003.md)・[C-0005](conjectures/C-0005.md) との関係。
- ベイズ統計の事後一致性：Doob、Schwartz、Diaconis–Freedman の不一致の例、Ghosal–van der Vaart。[C-0006](conjectures/C-0006.md) の反例と条件、[A-0007](assumptions/A-0007.md) の一致の定理の正確な形（原典の確認は T-0014 と共通）。
- 成果物：調査メモと、T-0004〜T-0006 で決める事項への候補。
- 第 16 回：ユーザーの判断で、事後一致性の領域のうち「A-0007 の一致の定理の正確な形」に重点を置き、本文で定理の仮定と結論を確かめた（[調査メモ](surveys/2026-09-30_16_merging-and-consistency.md)）。結果を A-0007・D-0005 に反映した。残るのは、Le Cam の理論と実験の比較、一般化確率論と Ludwig、弱い併合（Kalai–Lehrer 1994。第 16 回にユーザーの判断で扱わなかった）。
- 第 16 回の後に、ユーザーが実験の比較の原典 5 件を入手し、非公開リポジトリの `papers/` に置いた：`blackwell1951`（Blackwell, Comparison of experiments, Proc. Second Berkeley Symp., 1951）、`blackwell1953`（Blackwell, Equivalent comparisons of experiments, Ann. Math. Statist. 24, 1953）、`lecam1964`（Le Cam, Sufficiency and approximate sufficiency
…（以下 352 文字を省略）
```

</details>

<details><summary>ツール: Bash: Read relevant survey sections for leads</summary>

```text
awk '/^## 8/,0' surveys/2026-09-30_16_merging-and-consistency.md | head -40; echo ----; awk '/^## 6/,/^## 7/' surveys/2026-09-29_14_categorical-overview.md | head -40
```

</details>

<details><summary>結果: Bash: Read relevant survey sections for leads</summary>

```text
## 8. 今後の調査対象

- **弱い併合**（Kalai–Lehrer 1994）：一つ先の予測だけの一致で、絶対連続性より弱い条件で成り立つ（記憶による。未確認。定義と条件の確認は今後の調査事項）。A-0007 を弱められるかの検討に使える（第 16 回ではユーザーの判断で扱わず、まとめで言及するにとどめた）。
- T-0016 の残りの領域（Le Cam の理論、一般化確率論と Ludwig）。
----
## 6. 未確認・今後の課題

- 各文献の本文（定義と定理の正確な形）。特に、マルコフ圏の定義と、関手の間の構造、表現可能なマルコフ圏の条件。
- ブラックウェル–シャーマン–スタインの定理の圏論版が、実験の「模倣」の順序（本表の層 1 の射）とどう対応するか。
- Bohr トポスの内部スペクトルが、実際の観測量（有限な実験の族の極限）から得られるものと両立するか。
- 観測者の取り替えの亜群と、局所共変性（`brunetti2003`）の時空の圏の対応。
- 随伴の候補の検討（PR #29 のレビュー）：T-0009 で、二つの関手の向き（反対圏が要るかを含む）、自然な Hom 集合の対応（または単位・余単位と三角恒等式）を指定し、較正の整合条件がどの同型の条件に対応するかを確かめる。
- 模倣の向き（PR #29 のレビュー）：模倣 $`q = g ∘ p ∘ f`$ に設定の前処理 $`f`$ を含めると、$`f`$ は $`q`$ の始域から $`p`$ の始域へ向かい、射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ の可換な四角形とは向きが一般に合わない。T-0005・T-0006 で模倣の向きを式で固定し、射の圏だけで表せるかを検討する。
- 事後予測の一致の予想の候補（PR #29 のレビュー）：コルモゴロフ積を用意するだけでは、事後分布の極限や事後予測の一致は従わない。何が、どの意味で、どのデータ履歴について収束するか（通常はほとんど確実に）を定め、ド・フィネッティの定理を使うなら交換可能性も別に課す。T-0005・T-0006 で、予想の条件と結論に分けて書く。
- A-0006 を核の連続性として表すときの位相（弱収束か全変動距離か）は、A-0006 の未解決の点（T-0004）で扱う。
```

</details>

## Claude

第 17 回のセッションを始めます。準備と、最初の相談です。

#### 準備
- 両方のリポジトリで、作業ブランチ `claude/zealous-keller-o7r1sv` を最新の `main` から作り直しました（公開側は PR #33、非公開側は PR #10 までが入っています）。
- 非公開リポジトリの `papers/` には、実験の比較の原典 5 件（`blackwell1951`、`blackwell1953`、`lecam1964`、`shannon1958`、`raginsky2011`）がそろっています。

#### 今回のタスク
[`roadmap.md`](roadmap.md) の **T-0016「実験の族の位相と極限の先行研究の調査」の残り**を扱います。残っている領域は次の三つです。

1. **Le Cam の理論と実験の比較（comparison of experiments）**：Blackwell の順序（一方の実験が他方を「模倣」できるか）、Le Cam の不足度（deficiency）と距離。原典 5 件が手元にあります。
   - [D-0005](definitions/D-0005.md) の「有限な実験の族の極限」に使う位相や距離の候補になります。
   - 第 14 回の概観で出た「模倣」の順序の向きの問題（模倣 $`q = g ∘ p ∘ f`$ と射の圏の向きが合わない）にも関係します。
2. **一般化確率論（generalized probabilistic theories）と Ludwig**：実験から統計への対応（D-0001〜D-0004）の先行研究、状態空間の再構成、[C-0003](conjectures/C-0003.md)・[C-0005](conjectures/C-0005.md) との関係。文献は記憶によるもので、まだ確かめていません（arXiv にあるものは私が取得できます）。
3. **弱い併合（weak merging。Kalai–Lehrer 1994）**：[A-0007](assumptions/A-0007.md) の相互絶対連続性を弱められるかの検討。範囲は小さめです。

**私のおすすめは 1 です。** 原典がそろっていて、本文で定理の仮定と結論を確かめられます。また、段階 B（T-0004〜T-0006）で決める極限の位相に一番直結します。やり方は第 16 回と同じで、原典で定義と定理（Blackwell の同値な比較の定理、Le Cam の不足度とランダム化の基準など）を確かめ、調査メモにまとめて、D-0005 と第 14 回の「模倣」の向きの問題への候補を記録する、という形を考えています。

どの領域に重点を置くか（複数でも構いません）と、深さ（本文で定理を確かめるところまでか、要旨の確認にとどめるか）を決めてください。

<details><summary>ツール: Bash: Check ahead/behind status in both repos</summary>

```text
git status -sb | head -1; cd ../point-free-spacetime-private && git status -sb | head -1
```

</details>

<details><summary>結果: Bash: Check ahead/behind status in both repos</summary>

```text
## claude/zealous-keller-o7r1sv...origin/main
## claude/zealous-keller-o7r1sv...origin/main
```

</details>

<details><summary>ツール: Bash: Push updated branches in both repos</summary>

```text
for r in point-free-spacetime point-free-spacetime-private; do cd /home/user/$r && git push -u origin claude/zealous-keller-o7r1sv 2>&1 | tail -2; done
```

</details>

<details><summary>結果: Bash: Push updated branches in both repos</summary>

```text
* [new branch]      claude/zealous-keller-o7r1sv -> claude/zealous-keller-o7r1sv
branch 'claude/zealous-keller-o7r1sv' set up to track 'origin/claude/zealous-keller-o7r1sv'.
 * [new branch]      claude/zealous-keller-o7r1sv -> claude/zealous-keller-o7r1sv
branch 'claude/zealous-keller-o7r1sv' set up to track 'origin/claude/zealous-keller-o7r1sv'.
```

</details>

## Claude

両方のリポジトリで、作業ブランチ `claude/zealous-keller-o7r1sv` を push しました。

push を求められたのは、ブランチを最新の `main` から作り直したことで、リモートにない `main` のマージコミットが入ったためです。PR #33 と非公開側の PR #10 のマージ後に、リモートのブランチは消えていたので、新しいブランチとして作られました。どちらの中身も今の `main` と同じで、新しい変更はまだありません。

先ほどの相談はそのままです。T-0016 の残りのうち、どれに重点を置くかを決めてください。

1. **Le Cam の理論と実験の比較**（おすすめ）：原典 5 件がそろっていて、極限の位相の候補に一番つながります。
2. **一般化確率論と Ludwig**
3. **弱い併合**（Kalai–Lehrer 1994）

あわせて、深さも決めてください。本文で定理の仮定と結論まで確かめるか、要旨を確かめるだけにするかです。

## ユーザー

1 で、本文で定理まで確かめてください。

<details><summary>ツール: Bash: Extract text from the five comparison-of-experiments PDFs</summary>

```text
cd /home/user/point-free-spacetime-private/papers && which pdftotext pdfinfo; for f in blackwell1951 blackwell1953 lecam1964 shannon1958 raginsky2011; do echo "== $f"; pdfinfo $f.pdf 2>/dev/null | grep -E 'Pages|Title'; pdftotext -layout $f.pdf /tmp/claude-0/-home-user/[ID]/scratchpad/$f.txt && wc -w /tmp/claude-0/-home-user/[ID]/scratchpad/$f.txt; done
```

</details>

<details><summary>結果: Bash: Extract text from the five comparison-of-experiments PDFs</summary>

```text
/usr/bin/pdftotext
/usr/bin/pdfinfo
== blackwell1951
Pages:           10
5631 /tmp/claude-0/-home-user/[ID]/scratchpad/blackwell1951.txt
== blackwell1953
Pages:           8
21 /tmp/claude-0/-home-user/[ID]/scratchpad/blackwell1953.txt
== lecam1964
Pages:           37
21 /tmp/claude-0/-home-user/[ID]/scratchpad/lecam1964.txt
== shannon1958
Title:           PII: S0019-9958(58)90239-0
Pages:           8
2720 /tmp/claude-0/-home-user/[ID]/scratchpad/shannon1958.txt
== raginsky2011
Title:           Shannon Meets Blackwell and Le Cam: Channels, Codes, and Statistical Experiments
Pages:           5
4572 /tmp/claude-0/-home-user/[ID]/scratchpad/raginsky2011.txt
```

</details>

<details><summary>ツール: Bash: Read Blackwell 1951 text</summary>

```text
cat /tmp/claude-0/-home-user/[ID]/scratchpad/blackwell1951.txt
```

</details>

<details><summary>結果: Bash: Read Blackwell 1951 text</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

<details><summary>ツール: Read: /root/.claude/projects/-home-user/[ID]/tool-results/blhtfa1w1.txt</summary>

```text
（入力の本文は省略。項目: file_path）
```

</details>

<details><summary>結果: Read: /root/.claude/projects/-home-user/[ID]/tool-results/blhtfa1w1.txt</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

## Claude

Blackwell 1951 は本文を読みました。次に、スキャン版の Blackwell 1953 を読みます。

<details><summary>ツール: Read: /home/user/point-free-spacetime-private/papers/blackwell1953.pdf</summary>

```text
（入力の本文は省略。項目: file_path, pages）
```

</details>

<details><summary>結果: Read: /home/user/point-free-spacetime-private/papers/blackwell1953.pdf</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

## Claude

Blackwell 1953 も読みました。次は Le Cam 1964（37 ページ）です。

<details><summary>ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（入力の本文は省略。項目: file_path, pages）
```

</details>

<details><summary>結果: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

<details><summary>ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（入力の本文は省略。項目: file_path, pages）
```

</details>

<details><summary>結果: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

<details><summary>ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（入力の本文は省略。項目: file_path, pages）
```

</details>

<details><summary>結果: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

<details><summary>ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（入力の本文は省略。項目: file_path, pages）
```

</details>

<details><summary>結果: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

## Claude

Le Cam 1964 を読み終えました。続けて、Shannon 1958 と Raginsky 2011 を読みます。

<details><summary>ツール: Bash: Read Shannon 1958 text</summary>

```text
cat /tmp/claude-0/-home-user/[ID]/scratchpad/shannon1958.txt
```

</details>

<details><summary>ツール: Bash: Read Raginsky 2011 text</summary>

```text
cat /tmp/claude-0/-home-user/[ID]/scratchpad/raginsky2011.txt
```

</details>

<details><summary>結果: Bash: Read Shannon 1958 text</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

<details><summary>結果: Bash: Read Raginsky 2011 text</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

<details><summary>ツール: Read: /root/.claude/projects/-home-user/[ID]/tool-results/b8w9b84gi.txt</summary>

```text
（入力の本文は省略。項目: file_path）
```

</details>

<details><summary>結果: Read: /root/.claude/projects/-home-user/[ID]/tool-results/b8w9b84gi.txt</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。要旨は surveys/2026-09-30_17_comparison-of-experiments.md を参照）
```

</details>

## Claude

5 件をすべて読みました。報告の前に、プロジェクト側の対応箇所（D-0005 と、第 14 回の「模倣」）を確かめます。

<details><summary>ツール: Bash: Read D-0005 and find mimicry references</summary>

```text
cd /home/user/point-free-spacetime && cat definitions/D-0005.md; grep -n "模倣" -r surveys/2026-09-29_14_categorical-overview.md definitions assumptions conjectures roadmap.md | head -30
```

</details>

<details><summary>結果: Bash: Read D-0005 and find mimicry references</summary>

```text
# D-0005: 実際の観測量

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 観測量 |
| 依存する ID | [D-0002](../definitions/D-0002.md)、[D-0004](../definitions/D-0004.md)、[A-0007](../assumptions/A-0007.md) |
| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0005](../conjectures/C-0005.md)、[C-0006](../conjectures/C-0006.md) |
| 初出 | [2026-09-29 第 09 回](../summaries/2026-09-29_09_actual-and-possible-observables.md) |

## 定義

**実際の観測量**は、実際の実験の族の極限として得られる観測量である。

- **実際の実験の族**：実際に行われた実験（[D-0002](D-0002.md)）の列から作る部分列で、指定した空間で収束するもの。
- **極限**：有限な実験の族の各段階に、それまでのデータによる推定の事後分布を対応させる。族の極限で事後分布が一点に集中するとき、その点を族の極限の観測量とする。

## 注意

- 事後分布を置く空間は、作業上は応答関数（[D-0004](D-0004.md)）の空間と読む。
- 実験が有限個しかない段階では、実際の観測量はまだ定まらず、有限個のデータによる事後分布だけが得られる。実際の観測量が空でないこと（実験の無限列と、その収束する部分列があり、その族で事後分布が一点に集中すること）は、観測量の時空を再構成するための前提になる（[C-0002](../conjectures/C-0002.md)）。
- 事前分布から決まる予測分布どうしの相互絶対連続性（[A-0007](../assumptions/A-0007.md)）から得られるのは、将来のデータの予測の一致だけである。極限の観測量が事前分布によらないことには、識別可能性と、推定の対象への事後分布の集中が別に要る。
- 先行例：QBism の量子状態の断層撮影の読み替え（Caves–Fuchs–Schack 2002 など）では、情報的に完全な測定が識別可能性を与え、交換可能性と事前分布の正値性の下で、測っていない観測量の予測まで主体の間で一致するとされる（確認した範囲の文献では証明を見つけられなかった。第 16 回に、有限次元で結果が有限個の場合について、固定した真の状態が事前分布の台に入れば事後分布がその状態に集中することを、Schwartz の定理の当てはめとして確かめた。QBism の「データが指す状態」の定め方との対応は確かめていない。[第 16 回の調査メモ](../surveys/2026-09-30_16_merging-and-consistency.md)の 5.1 節。Claude の補足）。情報的に完全でない測定（例えば $`σ_z`$ だけの測定）では、測っていない $`σ_x`$ の予測に事前分布への依存が残る（Schack–Brun–Caves 2001）。[第 15 回の調査メモ](../surveys/2026-09-29_15_qbism-agreement.md)の 2.4・2.5・3.2 節。

## 未解決の点

- 極限の位相
…（以下 2038 文字を省略）
```

</details>

<details><summary>ツール: Bash: Skim related definitions, assumptions, conjectures</summary>

```text
for f in assumptions/A-0006.md assumptions/A-0007.md definitions/D-0001.md definitions/D-0004.md conjectures/C-0003.md conjectures/C-0005.md conjectures/C-0006.md; do echo "== $f"; sed -n '1,25p' $f | grep -v '^$' | head -22; done
```

</details>

<details><summary>結果: Bash: Skim related definitions, assumptions, conjectures</summary>

```text
== assumptions/A-0006.md
# A-0006: 実験の等価原理（連続性の形）
| 項目 | 値 |
| --- | --- |
| 状態 | 採用 |
| 層 | 実験 |
| 依存する ID | [D-0003](../definitions/D-0003.md)、[D-0004](../definitions/D-0004.md) |
| 関係する予想・結果 | [C-0006](../conjectures/C-0006.md) |
| 初出 | [2026-09-29 第 09 回](../summaries/2026-09-29_09_actual-and-possible-observables.md) |
## 主張
同一の実験プロトコルでは、実験パラメータが近ければ、結果の統計も近い。つまり、各プロトコル $`π`$ について、応答関数（[D-0004](../definitions/D-0004.md)）の写像 $`p_π : X_π → \mathrm{Prob}(Y_π)`$ は連続である。
## 採用の理由
ユーザーの提案は、「同一の実験プロトコルと実験パラメータの組で行った観測の結果の統計は、物理的に区別がつかない」というものである（第 09 回）。ただし、実数値のパラメータは任意の設定値を厳密に再現できるとは限らないので、近い設定どうしを比べられるように、連続性の形にした（ユーザーが同意）。なお、$`X`$ が異なる実験を比べる共通の添字の空間になるのは、$`X`$ の作り方（[D-0003](../definitions/D-0003.md)）によるもので、この前提の帰結ではない。異なるプロトコルの結果を比べるには、共通の空間への写像が別に要る（下の未解決の点）。
## 注意
- 同一のパラメータで統計が同じことから、連続性は論理的には従わない（閾値で統計が切り替わる模型は、前者を満たすが後者を満たさない）。連続性は追加して採用する仮定である。
- 等価原理は、結果の列の交換可能性を含まない。de Finetti の定理などを使うには、同時分布についての仮定が別に要る。
- この等価原理を前提として課すのか、プロトコルの形式化から定理として導くのかは、研究課題である（[C-0004](../conjectures/C-0004.md)）。
- 一般相対論の等価原理とは別のものである。
== assumptions/A-0007.md
# A-0007: 事前分布から決まる予測分布どうしの相互絶対連続性
| 項目 | 値 |
| --- | --- |
| 状態 | 採用 |
| 層 | 観測量 |
| 依存する ID | [D-0004](../definitions/D-0004.md) |
| 関係する予想・結果 | なし |
| 初出 | [2026-09-29 第 09 回](../summaries/2026-09-29_09_actual-and-possible-observables.md) |
## 主張
異なる主体の事前分布から決まる、無限のデータ列の上の予測分布どうしは、互いに絶対連続である。
条件を課すのは予測分布であって、事前分布そのものではない。例えば、互いに特異な二つの事前分布でも、それぞれが集中するパラメータが同じデータの分布を与えるなら、予測分布は一致する。
## 採用の理由
実際の観測量（[D-0005](../definitions/D-0005.md)）の
…（以下 7345 文字を省略）
```

</details>

## Claude

5 件の原典（Blackwell 1951・1953、Le Cam 1964、Shannon 1958、Raginsky 2011）を読み終えました。本文で確かめた定理の仮定と結論を報告します。そのうえで、プロジェクトへのつながりの候補を挙げます。候補は私の見立てで、原典に書いてあることではありません。

#### 1. 原典で確かめたこと

##### Blackwell 1951「Comparison of experiments」
- **実験の定義**：可測空間 $`(X, \mathcal{B})`$ の上の $`N`$ 個の確率測度 $`u_1, …, u_N`$ の組。パラメータの集合は有限です。
- **情報量の多さ $`α ⊃ β`$**（Bohnenblust–Shapley–Sherman による）：すべての決定問題（$`ℝ^N`$ の有界な損失ベクトルの集合 $`A`$）で、$`β`$ で達成できる損失ベクトルが $`α`$ でも達成できること。
  - 定理 2：この順序は、すべての事前分布でのベイズ・リスクの比較などと同値です。
- **標準実験**（定理 3）：一様な事前分布の下での事後分布 $`p(x)`$ の分布を**標準測度**（standard measure）と呼びます。実験は、自分の標準実験と同値です。
  - 標準測度は、単体の上の確率測度で重心が $`(1/N, …, 1/N)`$ のものと、一対一に対応します。
- **定理 4**（BSS による）：$`M ⊃ m`$ と、すべての連続な凸関数 $`g`$ について $`\int g\,dM ≥ \int g\,dm`$ が成り立つことは同値です。
- **十分性 $`α ≻ β`$**：マルコフ核による後処理で、$`β`$ の $`N`$ 個の分布をすべて再現できること。
  - 定理 6：平均を保つ核（$`\int p\,D(p^*, dp) = p^*`$）で $`M = Dm`$ と書けることと同値です。
  - 定理 8：$`≻ ⇒ ⊃`$ が成り立ちます。
  - 定理 10：$`N = 2`$ に限り、逆も示しています。一般の $`N`$ での逆は、この論文では未解決のまま残されています。
- **定理 9**：核の無限列の合成が収束することを、Doob のマルチンゲール収束定理で示しています。
- **定理 12**：独立な実験の組み合わせは $`≻`$ を保ちます。一方、$`(α, α) ≻ (β, β) ⇒ α ≻ β`$ かどうかは未解決の問いとして残されています。

##### Blackwell 1953「Equivalent comparisons of experiments」
- 定理 6（Sherman–Stein の定理）：結果が有限個の場合に $`P ⊃ Q ⇒ P ≻ Q`$ が成り立ちます（$`Q = PM`$ となるマルコフ行列 $`M`$ がある）。証明は、鞍点（ミニマックス）を使った新しいものです。
- **定理 8**：有限個の結果という制限を外しています。$`ℝ^n`$ の有界集合の上の測度で、凸順序が平均を保つ核の存在を導きます。
  - 証明は、有限集合への近似と、Doob のマルチンゲール定理とコルモゴロフの拡張定理によります。
  - これにより、パラメータが有限個なら、任意の実験で $`⊃ ⇔ ≻`$ が成り立ちます。1951 年の未解決の問いが解けたことになります。
- 5 節の **$`k`$ 決定問題 $`⊃_k`$**：
  - 定理 9 は、その三つの同値な形を示しています。
  - すべての $`k`$ で $`⊃_k`$ なら $`≻`$ です。
  - 一般には $`⊃_{k+1}`$ は $`⊃_k`$ より真に強い（Stein の未発表の結果として紹介）。
  - 定理 10：$`n = 2`$ なら $`⊃_2 ⇒ ≻`$ です。
  - 系：二者択一の場合は、第一種と第二種の誤りの曲線の比較と同値です。

##### Le Cam 1964「Sufficiency and approximate sufficiency」
- **実験の定義 1**：$`\{Θ, E, 𝔛, \{P_θ\}\}`$ の組です。
  - $`E`$ は $`𝔛`$ の上の有界関数のベクトル束で、定数 1 を含み、上限ノルムで完備なものです。
  - $`P_θ`$ は、$`E`$ の上の正で正規化された線形汎関数です。**σ 加法性は仮定しません**。
- **L 空間と M 空間**：L 空間は、$`E^*`$ の中で $`\{P_θ\}`$ を含む最小のバンドです。M 空間はその双対です。
  - 命題 4：M 空間は、コンパクト・ハウスドルフ空間 $`Z`$ の上の $`C(Z)`$ と同型です（Gelfand–Kakutani–Stone の表現）。
  - 4 節の終わりで、Le Cam は「集合 $`𝔛`$ と束 $`E`$ は実質的な役割を果たさず、定理は L 空間・M 空間と汎関数の族についての定理である」と述べています。
- **無作為化**（randomization。定義 6）：$`F × L`$ の上の、正で正規化された双線形関数です。有限な台を持つものが稠密です（定理 1）。
- **定理 3**（主定理。近似版のブラックウェル–シャーマン–スタインの定理）：次の四つは同値です。$`ε(θ) = 0`$ の場合が、Blackwell–Sherman–Stein の定理にあたります。
  1. ある無作為化 $`M`$ で、すべての $`θ`$ について $`\|MP_θ − Q_θ\| ≤ ε(θ)`$。
  2. $`𝓔`$ は $`𝓕`$ に対して $`ε`$ 不足（ε-deficient）：損失関数のノルムが $`\|W\|`$ のすべての決定問題（有限次元の凸でコンパクトな決定の空間の類 $`𝔇`$）で、有限な台の事前分布 $`μ`$ ごとに、$`𝓕`$ の手続きのリスクを $`\|W\| \int ε\,dμ`$ の範囲で再現できる。
  3. 2 と同じことを、ベイズ・リスクの包絡線の不等式で書いたもの。
  4. 2 と同じことを、事前分布ごとの手続きの存在で書いたもの。
- **定義 9**：不足度（deficiency）は $`δ(𝓔, 𝓕) = \inf_M \sup_θ \|MP_θ − Q_θ\|`$ です。$`Δ = \max(δ(𝓔,𝓕), δ(𝓕,𝓔))`$ は、**同じパラメータの集合 $`Θ`$ を持つ実験の上の擬距離**になります。
  - 標本空間は、実験ごとに違ってかまいません。
  - 本文の定義 9 では和 $`δ(𝓔,𝓕) + δ(𝓕,𝓔)`$ を $`Δ`$ としていますが、7 節では最大値で定義し直しています。どちらでも同じ擬距離の位相を与えます。
- **命題 12 の系**：二つの実験が同値であることは、$`\{P_θ\}`$ と $`\{Q_θ\}`$ が張る線形空間が等長であることと同値です（$`P_θ ↔ Q_θ`$ の対応による）。
- **命題 13**：$`δ(𝓔, 𝓕) = 0`$ は、$`𝓔`$ と $`𝓕`$ を周辺に持つ結合実験があり、その中で $`𝓔`$ が十分な部分実験になることと同値です。
- **6 節**：σ 加法的な結合分布を作るには、正則性が要ります。二つの実験が同値なのに結合分布が存在しない反例として、ルベーグ外測度が 1 の互いに補集合な 2 集合の例を挙げています。
- **7 節（統計の概念の安定性）**：
  - 安定性の原理：「観測でほとんど検出できない族の違いは、最適な手続きの選択を大きく変えるべきでない」。
  - 手法の安定性を、$`Δ`$ についての一様連続性として定義しています。
  - 十分性の原理とベイズの原理（平均の距離の場合）は安定で、最尤法は不安定です。
- **命題 17**：統計量が確率収束すれば、相対コンパクトなパラメータの集合の上で不足度は 0 に近づきます。

##### Shannon 1958「A note on a partial ordering for communication channels」
- **チャネルの包含 $`K_1 ⊇ K_2`$**：前処理 $`R_α`$ と後処理 $`T_α`$ の組を確率 $`g_α`$ で混ぜて、$`\sum_α g_α R_α K_1 T_α = K_2`$ と書けること。
  - 送信側と受信側で乱数を共有することを許しています。
  - 前処理と後処理は、純粋な（決定的な）チャネルに限ってもかまいません。
- **性質**：推移的で、チャネルの和と積で保たれます。包含されるチャネルの集合は凸です。
- **定理**：$`K_1 ⊇ K_2`$ なら、$`K_2`$ の符号と同じか、それより誤り確率の小さい符号が $`K_1`$ にあります。したがって、容量も $`K_1`$ の方が大きいか等しくなります。
- 2 入力 2 出力のチャネルでは、この順序は束になります。一般の場合は未解決です。

##### Raginsky 2011「Shannon meets Blackwell and Le Cam」
- **見方**：統計的実験は「入力を符号化しないチャネル」です。
  - Blackwell 十分性は、同じ入力で $`W' = TW`$ と書けること（後処理だけ）です。
  - Shannon 十分性は、前処理と後処理の組の凸結合です。
  - 入力が同じなら、Blackwell 十分性から Shannon 十分性が従います。逆は必ずしも成り立ちません。
- **Shannon 不足度 $`δ_S`$** を、Le Cam の不足度にならって定義しています。
  - 定理 1：$`δ_S(W, W') ≤ ε'`$ なら、$`W'`$ の $`(M, ε)`$ 符号から、$`W`$ の $`(M, ε+ε')`$ 符号が作れます。
- **定理 2**：Le Cam の不足度は、データ処理について単調です。
- **一般化**：データ処理不等式を満たす任意のダイバージェンスで、不足度の一般化が作れます。相対エントロピーで作ると、容量との関係が得られます（定理 6）。

#### 2. プロジェクトへのつながり（見立て。私の補足）

1. **D-0005 の未解決の点「実験そのものを共通の空間の元とみなす方法」への答えの候補**
   - Le Cam の不足度は、標本空間（本プロジェクトの結果の空間 $`Y_π`$）が異なる実験を、パラメータの集合 $`Θ`$ が共通であるというだけで比べられます。
   - $`Δ = 0`$ で割った「実験の型」の空間は、距離空間になります。
   - ここで、$`Θ`$ を推定の対象（応答関数やモデル）の空間と読むと、プロトコルが違う実験を一つの空間に置けます。
2. **「実験の列」と「事後分布の列」のどちらを収束させるか**
   - $`Θ`$ が有限なら、実験の型は標準測度（事後分布の分布）と一対一に対応します（Blackwell 1951 の定理 3）。そのため、二つの選択肢は同じものの二つの見方になります。
   - データを増やす族は、Blackwell の順序で単調に増えます（1951 年の定理 12）。
   - 事後分布はマルチンゲールなので、ほとんど確実に収束し、極限の実験の標準測度はその極限の分布になります（1951 年の定理 9 と同じ論法）。
   - 「事後分布が一点に集中する」ことは、極限の標準測度が単体の頂点に集中すること、つまり完全に情報的な実験になることと同じです。
   - 上の三つは、$`Θ`$ が有限の場合の私の検算です。有限でない $`Θ`$ への拡張と、$`Δ`$ の収束と標準測度の弱収束の関係は、記憶によるもので未確認です。
3. **第 14 回の「模倣」の向きの問題**
   - 模倣 $`q = g ∘ p ∘ f`$ は、Shannon の包含（前処理と後処理）の、乱数の共有がない場合にあたります。
   - これは、射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ ではなく、**ねじれ射の圏**（twisted arrow category）$`\mathrm{Tw}(\mathsf{Stoch})`$ の射の形そのものです。この圏の射 $`p → q`$ は、$`q = g ∘ p ∘ f`$ を満たす組 $`(f, g)`$ です。こう読めば、向きの食い違いは解消します。
   - 共有乱数を許すと凸結合が入るので、単一の射ではなく、射の凸包で表すことになります。
   - Blackwell の順序（後処理だけ）は、設定を固定した場合にあたります。
   - この対応は私の補足で、文献では確かめていません。
4. **Le Cam の実験の定義と、プロジェクトの構想の対応**
   - Le Cam は、標本空間の点を使わず、関数の束と汎関数（期待値）だけで実験を定義しています。そのうえで、標本空間を $`C(Z)`$ のスペクトルとして再構成しています。
   - これは、第 07 回のユーザーの構想（観測量の代数から空間を再構成する）と同じ型の構成です。
5. **Le Cam の安定性の原理と A-0006**
   - Le Cam の安定性の原理は、A-0006（実験の等価原理の連続性の形）の、統計の側での類例に見えます。
   - 違いは、A-0006 は設定についての連続性で、Le Cam は実験の族についての連続性だという点です。

#### 相談したいこと
次に進む前に、次の 3 点について判断をください。

1. 上の報告の内容について、疑問点や、掘り下げたい点はありますか。
2. このあと調査メモ（`surveys/2026-09-30_17_comparison-of-experiments.md`）に、1 節の確認内容と 2 節の候補をまとめる進め方でよいですか。2 節の候補は、D-0005 の未解決の点や、第 14 回の模倣の向きの論点に、候補として記録するつもりです。
3. 2 節の中で、今回もう少し踏み込みたいものはありますか。例えば、2 の有限な $`Θ`$ の場合の検算を調査メモに証明の形で書く、3 のねじれ射の圏の読み替えを式で確かめる、といったことができます。

## ユーザー

まずは、2 を実施して、本セッションを終えたいと思います。マージ後、2 の調査メモを確認し、そのあと次回以降のセッションで 1 や 3 を実施したいと思います。

## Claude

承知しました。調査メモを書き、セッションの終え方の手順に進みます。まず、書式を確かめます。

<details><summary>ツール: Bash: Read summary format and previous summary/survey</summary>

```text
cat summaries/README.md; echo ======; cat summaries/2026-09-30_16_merging-and-consistency.md; echo =====; sed -n '1,40p' surveys/2026-09-30_16_merging-and-consistency.md; ls surveys
```

</details>

<details><summary>結果: Bash: Read summary format and previous summary/survey</summary>

````text
# 対話のまとめ

各セッションの内容を整理したものです。ファイル名は [`logs/`](../logs/) の対話ログと同じです。

## 書式

```markdown
# YYYY-MM-DD 第 NN 回: <話題>

- 対話ログ: [logs/YYYY-MM-DD_NN_<話題>.md](../logs/YYYY-MM-DD_NN_<話題>.md)

## 要約
## 決定事項
## 得られた結果（検証済み）
## 新しい予想
## 未解決の論点
## 次にやること
```

検証済みの結果と、予想・推測とは、はっきり区別して書きます。
======
# 2026-09-30 第 16 回: 主体の間の一致と事後一致性

- 対話ログ: [logs/2026-09-30_16_merging-and-consistency.md](../logs/2026-09-30_16_merging-and-consistency.md)
- 調査メモ: [surveys/2026-09-30_16_merging-and-consistency.md](../surveys/2026-09-30_16_merging-and-consistency.md)

## 要約

ロードマップの T-0016「実験の族の位相と極限の先行研究の調査」を扱った。ユーザーの判断で、事後一致性の領域のうち「A-0007 の一致の定理の正確な形」に重点を置き、本文で定理の仮定と結論を確かめた。

- 前半は、Blackwell–Dubins 1962 の原典が取得できなかった。そのため二次文献（Pomatto–Al-Najjar–Sandroni 2014、Vovk 2023）で一致の定理を読み、事後一致性の定理（Miller 2018 の Doob の定理、Choi–Ramamoorthi 2008 と Kleijn–Zhao の Schwartz の定理）も読んだ。
- 後半は、ユーザーが入手した原典（Blackwell–Dubins 1962、Diaconis–Freedman 1986）を確かめた。そのうえで、前半に Claude が挙げた補足を証明の形で確かめ、A-0007 に反映した。

あわせて、次の三つを行った。

- 用語「主体」「観測者」「装置」の使い分けを、新しいタスク T-0018 として記録した。
- A-0001（実際の実験の可算性）の背景を記録した。
- 第 15 回の調査メモの数式（ケット）の表示の乱れを直した。

## 決定事項

- T-0016 の重点と深さ（上記。ユーザーの判断）。
- 進め方（ユーザーの判断）：
  - (a) 補足の検算を先に行い、次に (c) A-0007 への反映に移る。
  - (b) 弱い併合（Kalai–Lehrer 1994）は、このまとめで言及するにとどめる（下の「未解決の論点」）。
- A-0007 に新しく加えた論点（前提を相互の絶対連続性とするか片側とするか、フレームワークで採る一致の段階）は、今回は決めず、未解決の点として次に回した（ユーザーの判断）。ロードマップの T-0005 にも記録した。
- 新しいタスク T-0018「主体・観測者・装置の使い分け」を、T-0016 の次（段階 B の前）に置いた（Claude の提案に、ユーザーが賛成）。
  - 進め方は、既存研究での使われ方の調査をしてから、プロジェクト内の意味を決める。
- A-0001 の主張は変えず、背景と論
…（以下 5678 文字を省略）
````

</details>

<details><summary>ツール: Bash: Check survey index, bib entries, glossary terms</summary>

```text
cat surveys/README.md | tail -20; grep -n -A8 -E "@.*\{(blackwell1951|blackwell1953|lecam1964|shannon1958|raginsky2011|fritz2023representable|torgersen)" references.bib | head -80; grep -n -i -E "ブラックウェル|Blackwell|不足度|deficiency|マルコフ核|十分統計|標準測度|ねじれ" glossary.md symbols.md | head
```

</details>

<details><summary>結果: Bash: Check survey index, bib entries, glossary terms</summary>

````text
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
## 関連する予想・用語
```

他者の文章の長い引用は書かず、要約します。
670:@article{fritz2023representable,
671-  author  = {Fritz, Tobias and Gonda, Tom\'{a}\v{s} and Perrone, Paolo and Rischel, Eigil Fjeldgren},
672-  title   = {Representable {M}arkov categories and comparison of statistical experiments in categorical probability},
673-  journal = {Theoretical Computer Science},
674-  volume  = {961},
675-  pages   = {113896},
676-  year    = {2023},
677-  doi     = {10.1016/j.tcs.2023.113896},
678-  eprint  = {2010.07416},
--
831:@inproceedings{blackwell1951,
832-  author    = {Blackwell, David},
833-  title     = {Comparison of experiments},
834-  booktitle = {Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability},
835-  editor    = {Neyman, J.},
836-  pages     = {93--102},
837-  publisher = {University of California Press},
838-  address   = {Berkeley},
839-  year      = {1951},
--
843:@article{blackwell1953,
844-  author  = {Blackwell, David},
845-  title   = {Equivalent comparisons of experiments},
846-  journal = {The Annals of Mathematical Statistics},
847-  volume 
…（以下 2932 文字を省略）
````

</details>

<details><summary>ツール: Bash: Inspect glossary headers and symbols table</summary>

```text
sed -n '1,8p' glossary.md; cut -d'|' -f2 glossary.md | sed -n '5,200p' | tr '\n' ';'; echo; head -20 symbols.md; grep -c . symbols.md
```

</details>

<details><summary>結果: Bash: Inspect glossary headers and symbols table</summary>

```text
# 用語一覧

英語の原語を併記しています。項目は英語の原語のアルファベット順です。

| 英語 | 日本語 | 説明 | 初出 |
| --- | --- | --- | --- |
| actual observable | 実際の観測量 | 実際に行われた実験（高々可算個）の族の極限として定める観測量（第 09 回の作業上の定義の案）。実際の観測量から「観測量の時空」を再構成する。可能な観測量と区別する。本プロジェクトの定義は [D-0005](definitions/D-0005.md)。 | [第 09 回のまとめ](summaries/2026-09-29_09_actual-and-possible-observables.md) |
| atom | アトム | 束で、0 のすぐ上にある元（0 と自分の間に他の元がない元）。完備ブール代数の点は、アトムと一対一に対応する。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
 英語 ; --- ; actual observable ; atom ; Bayesian inversion ; causal coverage ; causal hull ; causal site ; completely prime filter ; conjugate operators ; contact algebra ; coupling region ; de Vries algebra ; dilation ; distal split property ; domain of dependence ; dual adjunction ; Egli–Milner order ; equivalence principle (of experiments) ; erosion ; exchangeability ; experimental spacetime ; finiteness of experiments ; frame ; functorial semantics ; geometric logic ; Giry monad ; Grothendieck topology ; Heyting algebra ; ideal measurement ; impossible measurement ; inclusion with margin ; induced observable ; informationally complete measurement ; infrared scale ; interpolation (of a relation) ; intuitionistic logic ; isotony ; Kochen–Specker theorem ; Kullback–Leibler support ; locale ; localic cones ; locality ; localization ; macroscopic observable ; Markov category ; merging of opinions ; modal logic S4 ; nuclearity ; nucleus ; observational spacetime ; observer independence ; occupied region (of an apparatus) 
…（以下 1895 文字を省略）
```

</details>

<details><summary>ツール: Bash: List symbol sections</summary>

```text
grep -n '^## ' symbols.md; awk '/^## 確率/,0' symbols.md | head -30
```

</details>

<details><summary>結果: Bash: List symbol sections</summary>

```text
9:## 順序と束
25:## 位相とロケール
37:## 圏論
44:## 様相論理・時制論理
54:## 時空の因果構造
66:## 順序付きロケールと因果被覆
77:## 最小の尺度と余白付きの包含
91:## 測定と観測者の族
```

</details>

<details><summary>ツール: Bash: Read category and measurement symbol sections</summary>

```text
sed -n '37,44p;91,200p' symbols.md
```

</details>

<details><summary>結果: Bash: Read category and measurement symbol sections</summary>

```text
## 圏論

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`F ⊣ G`$ | F は G の左随伴 | 順序集合の間の単調写像では $`F(a) ≤ b ⟺ a ≤ G(b)`$（ガロア接続）。圏の間の関手では、射の集合の自然な全単射 $`\mathrm{Hom}(F(a), b) ≅ \mathrm{Hom}(a, G(b))`$ | 順序集合の写像: `GaloisConnection F G`。関手: `F ⊣ G`（`CategoryTheory.Adjunction`） | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| $`𝒞^{\mathrm{op}}`$ | 𝒞 の反対圏 | 射の向きを逆にした圏 | `𝒞ᵒᵖ` | [調査 02](surveys/2026-09-25_02_pointfree-topology-basics.md) |

## 様相論理・時制論理
## 測定と観測者の族

| 記号 | 読み方 | 意味 | Lean | 初出 |
| --- | --- | --- | --- | --- |
| $`K`$ | 結合領域 | 系とプローブを相互作用させるコンパクトな時空の領域（Fewster–Verch） | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`ε_σ(B)`$ | 誘導される観測量 | プローブの初期状態 $`σ`$ とプローブの観測量 $`B`$ から誘導される系の観測量 | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`O`$ | 観測者側のデータ | 区別を行う側のデータ（結合領域、プローブの理論と結合、初期状態、観測量、使える資源、観測者の世界線の区間の両端の事象 $`p`$・$`q`$ など）。時間の向きを保つポアンカレ変換 $`g`$ で $`g\,O`$ に移る | | [NEXT.md](NEXT.md)（第 05 回の後）、[調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`T_O`$、$`N_O`$ | 観測者ごとの関係・膨張 | 観測者側のデータ $`O`$ を添字にした族。族の共変性は $`N_{gO}(g\,a) = g\,N_O\,a`$ | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`η`$ | ラピディティ | ブーストの大きさを表すパラメータ（ローレンツ因子は $`\cosh\,η`$） | | [調査 06](surveys/2026-09-26_06_minimal-length-covariance.md) |
| $`ℓ`$、$`R_O`$ | 紫外の下限、赤外の上限 | $`ℓ`$ は、実現できる領域の族に課す候補の許容条件の尺度（たとえば「領域が固有時間 $`ℓ`$ 以上の因果ダイヤモンドを含む」。最小の分解能とみなせるかは未検証）。$`R_O`$ は、観測者 $`O`$ が使える時空領域（有限な世界線の区間の両端の事象を頂点とする因果ダイヤ
…（以下 1597 文字を省略）
```

</details>

<details><summary>ツール: Bash: Find mimicry definition in session 14 files</summary>

```text
grep -n "模倣\|q = g" surveys/2026-09-29_14_categorical-overview.md summaries/2026-09-29_14_categorical-overview.md | head; grep -n -i "fritz2023representable" -r surveys summaries | head -5
```

</details>

<details><summary>結果: Bash: Find mimicry definition in session 14 files</summary>

```text
surveys/2026-09-29_14_categorical-overview.md:39:| 層 1：実験（D-0001〜D-0003） | プロトコル $`π`$（設定の空間 $`X_π`$ と結果の空間 $`Y_π`$ の組） | 実験の模倣：設定の変換と、結果の後処理の組 | 設定の空間の直和 $`X = ⨆_π X_π`$（D-0003）は、余積にあたる | 統計的実験の比較（`fritz2023representable`） |
surveys/2026-09-29_14_categorical-overview.md:40:| 層 1〜2：応答関数（D-0004） | 可測空間 | マルコフ核 | 応答関数 $`p_π : X_π → Y_π`$ は $`\mathsf{Stoch}`$ の**射**である。一つのモデルを関手とみなすには、プロトコルを射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ の対象 $`p_π`$ に送り、模倣を可換な四角形に送る、などの型の決め方が要る（候補。模倣に要求する可換性はまだ決めていない） | マルコフ圏（`fritz2020`）、ジリー・モナドのクライスリ圏（`giry1982`） |
surveys/2026-09-29_14_categorical-overview.md:53:- 一つのモデル（状態と装置のモデルを一つ決めたもの）は、プロトコル $`π`$ に応答関数 $`p_π`$（$`\mathsf{Stoch}`$ の射）を対応させる。これを関手とみなすには、終域を射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$（対象は射、射は可換な四角形）に取り、模倣を、設定の変換と結果の後処理が応答関数と可換になる四角形に送る、などの決め方が要る（候補。模倣に要求する可換性は決めていない）。
surveys/2026-09-29_14_categorical-overview.md:71:- 定義の候補：「実験の圏」（対象はプロトコル、射は模倣）、「モデルの圏」（実験の圏から射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ への関手の圏。型と可換性の決め方が先に要る）。
surveys/2026-09-29_14_categorical-overview.md:79:- ブラックウェル–シャーマン–スタインの定理の圏論版が、実験の「模倣」の順序（本表の層 1 の射）とどう対応するか。
surveys/2026-09-29_14_categorical-overview.md:83:- 模倣の向き（PR #29 のレビュー）：模倣 $`q = g ∘ p ∘ f`$ に設定の前処理 $`f`$ を含めると、$`f`$ は $`q`$ の始域から $`p`$ の始域へ向かい、射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ の可換な四角形とは向きが一般に合わない。T-0005・T-0006 で模倣の向きを式で固定し、射の圏だけで表せるかを検討する。
summaries/2026-09-29_14_categorical-overview.md:34:  - 定義の候補：「実験の圏」（対象はプロトコル、射は模倣）と「モデルの圏」（実験の圏から射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ への関手の圏。応答関数は $`\mathsf{Stoch}`$ の射なので、型と可換性
…（以下 728 文字を省略）
```

</details>

## Claude

手順を確かめ、報告した見立てのうち「極限」の部分を証明の形で検算しました。これから調査メモを書きます。

<details><summary>ツール: Write: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Edit: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md</summary>

```text
（入力の本文は省略。項目: file_path, new_string, old_string, replace_all）
```

</details>

<details><summary>結果: Edit: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md</summary>

```text
The file /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash: Inspect roadmap structure</summary>

```text
awk '/^### T-0016/,/^### T-0017/' roadmap.md | tail -3; grep -n "T-0016\|T-0018" roadmap.md | head -30; sed -n '1,40p' roadmap.md
```

</details>

<details><summary>結果: Bash: Inspect roadmap structure</summary>

```text
- 第 16 回の後に、ユーザーが実験の比較の原典 5 件を入手し、非公開リポジトリの `papers/` に置いた：`blackwell1951`（Blackwell, Comparison of experiments, Proc. Second Berkeley Symp., 1951）、`blackwell1953`（Blackwell, Equivalent comparisons of experiments, Ann. Math. Statist. 24, 1953）、`lecam1964`（Le Cam, Sufficiency and approximate sufficiency, Ann. Math. Statist. 35, 1964）、`shannon1958`（Shannon, A note on a partial ordering for communication channels, Information and Control 1, 1958）、`raginsky2011`（Raginsky, Shannon meets Blackwell and Le Cam: channels, codes, and statistical experiments, Proc. IEEE ISIT, 2011）。書誌情報は `references.bib` に登録済み。内容はこれから確かめる。

### T-0017 時空の側の先行研究の調査（第 15 回に追加）
3:最終更新: 2026-09-30（第 16 回。T-0016 を進行中にし、用語のタスク T-0018 を追加）
11:- 順序は、第 11 回にユーザーと相談して決めた（2 節）。第 13 回に、ユーザーの提案で T-0015（D-0003 の未解決の点の解決）を T-0002 の前に加えた。第 15 回に、調査が不足している領域を洗い出し、Claude の提案にユーザーが賛成して、調査のタスク T-0016（段階 B の前）と T-0017（T-0008 の前）を加えた。優先の順は、状況に応じてユーザーと相談して見直す。
18:\text{T-0001} \;→\; \text{T-0015} \;→\; \text{T-0002} \;→\; \text{T-0003} \;→\; \text{T-0016} \;→\; \text{T-0018} \;→\; \text{段階 B（T-0004〜T-0007）} \;→\; \text{T-0017} \;→\; \text{T-0008} \;→\; \text{段階 C（T-0009）} \;→\; \text{段階 D（T-0010）}
24:| （調査） | QBism の先行研究、実験の族の位相と極限 | T-0003、T-0016 |
25:| （用語） | 主体・観測者・装置の使い分け | T-0018 |
33:T-0015 は、番号は後から付けたが、順序は T-0001 の次である。T-0016 は T-0003 の次、T-0018 は T-0016 の次（第 16 回にユーザーと決めた）、T-0017 は段階 B の次（T-0008 の前）である。
56:| T-0016 | 実験の族の位相と極限の先行研究の調査 | 調査 | なし | [D-0001](definitions/D-0001.md)〜[D-0005](definitions/D-0005.md)、[A-0006]
…（以下 2519 文字を省略）
```

</details>

<details><summary>ツール: Bash: Move the unrequested Δ-convergence check to an outlook note</summary>

```text
python3 - <<'EOF'
p='surveys/2026-09-30_17_comparison-of-experiments.md'
s=open(p,encoding='utf-8').read()
start=s.index('- **(iv) 不足度での収束**')
end=s.index('- **(v) 事後分布の一点への集中**')
iv=s[start:end]
s=s[:start]+s[end:]
s=s.replace('- **(v) 事後分布の一点への集中**','- **(iv) 事後分布の一点への集中**')
note=('- **見通し（検算は今後）**：さらに、不足度の距離でも $`Δ(𝓔_n, 𝓔_∞) → 0`$ となりそうである。'
 '$`δ(𝓔_∞, 𝓔_n) = 0`$ は (ii) による。$`δ(𝓔_n, 𝓔_∞)`$ は、Le Cam の定理 3 の (1) と (3) の同値から、ベイズ・リスクの差の上限で評価でき、'
 'ベイズ・リスクを事後分布 $`π_n`$ と $`π_∞`$ で書けば、差は $`N\\,E_{\\bar{P}} \\|π_n − π_∞\\|_1`$ で上から抑えられる見込みである。'
 'この評価を証明の形で確かめることは、次回以降のセッションで扱う（ユーザーの判断）。\n')
s=s.replace('- **事前分布**：D-0005',note+'- **事前分布**：D-0005')
s=s.replace('(v) の集中の条件は変わらない','(iv) の集中の条件は変わらない')
s=s.replace('「データを増やす実験の族の極限」は、不足度の距離 $`Δ`$ で収束する列の極限として存在し、その標準測度は事後分布の極限の分布である。',
 '「データを増やす実験の族の極限」は、標準測度（事後分布の分布）の弱収束の意味で存在し、その標準測度は事後分布の極限の分布である（不足度の距離 $`Δ`$ での収束は、上の見通しにとどまる）。')
s=s.replace('D-0005 の未解決の点「収束させる対象：実験の列か、各段階のデータから得る事後分布の列か」について、$`Θ = \\{1, …, N\\}`$ が有限の場合を検算した。',
 'D-0005 の未解決の点「収束させる対象：実験の列か、各段階のデータから得る事後分布の列か」について、$`Θ = \\{1, …, N\\}`$ が有限の場合を検算した（第 17 回の報告で述べた見立てを、筋道が分かる程度に書いたもの。詳しい証明の形で確かめることは、次回以降のセッションで扱う。ユーザーの判断）。')
open(p,'w',encoding='utf-8').write(s)
EOF
grep -n "(iv)\|(v)\|見通し\|Δ(𝓔_n" surveys/2026-09-30_17_comparison-of-experiments.md
```

</details>

<details><summary>結果: Bash: Move the unrequested Δ-convergence check to an outlook note</summary>

```text
143:- **(iv) 事後分布の一点への集中**：$`M_∞`$ が単体の頂点に集中することは、各 $`i`$ について $`P_i`$ でほとんど確実に $`π_∞ = e_i`$（真のパラメータへの集中）となることと同値である。頂点に集中していれば、$`i ≠ j`$ について $`\bar{P}(θ = i, π_∞ = e_j) = E_{\bar{P}}[π_{∞,i}\,1\{π_∞ = e_j\}] = 0`$ なので、$`P_i`$ の下で $`π_∞ = e_i`$ である。逆は、$`\bar{P}`$ が $`P_i`$ の平均であることから従う。これは、極限の実験 $`𝓔_∞`$ が「完全に情報的」（$`P_i`$ がデータ列全体の上で互いに特異）であることと同じである。
144:- **見通し（検算は今後）**：さらに、不足度の距離でも $`Δ(𝓔_n, 𝓔_∞) → 0`$ となりそうである。$`δ(𝓔_∞, 𝓔_n) = 0`$ は (ii) による。$`δ(𝓔_n, 𝓔_∞)`$ は、Le Cam の定理 3 の (1) と (3) の同値から、ベイズ・リスクの差の上限で評価でき、ベイズ・リスクを事後分布 $`π_n`$ と $`π_∞`$ で書けば、差は $`N\,E_{\bar{P}} \|π_n − π_∞\|_1`$ で上から抑えられる見込みである。この評価を証明の形で確かめることは、次回以降のセッションで扱う（ユーザーの判断）。
145:- **事前分布**：D-0005 の事前分布は主体のもので一様ではない。$`Θ`$ が有限で、事前分布がすべての点に正の確率を与えるなら、その事後分布は一様な事前分布の事後分布の、単体の間の全単射な変換で得られる（重みを掛けて正規化する）ので、(iv) の集中の条件は変わらない。
146:- **まとめ**：$`Θ`$ が有限なら、「データを増やす実験の族の極限」は、標準測度（事後分布の分布）の弱収束の意味で存在し、その標準測度は事後分布の極限の分布である（不足度の距離 $`Δ`$ での収束は、上の見通しにとどまる）。D-0005 の「族の極限で事後分布が一点に集中する」は、極限の実験が完全に情報的であることにあたる。
```

</details>

<details><summary>ツール: Bash: Find where mimicry issue lives in roadmap/framework</summary>

```text
grep -n "模倣\|Arr(" roadmap.md definitions/*.md framework.md | head; awk '/^### T-0004/,/^### T-0008/' roadmap.md
```

</details>

<details><summary>結果: Bash: Find where mimicry issue lives in roadmap/framework</summary>

```text
roadmap.md:213:- 統計的実験の比較と収束の理論：Le Cam の不足度と距離、Blackwell の実験の比較、Torgersen。実験の族の極限の位相と距離の候補。第 14 回の概観の「模倣」の順序との対応（[調査メモ](surveys/2026-09-29_14_categorical-overview.md)の 6 節）。
### T-0004 実験パラメータの空間と、結果の統計の空間の位相

各ファイルの未解決の点のうち、位相に関するものをまとめて決める。

- [D-0003](definitions/D-0003.md)：$`X`$ の位相と、時空の部分と比べる写像は、第 13 回（T-0015）に決めた（直和の位相、観測者の座標 $`M_O`$ への換算）。残るのは、結果の読みでない座標の扱い。
- [D-0004](definitions/D-0004.md)・[A-0006](assumptions/A-0006.md)：$`\mathrm{Prob}(Y_π)`$ の位相（弱位相か全変動距離か）と、等価原理の「近い」の意味。
- [A-0005](assumptions/A-0005.md)：座標ごとの値域のコンパクト性か、$`X`$ 自体のコンパクト性か。「一様に有界」の範囲。
- [D-0001](definitions/D-0001.md)：結果の空間 $`Y_π`$ の意味。

### T-0005 尤度と同時分布、主体の間で共有するデータの空間

- [D-0004](definitions/D-0004.md)：複数回の結果の同時分布と尤度（条件付き独立を仮定するか）、推定の対象の区別。
- [A-0006](assumptions/A-0006.md)：交換可能性を別の前提として課すか。
- [A-0007](assumptions/A-0007.md)：予測分布を作る同時分布と尤度、主体の間で共有するデータの空間、適用範囲。前提を相互とするか片側とするか、フレームワークで採る一致の段階（第 16 回に加えた論点。ユーザーの判断で次に回した）。

### T-0006 極限と事後分布の集中

- [D-0005](definitions/D-0005.md)：極限の位相（一様構造、完備性、分離性）、収束させる対象、部分列の選び方、事後分布の集中の条件、事後分布を置く空間。
- [D-0006](definitions/D-0006.md)（層 5）：予備的な検討にとどめる。実際の観測量の極限の位相を決めるときに、可能な観測量にも同じ取り方が使えるかを確かめる。層 5 の定義と前提そのものは T-0010 で扱う。
- 関係する予想：[C-0005](conjectures/C-0005.md)、[C-0006](conjectures/C-0006.md)。

### T-0007 局在の詳細化

- [D-0008](definitions/D-0008.md)：$`o`$ を実際の観測量と可能な観測量のどちらで取るか、「有界」と「収まる」の意味、代数として閉じるか。
- [A-0008](assumptions/A-0008.md)：実験における時空の領域の与え方。
- [D-0001](definitions/D-0001.md)：各実験が占める領域の決め方。

### T-0008 C-0001・C-0007・C-0008 の検証
```

</details>

## Claude

Roadmap と D-0005 を更新します。

<details><summary>ツール: Bash: Update roadmap T-0016/T-0006 and D-0005 unresolved points</summary>

```text
python3 - <<'EOF'
import re
p='roadmap.md'
s=open(p,encoding='utf-8').read()
s=s.replace('最終更新: 2026-09-30（第 16 回。T-0016 を進行中にし、用語のタスク T-0018 を追加）',
 '最終更新: 2026-09-30（第 17 回。T-0016 のうち実験の比較の原典を確認し、調査メモの確認と掘り下げを T-0016 の続きとした）')
old='書誌情報は `references.bib` に登録済み。内容はこれから確かめる。\n'
assert old in s
s=s.replace(old,'書誌情報は `references.bib` に登録済み。\n'
 '- 第 17 回：ユーザーの判断で、残りのうち「Le Cam の理論と実験の比較」に重点を置き、上の原典 5 件の本文で定理の仮定と結論を確かめた（[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)）。プロジェクトへのつながりの候補（調査メモの 7 節。Claude の見立て）を、D-0005 の未解決の点と下の T-0006 に記録した。\n'
 '- 第 17 回の後の予定（ユーザーの判断）：PR のマージ後に、ユーザーが第 17 回の調査メモを確認する。次回以降のセッションで、(1) 報告と調査メモへの疑問点・掘り下げ、(3) 調査メモの 7 節の候補の検算（有限の $`Θ`$ での不足度の距離 $`Δ`$ での収束（7.2 節の見通し）の証明、ねじれ射の圏による模倣の読み替え（7.3 節）の式での確認）を行う。\n'
 '- 残るのは、上の確認と掘り下げ、一般化確率論と Ludwig、弱い併合（Kalai–Lehrer 1994）。\n')
old6='- 関係する予想：[C-0005](conjectures/C-0005.md)、[C-0006](conjectures/C-0006.md)。\n\n### T-0007'
assert old6 in s
s=s.replace(old6,'- 関係する予想：[C-0005](conjectures/C-0005.md)、[C-0006](conjectures/C-0006.md)。\n'
 '- 第 17 回の候補（[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)の 7 節）：実験を共通の空間に置く方法としての Le Cam の不足度（$`Θ`$ の読み方の二つの候補）、$`Θ`$ が有限の場合の極限の二つの見方の一致、模倣をねじれ射の圏 $`\\mathrm{Tw}(\\mathsf{Stoch})`$ の射と読む候補（第 14 回の模倣の向きの論点。T-0005 とも関係する）。\n\n### T-0007')
open(p,'w',encoding='utf-8').write(s)

p='definitions/D-0005.md'
s=open(p,encoding='utf-8').read()
old='- 収束させる対象：実験の列か、各段階のデータから得る事後分布の列か。実験の設定と結果の空間はプロトコルごとに異なるので、実験そのものを共通の空間の元とみなす方法は決まっていない。\n'
assert old in s
s=s.replace(old,
…（以下 642 文字を省略）
```

</details>

<details><summary>結果: Bash: Update roadmap T-0016/T-0006 and D-0005 unresolved points</summary>

```text
definitions/D-0005.md | 2 ++
 roadmap.md            | 8 ++++++--
 2 files changed, 8 insertions(+), 2 deletions(-)
```

</details>

<details><summary>ツール: Bash: Add glossary and symbol entries</summary>

```text
python3 - <<'EOF'
p='glossary.md'
s=open(p,encoding='utf-8').read()
L='[第 17 回の調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)'
def ins_after(prefix,row):
    global s
    i=s.index('\n| '+prefix)
    j=s.index('\n',i+1)
    s=s[:j+1]+row+'\n'+s[j+1:]
ins_after('causal site |','| comparison of experiments | 実験の比較 | 同じパラメータの集合を持つ二つの統計的実験の、情報量の多さの比較（Blackwell）。「すべての決定問題で、一方で達成できるリスクが他方でも達成できる」ことと、「結果の後処理（マルコフ核）で他方を再現できる（十分性）」ことは同値である（ブラックウェル–シャーマン–スタインの定理。パラメータが有限個の場合に Blackwell 1953 で一般の実験に拡張）。前処理も許すチャネルの比較（Shannon の包含）や、近似版の Le Cam の不足度がある。 | '+L+' |')
ins_after('de Vries algebra |','| deficiency (Le Cam) | 不足度 | 同じパラメータの集合 $`Θ`$ を持つ実験 $`𝓔 = \\{P_θ\\}`$ と $`𝓕 = \\{Q_θ\\}`$ について、$`δ(𝓔, 𝓕) = \\inf_M \\sup_θ \\|MP_θ − Q_θ\\|`$（$`M`$ は無作為化）。$`𝓔`$ で $`𝓕`$ をどれだけ近似できるかの尺度で、決定問題のリスクの差の上限と同値に言い換えられる（Le Cam 1964 の定理 3）。両向きの最大値 $`Δ`$ は実験の上の擬距離で、結果の空間が異なる実験も比べられる。 | '+L+' |')
ins_after('sprinkling |','| standard measure | 標準測度 | パラメータが有限個（$`N`$ 個）の実験で、一様な事前分布の下での事後分布の分布（単体の上の、重心が $`(1/N, …, 1/N)`$ の確率測度）。実験は標準測度で同値類まで決まり、実験の比較は標準測度の凸順序で表せる（Blackwell 1951・1953）。 | '+L+' |')
ins_after('topos |','| twisted arrow category | ねじれ射の圏 | 圏 $`𝒞`$ の射を対象とし、$`p : a → b`$ から $`q : a\' → b\'`$ への射を $`q = g ∘ p ∘ f`$ を満たす組 $`(f : a\' → a,\\ g : b → b\')`$ とする圏 $`\\mathrm{Tw}(𝒞)`$。本プロジェクトでは、実験の模倣（設定の前処理と結果の後処理）をこの圏の射と読む候補がある（第 17 回。Claude の補足で未確認）。 | '+L+' |')
open(p,'w',encoding='utf-8').write(s)

p='symbols.md'
s=open(p,encoding='utf-8').read()
C='[調査 17](surveys/2026-09-30_17_comparison-of-e
…（以下 760 文字を省略）
```

</details>

<details><summary>結果: Bash: Add glossary and symbol entries</summary>

```text
| $`π`$、$`X_π`$、$`Y_π`$ | 実験プロトコル、その設定の空間と結果の空間 | $`π`$ は有限の記述を持つ実験プロトコル。$`X_π`$、$`Y_π`$ はプロトコル $`π`$ の設定の空間と結果の空間で、プロトコルごとに異なりうる。統計は $`p_π : X_π → \mathrm{Prob}(Y_π)`$（第 09 回、PR #21 のレビューを受けて導入） | | [調査 08](surveys/2026-09-28_08_observation-as-limit.md)（1.4 節） |
| $`𝓔 ⊃ 𝓕`$ | 𝓔 は 𝓕 より情報量が多い | すべての決定問題で、$`𝓕`$ で達成できるリスクが $`𝓔`$ でも達成できる（Blackwell） | | [調査 17](surveys/2026-09-30_17_comparison-of-experiments.md) |
| $`𝓔 ≻ 𝓕`$ | 𝓔 は 𝓕 に対して十分 | 結果の後処理（マルコフ核）で $`𝓕`$ の分布をすべて再現できる（Blackwell）。パラメータが有限個なら $`⊃`$ と同値 | | [調査 17](surveys/2026-09-30_17_comparison-of-experiments.md) |
| $`δ(𝓔, 𝓕)`$、$`Δ(𝓔, 𝓕)`$ | 𝓔 の 𝓕 に対する不足度、Le Cam の距離 | $`δ(𝓔, 𝓕) = \inf_M \sup_θ \|MP_θ − Q_θ\|`$、$`Δ = \max\{δ(𝓔, 𝓕), δ(𝓕, 𝓔)\}`$（同じパラメータの集合 $`Θ`$ を持つ実験の上の擬距離） | | [調査 17](surveys/2026-09-30_17_comparison-of-experiments.md) |
 definitions/D-0005.md | 2 ++
 glossary.md           | 4 ++++
 roadmap.md            | 8 ++++++--
 symbols.md            | 4 ++++
 4 files changed, 16 insertions(+), 2 deletions(-)
```

</details>

<details><summary>ツール: Bash: Check math guide rules on tables and norms</summary>

```text
grep -n -i "表\|ノルム\|\\\\|" docs/math-guide.md | head -20
```

</details>

<details><summary>結果: Bash: Check math guide rules on tables and norms</summary>

````text
3:別のリポジトリで数式のテストページを Firefox と Chrome で表示して確認した結果をもとにした、書き方のルールです。
13:| 絶対値 | `\left\| x \right\|` | `\|x\|`、`\lvert x \rvert` |
19:表の中の `\|` は、Markdown の表の列区切りと区別するためのエスケープです。
27:例えば `f(x)\,dx` は、`$$...$$` だと `f(x), dx` と表示されました。
28:` ```math ` なら、書いたとおりに表示されます。
42:箇条書きの項目の続きとして字下げして書いた ` ```math ` は、数式として表示されず、普通のコードブロックになりました（第 02 回の調査メモで確認）。
68:`質量$m$の物体` のように全角文字に直接くっつけると、数式として認識されず、`$m$` がそのまま表示されました。
79:`\left| x \right|` だけが正しく表示されました。
93:`\mathbb{R}`、`\mathcal{L}`、`\mathfrak{g}`、`\boldsymbol{v}`、`\mathbf{E}` は、Firefox では正しく表示されますが、Chrome では普通の斜体の R、L、g、v、E になりました。
94:文字そのものを直接書くと、どちらのブラウザでも正しく表示されました。
116:`\sin x` は、Chrome では `sinx` とくっついて表示されました。
117:`\sin\,x` か `\sin(x)` なら、どちらのブラウザでも正しく表示されました。
131:GitHub では `\operatorname` が許可されておらず、`The following macros are not allowed: operatorname` というエラーが表示されました（第 08 回にユーザーが確認）。
146:## Firefox と Chrome で問題なく表示されたもの
156:ただし Chrome では、行列のかっこの内側の余白と、`aligned` の揃える位置の前の空白が、Firefox より少し広く表示されます。
````

</details>

<details><summary>ツール: Bash: Read norm/absolute value rules</summary>

```text
sed -n '8,20p;70,90p' docs/math-guide.md; grep -rn '\\|' surveys/2026-09-30_16_merging-and-consistency.md | head -3
```

</details>

<details><summary>結果: Bash: Read norm/absolute value rules</summary>

`````text
| --- | --- | --- |
| ブロック数式 | ` ```math ` コードブロック | `$$...$$` |
| 箇条書きの中のブロック数式 | 箇条書きをいったん終え、行頭（字下げなし）に ` ```math ` を書く | 箇条書きの中で字下げした ` ```math ` |
| インライン数式 | `` $`...`$ `` | `$...$`（簡単な式なら可） |
| 日本語との境目 | `質量 $m$ の物体`（前後に半角スペース） | `質量$m$の物体` |
| 絶対値 | `\left\| x \right\|` | `\|x\|`、`\lvert x \rvert` |
| 特殊な文字（ℝ、𝐄 など） | Unicode 文字を直接書く（`ℝ`、`𝐄`） | `\mathbb{R}`、`\mathbf{E}` などのコマンド |
| 関数名と変数 | `\sin\,x` または `\sin(x)` | `\sin x` |
| 定義済みでない関数名（diag など） | `\mathrm{diag}` | `\operatorname{diag}` |
| 数式ではないドル記号 | `\$100` | `$100` |

表の中の `\|` は、Markdown の表の列区切りと区別するためのエスケープです。
実際に書くときは、絶対値は `\left| x \right|`、避ける書き方は `|x|` です。
```markdown
質量 $m$ の物体
```

質量 $m$ の物体

### 絶対値は `\left| ... \right|` を使う

`|x|` と `\lvert x \rvert` は、Firefox でも Chrome でも右の縦線の後ろに余分な空白が入り、`|x |  =` のように見えました。
`\left| x \right|` だけが正しく表示されました。

````markdown
```math
\left| x \right| = \sqrt{x^2} \quad (x ∈ ℝ)
```
````

```math
\left| x \right| = \sqrt{x^2} \quad (x ∈ ℝ)
```
`````

</details>

## Claude

ノルムの書き方を、表の列区切りとぶつからない `\left\Vert … \right\Vert` にそろえます。

<details><summary>ツール: Bash: Replace norm bars with Vert delimiters</summary>

```text
python3 - <<'EOF'
import re
for p in ['surveys/2026-09-30_17_comparison-of-experiments.md','glossary.md','symbols.md']:
    s=open(p,encoding='utf-8').read()
    n0=s.count('\\|')
    s2=re.sub(r'\\\|([^|`]*?)\\\|', lambda m: '\\left\\Vert '+m.group(1).strip()+' \\right\\Vert', s)
    open(p,'w',encoding='utf-8').write(s2)
    print(p, n0, s2.count('\\|'))
EOF
grep -n 'Vert' surveys/2026-09-30_17_comparison-of-experiments.md glossary.md symbols.md | cut -c1-200; grep -n '[^\\]|[^ ]' surveys/2026-09-30_17_comparison-of-experiments.md | grep -v '^[0-9]*:|' | head
```

</details>

<details><summary>結果: Bash: Replace norm bars with Vert delimiters</summary>

```text
surveys/2026-09-30_17_comparison-of-experiments.md 20 0
glossary.md 2 0
symbols.md 3 1
surveys/2026-09-30_17_comparison-of-experiments.md:70:- **決定問題**：決定の集合 $`T`$ と、その上の有界関数のベクトル束 $`C`$、損失関数 $`W_θ^t`$（$`\left\Vert W \righ
surveys/2026-09-30_17_comparison-of-experiments.md:72:- **定義 8（$`ε`$ 不足）**：$`Θ`$ の上の非負関数 $`ε`$ について、$`𝓔`$ が $`𝓕`$ に対して $`ε`$ 不足である�
surveys/2026-09-30_17_comparison-of-experiments.md:74:  1. $`𝓔`$ から $`𝓕`$ の標本空間への無作為化 $`M`$ で、すべての $`θ`$ で $`\left\Vert MP_θ − Q_θ \right\Vert ≤ ε
surveys/2026-09-30_17_comparison-of-experiments.md:76:  3. 類 $`𝔇`$ の各決定問題と、有限な台を持つ各事前分布 $`μ`$ で、$`𝓔`$ のベイズ・リスクの包絡線が、$`�
surveys/2026-09-30_17_comparison-of-experiments.md:77:  4. 類 $`𝔇`$ の各決定問題、有限な台を持つ各事前分布 $`μ`$、$`𝓕`$ の各特別な手続き $`σ`$ に対し、$`𝓔`$
surveys/2026-09-30_17_comparison-of-experiments.md:81:- **定義 9（不足度と距離）**：$`δ(𝓔, 𝓕) = \inf_M \sup_θ \left\Vert MP_θ − Q_θ \right\Vert`$（$`M`$ は L 空間の間の�
surveys/2026-09-30_17_comparison-of-experiments.md:116:- **Blackwell 十分性**：同じ入力のチャネル $`W, W'`$ で、ある核 $`T`$ により $`W' = TW`$（後処理だけ）。**Le Cam 不
surveys/2026-09-30_17_comparison-of-experiments.md:117:- **Shannon 十分性**：入力が異なってよいチャネル $`W, W'`$ で、$`W' = \sum_i π_i S_i W T_i`$（前処理 $`T_i`$ と後処理
surveys/2026-09-30_17_comparison-of-experiments.md:144:- **見通し（検算は今後）**：さらに、不足度の距離でも $`Δ(𝓔_n, 𝓔_∞) → 0`$ となりそうである。$`δ(𝓔_�
glossary.md:19:| deficiency (Le Cam) | 不足度 | 同じパラメータの集合 $`Θ`$ を持つ実験 $`𝓔 = \{P_θ\}`$ と $`𝓕 = \{Q_θ\}`$ について、$`δ(𝓔, 𝓕) = \inf_M \sup_θ \l
symbols.md:110:| $`δ(𝓔, 𝓕)`$、$`Δ(𝓔, 𝓕)`$ | 𝓔 の 𝓕 に対する不足度、
…（以下 280 文字を省略）
```

</details>

<details><summary>ツール: Bash: Check remaining escaped bars and converted norms</summary>

```text
grep -n '\\|' symbols.md | tail -3 | cut -c1-300; grep -n 'Vert\|_∞\|_1' surveys/2026-09-30_17_comparison-of-experiments.md | grep -o '\\left\\Vert[^$]*' | head -20
```

</details>

<details><summary>結果: Bash: Check remaining escaped bars and converted norms</summary>

```text
82:| $`T`$、$`T[a]`$ | 識別の関係、a の T 近傍 | 点の間の「区別できないほど近い」という関係（許容関係など）と、a の点と T で結ばれる点全体 | `T : X → X → Prop`、`{y \| ∃ x ∈ a, T x y}` | [調査 05](surveys/2026-09-26_05_subordination.md) 
\left\Vert W \right\Vert = \sup \left| W_θ^t \right|`
\left\Vert W \right\Vert \int ε(θ)\,μ(dθ)`
\left\Vert MP_θ − Q_θ \right\Vert ≤ ε(θ)`
\left\Vert W \right\Vert \int ε\,dμ`
\left\Vert W \right\Vert \int ε\,dμ`
\left\Vert MP_θ − Q_θ \right\Vert`
\left\Vert TW − W' \right\Vert_∞`
\left\Vert \cdot \right\Vert_∞`
\left\Vert \sum π_i S_i W T_i − W' \right\Vert_∞`
\left\Vert π_n − π_∞ \right\Vert_1`
```

</details>

<details><summary>ツール: Bash: Check framework.md update conventions</summary>

```text
grep -n "最終更新\|第 16 回\|T-0016" framework.md | head; git log -3 --stat --oneline -- framework.md | head -20
```

</details>

<details><summary>結果: Bash: Check framework.md update conventions</summary>

```text
3:最終更新: 2026-09-30（第 16 回。4.2 節に一致の定理の原典の確認を加えた）
173:第 16 回に、Blackwell–Dubins 1962 と Diaconis–Freedman 1986 の原典を確かめた（[第 16 回の調査メモ](surveys/2026-09-30_16_merging-and-consistency.md)）。A-0007 の一致は、原典では片側の絶対連続性で成り立ち、主体自身の予測分布についてほとんど確実な、将来全体の全変動距離での一致である。真の状態を固定したときの一致には三つの段階（固定した個数の将来の結果、将来全体の全変動距離、主体の予測分布についてほとんど確実）があり、フレームワークでどれを採るかは A-0007 の未解決の点である。
584e8b5 第 16 回：主体の間の一致と事後一致性（T-0016 の一部）
 framework.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
6c54183 PR #30 の第 7 回のレビューに対応：事前分布の正値性の条件、証明がないという記述の範囲、例 2 の相関の意味を直す
 framework.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
70bea14 PR #30 の第 6 回のレビューに対応：A-0007 の対象外とする例を Fuchs–Schack 2009 の例に限り、σz の例を保証の範囲外の例として区別する
 framework.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

</details>

<details><summary>ツール: Bash: Read framework section around observables layer</summary>

```text
sed -n '150,200p' framework.md
```

</details>

<details><summary>結果: Bash: Read framework section around observables layer</summary>

````text
D_0009 --> R_0008
  C_0004 -. 目標 .-> A_0006
  C_0007 -. 目標 .-> A_0009
```
<!-- deps-graph:end -->

## 4.1 圏論的な概観（第 14 回）

フレームワークの要素を圏論の言葉で見直した（[調査メモ](surveys/2026-09-29_14_categorical-overview.md)。対応はすべて見立てで、新しい定義・予想は登録していない）。骨組みは次の二つである（第 14 回にユーザーと決めた）。

- **層 1〜2：マルコフ圏**。応答関数（D-0004）はマルコフ核（$`\mathsf{Stoch}`$ の射）で、一つのモデルは、射の圏 $`\mathrm{Arr}(\mathsf{Stoch})`$ への関手とみなせる可能性がある（候補。型と可換性の決め方が先に要る）。状態と装置のモデルは固定せず、**モデル全体の圏**を取る（ユーザーの判断）。実際の観測量の推定（D-0005）は、モデルの空間の上のベイズの逆と、コルモゴロフ積の上の極限として読める（A-0007 から期待できるのは事後予測の一致で、モデルの上の事後分布の一致ではない）。
- **層 3〜5：随伴の不動点**。観測量から空間を再構成する構成（D-0007）と、空間の中で可能な実験を記述し直す構成（C-0002・D-0006）を随伴とみなし、整合条件（D-0003）と不動点の条件（D-0006）を、その単位と余単位が同型になる対象として一つにまとめる見込みがある。

局在（D-0008）は領域の順序集合からの関手（AQFT のネット）、再構成（D-0007）の非可換な場合は Bohr トポス、膨張（D-0009）は収縮とのガロア接続として、その上に載る。

## 4.2 QBism との比較：主体の間の一致（第 15 回）

層 2 の推定（D-0005）と主体の間の一致（A-0007）を、QBism の量子 de Finetti 定理による一致と比べた（[調査メモ](surveys/2026-09-29_15_qbism-agreement.md)）。

- 調査した QBism の一致の主張は、交換可能性、情報的に完全な測定、データが指す状態の近傍で各主体の事前分布が 0 にならないこと（Claude の補足：正確には、その状態のすべての開近傍に正の確率を置くこと）、を課して、将来の系の状態の割り当て（測っていない観測量の予測を含む）の一致まで得る、とする。ただし、確認した範囲の文献では、この一致の主張の証明を見つけられなかった。
- 本プロジェクトは、交換可能性を課さず、予測分布の相互絶対連続性（A-0007）から将来のデータの予測の一致だけを得て、推定の対象の一致は識別可能性と事後分布の集中（D-0005 の未解決の点）に分ける。両者は矛盾しない。量子状態の割り当てが交換可能で、同一の情報的に完全な POVM を各系で独立に繰り返す場合には、A-0007 は事前分布の相互絶対連続性と同値になる（Claude の補足。測定を回ごとに変える場合は一般には従わない）。
- Fuchs–Schack 2009 が一致しない例として挙げるものは、どれも予測分布が互いに絶対連続でなく、A-0007 の対象外である（Claude の補足。例の一つは、測定の設定についての仮定の下で確かめた）。一方、$`σ_z`$ だけを測る例（Schack–Brun–Caves 2001
…（以下 976 文字を省略）
````

</details>

<details><summary>ツール: Bash: Add section 4.3 to framework.md and regenerate graph</summary>

```text
python3 - <<'EOF'
p='framework.md'
s=open(p,encoding='utf-8').read()
s=s.replace('最終更新: 2026-09-30（第 16 回。4.2 節に一致の定理の原典の確認を加えた）','最終更新: 2026-09-30（第 17 回。4.3 節に実験の比較の理論による候補を加えた）')
add='''## 4.3 実験の比較の理論（第 17 回）

層 1〜2 の実験の比較と、D-0005 の極限について、Blackwell（1951・1953）、Le Cam（1964）、Shannon（1958）、Raginsky（2011）の原典を確かめた（[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)）。次は候補で（Claude の見立て）、定義・前提は変えていない。

- Le Cam の不足度と距離 $`Δ`$ は、推定の対象の集合 $`Θ`$ が共通なら、結果の空間が異なる実験を比べられる。D-0005 の「実験を共通の空間の元とみなす方法」の候補になる。$`Θ`$ の読み方（推定の対象か設定か）は決まっていない。
- $`Θ`$ が有限なら、実験の型は事後分布の分布（標準測度）で決まり、データを増やす族の極限は事後分布のマルチンゲール収束で存在する。事後分布の一点への集中は、極限の実験が完全に情報的であることにあたる。
- 4.1 節の「模倣」（設定の前処理と結果の後処理）は、射の圏 $`\\mathrm{Arr}(\\mathsf{Stoch})`$ ではなく、ねじれ射の圏 $`\\mathrm{Tw}(\\mathsf{Stoch})`$ の射と読める可能性がある（未確認）。
- Le Cam は、標本空間の点を使わず、関数の束と期待値で実験を定め、標本空間を M 空間のスペクトルとして再構成する。観測量の代数からの再構成（D-0007）の、統計の側での先例とみなせる。

'''
s=s.replace('## 5. 結果の位置づけ',add+'## 5. 結果の位置づけ')
open(p,'w',encoding='utf-8').write(s)
EOF
python3 tools/deps_graph.py >/dev/null && git diff --stat framework.md
```

</details>

<details><summary>結果: Bash: Add section 4.3 to framework.md and regenerate graph</summary>

```text
framework.md | 11 ++++++++++-
 1 file changed, 10 insertions(+), 1 deletion(-)
```

</details>

## Claude

次に、対話ログを書き出します。

<details><summary>ツール: Bash: Locate the session transcript file</summary>

```text
ls -la ~/.claude/projects/*/ | head -20; grep -l "次のセッションを開始してください" ~/.claude/projects/*/*.jsonl
```

</details>

<details><summary>結果: Bash: Locate the session transcript file</summary>

```text
total 84836
drwx------ 28 root root     4096 Sep 30 07:42 .
drwx------  3 root root     4096 Sep 25 00:49 ..
drwx------  3 root root     4096 Sep 30 07:54 [ID]
-rw-------  1 root root  9757869 Sep 30 07:54 [ID].jsonl
drwx------  2 root root     4096 Sep 26 09:47 [ID]
-rw-------  1 root root   974979 Sep 26 09:51 [ID].jsonl
drwx------  2 root root     4096 Sep 28 00:37 [ID]
-rw-------  1 root root   916222 Sep 28 00:42 [ID].jsonl
drwx------  2 root root     4096 Sep 28 07:16 [ID]
-rw-------  1 root root     2082 Sep 28 07:21 [ID].jsonl
drwx------  2 root root     4096 Sep 25 10:34 [ID]
-rw-------  1 root root   404576 Sep 25 10:38 [ID].jsonl
drwx------  2 root root     4096 Sep 26 06:26 [ID]
-rw-------  1 root root     2082 Sep 26 06:29 [ID].jsonl
drwx------  3 root root     4096 Sep 29 07:45 [ID]
-rw-------  1 root root   616621 Sep 29 07:48 [ID].jsonl
drwx------  2 root root     4096 Sep 29 02:59 [ID]
-rw-------  1 root root     2082 Sep 29 03:03 [ID].jsonl
drwx------  3 r
…（以下 683 文字を省略）
```

</details>

<details><summary>ツール: Bash: Find session start timestamps and export tool options</summary>

```text
cd ~/.claude/projects/-home-user && python3 - <<'EOF'
import json
f='[ID].jsonl'
for line in open(f,encoding='utf-8'):
    try: d=json.loads(line)
    except: continue
    if d.get('type')!='user': continue
    m=d.get('message',{}); c=m.get('content')
    text=c if isinstance(c,str) else ''.join(x.get('text','') for x in c if isinstance(x,dict) and x.get('type')=='text')
    if '次のセッションを開始' in text or '<command-name>/clear' in text:
        print(d.get('timestamp'), repr(text[:60]))
EOF
python3 /home/user/point-free-spacetime/tools/export_log.py --help | head -30
```

</details>

<details><summary>結果: Bash: Find session start timestamps and export tool options</summary>

```text
2026-09-30T07:42:58.050Z '<command-name>/clear</command-name>\n            <command-mes'
2026-09-30T07:43:07.629Z '次のセッションを開始してください。'
usage: export_log.py [-h] [--title TITLE] [--redact-file REDACT_FILE]
                     [--since SINCE] [--until UNTIL]
                     jsonl output

Claude Code のセッション記録（JSONL）を、公開用の Markdown に変換する。

positional arguments:
  jsonl
  output

options:
  -h, --help            show this help message and exit
  --title TITLE
  --redact-file REDACT_FILE
                        伏せ字にする語句のファイル（1 行 1 語句）
  --since SINCE         この時刻（ISO 8601）以降の記録だけを出力する。同じセッション記録を複数回に分けて書き出すときに使う
  --until UNTIL         この時刻（ISO 8601）より前の記録だけを出力する。次の回の最初の発言の時刻を指定する
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Write: /home/user/point-free-spacetime/summaries/2026-09-30_17_comparison-of-experiments.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/summaries/2026-09-30_17_comparison-of-experiments.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/summaries/2026-09-30_17_comparison-of-experiments.md (file state is current in your context — no need to Read it back)
```

</details>

## Claude

Now NEXT.md.

<details><summary>ツール: Bash: Update NEXT.md status and next task</summary>

```text
cd /home/user/point-free-spacetime && python3 - <<'EOF'
p='NEXT.md'
s=open(p,encoding='utf-8').read()
s=s.replace('最終更新: 2026-09-30（第 16 回セッションの後）','最終更新: 2026-09-30（第 17 回セッションの後）')
old='- 第 16 回の PR #32 のマージ後に、ユーザーが実験の比較の原典 5 件を入手した（非公開リポジトリの PR #10）。次のセッションは T-0016 の残りから始めると決めた（セッションの間の短い相談として記録する）。\n'
assert old in s
s=s.replace(old, old+'- 第 17 回：ロードマップの T-0016 の残りのうち、ユーザーの判断で「Le Cam の理論と実験の比較」に重点を置き、原典 5 件（Blackwell 1951・1953、Le Cam 1964、Shannon 1958、Raginsky 2011）の本文で定理の仮定と結論を確かめた。プロジェクトへのつながりの候補（Le Cam の不足度による実験の比較、有限の $`Θ`$ での極限の二つの見方の一致、ねじれ射の圏による模倣の読み替えなど。Claude の見立て）を調査メモの 7 節にまとめ、D-0005 の未解決の点とロードマップの T-0006 に記録した。ユーザーの判断で、今回は調査メモの作成までとした（[まとめ](summaries/2026-09-30_17_comparison-of-experiments.md)、[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)）。\n')
start=s.index('## 次のタスク')
end=s.index('## ユーザーにお願いしていること')
new='''## 次のタスク

次のセッションでは、[`roadmap.md`](roadmap.md) の **T-0016「実験の族の位相と極限の先行研究の調査」の続き**（第 18 回の予定）を扱う。第 17 回の PR のマージ後に、ユーザーが第 17 回の[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)を確認してから始める（ユーザーの判断）。T-0018「主体・観測者・装置の使い分け」は T-0016 の次である（[`CLAUDE.md`](CLAUDE.md) の「セッションの進め方」）。その後の順序、長期のタスク、未解決の論点は `roadmap.md` にある。

- 扱う候補（第 17 回の最後の相談の番号。どちらから始めるかは、セッションの始めにユーザーと相談する）：
  - (1) 第 17 回の報告と調査メモへの、ユーザーの疑問点と掘り下げ。
  - (3) 調査メモの 7 節の候補の検算：有限の $`Θ`$ で、データを増やす実験の族が不足度の距離 $`Δ`$ で極限の実験に収束すること（7.2 節の見通し）の証明と、模倣をねじれ射の圏 $`\\mathrm{Tw}(\\mathsf{Stoch})`$ の射と読むこと（7.3 節）の式での確認。
- 手がかりは、`roadmap.md` の「T-0016」と「T-0006」の節、第 17 回の調査メモ（7・8 節）、[D-0005](definit
…（以下 308 文字を省略）
```

</details>

<details><summary>結果: Bash: Update NEXT.md status and next task</summary>

```text
## 次のタスク

次のセッションでは、[`roadmap.md`](roadmap.md) の **T-0016「実験の族の位相と極限の先行研究の調査」の続き**（第 18 回の予定）を扱う。第 17 回の PR のマージ後に、ユーザーが第 17 回の[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)を確認してから始める（ユーザーの判断）。T-0018「主体・観測者・装置の使い分け」は T-0016 の次である（[`CLAUDE.md`](CLAUDE.md) の「セッションの進め方」）。その後の順序、長期のタスク、未解決の論点は `roadmap.md` にある。

- 扱う候補（第 17 回の最後の相談の番号。どちらから始めるかは、セッションの始めにユーザーと相談する）：
  - (1) 第 17 回の報告と調査メモへの、ユーザーの疑問点と掘り下げ。
  - (3) 調査メモの 7 節の候補の検算：有限の $`Θ`$ で、データを増やす実験の族が不足度の距離 $`Δ`$ で極限の実験に収束すること（7.2 節の見通し）の証明と、模倣をねじれ射の圏 $`\mathrm{Tw}(\mathsf{Stoch})`$ の射と読むこと（7.3 節）の式での確認。
- 手がかりは、`roadmap.md` の「T-0016」と「T-0006」の節、第 17 回の調査メモ（7・8 節）、[D-0005](definitions/D-0005.md) の未解決の点、第 14 回の調査メモ（6 節の模倣の向き）にある。
- T-0016 のほかの残り（一般化確率論と Ludwig、弱い併合（Kalai–Lehrer 1994））の文献は記憶によるもので、未確認。
- T-0018：手がかりは、`roadmap.md` の「T-0018」の節と、[A-0001](assumptions/A-0001.md) の未解決の点にある。

## ユーザーにお願いしていること

- なし。arXiv の論文は Claude が取得できる。出版社版の本文（有料のもの）が必要になったら、その都度お願いする。

## 未解決の論点

未解決の論点は、[`roadmap.md`](roadmap.md) と、関係する定義・前提の「未解決の点」、予想の「詳細化の論点」に置く（第 11 回に移した）。
```

</details>

<details><summary>ツール: Bash: Note user's review request and run tools tests</summary>

```text
python3 - <<'EOF'
p='NEXT.md'
s=open(p,encoding='utf-8').read()
old='- なし。arXiv の論文は Claude が取得できる。'
s=s.replace(old,'- 第 17 回の PR のマージ後に、第 17 回の[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)を確認していただく（ユーザーの予定）。\n- arXiv の論文は Claude が取得できる。')
open(p,'w',encoding='utf-8').write(s)
EOF
cd tools && python3 -m pytest -q tests 2>&1 | tail -3
```

</details>

<details><summary>結果: Bash: Note user's review request and run tools tests</summary>

```text
.................................                                        [100%]
33 passed in 0.16s
```

</details>

## Claude

Tests pass. Exporting the log now (right before commit).

<details><summary>ツール: Bash: Export dialogue log and check redactions</summary>

```text
cd /home/user/point-free-spacetime && python3 tools/export_log.py ~/.claude/projects/-home-user/[ID].jsonl logs/2026-09-30_17_comparison-of-experiments.md --title "2026-09-30 第 17 回: 実験の比較と Le Cam の不足度" --redact-file ../point-free-spacetime-private/redactions.txt --since 2026-09-30T07:42:58Z && wc -c logs/2026-09-30_17_comparison-of-experiments.md && grep -v -e '^#' -e '^$' ../point-free-spacetime-private/redactions.txt | grep -iFcf - logs/2026-09-30_17_comparison-of-experiments.md; grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}' logs/2026-09-30_17_comparison-of-experiments.md | head; grep -nE 'sk-[A-Za-z0-9]{10,}|ghp_|OPENAI_API_KEY=' logs/2026-09-30_17_comparison-of-experiments.md | head
```

</details>
