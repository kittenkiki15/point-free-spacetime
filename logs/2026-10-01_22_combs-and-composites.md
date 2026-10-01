# 2026-10-01 第 22 回: 逐次・適応的な実験と複合系（量子コムと一般化確率論）

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> ツールの呼び出しは折りたたんで表示し、個人情報などは伏せ字にしています。

## ユーザー

次のセッションを開始してください。

<details><summary>ツール: Bash: Check git state and read NEXT.md</summary>

```text
cd /home/user/point-free-spacetime && git status | head -3 && git log --oneline -5 && cat NEXT.md
```

</details>

<details><summary>結果: Bash: Check git state and read NEXT.md</summary>

```text
On branch claude/clever-planck-pr5kq1
Your branch is up to date with 'origin/claude/clever-planck-pr5kq1'.

99d3871 A-0013 の複合のプロトコルでの写像の型を明記した（第 21 回のクロスモデルレビューの提案）
3ab1536 第 21 回のクロスモデルレビューに対応：まとめの同時読み出しの記述を同じプロトコルの並列の場合に限り、択一の組の名称を揃え、部分装置の事象の局所性を D-0013 の未解決の点に記録した
bfb5d13 D-0001 の異種の部分装置の同時読み出しの扱いを、ユーザーの判断で後に回したと記録した
aab4f3d 第 21 回のクロスモデルレビューの詳細化の論点（逐次の測定後の一括読み出し）を D-0001 の未解決の点に記録した
7dceddd 第 21 回のクロスモデルレビューに対応：D-0013 とまとめの N_e = 0 の較正の写像を、時空の読みを持つプロトコルの実験に限った
# 次のセッションでやること

最終更新: 2026-10-01（第 21 回セッションの後）

## 状況

- 第 01 回：リポジトリの運用ルールを決め、自動検証（Lean・Python・クロスモデルレビュー）を整えた。
- 第 02 回：点なし位相と論理・様相論理・因果・量子論のつながりを整理し、調査メモ・用語一覧・記号一覧・参考文献一覧を作った（[まとめ](summaries/2026-09-25_02_pointfree-logic.md)）。
- 第 03 回：Heunen–van der Schaaf の 2 本の論文メモを作り、「完備ブール代数の点はアトムと対応する」を Lean で形式化した（[まとめ](summaries/2026-09-25_03_ordered-locales.md)）。
- 第 04 回：第 03 回の結果をユーザーと確認し、論文メモを修正した。検証済みの主張を「結果」として管理する [`results/`](results/README.md) を作った（[まとめ](summaries/2026-09-25_04_review-and-results.md)）。
  - ユーザーの方針：予想の価値の主軸は、数学ではなく**物理学への寄与**（厳密な定義のない物理の概念や主張に数学的な定式化を与えることなど）に置く。
- 第 05 回：最小の長さと操作的な領域の構造について、おもちゃのモデルを多角的に検討した。最小の尺度の入れ方を型 I（小さい領域を捨てる）と型 II（余白に下限を置く）に分け、型 II を「膨張 $`N`$ による余白付きの包含が補間的でないこと」として点なしに表した。文献を調べ、数学の部分は既知と確認して結果 R-0006〜R-0008 に登録し、最初の予想 [C-0001](conjectures/C-0001.md)（優先度：高、[Issue #8](https://github.com/kittenkiki15/point-free-spacetime/issues/8)）を立てた（[まとめ](summaries/2026-09-26_05_minimal-scale.md)、[調査メモ](surveys/2026-09-26_05_subordination.md)）。
- 第 06 回：C-0001 を見直す前の先行研究の調査を行った。主張 4 と同じ
…（以下 10156 文字を省略）
```

</details>

<details><summary>ツール: Bash: Compare branch with main and read T-0019</summary>

```text
git fetch origin main -q && git log --oneline -3 origin/main && git rev-list --count origin/main..HEAD && git rev-list --count HEAD..origin/main; sed -n '/### T-0019/,/^### T-00[2-9]/p' roadmap.md | head -60
```

</details>

<details><summary>結果: Bash: Compare branch with main and read T-0019</summary>

```text
8f6382c Merge pull request #43 from kittenkiki15/claude/clever-planck-pr5kq1
99d3871 A-0013 の複合のプロトコルでの写像の型を明記した（第 21 回のクロスモデルレビューの提案）
3ab1536 第 21 回のクロスモデルレビューに対応：まとめの同時読み出しの記述を同じプロトコルの並列の場合に限り、択一の組の名称を揃え、部分装置の事象の局所性を D-0013 の未解決の点に記録した
0
1
### T-0019 量子・古典・混成の実験の扱いの先行研究の調査（第 19 回に追加）

第 19 回に、ユーザーの判断で追加した。フレームワークの要件として、量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えるようにしたい（ユーザーの方針。量子重力理論への寄与という目的による）。T-0016 では、Le Cam の実験の理論（結果が古典的な記録の実験）と Ludwig の構成（有限個の効果による位相）を調べたが、この要件に直接答える部分は調べていない。

- 調べること（文献は記憶による。未確認。主な文献は arXiv にあるはず）：
  1. 一般化確率論（Hardy、Barrett、Chiribella–D'Ariano–Perinotti）：古典・量子・混成の状態空間と効果空間の区別、複合系の扱い、状態空間の再構成（T-0016 から移した）。[C-0003](conjectures/C-0003.md) との関係。
  2. Le Cam の理論の量子版（量子統計的実験の比較。Buscemi、Jenčová、松本、Guţă–Kahn の量子局所漸近正規性）。
  3. 量子参照系と量子時計（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）。T-0017 の「操作的な座標づけと参照系」と重なる部分は、ここでは次の問いに絞る。
  4. 逐次・適応的な実験の扱い（測定後の状態まで与える測定（instrument）の合成、量子コム（Chiribella–D'Ariano–Perinotti）・量子戦略（Gutoski–Watrous）・process tensor、チャネルの識別と推定での適応的な戦略と並列の戦略の違い）。(a) の立場で、適応的な設定（[D-0001](definitions/D-0001.md)）の結果の族の分布を、履歴を入力とする古典的な核の合成として書けるか。核で表す対象を、「固定した選び方の規則での記録の同時分布」と「選び方の規則を変えても整合する同じ過程の記述」に分けて調べる（実数値の有限個の結果なら、前者は通常の可測性の条件の下で条件付き分布の核に分解できるが、それだけでは後者を扱えるとは限らない。PR #43 のレビューの論点）。[D-0002](definitions/D-0002.md)（選び方の規則の定義域・可測性・無作為な選択）、[D-0004](definitions/D-0004.md)・[A-0006](assumptions/A-0006.md)・[D-0006](definitions/D-0006.md)（履歴を入力とする核）の未解決の点の材料にする（決めるのは T-0004〜T-0006）。適応的な設定は、(b) の判定基準の論点（量子的な出力を後の装置につなぐ場合）のうち、古典的な記録を次の装置へ渡す部分にあたる（第 21 回に、ユーザーの判断で加えた
…（以下 1866 文字を省略）
```

</details>

<details><summary>ツール: Bash: Reset work branch to main and check private repo</summary>

```text
git checkout -B claude/clever-planck-pr5kq1 origin/main -q && git log --oneline -1; cd ../point-free-spacetime-private && git fetch origin main -q && git status | head -2 && git rev-list --count origin/main..HEAD; git rev-list --count HEAD..origin/main; ls; ls papers | wc -l
```

</details>

<details><summary>結果: Bash: Reset work branch to main and check private repo</summary>

```text
8f6382c Merge pull request #43 from kittenkiki15/claude/clever-planck-pr5kq1
On branch claude/clever-planck-pr5kq1
nothing to commit, working tree clean
0
0
CLAUDE.md
README.md
notes
papers
redactions.txt
65
```

</details>

<details><summary>ツール: AskUserQuestion</summary>

```text
（入力の本文は省略。項目: questions）
```

</details>

<details><summary>結果: AskUserQuestion</summary>

```text
Your questions have been answered: "第 22 回は T-0019（量子・古典・混成の実験の扱いの先行研究の調査）を行います。調べることが 5 項目あり、1 回では原典で確かめきれないため、重点を決めたいと思います。どこから始めますか？"="判定基準の枠組みから (推奨)". You can now continue with these answers in mind.
```

</details>

<details><summary>ツール: Bash: Check arXiv access and existing tools</summary>

```text
cd /home/user/point-free-spacetime && curl -sS -o /dev/null -w "%{http_code}\n" https://arxiv.org/abs/0904.4483; ls surveys | tail -5; ls tools; cat ../point-free-spacetime-private/papers/README.md | head -20
```

</details>

<details><summary>結果: Bash: Check arXiv access and existing tools</summary>

```text
200
2026-09-30_16_merging-and-consistency.md
2026-09-30_17_comparison-of-experiments.md
2026-09-30_18_limit-topology.md
2026-09-30_20_agent-observer-apparatus.md
README.md
__pycache__
deps_graph.py
export_log.py
tests
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
| `hossenfelder2013.pdf` | Hossenfelder, Minimal length scale scenarios for q
…（以下 611 文字を省略）
```

</details>

<details><summary>ツール: Bash: Inspect previous survey format and references</summary>

```text
head -60 surveys/2026-09-30_20_agent-observer-apparatus.md; cat surveys/README.md | head -30; grep -c . references.bib; grep -n "^@" references.bib | tail -5
```

</details>

<details><summary>結果: Bash: Inspect previous survey format and references</summary>

```text
# 主体・観測者・装置・設定の既存研究での使われ方

- 作成：[2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md)（[T-0018](../roadmap.md)）
- 目的：T-0018 の (C)「主体・観測者・装置の使い分け」を決める前に、既存研究での語の使われ方を原典で確かめる。深さは、arXiv などの原典で該当する定義と説明を確かめ、短い調査メモにまとめる（ユーザーの判断）。
- 2 節は原典で確かめた内容である（要約。他者の文章の長い引用はしない）。3 節の対応表は 2 節の整理で、4 節は原典に書かれていない、プロジェクトへのつながりの候補（Claude の見立て）である。

## 1. 読んだ文献

いずれも arXiv 版で、該当する節の本文を確かめた。

| 引用キー | 文献 | 読んだ範囲 | 役割 |
| --- | --- | --- | --- |
| `fewster2020` | Fewster–Verch, Quantum fields and local measurements (2020) | 1 節、3 節の冒頭 | 系・プローブ・実験者、結合の領域 |
| `hardy2001` | Hardy, Quantum theory from five reasonable axioms (2001) | 2 節（Setting the scene）、3 節の冒頭 | 準備・変換・測定の装置と、つまみの設定 |
| `chiribella2010` | Chiribella–D'Ariano–Perinotti, Probabilistic theories with purification (2010) | 2 節 A（Systems and tests） | 操作的確率論の系と試験（test） |
| `brunner2014` | Brunner ほか, Bell nonlocality (2014) | 2 節の冒頭 | ベル実験の入力（測定の設定）と出力 |
| `fuchs2014` | Fuchs–Mermin–Schack, An introduction to QBism (2014) | 1〜2 節 | QBism の agent |
| `brukner2018` | Brukner, A no-go theorem for observer-independent facts (2018) | 1 節、2 節 B | Wigner の友人の「観測者」 |
| `rovelli1996` | Rovelli, Relational quantum mechanics (1996) | 2 節の冒頭（用語の注意と、系と観測者の区別） | 関係的量子力学の「観測者」 |
| `rovelli2002` | Rovelli, Partial observables (2002) | 1〜2 節 | 部分観測量と完全観測量、時計の読み |
| `giacomini2019` | Giacomini–Castro-Ruiz–Brukner, Quantum mechanics and the covariance of physical laws in quantum reference frames (2019) | 序論 | 量子参照系 |

第 18 回に確かめた Ludwig（`lud
…（以下 2335 文字を省略）
```

</details>

<details><summary>ツール: Bash: Download candidate arXiv papers</summary>

```text
cd /home/user/point-free-spacetime-private/papers && which pdftotext; grep -n "chiribella\|gutoski\|pollock\|harrow\|barrett\|hardy" ../../point-free-spacetime/references.bib | head; for id in 0904.4483 0712.1325 quant-ph/0611234 1512.00589 0909.0256 0803.3237 quant-ph/0508211; do f=$(echo $id | tr '/' '_'); curl -sSL -o /tmp/claude-0/$f.pdf https://arxiv.org/pdf/$id; echo "$id $(stat -c %s /tmp/claude-0/$f.pdf)"; done
```

</details>

<details><summary>結果: Bash: Download candidate arXiv papers</summary>

```text
/usr/bin/pdftotext
934:@misc{hardy2001,
941:@article{chiribella2010,
0904.4483 602175
0712.1325 133766
quant-ph/0611234 193708
1512.00589 2153339
0909.0256 119942
0803.3237 130967
quant-ph/0508211 435878
```

</details>

<details><summary>ツール: Bash: Move PDFs to scratchpad and extract text</summary>

```text
S=/tmp/claude-0/-home-user/[ID]/scratchpad; mkdir -p $S/p; mv /tmp/claude-0/*.pdf $S/p/; cd $S/p; for f in *.pdf; do pdftotext -layout $f ${f%.pdf}.txt; echo "$f $(wc -l < ${f%.pdf}.txt) $(pdfinfo $f | grep -E '^Title|^Pages' | tr '\n' ' ')"; done; head -40 0904.4483.txt
```

</details>

<details><summary>結果: Bash: Move PDFs to scratchpad and extract text</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Locate definitions and theorems in CDP 2009</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && for f in *.pdf; do pdftotext $f ${f%.pdf}.r.txt; done; grep -n -i "Definition\|Theorem\|Lemma\|Corollary\|^[IVX]*\. \|tester" 0904.4483.r.txt | head -120
```

</details>

<details><summary>結果: Bash: Locate definitions and theorems in CDP 2009</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read CDP 2009 normalization lemma and Born rule</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 580,700p 0904.4483.r.txt; echo ----; sed -n 890,990p 0904.4483.r.txt
```

</details>

<details><summary>結果: Bash: Read CDP 2009 normalization lemma and Born rule</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read realization theorems and testers in CDP 2009</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1395,1430p 0904.4483.r.txt; echo ----; sed -n 1815,2060p 0904.4483.r.txt
```

</details>

<details><summary>結果: Bash: Read realization theorems and testers in CDP 2009</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Check CDP finiteness and locate Gutoski-Watrous structure</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && grep -n -i "finite.dimension\|finite dimension\|infinite" 0904.4483.r.txt | head; echo ---GW; grep -n -i "Definition\|Theorem\|Proposition\|^[0-9]\.[0-9]* \|^[0-9] [A-Z]\|strateg" quant-ph_0611234.r.txt | head -80
```

</details>

<details><summary>結果: Bash: Check CDP finiteness and locate Gutoski-Watrous structure</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read Gutoski-Watrous intro and theorem list</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 24,93p quant-ph_0611234.r.txt; grep -n "^Theorem\|^Corollary" quant-ph_0611234.r.txt
```

</details>

<details><summary>結果: Bash: Read Gutoski-Watrous intro and theorem list</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read Gutoski-Watrous Theorems 5, 6, 9</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 488,560p quant-ph_0611234.r.txt; sed -n 600,660p quant-ph_0611234.r.txt
```

</details>

<details><summary>結果: Bash: Read Gutoski-Watrous Theorems 5, 6, 9</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read Harrow et al. 2010 abstract and intro</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1,120p 0909.0256.r.txt
```

</details>

<details><summary>結果: Bash: Read Harrow et al. 2010 abstract and intro</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read classical examples section in Harrow et al.</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && grep -n "^[0-9] [A-Z]\|^[0-9]\.[0-9] " 0909.0256.r.txt; awk 'NR>=380 && NR<=470' 0909.0256.r.txt
```

</details>

<details><summary>結果: Bash: Read classical examples section in Harrow et al.</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Verify Harrow et al. classical example 1 numbers</summary>

```text
cat > /tmp/claude-0/-home-user/[ID]/scratchpad/hhlw.py <<'EOF'
from fractions import Fraction as F
from itertools import product
M=[[[F(1,3),F(8,9)],[F(2,3),F(1,9)]],[[F(0),F(1,3)],[F(1),F(2,3)]]]  # M[a][j][k]
def succ(dists):  # dists[a]: dict outcome->prob, prior 1/2
    keys=set(dists[0])|set(dists[1])
    return sum(max(dists[0].get(x,0),dists[1].get(x,0)) for x in keys)/2
best_na=max(succ([{(j1,j2):M[a][j1][k1]*M[a][j2][k2] for j1 in range(2) for j2 in range(2)} for a in range(2)]) for k1 in range(2) for k2 in range(2))
best_ad=max(succ([{(j1,j2):M[a][j1][k]*M[a][j2][f[j1]] for j1 in range(2) for j2 in range(2)} for a in range(2)]) for k in range(2) for f in product(range(2),repeat=2))
print(best_na,best_ad)
EOF
python3 /tmp/claude-0/-home-user/[ID]/scratchpad/hhlw.py
```

</details>

<details><summary>結果: Bash: Verify Harrow et al. classical example 1 numbers</summary>

```text
68/81 139/162
```

</details>

<details><summary>ツール: Bash: Enumerate all strategies for example 1</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && cat >> hhlw.py <<'EOF'
for k1 in range(2):
  for k2 in range(2):
    print('na',k1,k2,succ([{(j1,j2):M[a][j1][k1]*M[a][j2][k2] for j1 in range(2) for j2 in range(2)} for a in range(2)]))
for k in range(2):
  for f in product(range(2),repeat=2):
    print('ad',k,f,succ([{(j1,j2):M[a][j1][k]*M[a][j2][f[j1]] for j1 in range(2) for j2 in range(2)} for a in range(2)]))
print('one-shot',[succ([{j:M[a][j][k] for j in range(2)} for a in range(2)]) for k in range(2)])
EOF
python3 hhlw.py
```

</details>

<details><summary>結果: Bash: Enumerate all strategies for example 1</summary>

```text
68/81 139/162
na 0 0 7/9
na 0 1 43/54
na 1 0 43/54
na 1 1 68/81
ad 0 (0, 0) 7/9
ad 0 (0, 1) 43/54
ad 0 (1, 0) 7/9
ad 0 (1, 1) 43/54
ad 1 (0, 0) 43/54
ad 1 (0, 1) 7/9
ad 1 (1, 0) 139/162
ad 1 (1, 1) 68/81
one-shot [Fraction(2, 3), Fraction(7, 9)]
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Bash: Check example 1 matrix in layout text and render page</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && grep -n -B3 -A12 "Example 1\." 0909.0256.txt | head -40; pdftoppm -f 7 -l 8 -r 80 -png 0909.0256.pdf pg
```

</details>

<details><summary>結果: Bash: Check example 1 matrix in layout text and render page</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Check arXiv versions of Harrow et al.</summary>

```text
curl -sS https://arxiv.org/abs/0909.0256 | grep -o -i "\[v[0-9]\][^<]*\|Journal ref[^<]*<[^>]*>[^<]*" | head; curl -sS https://arxiv.org/abs/0909.0256 | grep -A2 -i "jref" | head -5
```

</details>

<details><summary>結果: Bash: Check arXiv versions of Harrow et al.</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read CDP 2008 papers abstracts</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1,60p 0803.3237.r.txt; echo ======; sed -n 1,80p 0712.1325.r.txt
```

</details>

<details><summary>結果: Bash: Read CDP 2008 papers abstracts</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read process tensor paper abstract and key terms</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1,40p 1512.00589.r.txt; grep -n -i "comb\|Kolmogorov\|containment\|linear\b" 1512.00589.r.txt | head -30
```

</details>

<details><summary>結果: Bash: Read process tensor paper abstract and key terms</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read process tensor definition and properties</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 130,250p 1512.00589.r.txt
```

</details>

<details><summary>結果: Bash: Read process tensor definition and properties</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Locate Barrett's assumptions on composite systems</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1,30p quant-ph_0508211.r.txt; grep -n -i "Assumption\|^[IVX]*\. [A-Z]\|joint system\|composite\|local operations\|fiducial\|no.signal" quant-ph_0508211.r.txt | head -60
```

</details>

<details><summary>結果: Bash: Locate Barrett's assumptions on composite systems</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read Barrett's assumptions 1, 4, 5 and joint states</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 170,200p quant-ph_0508211.r.txt; sed -n 494,560p quant-ph_0508211.r.txt; sed -n 655,700p quant-ph_0508211.r.txt
```

</details>

<details><summary>結果: Bash: Read Barrett's assumptions 1, 4, 5 and joint states</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read Barrett Theorems 2-3 and entanglement definition</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 700,800p quant-ph_0508211.r.txt; grep -n -i "entangle\|separable" quant-ph_0508211.r.txt | head
```

</details>

<details><summary>結果: Bash: Read Barrett Theorems 2-3 and entanglement definition</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Fetch CDP 2010 and find conditioning</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && curl -sSL -o 0908.1583.pdf https://arxiv.org/pdf/0908.1583 && pdftotext 0908.1583.pdf 0908.1583.r.txt && head -3 0908.1583.r.txt && grep -n -i "condition\|classical control\|local discrimin\|coarse.grain\|refine" 0908.1583.r.txt | head -40
```

</details>

<details><summary>結果: Bash: Fetch CDP 2010 and find conditioning</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read causality and conditioned tests in CDP 2010</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1460,1500p 0908.1583.r.txt; sed -n 1680,1760p 0908.1583.r.txt; grep -n "Definition 3[0-9]\|Lemma\|Theorem [0-9]" 0908.1583.r.txt | sed -n 1,30p
```

</details>

<details><summary>結果: Bash: Read causality and conditioned tests in CDP 2010</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read no-signalling, local discriminability, local tomography</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && sed -n 1636,1650p 0908.1583.r.txt; sed -n 2060,2075p 0908.1583.r.txt; sed -n 2117,2130p 0908.1583.r.txt; grep -n -i "finite.dimension\|we assume\|finite set" 0908.1583.r.txt | head
```

</details>

<details><summary>結果: Bash: Read no-signalling, local discriminability, local tomography</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Read D-0001 definition</summary>

```text
cd /home/user/point-free-spacetime && wc -l definitions/D-0001.md && sed -n 1,200p definitions/D-0001.md
```

</details>

<details><summary>結果: Bash: Read D-0001 definition</summary>

```text
55 definitions/D-0001.md
# D-0001: 有限な実験

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [A-0002](../assumptions/A-0002.md)、[A-0003](../assumptions/A-0003.md) |
| 関係する予想・結果 | [C-0003](../conjectures/C-0003.md) |
| 初出 | [2026-09-28 第 08 回](../summaries/2026-09-28_08_observation-as-limit.md) |

## 定義

**有限な実験**とは、一つの実験プロトコル $`π`$ に従い、有限の期間に、有限回の操作と有限回の観測を行って、観測ごとに結果を読み出すものである。操作の回数と期間の有限性は、観測の回数によらず（$`N_e = 0`$ の実験でも）、実験全体について課す（PR #42 のレビューを受けて、第 19 回までの「有限回の操作」の条件を明記し直した）。一つの有限な実験 $`e`$ について、次を指定する。

- プロトコル $`π`$（有限の記述を持つ。[A-0002](../assumptions/A-0002.md)）
- 観測の回数 $`N_e ∈ ℕ`$（$`N_e = 0`$ も許す）
- 設定の族 $`(x_i)_{i=1}^{N_e}`$：$`x_i`$ は $`i`$ 回目の観測の設定で、プロトコル $`π`$ の設定の空間 $`X_π`$ の元。初期状態の条件と測定の条件を定める実数の組（[A-0003](../assumptions/A-0003.md)）
- 結果の族 $`(y_i)_{i=1}^{N_e}`$：$`y_i`$ は $`i`$ 回目の観測の結果で、結果の空間 $`Y_π`$ の元（実数の組。[A-0003](../assumptions/A-0003.md)）
- **装置**：その実験で、準備から結果の読み出しまでに使う物理系
- **観測者**：その実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うもの

添字 $`i`$ は観測を実行した順序を表す。各観測の結果の読み出しは、添字の順に、観測者の基準の時計で互いに異なる時刻に行う（複数の観測の結果を同時に読み出すことと、添字と逆の順に読み出すことは許さない）。設定 $`x_i`$ は、それまでの結果 $`y_1, …, y_{i-1}`$ に応じて選んでもよい（適応的な設定）。その場合は、選び方の規則もプロトコルの記述に含める。装置と観測者は、実験ごとに一つずつ定まる（実験と 1 対 1 に対応する）。

## 注意

- $`N_e = 0`$ の実験は、観測を 1 回も行わない、情報を与えない実験である。統計的実験の比較（Blackwell の順序、Le Cam の不足度）では、どの実験からも後処理で模倣できる最小の実験にあたる（Claude の補足）。ただし、観測を行わなくても、プロトコル・装置・観測者があり、時間や資源を使いうるので、実験を順につなぐ操作の単位元とは限らない（PR #42 のレビュー）。実験の最初の何回かの観測への制限（[A-0012](../assumptions/A-0012.md)）を繰り返したときの行き着く先でもある。
- $`Y_π`$ は 1 回の観測の結果の空間である。同じ実験の中の結果どうし
…（以下 3165 文字を省略）
```

</details>

## Claude

ここまでの節目として、原典で確かめた内容と、私の見立てを報告します。

#### 原典で確かめた内容（いずれも arXiv 版の本文）

**1. 量子コム（Chiribella–D'Ariano–Perinotti 2009、arXiv:0904.4483）**
- 量子回路をつないだネットワーク（有向非巡回グラフ）は、その入出力の系の上の正の演算子 $`R`$（Choi 演算子）一つで表せます。この演算子は、正規化の連鎖 $`\mathrm{Tr}_{2j-1} R^{(j)} = I_{2j-2} ⊗ R^{(j-1)}`$ を満たします（補題 4、系 1）。
- 逆に、この連鎖を満たす正の演算子は、どれも等長写像の列（記憶を持つ通信路）で実現できます（定理 3）。結果の付いた版（一般化された instrument）は、最後に補助系を測定すれば実現できます（定理 4・10）。
- テスター（tester）は、ネットワークを確率に写す最も一般の操作です。確率は一般化ボルン則 $`p(i \mid R) = \mathrm{Tr}[P_i^T R]`$ で与えられます（定義 11）。テスターの実現には、一般に補助系ともつれた状態の準備が要ります（定理 11・12）。
- 同じ Choi 演算子を持つネットワークは、入出力の関係だけを見る限り、実験で区別できません（38 式の後の記述）。

**2. 量子戦略（Gutoski–Watrous 2007、quant-ph/0611234）**：多ラウンドの戦略を一つの半正定値演算子で表します。戦略の集合は線形の制約で特徴づけられ（定理 6）、コンパクトで凸です（系 8）。結果の確率は内積 $`\langle Q_a, R_b \rangle`$ で与えられます（定理 5）。量子コムと同じ構造を、別々に得ています。

**3. process tensor（Pollock ほか 2018、arXiv:1512.00589）**：系に施す制御操作の列から出力の状態への写像です。線形性・完全正値性・包含（時刻の因果的な順序）の三つの性質を満たします。逆に、この三つを満たすものは、どれも補助系との開放系の発展で実現できます（定理 2）。原典自身が、量子コムとの関係を述べています。

**4. 条件付きの試験と因果性（Chiribella–D'Ariano–Perinotti 2010、arXiv:0908.1583）**
- 前の結果に応じて次の試験を選ぶこと（条件付きの試験。定義 29）は、因果的な理論でだけ正規化が保たれます。因果的とは、決定的な効果が一つに決まることで、「未来からの信号がない」ことにあたります（定義 27、補題 4）。
- 逆に、条件付きの試験をすべて許すと、理論は因果的になります（補題 7）。
- 局所的な識別可能性（local discriminability）は、局所トモグラフィー（local tomography）と同値です（定義 32、補題 13）。

**5. 一般化確率論の複合系（Barrett 2007、quant-ph/0508211）**
- 次の二つを仮定します。仮定 4：局所的な操作は可換（ここから信号の不在が従う）。仮定 5：複合系の状態は、各部分系で基準の測定（fiducial measurements）を同時に行ったときの同時確率で決まる。
- この二つから、状態空間はテンソル積 $`V_{AB} = V_A ⊗ V_B`$ になります（定理 1）。複合系の状態は積状態の実係数の線形結合で書けますが、凸結合で書けるとは限りません。凸結合で書けないものが、もつれた状態です（定理 2 とその後の説明）。
- もつれと非局所性（ベルの不等式の破れ）は別の概念です。
- 時空の自由度は古典的に扱い、時空の構造は使わない、と明記しています。

**6. 適応的な戦略と並列の戦略**
- Chiribella ほか 2008（arXiv:0803.3237）：記憶を持つ通信路を最適に識別するには、逐次の（因果的な）方式が要ります。独立な複数のユニタリーの通信路では、並列の方式で足ります。
- Harrow ほか 2010（arXiv:0909.0256）：エンタングルメント破壊通信路（entanglement-breaking channel）の対があり、適応的に 2 回使えば完全に識別できますが、非適応的に使う場合は、有限回では何回使っても完全には識別できません。古典的な通信路でも、使用回数を固定すれば適応的な戦略が有利な例を挙げています。
  - 例 1 を検算したところ、論文の値（非適応 7/9、適応 65/81）と合いませんでした。私の計算では非適応 68/81、適応 139/162 で、どちらも 2 回目の入力の取り方が論文と違います。適応的な方が有利という結論は同じです。arXiv は v1 だけで、出版社版は確認していません。

#### 見立て（Claude の見立て。原典には書かれていません）

**(i) 適応的な設定の二つの対象（roadmap の項目 4）**
- 古典的な有限の場合、「選び方の規則を変えても整合する同じ過程の記述」は、古典的なコムにあたります。古典的なコムとは、条件付き分布 $`p(y_1,…,y_n \mid x_1,…,x_n)`$ のうち、前の結果の周辺分布が後の設定によらないものです（量子コムの正規化の連鎖の古典版）。
- 「固定した規則での記録の同時分布」は、コムと規則（co-strategy）をつないだもの（link product）です。
- 古典的な場合、コムは各段の核 $`k_j(y_j \mid x_{\le j}, y_{<j})`$ の列と同じで、非適応的な（設定を固定した）実験の記録の分布の全体から決まります。この全体が分かれば、どの適応的な規則での分布も計算できます。
- それでも、使用回数を固定した課題では、適応的な規則が有利になりえます（Harrow ほか）。
- 条件付きの試験をすべて許すことが因果性と同値だという点（補題 7）は、[A-0016](assumptions/A-0016.md) の観測の間の順序（前の登録が次の準備より後にない）の前提に対応しそうです。

**(ii) (a)・(b) の判定基準**
- 一つの実験全体なら、量子的なつなぎ方を装置の中に含めて装置を大きく取れば、(a)（古典的な記録とモデルの組）でいつでも書けます。
- 失われるのは合成性です。部分装置を記録の水準の記述（古典的なコム）で表しても、部分装置を量子的につないだときの予測は決まりません。量子的なつなぎ方まで予測を決めるのは量子コムで、それを確かめる最も一般の操作がテスターです（もつれた補助系を要します）。
- そこで、判定基準は次のように定式化できそうです。「許す後の操作の類 $`𝒯`$ を決め、$`𝒯`$ のどの操作でも同じ確率を与える二つの記述を同じとみなす。$`𝒯`$ が古典的な記録を経由する操作だけなら (a) で足り、量子的な出力に直接働く操作を含めるなら、部分装置の記述に量子コム（= (b) の対象）が要る。」
- 中間の立場として、「実際の記録は古典的（(a)）で、可能な実験の層の部分装置のモデルを量子コムで表す」というものもありえます。

**(iii) 複合のプロトコル $`π^M`$（項目 5）**：Barrett の仮定 5 の下では、もつれを表すのに、部分装置ごとの基準の設定のすべての組 $`(x^1, …, x^M)`$ での同時分布の族が要ります（一つの設定では足りません）。もつれは、その族が、理論が許す積状態の凸結合で書けないことで判定します。ただし、局所トモグラフィーは複素数の量子論では成り立ち、実数の量子論では成り立ちません。

ここで方針を相談させてください。

<details><summary>ツール: AskUserQuestion</summary>

```text
（入力の本文は省略。項目: questions）
```

</details>

<details><summary>結果: AskUserQuestion</summary>

```text
Your questions have been answered: "この後の進め方をどうしますか？"="調査メモにまとめる (推奨)". You can now continue with these answers in mind.
```

</details>

<details><summary>ツール: Bash: Inspect bib entry formats and existing mentions</summary>

```text
sed -n 930,1020p references.bib; grep -n "^@" references.bib | wc -l; grep -n "chiribella\|gutoski\|pollock\|barrett\|harrow" -r --include=*.md . | grep -v logs/ | head
```

</details>

<details><summary>結果: Bash: Inspect bib entry formats and existing mentions</summary>

```text
address   = {Berlin},
  year      = {1985},
}

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

…（以下 1224 文字を省略）
```

</details>

<details><summary>ツール: Bash: Fetch journal refs from arXiv abstracts</summary>

```text
for id in 0904.4483 0712.1325 quant-ph/0611234 1512.00589 0909.0256 0803.3237 quant-ph/0508211; do echo "== $id"; curl -sS https://arxiv.org/abs/$id | grep -o 'tablecell jref">[^<]*\|tablecell doi">.*\|citation_title" content="[^"]*\|citation_date" content="[^"]*' | head -4; done
```

</details>

<details><summary>結果: Bash: Fetch journal refs from arXiv abstracts</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: List existing bib keys and papers README tail</summary>

```text
grep -o "^@[a-z]*{[^,]*" references.bib | sed 's/.*{//' | tr '\n' ' '; echo; tail -15 ../point-free-spacetime-private/papers/README.md
```

</details>

<details><summary>結果: Bash: List existing bib keys and papers README tail</summary>

```text
johnstone1982 johnstone1983 picado2012 vickers1989 mckinsey1944 goldblatt1980 christensen2005 heunen2024 heunen2026 birkhoff1936 isham1998 heunen2009 vanderschaaf2024 arntzenius2003 jonsson1951 halvorson2001 doplicher1995 hossenfelder2013 derudder2020 heijmans1990 zeeman1962 connes2021 connes2022 dandrea2022 vakarelov2020 casini2002 cegla1977 sorkin1993 fewster2020 bostelmann2021 borsten2021 hossenfelder2006 dowker2004 bombelli2009 sorkin2007 halvorson2002 amelinocamelia2011 halvorson2001rs fewster2016 naaijkens2012 landsman2005 buchholz2001 morinelli2018 spitters2014 buchholz1986nuclear buchholz1987universal dantoni1987 dantoni1983 doplicher1983 fewster2015 doplicher1984 buchholz1986noether hepp1972 giry1982 lawvere1963 fritz2020 cho2019 fritz2020infinite fritz2021definetti fritz2023representable brunetti2003 porst1991 caves2002definetti caves2002bayes schack2001bayes fuchs2009priors fuchs2013 blackwell1962 diaconis1986 pomatto2014 vovk2023 miller2018 choi2008 kleijn2019 blackwell1951 blackwell1953 lecam1964 shannon1958 raginsky2011 lecam1972 vandervaart2002 torgersen1970 ludwig1968 ludwig1985 hardy2001 chiribella2010 brunner2014 fuchs2014 brukner2018 rovelli1996 rovelli2002 giacomini2019 
| `lecam1964.pdf` | Le Cam, Sufficiency and approximate sufficiency (1964) | 出版社版（JSTOR。Ann. Math. Statist. 35, 1419–1455。ユーザーが入手） |
| `shannon1958.pdf` | Shannon, A note on a partial ordering for communication channels (1958) | 出版社版（Information and Control 1, 390–397。ユーザーが入手） |
| `raginsk
…（以下 1969 文字を省略）
```

</details>

<details><summary>ツール: Bash: Identify arXiv versions of downloaded PDFs</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && for f in *.pdf; do echo "$f: $(grep -m1 -o 'arXiv:[^ ]*v[0-9]*  *\[[a-z-]*\]  *[0-9]* [A-Za-z]* [0-9]*' ${f%.pdf}.r.txt)"; done; cmp 0908.1583.pdf /home/user/point-free-spacetime-private/papers/chiribella2010.pdf && echo same
```

</details>

<details><summary>結果: Bash: Identify arXiv versions of downloaded PDFs</summary>

（論文の本文の抜粋を含む出力のため、公開版では省略した。内容の要約は [調査メモ](../surveys/2026-10-01_22_combs-and-composites.md) を参照）

</details>

<details><summary>ツール: Bash: Get remaining versions and copy PDFs to private repo</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/p && grep -m2 -o "quant-ph/0508211v[0-9][^\n]*" quant-ph_0508211.r.txt; grep -m1 -o "quant-ph/0611234v[0-9].*" quant-ph_0611234.r.txt; grep -m1 -i "Dated\|^(Dated" 1512.00589.r.txt; P=/home/user/point-free-spacetime-private/papers; cp 0904.4483.pdf $P/chiribella2009.pdf; cp 0712.1325.pdf $P/chiribella2008architecture.pdf; cp 0803.3237.pdf $P/chiribella2008memory.pdf; cp quant-ph_0611234.pdf $P/gutoski2007.pdf; cp 1512.00589.pdf $P/pollock2018.pdf; cp 0909.0256.pdf $P/harrow2010.pdf; cp quant-ph_0508211.pdf $P/barrett2007.pdf; ls $P | wc -l
```

</details>

<details><summary>結果: Bash: Get remaining versions and copy PDFs to private repo</summary>

```text
quant-ph/0508211v3 30 Nov 2006
quant-ph/0611234v2 2 Apr 2007
(Dated: February 1, 2018)
72
Shell cwd was reset to /home/user
```

</details>

## Claude

論文の PDF を非公開リポジトリに置き、参考文献一覧と調査メモを書いているところです。

<details><summary>ツール: Bash: Register papers in private README and references.bib</summary>

```text
cd /home/user/point-free-spacetime-private && cat >> papers/README.md <<'EOF'
| `chiribella2009.pdf` | Chiribella–D'Ariano–Perinotti, Theoretical framework for quantum networks (2009) | arXiv:0904.4483v2（第 22 回に取得。Phys. Rev. A 80, 022339） |
| `chiribella2008architecture.pdf` | Chiribella–D'Ariano–Perinotti, Quantum circuit architecture (2008) | arXiv:0712.1325v1（第 22 回に取得。Phys. Rev. Lett. 101, 060401） |
| `chiribella2008memory.pdf` | Chiribella–D'Ariano–Perinotti, Memory effects in quantum channel discrimination (2008) | arXiv:0803.3237v3（第 22 回に取得。Phys. Rev. Lett. 101, 180501） |
| `gutoski2007.pdf` | Gutoski–Watrous, Toward a general theory of quantum games (2007) | arXiv:quant-ph/0611234v2（第 22 回に取得。Proc. STOC 2007, 565–574） |
| `pollock2018.pdf` | Pollock ほか, Non-Markovian quantum processes: complete framework and efficient characterization (2018) | arXiv:1512.00589v3（第 22 回に取得。Phys. Rev. A 97, 012127） |
| `harrow2010.pdf` | Harrow–Hassidim–Leung–Watrous, Adaptive versus nonadaptive strategies for quantum channel discrimination (2010) | arXiv:0909.0256v1（第 22 回に取得。Phys. Rev. A 81, 032339） |
| `barrett2007.pdf` | Barrett, Information processing in generalized probabilistic theories (2007) | arXiv:quant-ph/0508211v3（第 22 回に取得。Phys. Rev. A 75, 032304） |
EOF
cd /home/user/point-free-spacetime && cat >> references.bib <<'EOF'

@article{chiribella2009,
  author  = {Chiribella, Giulio and D'Ariano, Giacomo Mauro and Perinotti, Paolo},
  title   = {Theoretical framework for quantu
…（以下 2355 文字を省略）
```

</details>

<details><summary>結果: Bash: Register papers in private README and references.bib</summary>

```text
0000300   2   1   1   }   ,  \n   }  \n
0000310
```

</details>

<details><summary>ツール: Bash: Find adaptive-related unresolved points in related files</summary>

```text
for f in definitions/D-0002.md definitions/D-0004.md assumptions/A-0006.md definitions/D-0006.md definitions/D-0013.md assumptions/A-0016.md; do echo "=== $f"; head -8 $f | sed -n 1p; grep -n "適応\|核\|T-0019\|確率的な較正" $f | head -12; done
```

</details>

<details><summary>結果: Bash: Find adaptive-related unresolved points in related files</summary>

```text
=== definitions/D-0002.md
# D-0002: 実際の実験と可能な実験
13:- **可能な実験**：プロトコル $`π`$、観測の回数 $`N`$、設定の族 $`(x_i)_{i=1}^{N}`$（$`x_i ∈ X_π`$）の組 $`(π, N, (x_i))`$。適応的な設定（[D-0001](D-0001.md)）の場合は、設定の族の代わりに、それまでの結果から設定を選ぶ規則を指定する。一般に非可算個ある。
15:- 実際の実験 $`e`$ から、結果の族・装置・観測者を忘れて、プロトコル・観測の回数・設定の族（適応的な場合は選び方の規則）だけを残す対応で、$`e`$ に一つの可能な実験が対応する。「実際の実験は可能な実験でもある」は、この対応の意味で用いる（PR #42 のレビュー）。
27:- 適応的な設定を選ぶ規則の定義域と可測性：各履歴から $`X_π`$ への規則を、どの履歴の上で定義するか、可測性を課すか、無作為に設定を選ぶ場合を含めるか（結果の族の分布を核から作る段階で要る。[D-0006](D-0006.md)。ロードマップの T-0005 などで決める。逐次・適応的な実験の先行研究での扱いは T-0019 で調べる。PR #42 のレビューの論点）。
=== definitions/D-0004.md
# D-0004: 応答関数
23:- 応答関数は、1 回の観測、または前の観測の履歴によらずに準備し直す観測の結果の統計である。複数回の観測で結果が前の結果に依存する場合は、履歴を入力とする核が別に要る（[A-0006](../assumptions/A-0006.md) の未解決の点。第 20 回に、実験に複数回の観測と適応的な設定を入れたのに合わせて明記した。PR #42 のレビュー）。
=== assumptions/A-0006.md
# A-0006: 実験の等価原理（連続性の形）
13:同一の実験プロトコルでは、設定が近ければ、結果の統計も近い。つまり、各プロトコル $`π`$ について、応答関数（[D-0004](../definitions/D-0004.md)）の写像 $`p_π : X_π → \mathrm{Prob}(Y_π)`$ は連続である。ここで $`p_π`$ は、1 回の観測、または前の観測の履歴によらずに準備し直す観測の結果の統計である（第 20 回に、実験に複数回の観測と適応的な設定を入れたのに合わせて限定した。PR #42 のレビュー）。
28:- 複数回の観測で、結果が前の結果に依存する場合（適応的な設定や、準備し直さない観測）。$`i`$ 回目の結果の分布を、$`(x_1, …, x_i, y_1, …, y_{i-1})`$ を入力とする核として別に定め（[D-0006](../definitions/D-0006.md) の未解決の点と共通）、その核に連続性を課すかを、この前提とは区別して決める（PR #42 のレビュー）。核の形（古典的な核の合成で足りるか）の材料は、T-0019 で逐次・適応的な実験の先行研究を調べて集める。
=== definitions/D-0006.md
# D-0006: 可能な観測量
21:- 極限の取り方。可能な実験はプロトコルと設定の族 $`(π, N, (x_i))`$ だけで結果の記録を含まないので、実際の観測量（[D-0005](D-0005.md)）と同じ形（データで更新した事後分布の極限）にはできない。可能
…（以下 2095 文字を省略）
```

</details>

<details><summary>ツール: Bash: Read math guide and summaries format</summary>

```text
sed -n 1,80p docs/math-guide.md | head -80; cat summaries/README.md | head -40
```

</details>

<details><summary>結果: Bash: Read math guide and summaries format</summary>

`````text
# GitHub で数式を書くときのガイド

別のリポジトリで数式のテストページを Firefox と Chrome で表示して確認した結果をもとにした、書き方のルールです。

## ルール一覧

| 用途 | 推奨する書き方 | 避ける書き方 |
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

## 理由

### ブロック数式は ` ```math ` を使う

`$$...$$` の中では、Markdown が先にバックスラッシュを処理してしまうことがあります。
例えば `f(x)\,dx` は、`$$...$$` だと `f(x), dx` と表示されました。
` ```math ` なら、書いたとおりに表示されます。

````markdown
```math
\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}
```
````

```math
\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}
```

### ` ```math ` は箇条書きの中で字下げしない

箇条書きの項目の続きとして字下げして書いた ` ```math ` は、数式として表示されず、普通のコードブロックになりました（第 02 回の調査メモで確認）。
ブロック数式は、箇条書きの外に、字下げせずに書きます。

````markdown
- フレームでは、次の分配律が成り立つ。

```math
a ∧ ⋁_{i ∈ I} b_i = ⋁_{i ∈ I} (a ∧ b_i)
```

- この分配律は Lean で検証した。
````

### インライン数式は `` $`...`$ `` を使う

今回のテストでは `$...$` も崩れませんでした。
ただし `_` や `*` を含む式では Markdown の強調記号と衝突するおそれがあるため、`` $`...`$ `` の方が安全です。

```markdown
添字を含む式 $`a_1 * b_1 + a_2
…（以下 622 文字を省略）
`````

</details>

<details><summary>ツール: Write: /home/user/point-free-spacetime/surveys/2026-10-01_22_combs-and-composites.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/surveys/2026-10-01_22_combs-and-composites.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/surveys/2026-10-01_22_combs-and-composites.md (file state is current in your context — no need to Read it back)
```

</details>

## Claude

調査メモの草稿を [`surveys/2026-10-01_22_combs-and-composites.md`](point-free-spacetime/surveys/2026-10-01_22_combs-and-composites.md) に書きました。PDF 7 件は非公開リポジトリに置き、参考文献一覧（`references.bib`）にも登録しました。

構成は次のとおりです。
- 1 節：読んだ文献 8 件と、読んだ範囲。
- 2 節：原典で確かめた内容（量子コム、量子戦略、process tensor、条件付きの試験と因果性、Barrett の複合系、適応的な方式と並列の方式）。
- 3 節：判定基準の整理（見立て）。予測が同じかどうかは「許す後の操作の類 $`𝒯`$」で決まる、と整理しました。一つの実験全体なら (a) でいつでも書けますが、(a) では部分の記述が量子的な合成の下で閉じません。そのため、(a)・(b) の違いは「部分の記述を、量子的な合成の下で閉じたものにするか」にある、としました。中間の立場（記録は古典的なまま、量子コムを可能な実験のモデルの側に置く）も挙げています。
- 4 節：プロジェクトへのつながり（見立て）。
  - 4.1：適応的な設定は古典的なコム（核の列）で表せます。(a) の立場では、[A-0006](point-free-spacetime/assumptions/A-0006.md)・[D-0006](point-free-spacetime/definitions/D-0006.md) の問い「古典的な核の合成で足りるか」には「足りる」が答えの候補になります。因果性の前提の候補も挙げました。
  - 4.2：$`π^M`$ でもつれを表すには、基準の設定のすべての組合せでの同時分布の族が要ります。
  - 4.3：逐次の測定を最後にまとめて読み出す場合は、テスターとして扱えます。
- Harrow ほか 2010 の例 1 は、論文の数値と私の検算が合わなかったことを、2.6 節に記録しました（結論は変わりません）。

セッションの終わりには、ここから次の記録と更新を行う予定です。
- 定義・前提の未解決の点：D-0001、D-0002、A-0006、D-0006、D-0013 に、メモの該当節への参照を加えます。
- `roadmap.md`：T-0019 の進み具合を記録します（項目 4・1 は済み、項目 2・3 は残り）。
- `NEXT.md`：次回は T-0019 の続き（項目 2・3）にします。

草稿についてご意見があれば直します。このまま対話を終えてよければ、終了を告げてください。終えたら、ログ・まとめ・関連ファイルの更新と PR の作成に進みます。

<details><summary>ツール: Bash: Commit and push draft work in both repos</summary>

```text
git add -A && git commit -q -m "第 22 回（途中）：T-0019 の項目 4・1 の調査メモの草稿と参考文献を追加した

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: [セッション URL]" && git push -q -u origin claude/clever-planck-pr5kq1 2>&1 | tail -2; cd ../point-free-spacetime-private && git checkout -q -B claude/clever-planck-pr5kq1 origin/main && git add -A && git commit -q -m "第 22 回：量子コム・一般化確率論の論文 7 件の PDF を追加した

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: [セッション URL]" && git push -q -u origin claude/clever-planck-pr5kq1 2>&1 | tail -2; git log --oneline -1; cd ../point-free-spacetime && git status -s | head
```

</details>

<details><summary>結果: Bash: Commit and push draft work in both repos</summary>

```text
remote:      https://github.com/kittenkiki15/point-free-spacetime/pull/new/claude/clever-planck-pr5kq1        
remote: 
remote:      https://github.com/kittenkiki15/point-free-spacetime-private/pull/new/claude/clever-planck-pr5kq1        
remote: 
82b7619 第 22 回：量子コム・一般化確率論の論文 7 件の PDF を追加した
```

</details>

## Claude

作業が失われないよう、ここまでの変更を両方のリポジトリの作業ブランチ `claude/clever-planck-pr5kq1` にコミットして push しました。
- 公開側：調査メモの草稿と、`references.bib` に加えた 7 件。
- 非公開側：PDF 7 件と、`papers/README.md` の一覧への追記。

PR はまだ作っていません。対話ログ・まとめ・関連ファイルの更新も、まだ行っていません。対話の終了を告げていただいたら、これらを行ってから PR を作ります。調査メモの草稿についてご意見があれば、先に直します。

<details><summary>ツール: mcp__claude-code-remote__delete_trigger</summary>

```text
（入力の本文は省略。項目: trigger_id）
```

</details>

<details><summary>結果（エラー）: mcp__claude-code-remote__delete_trigger</summary>

```text
failed to delete trigger: the requested resource was not found
```

</details>

## Claude

PR [kittenkiki15/point-free-spacetime#43](https://github.com/kittenkiki15/point-free-spacetime/pull/43) がマージされたので、第 21 回のセッションはこれで終わりです。PR の通知の受け取りは、マージで自動的に止まりました。PR の確認のために入れていた予定を取り消そうとしたところ、その予定は既に見つかりませんでした。

次のセッション（第 22 回）では、`NEXT.md` にあるとおり、T-0019「量子・古典・混成の実験の扱いの先行研究の調査」を扱います。今回加えた調べること（項目 4 の逐次・適応的な実験、項目 5 の複合のプロトコル）も含みます。`/clear` の後は、`NEXT.md` から始めてください。

ありがとうございました。

## ユーザー

ここで対話を終了したいと思います。

## Claude

PR [kittenkiki15/point-free-spacetime#43](https://github.com/kittenkiki15/point-free-spacetime/pull/43) がマージされたので、運用に従い第 21 回のセッションをここで終えます。

- **今回の成果**：
  - 適応的な設定の扱いを整理し、T-0019 の調査項目に加えました。
  - A-0012・A-0016・D-0013 の未解決の点のうち、ユーザーの判断で決められたものを解消しました。
  - 前提の「択一の組と体系」の運用を入れ、A-0014・A-0015 を採用にしました。
  - 同時読み出しを除き、並列の観測を複合のプロトコル π^M で表すことにしました。
- **次のセッション（第 22 回）**：T-0019「量子・古典・混成の実験の扱いの先行研究の調査」です。`NEXT.md` に記録してあります。後に回した論点（異なるプロトコルの部分装置の同時読み出しなど）は、各ファイルの「未解決の点」と T-0019 の節にあります。
- **PR の確認の予定**：12:01 UTC に入れていた PR の確認の予定は、取り消そうとしたところ「見つからない」と返りました。既に消えている可能性がありますが、確かめられていません。もし届いても、PR はマージ済みなので対応は要りません。

`/clear` でコンテキストを初期化してから、次のセッションを始めてください。ありがとうございました。

## ユーザー

対話を終えて、ログ・まとめ・関連ファイルの更新と PR の作成に進んでください。

会話の履歴が失われているようなので、前回のターンのあなたの回答を以下に再掲します。
***
Chiribella–D'Ariano–Perinotti (2009) をarXivから取得し、定理の仮定と結論を確認しています。続けてGutoski–Watrous、Harrowらの適応的・並列戦略の論文、Barrettの一般化確率論の論文を読みます。
Gutoski–Watrousの量子戦略の表現定理（定理5・6）を確認しました。次は適応的戦略と並列戦略の違い（Harrowほか2010、Chiribellaほか2008）を読みます。
Harrow et al. 2010の通信路の例1をPythonで検算したところ、論文の数値（7/9、65/81）と私の計算結果（68/81、139/162）が一致しませんでした。arXiv版の原文を確認してみます。
ここまでの節目として、原典で確かめた内容と、私の見立てを報告します。
原典で確かめた内容（いずれも arXiv 版の本文）
1. 量子コム（Chiribella–D'Ariano–Perinotti 2009、arXiv:0904.4483）

* 量子回路をつないだネットワーク（有向非巡回グラフ）は、その入出力の系の上の正の演算子 $`R`$（Choi 演算子）一つで表せます。この演算子は、正規化の連鎖 $`\mathrm{Tr}_{2j-1} R^{(j)} = I_{2j-2} ⊗ R^{(j-1)}`$ を満たします（補題 4、系 1）。
* 逆に、この連鎖を満たす正の演算子は、どれも等長写像の列（記憶を持つ通信路）で実現できます（定理 3）。結果の付いた版（一般化された instrument）は、最後に補助系を測定すれば実現できます（定理 4・10）。
* テスター（tester）は、ネットワークを確率に写す最も一般の操作です。確率は一般化ボルン則 $`p(i \mid R) = \mathrm{Tr}[P_i^T R]`$ で与えられます（定義 11）。テスターの実現には、一般に補助系ともつれた状態の準備が要ります（定理 11・12）。
* 同じ Choi 演算子を持つネットワークは、入出力の関係だけを見る限り、実験で区別できません（38 式の後の記述）。

2. 量子戦略（Gutoski–Watrous 2007、quant-ph/0611234）：多ラウンドの戦略を一つの半正定値演算子で表します。戦略の集合は線形の制約で特徴づけられ（定理 6）、コンパクトで凸です（系 8）。結果の確率は内積 $`\langle Q_a, R_b \rangle`$ で与えられます（定理 5）。量子コムと同じ構造を、別々に得ています。
3. process tensor（Pollock ほか 2018、arXiv:1512.00589）：系に施す制御操作の列から出力の状態への写像です。線形性・完全正値性・包含（時刻の因果的な順序）の三つの性質を満たします。逆に、この三つを満たすものは、どれも補助系との開放系の発展で実現できます（定理 2）。原典自身が、量子コムとの関係を述べています。
4. 条件付きの試験と因果性（Chiribella–D'Ariano–Perinotti 2010、arXiv:0908.1583）

* 前の結果に応じて次の試験を選ぶこと（条件付きの試験。定義 29）は、因果的な理論でだけ正規化が保たれます。因果的とは、決定的な効果が一つに決まることで、「未来からの信号がない」ことにあたります（定義 27、補題 4）。
* 逆に、条件付きの試験をすべて許すと、理論は因果的になります（補題 7）。
* 局所的な識別可能性（local discriminability）は、局所トモグラフィー（local tomography）と同値です（定義 32、補題 13）。

5. 一般化確率論の複合系（Barrett 2007、quant-ph/0508211）

* 次の二つを仮定します。仮定 4：局所的な操作は可換（ここから信号の不在が従う）。仮定 5：複合系の状態は、各部分系で基準の測定（fiducial measurements）を同時に行ったときの同時確率で決まる。
* この二つから、状態空間はテンソル積 $`V_{AB} = V_A ⊗ V_B`$ になります（定理 1）。複合系の状態は積状態の実係数の線形結合で書けますが、凸結合で書けるとは限りません。凸結合で書けないものが、もつれた状態です（定理 2 とその後の説明）。
* もつれと非局所性（ベルの不等式の破れ）は別の概念です。
* 時空の自由度は古典的に扱い、時空の構造は使わない、と明記しています。

6. 適応的な戦略と並列の戦略

* Chiribella ほか 2008（arXiv:0803.3237）：記憶を持つ通信路を最適に識別するには、逐次の（因果的な）方式が要ります。独立な複数のユニタリーの通信路では、並列の方式で足ります。
* Harrow ほか 2010（arXiv:0909.0256）：エンタングルメント破壊通信路（entanglement-breaking channel）の対があり、適応的に 2 回使えば完全に識別できますが、非適応的に使う場合は、有限回では何回使っても完全には識別できません。古典的な通信路でも、使用回数を固定すれば適応的な戦略が有利な例を挙げています。
   * 例 1 を検算したところ、論文の値（非適応 7/9、適応 65/81）と合いませんでした。私の計算では非適応 68/81、適応 139/162 で、どちらも 2 回目の入力の取り方が論文と違います。適応的な方が有利という結論は同じです。arXiv は v1 だけで、出版社版は確認していません。

見立て（Claude の見立て。原典には書かれていません）
(i) 適応的な設定の二つの対象（roadmap の項目 4）

* 古典的な有限の場合、「選び方の規則を変えても整合する同じ過程の記述」は、古典的なコムにあたります。古典的なコムとは、条件付き分布 $`p(y_1,…,y_n \mid x_1,…,x_n)`$ のうち、前の結果の周辺分布が後の設定によらないものです（量子コムの正規化の連鎖の古典版）。
* 「固定した規則での記録の同時分布」は、コムと規則（co-strategy）をつないだもの（link product）です。
* 古典的な場合、コムは各段の核 $`k_j(y_j \mid x_{\le j}, y_{<j})`$ の列と同じで、非適応的な（設定を固定した）実験の記録の分布の全体から決まります。この全体が分かれば、どの適応的な規則での分布も計算できます。
* それでも、使用回数を固定した課題では、適応的な規則が有利になりえます（Harrow ほか）。
* 条件付きの試験をすべて許すことが因果性と同値だという点（補題 7）は、A-0016 の観測の間の順序（前の登録が次の準備より後にない）の前提に対応しそうです。

(ii) (a)・(b) の判定基準

* 一つの実験全体なら、量子的なつなぎ方を装置の中に含めて装置を大きく取れば、(a)（古典的な記録とモデルの組）でいつでも書けます。
* 失われるのは合成性です。部分装置を記録の水準の記述（古典的なコム）で表しても、部分装置を量子的につないだときの予測は決まりません。量子的なつなぎ方まで予測を決めるのは量子コムで、それを確かめる最も一般の操作がテスターです（もつれた補助系を要します）。
* そこで、判定基準は次のように定式化できそうです。「許す後の操作の類 $`𝒯`$ を決め、$`𝒯`$ のどの操作でも同じ確率を与える二つの記述を同じとみなす。$`𝒯`$ が古典的な記録を経由する操作だけなら (a) で足り、量子的な出力に直接働く操作を含めるなら、部分装置の記述に量子コム（= (b) の対象）が要る。」
* 中間の立場として、「実際の記録は古典的（(a)）で、可能な実験の層の部分装置のモデルを量子コムで表す」というものもありえます。

(iii) 複合のプロトコル $`π^M`$（項目 5）：Barrett の仮定 5 の下では、もつれを表すのに、部分装置ごとの基準の設定のすべての組 $`(x^1, …, x^M)`$ での同時分布の族が要ります（一つの設定では足りません）。もつれは、その族が、理論が許す積状態の凸結合で書けないことで判定します。ただし、局所トモグラフィーは複素数の量子論では成り立ち、実数の量子論では成り立ちません。
ここで方針を相談させてください。
論文の PDF を非公開リポジトリに置き、参考文献一覧と調査メモを書いているところです。
調査メモの草稿を `surveys/2026-10-01_22_combs-and-composites.md` に書きました。PDF 7 件は非公開リポジトリに置き、参考文献一覧（`references.bib`）にも登録しました。
構成は次のとおりです。

* 1 節：読んだ文献 8 件と、読んだ範囲。
* 2 節：原典で確かめた内容（量子コム、量子戦略、process tensor、条件付きの試験と因果性、Barrett の複合系、適応的な方式と並列の方式）。
* 3 節：判定基準の整理（見立て）。予測が同じかどうかは「許す後の操作の類 $`𝒯`$」で決まる、と整理しました。一つの実験全体なら (a) でいつでも書けますが、(a) では部分の記述が量子的な合成の下で閉じません。そのため、(a)・(b) の違いは「部分の記述を、量子的な合成の下で閉じたものにするか」にある、としました。中間の立場（記録は古典的なまま、量子コムを可能な実験のモデルの側に置く）も挙げています。
* 4 節：プロジェクトへのつながり（見立て）。
   * 4.1：適応的な設定は古典的なコム（核の列）で表せます。(a) の立場では、A-0006・D-0006 の問い「古典的な核の合成で足りるか」には「足りる」が答えの候補になります。因果性の前提の候補も挙げました。
   * 4.2：$`π^M`$ でもつれを表すには、基準の設定のすべての組合せでの同時分布の族が要ります。
   * 4.3：逐次の測定を最後にまとめて読み出す場合は、テスターとして扱えます。
* Harrow ほか 2010 の例 1 は、論文の数値と私の検算が合わなかったことを、2.6 節に記録しました（結論は変わりません）。

セッションの終わりには、ここから次の記録と更新を行う予定です。

* 定義・前提の未解決の点：D-0001、D-0002、A-0006、D-0006、D-0013 に、メモの該当節への参照を加えます。
* `roadmap.md`：T-0019 の進み具合を記録します（項目 4・1 は済み、項目 2・3 は残り）。
* `NEXT.md`：次回は T-0019 の続き（項目 2・3）にします。

草稿についてご意見があれば直します。このまま対話を終えてよければ、終了を告げてください。終えたら、ログ・まとめ・関連ファイルの更新と PR の作成に進みます。
作業が失われないよう、ここまでの変更を両方のリポジトリの作業ブランチ `claude/clever-planck-pr5kq1` にコミットして push しました。

* 公開側：調査メモの草稿と、`references.bib` に加えた 7 件。
* 非公開側：PDF 7 件と、`papers/README.md` の一覧への追記。

PR はまだ作っていません。対話ログ・まとめ・関連ファイルの更新も、まだ行っていません。対話の終了を告げていただいたら、これらを行ってから PR を作ります。調査メモの草稿についてご意見があれば、先に直します。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git status --short | head; git log --oneline -5; git fetch -q origin main && git log --oneline -3 origin/main; git diff --stat origin/main...HEAD | tail -3; ls surveys | tail -3; cd ../point-free-spacetime-private && git status --short | head; git log --oneline -3; git fetch -q origin main; git log --oneline -2 origin/main; git diff --stat origin/main...HEAD | tail -2
```

</details>

<details><summary>結果: Bash</summary>

```text
0bf5e58 第 22 回（途中）：T-0019 の項目 4・1 の調査メモの草稿と参考文献を追加した
8f6382c Merge pull request #43 from kittenkiki15/claude/clever-planck-pr5kq1
99d3871 A-0013 の複合のプロトコルでの写像の型を明記した（第 21 回のクロスモデルレビューの提案）
3ab1536 第 21 回のクロスモデルレビューに対応：まとめの同時読み出しの記述を同じプロトコルの並列の場合に限り、択一の組の名称を揃え、部分装置の事象の局所性を D-0013 の未解決の点に記録した
bfb5d13 D-0001 の異種の部分装置の同時読み出しの扱いを、ユーザーの判断で後に回したと記録した
8f6382c Merge pull request #43 from kittenkiki15/claude/clever-planck-pr5kq1
99d3871 A-0013 の複合のプロトコルでの写像の型を明記した（第 21 回のクロスモデルレビューの提案）
3ab1536 第 21 回のクロスモデルレビューに対応：まとめの同時読み出しの記述を同じプロトコルの並列の場合に限り、択一の組の名称を揃え、部分装置の事象の局所性を D-0013 の未解決の点に記録した
 references.bib                                |  76 +++++++++++++++
 surveys/2026-10-01_22_combs-and-composites.md | 135 ++++++++++++++++++++++++++
 2 files changed, 211 insertions(+)
2026-09-30_20_agent-observer-apparatus.md
2026-10-01_22_combs-and-composites.md
README.md
82b7619 第 22 回：量子コム・一般化確率論の論文 7 件の PDF を追加した
97555ba Merge pull request #12 from kittenkiki15/claude/zealous-keller-o7r1sv
100e614 第 20 回：主体・観測者・装置の用語の調査で読んだ arXiv 版の論文 8 件を追加
97555ba Merge pull request #12 from kittenkiki15/claude/zealous-keller-o7r1sv
100e614 第 20 回：主体・観測者・装置の用語の調査で読んだ arXiv 版の論文 8 件を追加
 papers/pollock2018.pdf                | Bin 0 -> 2153339 bytes
 8 files changed, 7 insertions(+)
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && cat surveys/2026-10-01_22_combs-and-composites.md; ls -la ~/.claude/projects/*/ | head
```

</details>

<details><summary>結果: Bash</summary>

```text
# 逐次・適応的な実験と複合系：量子コムと一般化確率論

- 作成：[2026-10-01 第 22 回](../summaries/2026-10-01_22_combs-and-composites.md)（[T-0019](../roadmap.md)）
- 目的：T-0019 の問い（「量子的な観測」を (a) 古典的な記録と読むか、(b) 量子的な出力を実験の対象に含めると読むか）について、「書き直せる」の判定基準を明確にする材料を集める。ユーザーの判断で、T-0019 の調べることのうち、項目 4（逐次・適応的な実験の扱い）と項目 1（一般化確率論の複合系）を先に原典で確かめた。項目 2（Le Cam の理論の量子版）と項目 3（量子参照系・量子時計）は次回以降に回す。
- 2 節は原典で確かめた内容である（要約。他者の文章の長い引用はしない）。3 節と 4 節は原典に書かれていない、判定基準の整理とプロジェクトへのつながりの候補（Claude の見立て）である。

## 1. 読んだ文献

いずれも arXiv 版で、該当する節の本文を確かめた。PDF は非公開リポジトリの `papers/` にある。

| 引用キー | 文献 | 読んだ範囲 | 役割 |
| --- | --- | --- | --- |
| `chiribella2009` | Chiribella–D'Ariano–Perinotti, Theoretical framework for quantum networks (2009) | 序論、III 節（補題 4、系 1、定理 3・4、系 2 と 38 式の後の説明）、IV 節の定理 6〜12、定義 10・11 | 量子コム、テスター、実現定理 |
| `chiribella2008architecture` | Chiribella–D'Ariano–Perinotti, Quantum circuit architecture (2008) | 要旨と序論 | 量子コムの導入 |
| `gutoski2007` | Gutoski–Watrous, Toward a general theory of quantum games (2007) | 1 節、3 節（定義 3・4、定理 5・6、系 7・8、定理 9 の主張） | 量子戦略と co-strategy |
| `pollock2018` | Pollock ほか, Non-Markovian quantum processes: complete framework and efficient characterization (2018) | 要旨、II 節（性質 P1〜P3、定理 2） | process tensor |
| `chiribella2010` | Chiribella–D'Ariano–Perinotti, Probabilistic theories with purification (2010) | III 節 A・B（定義 27・29、補題 4・7、定理 1）、IV 節（定義 32、補題 13 の主張） | 因果性と条件付きの試験、局所的な識別可能性 |
| `barrett2007` | Barrett, Information processing in generalized probabilistic theories (2007) | 要旨、II 節（仮定 1、仮定 4・5、系 1、定理 1〜3、もつれ
…（以下 9672 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd ~/.claude/projects/-home-user && for f in *.jsonl; do echo "== $f"; python3 - "$f" <<'EOF'
import json,sys
for l in open(sys.argv[1]):
    d=json.loads(l)
    if d.get('type')=='user' and d.get('timestamp','')>'2026-10-01T11:20':
        c=d['message']['content']
        t=c if isinstance(c,str) else (c[0].get('text','') if isinstance(c,list) and c and c[0].get('type')=='text' else '')
        if t and not t.startswith('<'): print(d['timestamp'], t[:70].replace('\n',' '))
EOF
done
```

</details>

<details><summary>結果: Bash</summary>

```text
== [ID].jsonl
2026-10-01T11:25:22.110Z 次のセッションを開始してください。
2026-10-01T11:37:34.758Z Stop hook feedback: [~/.claude/stop-hook-git-check.sh]: There are unco
2026-10-01T11:45:48.332Z Continue from where you left off.
2026-10-01T11:46:55.298Z ここで対話を終了したいと思います。
2026-10-01T11:50:11.685Z 対話を終えて、ログ・まとめ・関連ファイルの更新と PR の作成に進んでください。  会話の履歴が失われているようなので、前回のターンのあなた
== [ID].jsonl
2026-10-01T11:25:22.110Z 次のセッションを開始してください。
2026-10-01T11:37:34.758Z Stop hook feedback: [~/.claude/stop-hook-git-check.sh]: There are unco
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd ~/.claude/projects/-home-user && for f in *.jsonl; do echo "== $f"; grep -c "ここで方針を相談させてください" $f; grep -c "Harrow ほか 2010" $f; done; python3 - <<'EOF'
import json
n=0
for l in open('[ID].jsonl'):
    d=json.loads(l)
    if d.get('type')=='assistant' and d.get('timestamp','')>'2026-10-01T11:25':
        for c in d['message']['content']:
            if c.get('type')=='text' and c['text'].strip(): n+=1; print(d['timestamp'], c['text'][:60].replace('\n',' '))
print(n)
EOF
```

</details>

<details><summary>結果: Bash</summary>

```text
== [ID].jsonl
4
5
== [ID].jsonl
1
2
2026-10-01T11:32:22.358Z ここまでの節目として、原典で確かめた内容と、私の見立てを報告します。  ## 原典で確かめた内容（いずれも arXiv 
2026-10-01T11:35:23.182Z 論文の PDF を非公開リポジトリに置き、参考文献一覧と調査メモを書いているところです。
2026-10-01T11:37:32.964Z 調査メモの草稿を [`surveys/2026-10-01_22_combs-and-composites.md`](p
2026-10-01T11:37:50.076Z 作業が失われないよう、ここまでの変更を両方のリポジトリの作業ブランチ `claude/clever-planck-pr5
2026-10-01T11:45:59.425Z PR [kittenkiki15/point-free-spacetime#43](https://github.com
2026-10-01T11:47:02.896Z PR [kittenkiki15/point-free-spacetime#43](https://github.com
6
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd ~/.claude/projects/-home-user && python3 - <<'EOF'
import json
for l in open('[ID].jsonl'):
    d=json.loads(l)
    if d.get('timestamp','')<'2026-10-01T11:25': continue
    if d.get('type')=='assistant':
        for c in d['message']['content']:
            if c.get('type')=='tool_use' and c['name']=='AskUserQuestion': print('Q',json.dumps(c['input'],ensure_ascii=False)[:600])
    if d.get('type')=='user':
        c=d['message']['content']
        if isinstance(c,list):
            for x in c:
                if x.get('type')=='tool_result' and 'answered' in str(x.get('content'))[:200]: print('A',str(x.get('content'))[:500])
EOF
```

</details>

<details><summary>結果: Bash</summary>

```text
Q {"questions": [{"header": "重点", "multiSelect": false, "options": [{"description": "項目 4（instrument の合成、量子コム、適応的な戦略）と項目 1（一般化確率論の複合系）を先に原典で確かめ、問い (a)/(b) の「書き直せる」の判定基準（量子的な出力を後の装置につなぐ場合の予測）を明確にする。項目 3 は次回以降に回す。", "label": "判定基準の枠組みから (推奨)"}, {"description": "項目 3（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）を先に調べ、量子時計の既存の扱いが (a) の『古典的な記録とモデルの組』として書けるかを具体例で確かめる。", "label": "量子時計・量子参照系から"}, {"description": "項目 2（Buscemi、Jenčová、松本、Guţă–Kahn）を先に調べ、第 17・18 回の Le Cam の理論の調査の続きとして、量子統計的実験の比較を確かめる。", "label": "Le Cam の量子版から"}, {"description": "各項目の主要文献を要旨で確認して全体の地図を作り、原典での確認は次回以降に回す。", "label": "5 項
A Your questions have been answered: "第 22 回は T-0019（量子・古典・混成の実験の扱いの先行研究の調査）を行います。調べることが 5 項目あり、1 回では原典で確かめきれないため、重点を決めたいと思います。どこから始めますか？"="判定基準の枠組みから (推奨)". You can now continue with these answers in mind.
Q {"questions": [{"header": "次の一手", "multiSelect": false, "options": [{"description": "今回は項目 4・1 に絞り、上の内容を調査メモにして、(i)〜(iii) を D-0001・D-0004 などの未解決の点と roadmap に記録する。項目 2・3 と (a)/(b) の判断は次回以降。", "label": "調査メモにまとめる (推奨)"}, {"description": "(ii) の「許す後の操作の類 𝒯」による判定基準を対話で検討し、その後に調査メモにまとめる。", "label": "判定基準をもう少し詰める"}, {"description": "(i) の古典的な場合の主張（コム↔核の列、非適応的な記録から決まること）を、有限集合で Lean か Python で確かめ、結果として登録する。", "label": "古典的なコムを検証する"}, {"description": "判定基準を Page–Wootters などの量子時計に当てはめてみる。", "label": "項目 3（量子時計）も調べる"}], "question": "この後の進め方をどうしますか？"}]}
A Your questions have been answered: "この後の進め方をどうしますか？"="調査メモにまとめる (推奨)". You can now continue with these answers in mind.
Shell cwd was res
…（以下 16 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && awk '/^### T-0019/{f=1} /^## 5\./{f=0} f' roadmap.md | cut -c1-200; grep -n "T-0019" roadmap.md | head -3 | cut -c1-120; sed -n '/## 次のタスク/,/## ユーザー/p' NEXT.md | cut -c1-200
```

</details>

<details><summary>結果: Bash</summary>

```text
### T-0019 量子・古典・混成の実験の扱いの先行研究の調査（第 19 回に追加）

第 19 回に、ユーザーの判断で追加した。フレームワークの要件として、量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えるよ�

- 調べること（文献は記憶による。未確認。主な文献は arXiv にあるはず）：
  1. 一般化確率論（Hardy、Barrett、Chiribella–D'Ariano–Perinotti）：古典・量子・混成の状態空間と効果空間の区別、複合系の扱い、状態空間の再構成（T-0
  2. Le Cam の理論の量子版（量子統計的実験の比較。Buscemi、Jenčová、松本、Guţă–Kahn の量子局所漸近正規性）。
  3. 量子参照系と量子時計（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）。T-0017 の「操作的な座標づけと参照系」と重なる部分は、ここでは次の問�
  4. 逐次・適応的な実験の扱い（測定後の状態まで与える測定（instrument）の合成、量子コム（Chiribella–D'Ariano–Perinotti）・量子戦略（Gutoski–Watrous）
  5. 複合のプロトコル $`π^M`$（[D-0001](definitions/D-0001.md) の注意。$`M`$ 個の部分装置で並列に観測し、同時に読み出す）の結果の同時分布と、一般化確�
- 問い：「量子的な観測」を、(a) 量子系を測った古典的な記録（本プロジェクトの今の立場。実際の観測結果は高々可算個の実数で、量子的な時計�
- Claude の見立て（第 19 回。記法 $`τ^O_π`$ は第 19 回のもので、第 20 回からは実験ごとの $`τ_e`$・$`σ_e`$（[D-0013](definitions/D-0013.md)）にあたる）：Ludwig 
- 成果物：調査メモと、(a)・(b) の判断の材料。
- 順序：T-0018 の次、段階 B の前（第 19 回にユーザーと決めた）。

11:- 順序は、第 11 回にユーザーと相談して決めた（2 節）。第 13 回に、ユーザーの提案で
18:\text{T-0001} \;→\; \text{T-0015} \;→\; \text{T-0002} \;→\; \text{T-0003} \;→\; \text{T-0016} \;→\; \text{T
26:| （調査） | 量子・古典・混成の実験の扱い（一般化確率論、Le Cam の量子版、量子参照
## 次のタスク

次のセッション（第 22 回の予定）では、[`roadmap.md`](roadmap.md) の **T-0019「量子・古典・混成の実験の扱いの先行研究の調査」**を行う。T-0019 の後は段�

- 手がかりは、`roadmap.md` の「T-0019」の節にある。調べるのは、一般化確率論、Le Cam の理論の量子版、量子参照系・量子時計である（文献は記憶によ�
- 問い：「量子的な観測」を、(a) 量子系を測った古典的な記録（今の立場）と読むか、(b) 時計を含む量子系を、古典的な記録へ読み出す前の量子的�
- 逐次・適応的な実験の扱い（instrument の合成、量子コム・量子戦略、適応的な戦略と並列の戦略の違い）も調べる（第 21 回に加えた。roadmap の T-0019
- 第 20 回の再編で、較正の写像
…（以下 199 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n "逐次に測定し\|適応的な設定を選ぶ規則の定義域\|核の形（古典的な核の合成で足りるか）\|N > 1\`\$ や適応的な設定の場合\|τ_e^k\`\$・\$\`σ_e^k\`\$ の入力を\|較正が確率的になる場合" definitions/*.md assumptions/*.md | cut -c1-90
```

</details>

<details><summary>結果: Bash</summary>

```text
definitions/D-0001.md:40:- 同じ物理系を逐次に測定し、結果を蓄えて最後
definitions/D-0002.md:27:- 適応的な設定を選ぶ規則の定義域と可測性：各
definitions/D-0006.md:21:- 極限の取り方。可能な実験はプロトコルと設定
definitions/D-0013.md:45:- 複合のプロトコルで、第 $`k`$ 部分装置の事象 $
definitions/D-0013.md:53:- 較正が確率的になる場合（時計が量子系である
assumptions/A-0006.md:28:- 複数回の観測で、結果が前の結果に依存する場
assumptions/A-0013.md:30:- 較正が確率的になる場合（[D-0013](../definitions/D-0
```

</details>

<details><summary>ツール: Bash</summary>

```text
for spec in "definitions/D-0001.md 40" "definitions/D-0002.md 27" "definitions/D-0006.md 21" "definitions/D-0013.md 45" "assumptions/A-0006.md 28"; do set -- $spec; sed -n "${2}p" $1 | tail -c 250; echo; done
```

</details>

<details><summary>結果: Bash</summary>

```text
��定の結果の列を 1 回の観測の結果とする別のプロトコルとして表すか、ほかの記述を設けるかを決める（[T-0019](../roadmap.md) の逐次の実験の扱いと関係する。PR #43 のレビューの論点）。

（結果の族の分布を核から作る段階で要る。[D-0006](D-0006.md)。ロードマップの T-0005 などで決める。逐次・適応的な実験の先行研究での扱いは T-0019 で調べる。PR #42 のレビューの論点）。

核として与え、それを合成して結果の族の分布を作る（各回の結果どうしの依存は D-0004 の未解決の点。適応的な場合は、設定の族の代わりに選び方の規則を使う。PR #42 のレビュー）。

��並列の観測のうち独立した局所的な操作を表すには、どの条件の下で入力を局所的な成分に限るかを決める（[T-0019](../roadmap.md) の複合系の扱いと関係する。PR #43 のレビューの論点）。

�核に連続性を課すかを、この前提とは区別して決める（PR #42 のレビュー）。核の形（古典的な核の合成で足りるか）の材料は、T-0019 で逐次・適応的な実験の先行研究を調べて集める。
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
SV="[第 22 回の調査メモ](../surveys/2026-10-01_22_combs-and-composites.md)"
def rw(p,o,n,hist=None):
    s=open(p).read(); assert s.count(o)==1,(p,o[:40]); s=s.replace(o,n)
    if hist: s=s.rstrip("\n")+"\n"+hist+"\n"
    open(p,'w').write(s)
rw('definitions/D-0001.md',"（[T-0019](../roadmap.md) の逐次の実験の扱いと関係する。PR #43 のレビューの論点）。",
 f"（[T-0019](../roadmap.md) の逐次の実験の扱いと関係する。PR #43 のレビューの論点）。第 22 回の見立て：結果の列を一つの結果とする案は、量子コムのテスター（ネットワーク全体を一つの操作で測るもの）の考え方と整合する（{SV}の 4.3 節）。")
rw('definitions/D-0002.md',"逐次・適応的な実験の先行研究での扱いは T-0019 で調べる。PR #42 のレビューの論点）。",
 f"逐次・適応的な実験の先行研究での扱いは T-0019 で調べる。PR #42 のレビューの論点）。第 22 回の見立て：規則を各段の核 $`s_j(x_j \\mid x_{{<j}}, y_{{<j}})`$ で表せば、決定的な規則と無作為な選択を同じ形で含められる（{SV}の 4.1 節）。")
rw('definitions/D-0006.md',"適応的な場合は、設定の族の代わりに選び方の規則を使う。PR #42 のレビュー）。",
 f"適応的な場合は、設定の族の代わりに選び方の規則を使う。PR #42 のレビュー）。第 22 回の見立て：結果の族の分布は、各段の核の列（古典的なコム）と選び方の規則の核の積で書け、核の列は非適応的な実験の記録の分布の全体から決まる（{SV}の 4.1 節）。")
rw('definitions/D-0013.md',"（[T-0019](../roadmap.md) の複合系の扱いと関係する。PR #43 のレビューの論点）。",
 f"（[T-0019](../roadmap.md) の複合系の扱いと関係する。PR #43 のレビューの論点）。一般化確率論の「局所的な操作は可換」という仮定（Barrett 2007）と関係する。可換性と信号の不在を、部分装置の事象の時空的な配置から導くか、前提として置くかの論点になる（第 22 回の見立て。{SV}の 4.2 節）。")
rw('assumptions/A-0006.md',"核の形（古典的な核の合成で足りるか）の材料は、T-0019 で逐次・適応的な実験の先行研究を調べて集める。",
 f"核の形（古典的な核の合成で足りるか）の材料は、T-0019 で逐次・適応的な実験の先行研究を調べて集める。第 22 回の見立て：(a) の立場（設定と結果が古典的）では、装置の中に量子的な記憶があっても、観測される過程は古典的なコム（履歴に依存する核の列）になるので、古典的な核の合成で足りる。ただし、核は一般に履歴全体に依存し、1 回ごとの応答関数の積にはならない（{SV}の 4.1 節）。")
EOF
python3 -m pytest -q to
…（以下 24 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
35 passed in 0.27s
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
def rw(p,o,n):
    s=open(p).read(); assert s.count(o)==1,(p,o[:40]); open(p,'w').write(s.replace(o,n))
s=open('roadmap.md').read()
import re
lines=s.split('\n')
for i,l in enumerate(lines):
    if l.startswith('| T-0019 |'):
        assert l.endswith('| 未着手 |'); lines[i]=l[:-len('| 未着手 |')]+'| 進行中 |'
s='\n'.join(lines)
o="- 成果物：調査メモと、(a)・(b) の判断の材料。\n- 順序：T-0018 の次、段階 B の前（第 19 回にユーザーと決めた）。"
assert s.count(o)==1
s=s.replace(o,o+"""
- 第 22 回の進み具合（[調査メモ](surveys/2026-10-01_22_combs-and-composites.md)、[まとめ](summaries/2026-10-01_22_combs-and-composites.md)）：ユーザーの判断で、項目 4（逐次・適応的な実験）と項目 1（一般化確率論の複合系）を先に原典（arXiv 版の 8 件）で確かめた。量子コム・量子戦略・process tensor・条件付きの試験と因果性・Barrett の複合系・適応的な方式と並列の方式を確かめ、判定基準を「許す後の操作の類 $`𝒯`$」で整理した（見立て）。(a) と (b) の違いは、部分の記述を量子的な合成の下で閉じたものにするかにある、とした（見立て）。項目 5 は、調査メモの 4.2 節に見立てを置いた。
- 残り：項目 2（Le Cam の理論の量子版）と項目 3（量子参照系・量子時計）。その後、(a)・(b) の判断をユーザーが行う。""")
open('roadmap.md','w').write(s)
EOF
grep -n "^| T-0019" roadmap.md | tail -c 20
```

</details>

<details><summary>結果: Bash</summary>

```text
3.md) | 進行中 |
```

</details>

## Claude

ロードマップと定義・前提の未解決の点を更新しました。次に用語一覧・NEXT.md・まとめを書きます。

<details><summary>ツール: Bash</summary>

```text
grep -n "^| quantum comb\|^| instrument\|^| local tomography\|^| tester\|^| process tensor\|^| quantum strategy\|^| causal theory\|^| link product" glossary.md | cut -c1-200
```

</details>

<details><summary>結果: Bash</summary>

```text
48:| instrument (quantum) | 量子インストルメント | 測定の結果の確率だけでなく、結果ごとの測定後の状態も与える量子的な測定の記述。逐次の測定の合�
85:| quantum comb | 量子コム | 入力と出力を交互に持つ量子的な回路の部分を、一つの対象として扱う枠組み（Chiribella–D'Ariano–Perinotti。記憶による。未
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='glossary.md'; L=open(p).read().split('\n')
S='[調査 22](surveys/2026-10-01_22_combs-and-composites.md)'
i=[k for k,l in enumerate(L) if l.startswith('| quantum comb |')][0]
cols=L[i].split(' | ')
L[i]=f"| quantum comb | 量子コム | 量子回路をつないだネットワークを、外に出ている入出力の系の上の一つの正の演算子（Choi 演算子）で表したもの。正規化の連鎖を満たす演算子は、どれも記憶を持つ通信路（等長写像の列）で実現できる（Chiribella–D'Ariano–Perinotti 2009 の定理 3）。逐次・適応的な実験の記述に使う。 | {S}（初出は [第 21 回](summaries/2026-10-01_21_adaptive-settings-and-systems.md)） |"
j=[k for k,l in enumerate(L) if l.startswith('| instrument (quantum) |')][0]
L[j]=L[j].replace("（Davies–Lewis。記憶による。未確認）","（Davies–Lewis。記憶による。未確認。結果の付いたネットワークへの一般化は Chiribella–D'Ariano–Perinotti 2009 の一般化された instrument。"+S+"）")
new={
"local tomography":f"| local tomography | 局所トモグラフィー | 複合系の状態が、部分系ごとの測定の同時確率で決まること。一般化確率論では、局所的な識別可能性と同値で（Chiribella–D'Ariano–Perinotti 2010）、状態空間がテンソル積になることを導く（Barrett 2007 の仮定 5、定理 1）。複素数の量子論では成り立ち、実数の量子論では成り立たない。 | {S} |",
"process tensor":f"| process tensor | process tensor | 系に施す制御操作の列から、最終時刻の系の状態への写像。線形性・完全正値性・包含（時刻の因果的な順序）を満たし、逆にこれらを満たすものは補助系を加えた開放系の発展で実現できる（Pollock ほか 2018）。量子コムと同じ構造を持つ。 | {S} |",
"quantum strategy":f"| quantum strategy | 量子戦略 | 多ラウンドの量子的なやりとりで一方が取る行動を、一つの半正定値演算子で表したもの。表現は線形の制約で特徴づけられ、結果の確率は相手の co-strategy の表現との内積で与えられる（Gutoski–Watrous 2007）。量子コムと同じ構造を独立に与えている。 | {S} |",
"tester":f"| tester | テスター | 量子コム（ネットワーク）を確率に写す最も一般の操作。確率は一般化ボルン則 $`p(i \\mid R) = \\mathrm{{Tr}}[P_i^T R]`$ で与えられ、実現には一般に補助系ともつれた状態の準備が要る（Chiribella–D'Ariano–Perinotti 2009）。 | {S
…（以下 425 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
54:| local tomography | 局所トモグ�
81:| process tensor | process tensor | �
89:| quantum strategy | 量子戦略 | �
102:| tester | テスター | 量子コ�
��の弱収束と同値。 | [第 18 回の調査メモ](surveys/2026-09-30_18_limit-topology.md) |
```

</details>

<details><summary>ツール: Bash</summary>

```text
tail -c1 glossary.md | xxd | head -1; git show HEAD:glossary.md | tail -c1 | xxd
```

</details>

<details><summary>結果（エラー）: Bash</summary>

```text
Exit code 127
/bin/bash: line 1: xxd: command not found
/bin/bash: line 1: xxd: command not found
```

</details>

<details><summary>ツール: Bash</summary>

```text
tail -c1 glossary.md | od -c | head -1; git diff --stat glossary.md
```

</details>

<details><summary>結果: Bash</summary>

```text
0000000  \n
 glossary.md | 8 ++++++--
 1 file changed, 6 insertions(+), 2 deletions(-)
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='NEXT.md'; s=open(p).read()
S='summaries/2026-10-01_22_combs-and-composites.md'
s=s.replace("最終更新: 2026-10-01（第 21 回セッションの後）","最終更新: 2026-10-01（第 22 回セッションの後）")
o="\n## 次のタスク"
i=s.index(o)
s=s[:i].rstrip('\n')+f"\n- 第 22 回：ロードマップの T-0019 を始めた（進行中）。ユーザーの判断で、項目 4（逐次・適応的な実験）と項目 1（一般化確率論の複合系）を先に、arXiv 版の原典 8 件（量子コム、量子戦略、process tensor、条件付きの試験と因果性、Barrett の複合系、適応的な方式と並列の方式）で確かめた。判定基準を「許す後の操作の類」で整理し、(a)・(b) の違いは部分の記述を量子的な合成の下で閉じたものにするかにある、という見立てを置いた。適応的な設定は古典的なコム（履歴に依存する核の列）で表せる、という見立ても置いた（[まとめ]({S})、[調査メモ](surveys/2026-10-01_22_combs-and-composites.md)）。\n"+s[i:]
a=s.index("## 次のタスク"); b=s.index("## ユーザーにお願いしていること")
s=s[:a]+"""## 次のタスク

次のセッション（第 23 回の予定）では、[`roadmap.md`](roadmap.md) の **T-0019「量子・古典・混成の実験の扱いの先行研究の調査」の続き**を行う。T-0019 の後は段階 B（T-0004〜T-0007）である（[`CLAUDE.md`](CLAUDE.md) の「セッションの進め方」）。その後の順序、長期のタスク、未解決の論点は `roadmap.md` にある。

- 手がかりは、`roadmap.md` の「T-0019」の節と、[第 22 回の調査メモ](surveys/2026-10-01_22_combs-and-composites.md)の 3〜5 節にある。
- 残りは、項目 2（Le Cam の理論の量子版。Buscemi、Jenčová、松本、Guţă–Kahn）と項目 3（量子参照系・量子時計。Page–Wootters、Giacomini–Castro-Ruiz–Brukner）である（文献は記憶による。未確認。主な文献は arXiv にあるはず）。調査メモの 3 節の判定基準（許す後の操作の類 $`𝒯`$）を、量子時計の既存の扱いに当てはめる。
- 問い：「量子的な観測」を、(a) 量子系を測った古典的な記録（今の立場）と読むか、(b) 時計を含む量子系を、古典的な記録へ読み出す前の量子的な出力として実験の対象に含めると読むか。判断は調査の後にユーザーが行う。
- 確率的な較正の扱い（[D-0013](definitions/D-0013.md) の未解決の点）も、項目 3 の論点である。
- 新しい定義・前提のうち、A-0014・A-0015 は第 21 回に「採用」にした。残りの D-0012・D-0013・A-0011〜A-0013・A-0016 の状態は、ユーザーと決める。

"""+s[b:]
open(p,'w').write(s)
EOF
sed -n '/## 次のタスク/
…（以下 43 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
## 次のタスク

次のセッション（第 23 回の予定）では、[`roadmap.md`](roadmap.md
```

</details>

## Claude

Now the summary.

<details><summary>ツール: Write: /home/user/point-free-spacetime/summaries/2026-10-01_22_combs-and-composites.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/summaries/2026-10-01_22_combs-and-composites.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/summaries/2026-10-01_22_combs-and-composites.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 tools/deps_graph.py >/dev/null; python3 -m pytest -q tools/tests 2>&1 | tail -1; L=logs/2026-10-01_22_combs-and-composites.md; python3 tools/export_log.py ~/.claude/projects/-home-user/[ID].jsonl $L --title "2026-10-01 第 22 回: 逐次・適応的な実験と複合系（量子コムと一般化確率論）" --redact-file ../point-free-spacetime-private/redactions.txt --since 2026-10-01T11:25:00Z && grep -v -e '^#' -e '^$' ../point-free-spacetime-private/redactions.txt | grep -iFcf - $L; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}|sk-[A-Za-z0-9]{10,}' $L; wc -l $L; grep -n "^## " $L | head -20
```

</details>
