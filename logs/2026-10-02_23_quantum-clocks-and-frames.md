# 2026-10-02 第 23 回: 量子時計と量子参照系（較正の段階）

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> ツールの呼び出しは折りたたんで表示し、個人情報などは伏せ字にしています。

## ユーザー

次のセッションを開始してください。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git status | head -3 && git log --oneline -3 && cat NEXT.md
```

</details>

<details><summary>結果: Bash</summary>

```text
On branch claude/clever-planck-pr5kq1
Your branch is up to date with 'origin/claude/clever-planck-pr5kq1'.

99d353a 第 22 回のクロスモデルレビューの詳細化の論点（適応的な設定の核の不変性と乱数の独立性）を A-0006 の未解決の点に記録した
9d21ed2 R-0009 に、記憶のない通信路を 2 回使う設定であることを明記した（第 22 回のクロスモデルレビューの詳細化の論点）
809a263 第 22 回のクロスモデルレビューに対応：中間の立場で合成性を保つ条件を全体のコムまたは因子化の条件に限定し、設定の追加の扱いを D-0001 の未解決の点に記録した
# 次のセッションでやること

最終更新: 2026-10-01（第 22 回セッションの後）

## 状況

- 第 01 回：リポジトリの運用ルールを決め、自動検証（Lean・Python・クロスモデルレビュー）を整えた。
- 第 02 回：点なし位相と論理・様相論理・因果・量子論のつながりを整理し、調査メモ・用語一覧・記号一覧・参考文献一覧を作った（[まとめ](summaries/2026-09-25_02_pointfree-logic.md)）。
- 第 03 回：Heunen–van der Schaaf の 2 本の論文メモを作り、「完備ブール代数の点はアトムと対応する」を Lean で形式化した（[まとめ](summaries/2026-09-25_03_ordered-locales.md)）。
- 第 04 回：第 03 回の結果をユーザーと確認し、論文メモを修正した。検証済みの主張を「結果」として管理する [`results/`](results/README.md) を作った（[まとめ](summaries/2026-09-25_04_review-and-results.md)）。
  - ユーザーの方針：予想の価値の主軸は、数学ではなく**物理学への寄与**（厳密な定義のない物理の概念や主張に数学的な定式化を与えることなど）に置く。
- 第 05 回：最小の長さと操作的な領域の構造について、おもちゃのモデルを多角的に検討した。最小の尺度の入れ方を型 I（小さい領域を捨てる）と型 II（余白に下限を置く）に分け、型 II を「膨張 $`N`$ による余白付きの包含が補間的でないこと」として点なしに表した。文献を調べ、数学の部分は既知と確認して結果 R-0006〜R-0008 に登録し、最初の予想 [C-0001](conjectures/C-0001.md)（優先度：高、[Issue #8](https://github.com/kittenkiki15/point-free-spacetime/issues/8)）を立てた（[まとめ](summaries/2026-09-26_05_minimal-scale.md)、[調査メモ](surveys/2026-09-26_05_subordination.md)）。
- 第 06 回：C-0001 を見直す前の先行研究の調査を行った。主張 4 と同じ型の no-go 型の結果（因果集合の非局所性、粒子の局在）、測定と局所性（Sorkin の不可能な測定、Fewster–Verch のプローブによる測定の枠組み）、最小の長さの観測者非依存性（DFR、Hossenfelder）を原典で確かめた。主張
…（以下 10661 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
git fetch origin main 2>&1 | tail -1; git log --oneline -3 origin/main; git merge-base --is-ancestor HEAD origin/main && echo "HEAD in main"; git log --oneline origin/main..HEAD | head; cd ../point-free-spacetime-private && git status | head -2 && git fetch origin main 2>&1|tail -1; git log --oneline origin/main..HEAD | head
```

</details>

<details><summary>結果: Bash</summary>

```text
8f6382c..4238cba  main       -> origin/main
4238cba Merge pull request #44 from kittenkiki15/claude/clever-planck-pr5kq1
99d353a 第 22 回のクロスモデルレビューの詳細化の論点（適応的な設定の核の不変性と乱数の独立性）を A-0006 の未解決の点に記録した
9d21ed2 R-0009 に、記憶のない通信路を 2 回使う設定であることを明記した（第 22 回のクロスモデルレビューの詳細化の論点）
HEAD in main
On branch claude/clever-planck-pr5kq1
Your branch is up to date with 'origin/claude/clever-planck-pr5kq1'.
   97555ba..91dd8d1  main       -> origin/main
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git checkout -B claude/clever-planck-pr5kq1 origin/main -q && git log --oneline -1; cd ../point-free-spacetime-private && git merge-base --is-ancestor HEAD origin/main && git checkout -B claude/clever-planck-pr5kq1 origin/main -q && git log --oneline -1
```

</details>

<details><summary>結果: Bash</summary>

```text
4238cba Merge pull request #44 from kittenkiki15/claude/clever-planck-pr5kq1
91dd8d1 Merge pull request #13 from kittenkiki15/claude/clever-planck-pr5kq1
```

</details>

## Claude

Now let me read the T-0019 section of the roadmap and sections 3–5 of the session 22 survey notes.

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && awk '/^### T-0019/,/^### T-0020|^## /' roadmap.md | head -80; echo ----; grep -n '^## ' surveys/2026-10-01_22_combs-and-composites.md
```

</details>

<details><summary>結果: Bash</summary>

```text
### T-0019 量子・古典・混成の実験の扱いの先行研究の調査（第 19 回に追加）

第 19 回に、ユーザーの判断で追加した。フレームワークの要件として、量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えるようにしたい（ユーザーの方針。量子重力理論への寄与という目的による）。T-0016 では、Le Cam の実験の理論（結果が古典的な記録の実験）と Ludwig の構成（有限個の効果による位相）を調べたが、この要件に直接答える部分は調べていない。

- 調べること（文献は記憶による。未確認。主な文献は arXiv にあるはず）：
  1. 一般化確率論（Hardy、Barrett、Chiribella–D'Ariano–Perinotti）：古典・量子・混成の状態空間と効果空間の区別、複合系の扱い、状態空間の再構成（T-0016 から移した）。[C-0003](conjectures/C-0003.md) との関係。
  2. Le Cam の理論の量子版（量子統計的実験の比較。Buscemi、Jenčová、松本、Guţă–Kahn の量子局所漸近正規性）。
  3. 量子参照系と量子時計（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）。T-0017 の「操作的な座標づけと参照系」と重なる部分は、ここでは次の問いに絞る。
  4. 逐次・適応的な実験の扱い（測定後の状態まで与える測定（instrument）の合成、量子コム（Chiribella–D'Ariano–Perinotti）・量子戦略（Gutoski–Watrous）・process tensor、チャネルの識別と推定での適応的な戦略と並列の戦略の違い）。(a) の立場で、適応的な設定（[D-0001](definitions/D-0001.md)）の結果の族の分布を、履歴を入力とする古典的な核の合成として書けるか。核で表す対象を、「固定した選び方の規則での記録の同時分布」と「選び方の規則を変えても整合する同じ過程の記述」に分けて調べる（実数値の有限個の結果なら、前者は通常の可測性の条件の下で条件付き分布の核に分解できるが、それだけでは後者を扱えるとは限らない。PR #43 のレビューの論点）。[D-0002](definitions/D-0002.md)（選び方の規則の定義域・可測性・無作為な選択）、[D-0004](definitions/D-0004.md)・[A-0006](assumptions/A-0006.md)・[D-0006](definitions/D-0006.md)（履歴を入力とする核）の未解決の点の材料にする（決めるのは T-0004〜T-0006）。適応的な設定は、(b) の判定基準の論点（量子的な出力を後の装置につなぐ場合）のうち、古典的な記録を次の装置へ渡す部分にあたる（第 21 回に、ユーザーの判断で加えた）。
  5. 複合のプロトコル $`π^M`$（[D-0001](definitions/D-0001.md) の注意。$`M`$ 個の部分装置で並列に観測し、同時に読み出す）の結果の同時分布と、一般化確率論・量子論の複合系の扱い（テンソル積、局所的な効果、もつれ）との対応（第 21 回に加えた）。一つの設定で得た同時分布が積でないことだけでは、もつれと古典的な相関を区別できない。もつれを表すと言うときに、複数の設定にわたる統計や後続の操作まで、どの予測を再現することを求めるか
…（以下 2004 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 79,200p surveys/2026-10-01_22_combs-and-composites.md
```

</details>

<details><summary>結果: Bash</summary>

```text
## 3. 判定基準の整理（Claude の見立て）

T-0019 の問い（(a)・(b)）の「書き直せる」の判定基準を、2 節の言葉で整理する。

### 3.1 予測の同等性は、許す後の操作の類で決まる

2.1 の 38 式の後の説明から、記述どうしの同等性は、「その記述を、許す操作の類 $`𝒯`$ のどの操作につないでも、同じ確率を与えること」と定式化できる。$`𝒯`$ が大きいほど、区別が細かくなる。

- $`𝒯`$ を、古典的な記録を経由する操作（結果を読み出してから、それに応じて次の操作を選ぶもの。2.4 の条件付きの試験）に限るとき：4.1 節の条件（後の設定を前もって装置に知らせない因果的なつなぎ方であること、設定を選ぶ乱数が装置の観測されない記憶と独立で、選び方の規則によって装置の応答が変わらないこと）の下で、記述は、古典的な入力（設定）と古典的な出力（結果）の間の古典的なコム（4.1 節）で足りる。ただし、足りるのは部分装置どうしの相関を含む**全体**の古典的なコムである。部分装置の間に前もって共有した相関（共有の乱数や、もつれた状態）があれば、部分装置ごとの古典的なコムを合成しても全体の分布は決まらない（各部分装置が公平な 1 ビットを出す場合、ビットを共有するか独立かで、個別の分布は同じでも同時分布は異なる）。前もって共有した相関がある場合、部分装置ごとのコムだけでは、一般には全体の分布が決まらない（許された操作がその相関を利用せず、観測される同時分布が積になる場合などは、個別の記述から予測できる。PR #44 のレビューを受けて区別した）。
- $`𝒯`$ が、量子的な出力に直接働く操作（もつれた補助系を使うテスター、量子的な出力を次の部分装置の入力につなぐこと）を含むとき：量子的な入出力を持つ量子コムは、それらの操作の予測に十分である。量子コム全体が必要になるのは、許す操作が入出力をトモグラフィー的に識別できる場合などに限る（例えば、量子的な出力を $`Z`$ 回転に通してから $`Z`$ 測定する操作だけを許すなら、予測は $`Z`$ 測定の古典的な確率だけで決まる。どこまでの記述が要るかは $`𝒯`$ で決まる。PR #44 のレビューを受けて書き分けた）。許した準備・介入・読み出しの組がトモグラフィーに足りない記録から作った古典的なコムは、量子コムを決めない（1 スロットの通信路なら、読み出しが固定されていても、それが情報的に完全で、準備を情報的に完全に変えられれば、トモグラフィーには足りる。複数スロットのコムでは、各中間時刻にも情報的に完全な介入の組が要る（前半が恒等で後半が完全脱分極の通信路と、その順序を逆にしたものは、初期の準備と最終の測定だけでは区別できないが、途中で状態を準備し直せば区別できる）。PR #44 のレビューを受けて条件を統一した）。一方、有限次元で、設定として情報的に完全な準備・測定・介入を許し、それらが較正されていれば、古典的な記録の確率から量子コムを再構成でき（プロセス・トモグラフィー）、量子的なつなぎ方の予測も計算できる（PR #44 のレビューを受けて条件を明記した）。2.6 の `harrow2010` の量子の例では、最良の方式が、1 回目の出力から取り出した状態を量子的なまま 2 回目の入力に入れる。

### 3.2 一つの実験全体と、部分の合成とを分ける

- 一つの実験全体（実験の対象と、量子的なつなぎ方をすべて装置の中に含めたもの）については、(a)（古典的な
…（以下 6464 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime-private && ls papers | tail -30; cd ../point-free-spacetime && ls summaries | tail -2; curl -sS -o /dev/null -w "%{http_code}\n" https://arxiv.org/abs/1310.4691
```

</details>

<details><summary>結果: Bash</summary>

```text
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
lecam1972.pdf
ludwig1968.pdf
miller2018.pdf
morinelli2018.pdf
naaijkens2012.pdf
pollock2018.pdf
pomatto2014.pdf
raginsky2011.pdf
rovelli1996.pdf
rovelli2002.pdf
schack2001bayes.pdf
shannon1958.pdf
sorkin1993.pdf
sorkin2007.pdf
spitters2014.pdf
torgersen1970.pdf
vanderschaaf2024.pdf
vandervaart2002.pdf
vovk2023.pdf
2026-10-01_22_combs-and-composites.md
README.md
200
```

</details>

<details><summary>ツール: AskUserQuestion</summary>

```text
（入力の本文は省略。項目: questions）
```

</details>

<details><summary>結果: AskUserQuestion</summary>

```text
Your questions have been answered: "今回はどちらの項目を中心に調べますか？"="項目 3 を先に（推奨）", "調べる深さはどうしますか？"="中心の文献の本文で確認（推奨）". You can now continue with these answers in mind.
```

</details>

## Claude

項目 3 を中心に、原典の本文で確かめます。まず候補の文献の arXiv の番号と書誌情報を確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad 2>/dev/null || mkdir -p /tmp/claude-0/-home-user/[ID]/scratchpad; cd /tmp/claude-0/-home-user/[ID]/scratchpad; for id in 1504.04215 1712.07207 1908.10165 1912.00033 1703.10434 quant-ph/0610030 1904.12390 1811.04587; do echo "== $id"; curl -sS "https://export.arxiv.org/api/query?id_list=$id" | python3 -c "
import sys,re;t=sys.stdin.read()
e=t.split('<entry>')[1] if '<entry>' in t else ''
print(re.sub(r'\s+',' ',re.search(r'<title>(.*?)</title>',e,re.S).group(1)) if e else 'NONE')
print(', '.join(re.findall(r'<name>(.*?)</name>',e)))
m=re.search(r'<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>',e,re.S);print(m.group(1) if m else '')"; done
```

</details>

<details><summary>結果: Bash</summary>

```text
== 1504.04215
Quantum Time
Vittorio Giovannetti, Seth Lloyd, Lorenzo Maccone
Phys. Rev. D 92, 045033 (2015)
== 1712.07207
Quantum mechanics and the covariance of physical laws in quantum reference frames
Flaminia Giacomini, Esteban Castro-Ruiz, Časlav Brukner
Nat. Commun. 10, 494 (2019)
== 1908.10165
Quantum clocks and the temporal localisability of events in the presence of gravitating quantum systems
Esteban Castro-Ruiz, Flaminia Giacomini, Alessio Belenchia, Časlav Brukner
Nat Commun 11, 2672 (2020)
== 1912.00033
The Trinity of Relational Quantum Dynamics
Philipp A. Hoehn, Alexander R. H. Smith, Maximilian P. E. Lock
Phys. Rev. D 104, 066001 (2021)
== 1703.10434
Symmetry, Reference Frames, and Relational Quantities in Quantum Mechanics
Leon Loveridge, Takayuki Miyadera, Paul Busch

== quant-ph/0610030
Reference frames, superselection rules, and quantum information
Stephen D. Bartlett, Terry Rudolph, Robert W. Spekkens
Rev. Mod. Phys. 79, 555 (2007)
== 1904.12390
Quantum clocks observe classical and quantum time dilation
Alexander R. H. Smith, Mehdi Ahmadi
Nat. Commun. 11, 5360 (2020)
== 1811.04587
Analysis of multivariate Gegenbauer approximation in the hypercube
Haiyong Wang, Lun Zhang
Shell cwd was reset to /home/user
```

</details>

## Claude

中心の文献を 7 件に絞ります。PDF を取得し、本文をテキストにします。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && for p in "giovannetti2015:1504.04215" "giacomini2019:1712.07207" "castroruiz2020:1908.10165" "hoehn2021:1912.00033" "loveridge2018:1703.10434" "smith2020:1904.12390" "bartlett2007:quant-ph/0610030"; do k=${p%%:*}; id=${p#*:}; curl -sSL -o $k.pdf "https://arxiv.org/pdf/$id"; pdftotext -layout $k.pdf $k.txt 2>/dev/null; echo "$k $(wc -l < $k.txt) $(file -b $k.pdf | cut -c1-20)"; done
```

</details>

<details><summary>結果: Bash</summary>

```text
giovannetti2015 538 PDF document, versio
giacomini2019 1945 PDF document, versio
castroruiz2020 1798 PDF document, versio
hoehn2021 4201 PDF document, versio
loveridge2018 2701 PDF document, versio
smith2020 1015 PDF document, versio
bartlett2007 3839 PDF document, versio
Shell cwd was reset to /home/user
```

</details>

## Claude

まず Giovannetti–Lloyd–Maccone 2015（Page–Wootters の定式化の再検討）を読みます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,300p giovannetti2015.txt
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 300,440p giovannetti2015.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>結果: Bash</summary>

```text
<persisted-output>
Output too large (32.3KB). Full output saved to: /root/.claude/projects/-home-user/[ID]/tool-results/bv25yka7z.txt

Preview (first 2KB):
                                                                                                  Quantum Time
                                                                              Vittorio Giovannetti,1 Seth Lloyd2 , Lorenzo Maccone3
                                                               1
                                                                NEST-INFM & Scuola Normale Superiore, Piazza dei Cavalieri 7, I-56126, Pisa, Italy.
                                                2
                                                    RLE and Dept. of Mech. Eng., Massachusetts Institute of Technology, 77 Mass. Av., Cambridge, MA 02139, USA.
                                                         3
                                                           Dip. Fisica “A. Volta” & INFN Sez. Pavia, Università di Pavia, via Bassi 6, I-27100 Pavia, Italy.

                                                              We give a consistent quantum description of time, based on Page and Wootters’ conditional prob-
                                                           abilities mechanism, that overcomes the criticisms that were raised against similar previous propos-
                                                           als. In particular we show how the model allows to 
…（以下 576 文字を省略）
```

</details>

## Claude

二段組みで読みにくいので、段組みを解いてテキストにし直します。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && for k in giovannetti2015 giacomini2019 castroruiz2020 hoehn2021 loveridge2018 smith2020 bartlett2007; do pdftotext $k.pdf $k.raw.txt; done; grep -n -i -E "constraint|conditional|criticism|Kucha|clock" giovannetti2015.raw.txt | head -60
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 19,140p giovannetti2015.raw.txt; echo ......; sed -n 280,420p giovannetti2015.raw.txt; echo .....; sed -n 732,830p giovannetti2015.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,80p hoehn2021.raw.txt; grep -n -E "^[IVX]+\. |^[A-H]\. [A-Z]|^Theorem|^Lemma|^Corollary|^Definition" hoehn2021.raw.txt | head -80
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -E "B\. Quantum time observables|covariant POVM|ideal clock|Unruh|monoton" hoehn2021.raw.txt | head -40
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 686,960p hoehn2021.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -E "Resolving Kuchař|C\. Resolving|two-time|transition probabilit|second criticism|third criticism|first criticism" hoehn2021.raw.txt | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

## Claude

Höhn–Smith–Lock の時計の POVM の節を読み終えました。続けて、同じ論文の Kuchař の批判への応答（2 時刻の条件付き確率）の節を読みます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 4330,4580p hoehn2021.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -E "^\[(21|49|50|71|83|84)\]" hoehn2021.raw.txt; grep -n -A2 -E "^\[(21|49|71)\] " hoehn2021.raw.txt | head
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n "(35)" hoehn2021.raw.txt | head -3; sed -n 2230,2360p hoehn2021.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -B3 -A12 "(4)$" hoehn2021.raw.txt | sed -n 1,40p; grep -n -E "interaction|interacting" hoehn2021.raw.txt | head -20
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n "Temporal localization is frame dependent" hoehn2021.raw.txt; awk 'NR>=4060 && NR<=4110' hoehn2021.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 3852,3900p hoehn2021.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

## Claude

Höhn–Smith–Lock の要点を確かめ終えました。次は Smith–Ahmadi 2020（量子時計の POVM と時間の遅れ）を読みます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,60p smith2020.raw.txt; grep -n -i -E "POVM|covariant|probabilit|Eq. \(|quantum time dilation|proper time" smith2020.raw.txt | head -60
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 95,135p smith2020.raw.txt; sed -n 325,470p smith2020.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 470,560p smith2020.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 560,660p smith2020.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,140p giacomini2019.raw.txt
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 140,330p giacomini2019.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -E "^[A-H]\. |^[IV]+\. |measurement|Measurement" giacomini2019.raw.txt | head -50
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

## Claude

Giacomini ほかの、量子参照系の変換の構成を読みました。続けて、測定が参照系の取り替えでどう変わるかを論じた節（Methods II E）を読みます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 2007,2200p giacomini2019.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 2270,2360p giacomini2019.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,120p castroruiz2020.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -i -E "event|locali[sz]|switch|indefinite causal" castroruiz2020.raw.txt | sed -n 20,90p
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 195,300p castroruiz2020.raw.txt; sed -n 626,680p castroruiz2020.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -E "Gravitational quantum switch|Knob settings and external evolution" castroruiz2020.raw.txt; awk '/^Gravitational quantum switch/{f=1} f{print NR": "$0; if(++n>90) exit}' castroruiz2020.raw.txt | tail -88
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

## Claude

Castro-Ruiz ほかの「重力による量子スイッチ」の節を読んでいます（PDF の図の埋め込みデータが混じったので、本文だけを抜き出します）。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1030,1460p castroruiz2020.raw.txt | grep -v -E "latexit|^sha1|^[A-Za-z]{0,3}$|^\s*$" | head -120
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1454,1560p castroruiz2020.raw.txt | grep -v -E "latexit|^sha1" 
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,60p loveridge2018.raw.txt; grep -n -E "^[0-9]+(\.[0-9]+)* [A-Z]|^Theorem|^Proposition|^Definition|^Lemma|^Corollary" loveridge2018.raw.txt | head -60
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 60,93p loveridge2018.raw.txt; sed -n 455,520p loveridge2018.raw.txt; sed -n 1085,1130p loveridge2018.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 940,1000p loveridge2018.raw.txt; sed -n 1505,1530p loveridge2018.raw.txt; sed -n 1570,1600p loveridge2018.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1530,1569p loveridge2018.raw.txt; sed -n 1625,1645p loveridge2018.raw.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 1,140p bartlett2007.raw.txt | grep -v "^\s*$" | head -110
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && grep -n -E "^A\. Reference frames in quantum theory|^1\. Quantization of a phase reference|^2\. Dequantization|^C\. Are certain superselection|^B\. Quantization of a general|^VI\.|bounded" bartlett2007.raw.txt | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 362,470p bartlett2007.raw.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad && sed -n 2330,2420p bartlett2007.raw.txt | grep -v "^\s*$"; echo ....; sed -n 2509,2560p bartlett2007.raw.txt | grep -v "^\s*$"; echo ....; sed -n 2766,2830p bartlett2007.raw.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_23_quantum-clocks-and-frames.md の 2 節に要約している）
```

</details>

## Claude

7 件を読み終えました。結果をまとめる前に、照合する定義・前提（D-0013、A-0016、A-0014、A-0015）の現在の内容を確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && sed -n 1,200p definitions/D-0013.md | cut -c1-600
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && for f in assumptions/A-0016.md assumptions/A-0014.md assumptions/A-0015.md assumptions/A-0011.md; do echo "=== $f"; sed -n '/^## 主張/,/^## 注意/p' $f | cut -c1-800; done
```

</details>

<details><summary>結果: Bash</summary>

```text
# D-0013: 観測者の実験における時空と較正

| 項目 | 値 |
| --- | --- |
| 状態 | 作業上 |
| 層 | 実験 |
| 依存する ID | [D-0001](../definitions/D-0001.md)、[D-0003](../definitions/D-0003.md)、[A-0003](../assumptions/A-0003.md)、[A-0010](../assumptions/A-0010.md) |
| 関係する予想・結果 | [C-0002](../conjectures/C-0002.md)、[C-0008](../conjectures/C-0008.md)、[C-0009](../conjectures/C-0009.md)、[C-0010](../conjectures/C-0010.md)、[C-0011](../conjectures/C-0011.md)、[C-0012](../conjectures/C-0012.md)、[C-0013](../conjectures/C-0013.md) |
| 初出 | [2026-09-30 第 20 回](../summaries/2026-09-30_20_terms-setting-and-agents.md) |

## 定義

有限な実験 $`e`$（[D-0001](D-0001.md)）のプロトコルを $`π`$、観測者を $`O_e`$ とする。

1. **観測者の実験における時空**：観測者 $`O`$ の基準の時計と物差しで決まる座標 $`(t, 𝐱)`$ の空間 $`M_O := ℝ^{1+n}`$。座標の位相と、$`ℝ^{1+n}`$ の上のノルムから決まる座標の距離 $`d_O`$（例えば、$`d_O = \max(v_0 \left| Δt \right|, \left| Δ𝐱 \right|)`$）。ここで $`v_0 > 0`$ は時間と長さの単位を換算する任意の有限な係数で、[C-0009](../conjectures/C-0009.md) の不変な速さ $`c`$ とは別物である（ガリレイ変換の場合の $`c = ∞`$ では、距離にならないため。PR #42 �
2. **較正の写像**：時空の読みを持つプロトコルの実験 $`e`$ について、[A-0010](../assumptions/A-0010.md) の換算を、次の二つの連続な部分写像として書く。
   - **準備の事象**：$`τ_e : X_π ⇀ M_{O_e}`$。設定 $`x`$ の観測で、準備（放出、開始など）を行う時刻と場所を、観測者 $`O_e`$ の座標で表したもの。
   - **登録の事象**：$`σ_e : X_π × Y_π ⇀ M_{O_e}`$。設定 $`x`$ の観測で結果 $`y`$ を得たとき、装置が登録（検出など）した時刻と場所を、観測者 $`O_e`$ の座標で表したもの。
   - **複合のプロトコル**（[D-0001](D-0001.md) の注意。$`M`$ 個の部分装置で並列に観測する $`π^M`$）では、準備の事象と登録の事象を部分装置ごとに定め、値を $`M_{O_e}^M`$ にとる：$`τ_e : X_π^M ⇀ M_{O_e}^M`$、$`σ_e : X_π^M × Y_π^M ⇀ M_{O_e}^M`$。第 $`k`$ 成分 $`τ_e^k`$・$`σ_e^k`$ 
…（以下 4235 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
=== assumptions/A-0016.md
## 主張

実際の実験 $`e`$（[D-0002](../definitions/D-0002.md)）の各観測 $`i`$ について、準備の事象 $`τ_e(x_i)`$ と登録の事象 $`σ_e(x_i, y_i)`$（[D-0013](../definitions/D-0013.md)）がともに定まるなら、観測者 $`O_e`$ の時刻の座標で、登録の事象は準備の事象より前にない：$`t\bigl(σ_e(x_i, y_i)\bigr) ≥ t\bigl(τ_e(x_i)\bigr)`$。複合のプロトコル（[D-0013](../definitions/D-0013.md)。$`M`$ 個の部分装置）では、部分装置ごとに $`t\bigl(σ_e^k(x_i, y_i)\bigr) ≥ t\bigl(τ_e^k(x_i)\bigr)`$（$`k = 1, …, M`$）とする。

さらに、適応的な設定（[D-0001](../definitions/D-0001.md)）で、$`i`$ 回目の設定 $`x_i`$ が $`j`$ 回目（$`j < i`$）の結果 $`y_j`$ に依存して選ばれ、観測の事象の族（[D-0013](../definitions/D-0013.md) の 3。各回の準備の時刻と場所を区別する読みが、その回の設定に含まれる場合）の中で $`j`$ 回目の登録の事象と $`i`$ 回目の準備の事象がともに定まるなら、観測者 $`O_e`$ の時刻の座標で、$`j`$ 回目の登録の事象は $`i`$ 回目の準備の事象より後にない：$`t\bigl(σ_e(x_j, y_j)\bigr) ≤ t\bigl(τ_e(x_i)\bigr)`$。複合のプロトコルでは、すべての部分装置の組 $`k`$、$`l`$ について $`t\bigl(σ_e^k(x_j, y_j)\bigr) ≤ t\bigl(τ_e^l(x_i)\bigr)`$ と

## 採用の理由

ユーザーの提案（第 20 回）。実際の実験で因果的な順序を破るものがないことは、ほかのどの定義・前提からも導けないので、前提として置く（ユーザーの提案は因果的な順序についてのものだが、今の段階で述べられるのは、一人の観測者の座標時刻での順序だけである）。可能な実験について同じことが成り立つかは、予想 [C-0012](../conjectures/C-0012.md) とする。

## 注意
=== assumptions/A-0014.md
## 主張

二つの実際の観測者 $`O`$、$`O'`$（[D-0001](../definitions/D-0001.md)・[D-0002](../definitions/D-0002.md)）の基準の時計と物差しを比べる実際の実験（比較の実験）$`c`$ を行ったとき、座標の間の取り替え $`φ_c : M_O ⇀ M_{O'}`$（[D-0013](../definitions/D-0013.md)）を、比較を行った範囲に限って、その記録から定まる部分写像として与える。比較の実験の連鎖 $`γ = (c_1, …, c_k)`$ については、合成が定義できる範囲で、経路に付いた取り替え $`φ_γ := φ_{c_k} ∘ ⋯ ∘ φ_{c_1}`$ を与える。取り替えについて、それ以外の仮定（経路に依らないこと、合成の整合性、写像の形）は置かない。観測者の組だ
…（以下 911 文字を省略）
```

</details>

## Claude

7 件の原典（arXiv 版の本文）を読み終えたので、結果を報告します。各文献の定理・式は本文で確かめたものです。見出しに「Claude の見立て」と付けた部分は、プロジェクトへの当てはめで、私の解釈です。

#### 1. 原典で確かめた内容

| 文献 | 確かめた内容 |
| --- | --- |
| Giovannetti–Lloyd–Maccone 2015（PRD 92, 045033） | Page–Wootters の形（拘束 $`\hat{J}\lvert Ψ⟩⟩ = 0`$、時計の時刻 $`t`$ での条件付け）で 2 時刻の統計を出すときは、測定ごとに記憶系 $`M_n`$ を足し、結果を記録させる。そのうえで、**時計のただ一つの時刻 $`t`$ で、すべての記憶をまとめて読む**（式 (45)・(46)）。Kuchař の「時計が止まる」批判への答えは「過去は今の記録としてだけ存在する」というもの。時計は直線上の粒子として理想化している（ハミルトニアンは有界でない）。 |
| Höhn–Smith–Lock 2021（PRD 104, 066001） | 時計の時刻は、時計のハミルトニアンについて共変な POVM で表す（式 (7)〜(12)）。ハミルトニアンが有界な時計では、時計の状態が直交せず、**読みは完全には区別できない**（それでも単調で、確率としての解釈はある。Unruh–Wald の批判への応答）。定理 4：1 時刻の条件付き確率は、関係的なディラック観測量の期待値に等しい（ゲージ不変）。2 時刻の条件付き確率は式 (76)〜(78) で、補助系なしに正しい遷移確率を与える。前提として、**時計と系の相互作用がないこと**（式 (4)）を置いている。また、時間的な局在は時計の選び方に依存する（VII C 節）。 |
| Smith–Ahmadi 2020（Nat. Commun. 11, 5360） | 二つの時計の読みの条件付き確率 $`P(τ_A \mid τ_B)`$（式 (14)）。運動量の波束では、古典的な時間の遅れと平均で一致する。運動量の重ね合わせでは、同じ重みの**古典的な混合とは違う遅れ** $`γ_Q^{-1}`$ が現れる（式 (23)〜(25)。干渉の項 $`\cos φ`$ を含む）。 |
| Giacomini–Castro-Ruiz–Brukner 2019（Nat. Commun. 10, 494） | 量子参照系の取り替えは、「座標変換の重ね合わせ」としてのユニタリ $`\hat{S}_x = \hat{P}_{AC}\, e^{\frac{i}{ℏ} \hat{x}_A \hat{p}_B}`$（式 (2)）で表す。もつれや重ね合わせは参照系に依存する。測定の結果の確率は参照系によらない（式 (31)）。一方、**どの系のどの観測量を測ったかの記述**は、参照系によって変わる（Methods の測定の節）。 |
| Castro-Ruiz–Giacomini–Belenchia–Brukner 2020（Nat. Commun. 11, 2672） | 実験は二段階で記述される（図 1）。準備の段階では、つまみの設定を選び、時計が $`t^*`$ を示したときに操作を起こすよう仕込む。検出の段階では、時計と補助系の記録を読む。設定の選択は後の結果に依存しないと仮定し、すべての記録を共有して事象を時空に写す。時計が重力で相互作用すると、**事象の時間的な局在が参照系に依存する**。「どの事象もはっきり局在する時間参照系が存在すること」を、計量が確定していることの特徴づけとして提案している。重力による量子スイッチ（因果順序の重ね合わせ）の例もある。確率は $`p = \mathrm{Tr}\, W M`$（時空の側 $`W`$ と局所的な操作 $`M`$）に分かれる（式 (35)）。 |
| Loveridge–Miyadera–Busch 2018（Found. Phys. 48, 135） | 観測量は、系と参照系の相対量（対称性の下で不変なもの）と考える。「絶対的な」量は、参照系の状態で制限した相対量に当たる。参照系の状態がよく局在していれば、絶対的な量はよい近似になる（定理 1、命題 7）。逆に、近似がよいためには、参照系の生成子の広がりが大きいこと、つまり参照系が大きいことが要る（定理 3）。 |
| Bartlett–Rudolph–Spekkens 2007（RMP 79, 555） | 参照系がないことは、群の平均（twirl）による超選択則と同じになる。有界でない量子参照系を系に加えれば、**すべての準備・操作・測定について**元の統計を再現できる（式 (4.22)。参照系の量子化）。逆の操作（脱量子化）には、参照系が系より十分大きいという条件が要る。有界な参照系の場合は近似になる。 |

#### 2. 判定基準 $`𝒯`$ への当てはめ（Claude の見立て）

- **(a) で書き直せること**：読んだ扱いはどれも、予測を**時計の読みと記録（ポインタ・記憶・補助系）の確率**として出している。どれも、読み出す前の量子的な出力を残したまま、実験の対象にするものではない。したがって、「古典的な記録と、量子的な時計を含むモデルの組」として (a) で書き直せる。GLM の「記憶をまとめて読む」構成は、D-0001 の「逐次の測定の一括読み出し」（第 22 回の調査メモの 4.3）と同じ形である。
- **ただし、揺らぐのは (a)・(b) の区別ではなく、D-0013 の較正の構造である。** 見えてきた段階は三つある。
  1. **決定的な較正**（今の D-0013）：Loveridge ほかの定理と Bartlett ほかの式 (4.22) から、参照系が大きく、よく局在している極限での近似として正当化できる。
  2. **確率的な較正（マルコフ核）**：有界な時計は POVM で表され、読みが揺らぐ。$`P(τ_A \mid τ_B)`$ はそのまま核の例になる。
     - 注意 1：数学的には、どんな核も「決定的な写像を乱数で混ぜたもの」に書ける。Smith–Ahmadi の量子的な時間の遅れが示すのは、その混合を「用意した運動量の分布に従う古典的な世界線」と同一視できないことである。
     - 注意 2：核は時計の運動状態に依存するので、A-0013（較正の普遍性）と緊張がある。
  3. **事象ごとに位置を定めない場合**：量子スイッチで制御系を重ね合わせの基底で測る場合、事象の位置を確率的に割り当てる記述（因果順序の混合）では統計を再現できない、とされている。これは因果的非分離性（causal non-separability）の結果で、今回は**原典を確かめていない**。この場合でも、実験全体の記録の分布は (a) で書ける。失われるのは、各事象が $`M_O`$ に位置を持つという D-0013 の仮定と、A-0016 の順序である。
- **参照系の取り替え**：Giacomini ほかの取り替えは、$`M_O`$ の上の点の写像ではなく、モデル（ヒルベルト空間）の側のユニタリである。A-0015 の群 $`G`$ の作用には収まらない。記録から取り替えを与える A-0014 の体系なら、記録の分布の不変性（式 (31)）とは両立しうる。

**(a)・(b) の判断に向けたまとめ**（見立て）：量子時計・量子参照系の既存の扱いは、どれも (b) を必要としない。本当の論点は、「(a) の中で、較正を決定的・確率的・事象ごとに位置を定めない、のどの段階まで許すか」にある。

この先の進め方を相談させてください。

<details><summary>ツール: AskUserQuestion</summary>

```text
（入力の本文は省略。項目: questions）
```

</details>

<details><summary>結果: AskUserQuestion</summary>

```text
Your questions have been answered: "次に何をしますか？"="調査メモにまとめる（推奨）", "上の見立て（論点を「(a) の中での較正の 3 段階」として整理する）をどう扱いますか？"="見立てとして記録のみ（推奨）". You can now continue with these answers in mind.
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git status --short | head; git branch --show-current; git log --oneline -5; git fetch -q origin main && git log --oneline -3 origin/main; ls surveys | tail -3; cd ../point-free-spacetime-private && git status --short | head; git log --oneline -3; ls -t papers | head -10; ls -t /tmp/claude-0/-home-user/[ID]/scratchpad 2>/dev/null | head -20
```

</details>

<details><summary>結果: Bash</summary>

```text
claude/clever-planck-pr5kq1
4238cba Merge pull request #44 from kittenkiki15/claude/clever-planck-pr5kq1
99d353a 第 22 回のクロスモデルレビューの詳細化の論点（適応的な設定の核の不変性と乱数の独立性）を A-0006 の未解決の点に記録した
9d21ed2 R-0009 に、記憶のない通信路を 2 回使う設定であることを明記した（第 22 回のクロスモデルレビューの詳細化の論点）
809a263 第 22 回のクロスモデルレビューに対応：中間の立場で合成性を保つ条件を全体のコムまたは因子化の条件に限定し、設定の追加の扱いを D-0001 の未解決の点に記録した
e7f23e7 第 22 回のクロスモデルレビューに対応：合成性が失われる原因を、トモグラフィーの不足と共有相関の欠落の二つとして並べた
4238cba Merge pull request #44 from kittenkiki15/claude/clever-planck-pr5kq1
99d353a 第 22 回のクロスモデルレビューの詳細化の論点（適応的な設定の核の不変性と乱数の独立性）を A-0006 の未解決の点に記録した
9d21ed2 R-0009 に、記憶のない通信路を 2 回使う設定であることを明記した（第 22 回のクロスモデルレビューの詳細化の論点）
2026-09-30_20_agent-observer-apparatus.md
2026-10-01_22_combs-and-composites.md
README.md
91dd8d1 Merge pull request #13 from kittenkiki15/claude/clever-planck-pr5kq1
82b7619 第 22 回：量子コム・一般化確率論の論文 7 件の PDF を追加した
97555ba Merge pull request #12 from kittenkiki15/claude/zealous-keller-o7r1sv
README.md
barrett2007.pdf
harrow2010.pdf
pollock2018.pdf
gutoski2007.pdf
chiribella2008memory.pdf
chiribella2008architecture.pdf
chiribella2009.pdf
vandervaart2002.pdf
vovk2023.pdf
```

</details>

<details><summary>ツール: Bash</summary>

```text
ls -la ~/.claude/projects/-home-user/ ; cd ~/.claude/projects/-home-user && for f in *.jsonl; do echo "== $f"; python3 - "$f" <<'EOF'
import json,sys
for l in open(sys.argv[1]):
    d=json.loads(l)
    if d.get('type')=='user' and d.get('timestamp','')>'2026-10-01T15:15':
        c=d['message']['content']
        t=c if isinstance(c,str) else (c[0].get('text','') if isinstance(c,list) and c and c[0].get('type')=='text' else '')
        if t and not t.startswith('<'): print(d['timestamp'], t[:80].replace('\n',' '))
EOF
done
```

</details>

<details><summary>結果: Bash</summary>

```text
total 11044
drwx------ 6 root root    4096 Oct  1 23:52 .
drwx------ 3 root root    4096 Oct  1 08:36 ..
drwx------ 3 root root    4096 Oct  1 23:57 [ID]
-rw------- 1 root root 1420163 Oct  2 00:01 [ID].jsonl
drwx------ 2 root root    4096 Oct  1 15:18 [ID]
-rw------- 1 root root    2054 Oct  1 15:23 [ID].jsonl
drwx------ 3 root root    4096 Oct  2 00:52 [ID]
-rw------- 1 root root 8658014 Oct  2 00:52 [ID].jsonl
drwx------ 2 root root    4096 Oct  1 11:37 [ID]
-rw------- 1 root root 1184405 Oct  1 11:42 [ID].jsonl
== [ID].jsonl
2026-10-01T23:52:15.493Z 次のセッションを開始してください。
== [ID].jsonl
== [ID].jsonl
2026-10-01T23:52:15.493Z 次のセッションを開始してください。
== [ID].jsonl
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd ~/.claude/projects/-home-user && python3 - <<'EOF'
import json
for l in open('[ID].jsonl'):
    d=json.loads(l)
    if d.get('timestamp','')<'2026-10-01T23:50': continue
    if d.get('type')=='assistant':
        for c in d['message']['content']:
            if c.get('type')=='text' and c['text'].strip(): print('A',d['timestamp'], c['text'][:3000]); print()
            if c.get('type')=='tool_use': print('T',d['timestamp'], c['name'], json.dumps(c['input'],ensure_ascii=False)[:200])
    if d.get('type')=='user':
        c=d['message']['content']
        if isinstance(c,list):
            for x in c:
                if x.get('type')=='tool_result' and 'answered' in str(x.get('content'))[:100]: print('ANS',str(x.get('content'))[:600])
EOF
```

</details>

<details><summary>結果: Bash</summary>

```text
T 2026-10-01T23:52:17.460Z Bash {"command": "cd /home/user/point-free-spacetime && git status | head -3 && git log --oneline -3 && cat NEXT.md"}
T 2026-10-01T23:52:21.389Z Bash {"command": "git fetch origin main 2>&1 | tail -1; git log --oneline -3 origin/main; git merge-base --is-ancestor HEAD origin/main && echo \"HEAD in main\"; git log --oneline origin/main..HEAD | head;
T 2026-10-01T23:52:27.282Z Bash {"command": "cd /home/user/point-free-spacetime && git checkout -B claude/clever-planck-pr5kq1 origin/main -q && git log --oneline -1; cd ../point-free-spacetime-private && git merge-base --is-ancesto
A 2026-10-01T23:52:29.017Z Now let me read the T-0019 section of the roadmap and sections 3–5 of the session 22 survey notes.

T 2026-10-01T23:52:29.754Z Bash {"command": "cd /home/user/point-free-spacetime && awk '/^### T-0019/,/^### T-0020|^## /' roadmap.md | head -80; echo ----; grep -n '^## ' surveys/2026-10-01_22_combs-and-composites.md"}
T 2026-10-01T23:52:31.421Z Bash {"command": "sed -n 79,200p surveys/2026-10-01_22_combs-and-composites.md"}
T 2026-10-01T23:52:34.543Z Bash {"command": "cd /home/user/point-free-spacetime-private && ls papers | tail -30; cd ../point-free-spacetime && ls summaries | tail -2; curl -sS -o /dev/null -w \"%{http_code}\\n\" https://arxiv.org/ab
T 2026-10-01T23:52:46.132Z AskUserQuestion {"questions": [{"header": "重点", "multiSelect": false, "options": [{"description": "量子参照系・量子時計（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）を原典で確かめ、判定基準 𝒯 を当て
…（以下 13560 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd ~/.claude/projects/-home-user && python3 - <<'EOF' > /tmp/claude-0/-home-user/[ID]/scratchpad/s23report.md
import json
for l in open('[ID].jsonl'):
    d=json.loads(l)
    t=d.get('timestamp','')
    if t<'2026-10-01T23:52' or t>'2026-10-01T23:58': continue
    if d.get('type')=='assistant':
        for c in d['message']['content']:
            if c.get('type')=='text' and len(c['text'])>2000: print(c['text'])
            if c.get('type')=='tool_use' and c['name']=='AskUserQuestion': print(json.dumps(c['input'],ensure_ascii=False,indent=1))
            if c.get('type')=='tool_use' and 'giovannetti2015:1504' in json.dumps(c['input']): print(c['input']['command'])
EOF
wc -c /tmp/claude-0/-home-user/[ID]/scratchpad/s23report.md; ls /tmp/claude-0/-home-user/[ID]/scratchpad/ | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
10917 /tmp/claude-0/-home-user/[ID]/scratchpad/s23report.md
bartlett2007.pdf
bartlett2007.raw.txt
bartlett2007.txt
castroruiz2020.pdf
castroruiz2020.raw.txt
castroruiz2020.txt
giacomini2019.pdf
giacomini2019.raw.txt
giacomini2019.txt
giovannetti2015.pdf
giovannetti2015.raw.txt
giovannetti2015.txt
hoehn2021.pdf
hoehn2021.raw.txt
hoehn2021.txt
loveridge2018.pdf
loveridge2018.raw.txt
loveridge2018.txt
smith2020.pdf
smith2020.raw.txt
smith2020.txt
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Read: /tmp/claude-0/-home-user/[ID]/scratchpad/s23report.md</summary>

```text
（入力の本文は省略。項目: file_path）
```

</details>

<details><summary>結果: Read: /tmp/claude-0/-home-user/[ID]/scratchpad/s23report.md</summary>

```text
1	{
2	 "questions": [
3	  {
4	   "header": "重点",
5	   "multiSelect": false,
6	   "options": [
7	    {
8	     "description": "量子参照系・量子時計（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）を原典で確かめ、判定基準 𝒯 を当てはめる。(a)・(b) の判断に直接効く。項目 2 は時間があれば。",
9	     "label": "項目 3 を先に（推奨）"
10	    },
11	    {
12	     "description": "Le Cam の理論の量子版（Buscemi、Jenčová、松本、Guţă–Kahn）を原典で確かめる。項目 3 は時間があれば。",
13	     "label": "項目 2 を先に"
14	    },
15	    {
16	     "description": "両方の主要な文献で、定理の仮定と結論だけを確かめ、T-0019 を今回で閉じることを目指す。",
17	     "label": "両方を浅く"
18	    }
19	   ],
20	   "question": "今回はどちらの項目を中心に調べますか？"
21	  },
22	  {
23	   "header": "深さ",
24	   "multiSelect": false,
25	   "options": [
26	    {
27	     "description": "第 22 回と同じく、arXiv 版の原典の本文で、定理の仮定と結論を確かめる（数件〜8 件程度）。",
28	     "label": "中心の文献の本文で確認（推奨）"
29	    },
30	    {
31	     "description": "文献の範囲を広く取り、要旨と主要な結果の確認にとどめる。",
32	     "label": "要旨と主要な結果のみ"
33	    }
34	   ],
35	   "question": "調べる深さはどうしますか？"
36	  }
37	 ]
38	}
39	cd /tmp/claude-0/-home-user/[ID]/scratchpad && for p in "giovannetti2015:1504.04215" "giacomini2019:1712.07207" "castroruiz2020:1908.10165" "hoehn2021:1912.00033" "loveridge2018:1703.10434" "smith2020:1904.12390" "bartlett2007:quant-ph/0610030"; do k=${p%%:*}; id=${p#*:}; curl -sSL -o $k.pdf "https://arxiv.org/pdf/$id"; pdftotext -layout $k.pdf $k.txt 2>/dev/null; echo "$k $(wc -l < $k.txt) $(file -b $k.pdf | cut -c1-20)"; done
40	7 件の原典（arXiv 版の本文）を読み終えたので、結果を報告します。各文献の定理・式は本文で確かめたものです。見出しに「Claud
…（以下 4303 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && for k in giovannetti2015 giacomini2019 castroruiz2020 hoehn2021 loveridge2018 smith2020 bartlett2007; do echo "$k: $(grep -c "{$k," references.bib)"; done; grep -n -A10 "@article{harrow2010" references.bib; grep -n "harrow2010" ../point-free-spacetime-private/papers/README.md; S=/tmp/claude-0/-home-user/[ID]/scratchpad; for k in giovannetti2015 giacomini2019 castroruiz2020 hoehn2021 loveridge2018 smith2020 bartlett2007; do head -c 300 $S/$k.txt | tr '\n' ' ' | cut -c1-200; echo; done
```

</details>

<details><summary>結果: Bash</summary>

```text
giovannetti2015: 0
giacomini2019: 1
castroruiz2020: 0
hoehn2021: 0
loveridge2018: 0
smith2020: 0
bartlett2007: 0
1072:@article{harrow2010,
1073-  author  = {Harrow, Aram W. and Hassidim, Avinatan and Leung, Debbie W. and Watrous, John},
1074-  title   = {Adaptive versus nonadaptive strategies for quantum channel discrimination},
1075-  journal = {Physical Review A},
1076-  volume  = {81},
1077-  pages   = {032339},
1078-  year    = {2010},
1079-  doi     = {10.1103/PhysRevA.81.032339},
1080-  eprint  = {0909.0256},
1081-}
1082-
76:| `harrow2010.pdf` | Harrow–Hassidim–Leung–Watrous, Adaptive versus nonadaptive strategies for quantum channel discrimination (2010) | arXiv:0909.0256v1（第 22 回に取得。Phys. Rev. A 81, 032339） |
                                                                                                  Quantum Time                                                                               Vittorio Gi

                                           Quantum mechanics and the covariance of physical laws in quantum reference frames                                                              Flaminia Giaco

                                                  Quantum clocks and the temporal localisability of events in the presence of                                                                        gra

                                                                            The Trinity of Relational Quantum Dynamics                                                 
…（以下 638 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n -A9 "{giacomini2019," references.bib; ls ../point-free-spacetime-private/papers | grep -i "giacomini\|bartlett\|hoehn"; for id in 1504.04215 1712.07207 1908.10165 1912.00033 1703.10434 1904.12390 quant-ph/0610030; do curl -sSL "https://arxiv.org/abs/$id" | grep -o -E 'arXiv:[0-9a-z./-]+v[0-9]+|<td class="tablecell jref">[^<]*|citation_title" content="[^"]*|citation_author" content="[^"]*' | head -8 | tr '\n' ' '; echo; done
```

</details>

<details><summary>結果: Bash</summary>

```text
1007:@article{giacomini2019,
1008-  author  = {Giacomini, Flaminia and Castro-Ruiz, Esteban and Brukner, \v{C}aslav},
1009-  title   = {Quantum mechanics and the covariance of physical laws in quantum reference frames},
1010-  journal = {Nature Communications},
1011-  volume  = {10},
1012-  pages   = {494},
1013-  year    = {2019},
1014-  doi     = {10.1038/s41467-018-08155-0},
1015-  eprint  = {1712.07207},
1016-}
giacomini2019.pdf
citation_title" content="Quantum Time citation_author" content="Giovannetti, Vittorio citation_author" content="Lloyd, Seth citation_author" content="Maccone, Lorenzo arXiv:1504.04215v3 <td class="tablecell jref">Phys. Rev. D 92, 045033 (2015) 
citation_title" content="Quantum mechanics and the covariance of physical laws in quantum reference frames citation_author" content="Giacomini, Flaminia citation_author" content="Castro-Ruiz, Esteban citation_author" content="Brukner, Časlav arXiv:1712.07207v2 <td class="tablecell jref">Nat. Commun. 10, 494 (2019) 
citation_title" content="Quantum clocks and the temporal localisability of events in the presence of gravitating quantum systems citation_author" content="Castro-Ruiz, Esteban citation_author" content="Giacomini, Flaminia citation_author" content="Belenchia, Alessio citation_author" content="Brukner, Časlav arXiv:1908.10165v2 <td class="tablecell jref">Nat Commun 11, 2672 (2020) 
citation_title" content="The Trinity of Relational Quantum Dynamics citation_author" content="Hoehn, Philipp A. citati
…（以下 970 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime-private && git checkout -q -B claude/clever-planck-pr5kq1 origin/main 2>/dev/null || (git fetch -q origin main && git checkout -q -B claude/clever-planck-pr5kq1 origin/main); git log --oneline -1; S=/tmp/claude-0/-home-user/[ID]/scratchpad; for k in giovannetti2015 castroruiz2020 hoehn2021 loveridge2018 smith2020 bartlett2007; do cp $S/$k.pdf papers/; done; python3 - <<'EOF'
p='papers/README.md'; s=open(p).read().rstrip('\n')
rows=[
("giovannetti2015","Giovannetti–Lloyd–Maccone, Quantum time (2015)","arXiv:1504.04215v3（第 23 回に取得。Phys. Rev. D 92, 045033）"),
("castroruiz2020","Castro-Ruiz–Giacomini–Belenchia–Brukner, Quantum clocks and the temporal localisability of events in the presence of gravitating quantum systems (2020)","arXiv:1908.10165v2（第 23 回に取得。Nat. Commun. 11, 2672）"),
("hoehn2021","Höhn–Smith–Lock, The trinity of relational quantum dynamics (2021)","arXiv:1912.00033v3（第 23 回に取得。Phys. Rev. D 104, 066001）"),
("loveridge2018","Loveridge–Miyadera–Busch, Symmetry, reference frames, and relational quantities in quantum mechanics (2018)","arXiv:1703.10434v1（第 23 回に取得。Found. Phys. 48, 135）"),
("smith2020","Smith–Ahmadi, Quantum clocks observe classical and quantum time dilation (2020)","arXiv:1904.12390v3（第 23 回に取得。Nat. Commun. 11, 5360）"),
("bartlett2007","Bartlett–Rudolph–Spekkens, Reference frames, superselection rules, and quantum information (2007)","arXiv:quant-ph/0610030v3（第 23 回に取得。Rev. Mod. Phys. 
…（以下 154 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
91dd8d1 Merge pull request #13 from kittenkiki15/claude/clever-planck-pr5kq1
| `harrow2010.pdf` | Harrow–Hassidim–Leung–Watrous, Adaptive versus nonada
| `barrett2007.pdf` | Barrett, Information processing in generalized probabilist
| `giovannetti2015.pdf` | Giovannetti–Lloyd–Maccone, Quantum time (2015) | a
| `castroruiz2020.pdf` | Castro-Ruiz–Giacomini–Belenchia–Brukner, Quantum 
| `hoehn2021.pdf` | Höhn–Smith–Lock, The trinity of relational quantum dyna
| `loveridge2018.pdf` | Loveridge–Miyadera–Busch, Symmetry, reference frames
| `smith2020.pdf` | Smith–Ahmadi, Quantum clocks observe classical and quantum
| `bartlett2007.pdf` | Bartlett–Rudolph–Spekkens, Reference frames, supersel
 M papers/README.md
?? papers/bartlett2007.pdf
?? papers/castroruiz2020.pdf
?? papers/giovannetti2015.pdf
?? papers/hoehn2021.pdf
?? papers/loveridge2018.pdf
?? papers/smith2020.pdf
```

</details>

## Claude

Now the bib entries.

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && cat >> references.bib <<'EOF'

@article{giovannetti2015,
  author  = {Giovannetti, Vittorio and Lloyd, Seth and Maccone, Lorenzo},
  title   = {Quantum time},
  journal = {Physical Review D},
  volume  = {92},
  pages   = {045033},
  year    = {2015},
  doi     = {10.1103/PhysRevD.92.045033},
  eprint  = {1504.04215},
}

@article{castroruiz2020,
  author  = {Castro-Ruiz, Esteban and Giacomini, Flaminia and Belenchia, Alessio and Brukner, \v{C}aslav},
  title   = {Quantum clocks and the temporal localisability of events in the presence of gravitating quantum systems},
  journal = {Nature Communications},
  volume  = {11},
  pages   = {2672},
  year    = {2020},
  doi     = {10.1038/s41467-020-16013-1},
  eprint  = {1908.10165},
}

@article{hoehn2021,
  author  = {H{\"o}hn, Philipp A. and Smith, Alexander R. H. and Lock, Maximilian P. E.},
  title   = {Trinity of relational quantum dynamics},
  journal = {Physical Review D},
  volume  = {104},
  pages   = {066001},
  year    = {2021},
  doi     = {10.1103/PhysRevD.104.066001},
  eprint  = {1912.00033},
}

@article{loveridge2018,
  author  = {Loveridge, Leon and Miyadera, Takayuki and Busch, Paul},
  title   = {Symmetry, reference frames, and relational quantities in quantum mechanics},
  journal = {Foundations of Physics},
  volume  = {48},
  pages   = {135--198},
  year    = {2018},
  doi     = {10.1007/s10701-018-0138-3},
  eprint  = {1703.10434},
}

@article{smith2020,
  author  = {Smith
…（以下 697 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
doi     = {10.1103/RevModPhys.79.555},
  eprint  = {quant-ph/0610030},
}
 M references.bib
```

</details>

<details><summary>ツール: Write: /home/user/point-free-spacetime/surveys/2026-10-02_23_quantum-clocks-and-frames.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/surveys/2026-10-02_23_quantum-clocks-and-frames.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/surveys/2026-10-02_23_quantum-clocks-and-frames.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash</summary>

```text
for f in definitions/D-0013.md assumptions/A-0013.md assumptions/A-0016.md assumptions/A-0014.md assumptions/A-0015.md; do echo "=== $f"; sed -n '/## 未解決の点/,/## 履歴/p' $f | grep -n "確率的\|較正が\|因果的な順序\|強い形\|観測者の全体\|比較の実験の形" | cut -c1-120; done
```

</details>

<details><summary>結果: Bash</summary>

```text
=== definitions/D-0013.md
7:- **因果的な順序**：実際の実験について、観測者の座標時刻で登録の事象が準備の事象�
11:- 較正が確率的になる場合（時計が量子系である場合など。[T-0019](../roadmap.md)）の扱い�
=== assumptions/A-0013.md
6:- 較正が確率的になる場合（[D-0013](../definitions/D-0013.md) の未解決の点）の普遍性の述べ方
=== assumptions/A-0016.md
3:- 複合のプロトコルで、適応的な場合の順序をすべての部分装置の組について課すか（�
5:- 強い形（登録の事象が準備の事象の因果的な未来にある）への置き換えと、そのため�
=== assumptions/A-0014.md
3:- 比較の実験の形（レーダー座標、時計の運搬など。ロードマップの T-0017 の操作的な座
=== assumptions/A-0015.md
3:- 観測者の全体（実際の観測者か、可能な観測者も含むか）。
4:- 取り替えを $`M_O`$ 全体の上の写像とすることと、較正が観測者の世界線の区間の近く�
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
SV="[第 23 回の調査メモ](../surveys/2026-10-02_23_quantum-clocks-and-frames.md)"
def add_after_line(p, startswith, text):
    L=open(p).read().split('\n')
    i=[k for k,l in enumerate(L) if l.startswith(startswith)]
    assert len(i)==1,(p,startswith,len(i))
    # append to end of that bullet line
    L[i[0]]=L[i[0]]+text
    open(p,'w').write('\n'.join(L))
add_after_line('definitions/D-0013.md',"- 較正が確率的になる場合（時計が量子系である場合など。",
 f" 第 23 回の見立て：量子時計・量子参照系の既存の扱いを当てはめると、較正には三つの段階がある。(1) 決定的な較正（参照系が大きく、よく局在している極限での近似。Loveridge ほか 2018、Bartlett ほか 2007）、(2) 確率的な較正（有界な時計の POVM による読みの揺らぎ。核は時計の運動状態に依存する。Höhn ほか 2021、Smith–Ahmadi 2020）、(3) 事象ごとに位置を定めない場合（量子スイッチなど。各事象が $`M_O`$ に位置を持つという仮定が失われる。因果的非分離性の原典は未確認）。どの段階まで許すかは、T-0019 の後にユーザーが判断する（{SV}の 3.2 節）。")
add_after_line('assumptions/A-0013.md',"- 較正が確率的になる場合（",
 f" 第 23 回の見立て：有界な量子時計では、較正の核が時計の運動状態に依存する（Smith–Ahmadi 2020 の量子的な時間の遅れ）。普遍性を保つには、時計の状態を設定に含めるか、推定の対象ごとの核を使う形に改める必要がありうる（{SV}の 3.2 節・4 節）。")
add_after_line('assumptions/A-0016.md',"- 強い形（登録の事象が準備の事象の因果的な未来にある）",
 f" 第 23 回の見立て：事象の位置を確率的に割り当てる記述で再現できない実験（重力による量子スイッチなど。Castro-Ruiz ほか 2020）では、観測者の座標時刻での順序そのものが定まらない。この前提の順序は、較正が決定的か確率的な範囲での前提と位置づけられる（{SV}の 3.2 節）。")
add_after_line('assumptions/A-0015.md',"- 観測者の全体（",
 f"\n- 量子参照系の取り替え（Giacomini ほか 2019）は、$`M_O`$ の上の点の写像ではなく、モデル（ヒルベルト空間）の側のユニタリであり、この前提の群 $`G`$ の作用には収まらない。量子的な観測者を可能な観測者に含めるなら、この体系の適用範囲を限る必要がある（第 23 回の見立て。{SV}の 3.3 節）。")
add_after_line('assumptions/A-0014.md',"- 比較の実験の形（",
 f"\n- 量子参照系の取り替え（Giacomini ほか 2019）
…（以下 191 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
35 passed in 0.17s
 assumptions/A-0013.md |  2 +-
 assumptions/A-0014.md |  1 +
 assumptions/A-0015.md |  1 +
 assumptions/A-0016.md |  2 +-
 definitions/D-0013.md |  2 +-
 references.bib        | 66 +++++++++++++++++++++++++++++++++++++++++++++++++++
 6 files changed, 71 insertions(+), 3 deletions(-)
```

</details>

<details><summary>ツール: Bash</summary>

```text
git add -A && git commit -q -m "第 23 回（途中）：T-0019 の項目 3（量子時計・量子参照系）の調査メモと参考文献を追加し、D-0013・A-0013〜A-0016 の未解決の点に見立てを記録した

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: [セッション URL]" && git push -q -u origin claude/clever-planck-pr5kq1 2>&1 | tail -2; git log --oneline -1; cd ../point-free-spacetime-private && git add -A && git commit -q -m "第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加した

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: [セッション URL]" && git push -q -u origin claude/clever-planck-pr5kq1 2>&1 | tail -2; git log --oneline -1
```

</details>

<details><summary>結果: Bash</summary>

```text
remote:      https://github.com/kittenkiki15/point-free-spacetime/pull/new/claude/clever-planck-pr5kq1        
remote: 
7fa413f 第 23 回（途中）：T-0019 の項目 3（量子時計・量子参照系）の調査メモと参考文献を追加し、D-0013・A-0013〜A-0016 の未解決の点に見立てを記録した
remote:      https://github.com/kittenkiki15/point-free-spacetime-private/pull/new/claude/clever-planck-pr5kq1        
remote: 
cdd152d 第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加した
```

</details>

## Claude

お選びいただいた「調査メモにまとめる」「見立てとして記録のみ」に沿って、調査メモの草稿を書き、未解決の点にも記録しました。

途中で会話の履歴が一部失われましたが、セッション記録から第 23 回の経緯を確かめて作業しています。経緯は次のとおりです。
- 項目 3 を先に、中心の文献の本文で調べることにした（ユーザーの判断）。
- 7 件の原典を読み、内容を報告した。
- その後、上の二つをお選びいただいた。

**調査メモ**（`surveys/2026-10-02_23_quantum-clocks-and-frames.md`）
- 1・2 節：7 件の文献と、原典で確かめた内容です。
  - Giovannetti ほか 2015、Höhn ほか 2021、Smith–Ahmadi 2020、Giacomini ほか 2019、Castro-Ruiz ほか 2020、Loveridge ほか 2018、Bartlett ほか 2007。
- 3 節（見立て）：既存の扱いは、どれも (a) で書き直せます。論点は (a)・(b) の区別ではなく、較正をどの段階まで許すかにあると整理しました。段階は次の三つです。
  - 決定的な較正
  - 確率的な較正（核）
  - 事象ごとに時空上の位置を定めない場合
- 3 節では、量子参照系の取り替えが A-0015 の群の枠に収まらないことも書きました。
- 段階 3 を支える因果的非分離性の原典は、まだ確かめていません。その旨を明記しています。

**未解決の点への記録**（見立てとして）
- D-0013：較正の三つの段階
- A-0013：核が時計の状態に依存し、較正の普遍性と緊張すること
- A-0016：順序が成り立つ範囲
- A-0014・A-0015：量子参照系の取り替えとの関係

**参考文献と PDF**
- `references.bib` に 6 件を追加しました。Giacomini ほか 2019 は登録済みです。
- 非公開リポジトリに PDF 6 件を置き、`papers/README.md` の一覧に加えました。

作業が失われないよう、両方のリポジトリの作業ブランチに commit して push しました。PR はまだ作っていません。対話ログ・まとめ・ロードマップ・`NEXT.md` の更新も、まだです。

調査メモについてご意見があれば直します。このまま対話を終えてよければ、終了を告げてください。その後、ログ・まとめ・関連ファイルを更新して PR を作ります。次回は、T-0019 の項目 2（Le Cam の理論の量子版）を予定しています。

## ユーザー

このまま対話を終了してください。

## Claude

セッションを終えます。まず、まとめの書式と、関連ファイルの現状を確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && cat summaries/README.md | head -60; echo ====; cat summaries/2026-10-01_22_combs-and-composites.md | head -80
```

</details>

<details><summary>結果: Bash</summary>

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
====
# 2026-10-01 第 22 回: 逐次・適応的な実験と複合系（量子コムと一般化確率論）

- 対話ログ: [logs/2026-10-01_22_combs-and-composites.md](../logs/2026-10-01_22_combs-and-composites.md)
- 調査メモ: [surveys/2026-10-01_22_combs-and-composites.md](../surveys/2026-10-01_22_combs-and-composites.md)

## 要約

ロードマップの T-0019「量子・古典・混成の実験の扱いの先行研究の調査」を始めた。調べることが 5 項目あり、1 回では原典で確かめきれないため、ユーザーの判断で「判定基準の枠組みから」、つまり項目 4（逐次・適応的な実験の扱い）と項目 1（一般化確率論の複合系）を先に原典で確かめた。

**原典で確かめた内容**（arXiv 版の 8 件。PDF 7 件を非公開リポジトリに置いた。詳細は調査メモの 2 節）

- 量子コム（Chiribella–D'Ariano–Perinotti 2009）：量子回路のネットワークは一つの正の演算子で表せる。決定的なネットワークの演算子は正規化の連鎖を満たし、逆にそのような演算子はどれも記憶を持つ通信路で実現できる。確率的な結果に対応する演算子は、その和が決定的なコムになる。コムを確率に写す最も一般の操作はテスターで、実現には一般にもつれた補助系が要る。同じ Choi 演算子を持つネットワークは、入出力の関係だけでは区別できない。
- 量子戦略（Gutoski–Watrous 2007）と process tensor（Pollock ほか 2018）は、量子コムと同じ構造を別々に与えている。
- 条件付きの試験と因果性（Chiribella–D'Ariano–Perinotti 2010）：前の結果に応じて次の試験を選ぶこと（条件付きの試験）をすべて許すことは、理論が因果的であることと結びつく。局所的な識別可能性は局所トモグラフィーと同値である。
- 一般化確率論の複合系（Barrett 2007）：局所的な操作の可換性と、部分系の基準の測定の同時確率で全体の状態が決まること、の二つから、状態のベクトルを含むベクトル空間をテンソル積と同一視できる（複合状態はテンソル積の空間に埋め込まれるが、許される状態がその全体を張るとは限らず、許される状態の集合はこれだけでは決まらない）。もつれは積状態の凸結合で書けないことで、非局所性とは別の概念である。
- 適応的な方式と並列の方式（Chiribella ほか 2008、Harrow ほか 2010）：記憶を持つ通信路には、最適な識別に逐次の方式が要るもの（並列の方式より有利になる例）がある
…（以下 2236 文字を省略）
````

</details>

<details><summary>ツール: Bash</summary>

```text
grep -n -i "page–wootters\|参照系\|POVM\|超選択\|量子スイッチ\|共変" glossary.md | head; grep -n "^## \|^### " glossary.md | head -30; grep -n "T-0019" framework.md | head; grep -n "第 22 回\|最終更新" framework.md roadmap.md | head
```

</details>

<details><summary>結果: Bash</summary>

```text
22:| coupling region | 結合領域 | Fewster–Verch の測定の枠組みで、系とプローブを相互作用させるコンパクトな時空の領域 K。入る領域と出る領域は K だけから共変に決まる。 | [第 06 回の調査メモ](surveys/2026-09-26_06_minimal-length-covariance.md) |
26:| distal split property | 遠隔 split 性 | 十分離れた領域の組（余白が十分大きい包含）では split property が成り立つこと。同心球の模型（D'Antoni–Doplicher–Fredenhagen–Longo 1987）では、半径の差が分離の距離 d(r) を超えれば成り立つ、という具体的な閾値がある。toric code の錐では、錐の境界が十分離れていることが条件になる。狭い余白で split が成り立たないこと（正の最小の距離があること）は、別の主張として区別する。場の数が質量について指数関数的に増える模型（D'Antoni–Doplicher–Fredenhagen–Longo 1987）や、toric code の錐（Naaijkens）で成り立つ。[C-0007](conjectures/C-0007.md)（旧 C-0001 の主張 2）の「最小の余白」の具体的な模型の候補。局所共変な理論で、状態空間が局所準同値性を満たし、時間スライス性を仮定すると、球と微分同相な集合について、分離の距離は 0 か ∞ に限られる（Fewster の紹介による）。 | [第 08 回の調査メモ](surveys/2026-09-28_08_observation-as-limit.md) |
46:| informationally complete measurement | 情報的に完全な測定 | 結果の確率から密度作用素がただ一つ決まる POVM。$`d`$ 次元では少なくとも $`d^2`$ 個の要素が要る。QBism の主体の間の一致の主張では、識別可能性を与える条件として使われる。 | [第 15 回の調査メモ](surveys/2026-09-29_15_qbism-agreement.md) |
59:| macroscopic observable | 巨視的な観測量 | 多数の同じ系の、対称化して平均した観測量の、系の数を無限にした極限。互いに可換になり、古典的な量として振る舞い、極限の系の超選択セクターを区別する（Landsman の紹介する Hepp などの結果）。無限遠の観測量（observables at infinity）とも関係する。 | [第 08 回の調査メモ](surveys/2026-09-28_08_observation-as-limit.md) |
66:| observer | 観測者 | 本プロジェクトでは、実験の期間にあたる世界線の区間で、基準の時計と物差しを伴うもの。実験と 1 対 1 に対応する（[D-0001](definitions/D-0001.md)）。既存研究では、時計と物差しを備えた時空の基準系の意味（相対論、量子参照系）、関係的な記述の基準となる任意の物理系の意味（関係的量子力学。時空の基準系とは同じでない）、結果を知覚する者の意味（Wigner の友人）があり、本プロジェクトは一つ目に当たる。後者の「実験を行う者」は主体とよぶ。 | [第 20 回の調査メモ](surveys/
…（以下 1731 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 1,12p glossary.md; grep -n "^| [pqtc]" glossary.md | cut -c1-60 | head -40; grep -n "第 2[12] 回\|較正" framework.md | cut -c1-200 | head -20
```

</details>

<details><summary>結果: Bash</summary>

```text
# 用語一覧

英語の原語を併記しています。項目は英語の原語のアルファベット順です。

| 英語 | 日本語 | 説明 | 初出 |
| --- | --- | --- | --- |
| actual observable | 実際の観測量 | 実際に行われた実験（高々可算個）の族の極限として定める観測量（第 09 回の作業上の定義の案）。実際の観測量から「観測量の時空」を再構成する。可能な観測量と区別する。本プロジェクトの定義は [D-0005](definitions/D-0005.md)。 | [第 09 回のまとめ](summaries/2026-09-29_09_actual-and-possible-observables.md) |
| adaptive setting | 適応的な設定 | 実験の $`i`$ 回目の観測の設定を、それまでの結果 $`y_1, …, y_{i-1}`$ に応じて選ぶこと。選び方の規則もプロトコルの記述に含める（[D-0001](definitions/D-0001.md)）。実際の実験で結果に依存して選ぶ場合、観測の事象の族（[D-0013](definitions/D-0013.md) の 3）の中で依存先の観測の登録の事象と次の観測の準備の事象がともに定まるなら、観測者の座標時刻で、登録は準備より後にない（[A-0016](assumptions/A-0016.md)。因果的な順序ではない）。 | [第 20 回](summaries/2026-09-30_20_terms-setting-and-agents.md) |
| agent | 主体 | 事前分布を持ち、実験の記録から信念を更新する者。実験を行う（設定を選び、結果の記録を得る）こともある（0 個でもよい）。QBism の agent（行為する者）に合わせた語。一つの主体は複数の実験を行えるので、実験と 1 対 1 に対応する観測者・装置とは別の概念。実際の主体（高々可算。A-0001）と可能な主体（非可算も許す）に分ける。本プロジェクトの定義は [D-0012](definitions/D-0012.md)。 | [第 20 回の調査メモ](surveys/2026-09-30_20_agent-observer-apparatus.md) |
| alternative assumptions | 択一の組（前提の） | 同時には議論の土台に置かない代替の前提の組。組の各前提が一つの体系を定め、組の前提の「採用」は、その前提を置く体系の土台にすることを意味する（[前提の一覧](assumptions/README.md) の「択一の組と体系」。例：[A-0014](assumptions/A-0014.md) の体系 E と [A-0015](assumptions/A-0015.md) の体系 P）。 | [第 21 回](summaries/2026-10-01_21_adaptive-settings-and-systems.md) |
| apparatus | 装置 | 実験で、準備から結果の読み出しまでに使う物理系。本プロジェクトでは実験と 1 対 1 に対応し、同じ機器を別の実験で使っても別の装置として数える（[D-0001](definitions/D-0001.md)）。既存研究では、Hardy の準備・変換・測定の装置、Ludwig の準備装置と登録装置、Fewster–Verch のプローブなどに当たる。
…（以下 1974 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 245,262p framework.md; git log --oneline -8 -- framework.md roadmap.md glossary.md | cat
```

</details>

<details><summary>結果: Bash</summary>

```text
各ファイルの「未解決の点」のうち、フレームワーク全体に関わるものです。

- 極限の位相と、事後分布を置く空間（[D-0005](definitions/D-0005.md)）。
- 観測者の実験における時空と、観測における時空との整合条件（[D-0013](definitions/D-0013.md)）。異なる実験の観測者の取り替えの与え方（[A-0014](assumptions/A-0014.md) と [A-0015](assumptions/A-0015.md) で体系を分ける）。
- 観測における時空を再構成するときの入力と一意性（[D-0007](definitions/D-0007.md)）。
- 層 4・6 の定義と前提。
- 量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えること（第 19 回のユーザーの方針。量子重力理論への寄与という目的による）。今の定義では、結果は実数値の記録で（[A-0003](assumptions/A-0003.md)）、量子の測定は応答関数の形として入る（[D-0004](definitions/D-0004.md)）。「量子的な観測」を量子系を測った古典的な記録と読むか、時計を含む量子系を、古典的な記録へ読み出す前の量子的な出力として実験の対象に含めると読むかは、ロードマップの T-0019 の調査の後に決める。
- 第 20 回の再編（ロードマップの T-0018。完了）の後に残った論点：観測者の取り替えの与え方の比較（[A-0014](assumptions/A-0014.md) と [A-0015](assumptions/A-0015.md)）、主体と観測者の関係（[D-0012](definitions/D-0012.md)）、較正の写像の入力と確率的な較正（[D-0013](definitions/D-0013.md)）。

これらを含む作業の順序は、[ロードマップ](roadmap.md) で管理します。
0608cbf 第 22 回の 14 回目のクロスモデルレビューに対応：Barrett の定理 1 を原典の文言（状態のベクトルを含む空間の同一視）に合わせ、埋め込みと線形包を区別した
6246a2e 第 22 回の 13 回目のクロスモデルレビューに対応：用語一覧の量子コムの実現定理に正値性を加え、合成性の不足の条件に部分の間の同時分布・共有相関の不足を加えた
9aaf67c 第 22 回の 11 回目のクロスモデルレビューに対応：合成性が失われる条件を「準備・介入・読み出しの組がトモグラフィーに足りない場合」に統一し、因子化を求める対象をつなぐ前の過程と明記した
f0c24eb 第 22 回の 10 回目のクロスモデルレビューに対応：もつれを複合状態の性質として定義し直し、用語一覧の局所トモグラフィーで Barrett の仮定 4・5 と合成の前提を明記した
55e1006 第 22 回の 8 回目のクロスモデルレビューへの対応の残り：ロードマップの (a)・(b) の区別、まとめと調査メモの数値の照合の範囲、D-0013 の詳細化の論点
b2a86e0 第 22 回のクロスモデルレビューに対応：合成性の喪失と古典的なコムの限界を読み出しの情報的な完全性の条件付きで書き直し、もつれの判定に要る設定とテスターの正規化、局所トモグラフィーのテンソル積の意味を正した
bdbb3da 第 22 回：T-0019 の項目 4・1 の調査（量子コム・量子戦略・proces
…（以下 156 文字を省略）
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
import re
SV="surveys/2026-10-02_23_quantum-clocks-and-frames.md"
SM="summaries/2026-10-02_23_quantum-clocks-and-frames.md"
# glossary
p='glossary.md'; L=open(p).read().split('\n')
new={
"covariant time observable":f"| covariant time observable | 共変な時間観測量 | 時計のハミルトニアンが生成する時間並進について共変な POVM として表した、時計の時刻の観測量。ハミルトニアンが有界な時計でも定義でき、読みは単調だが、異なる時刻の時計の状態が直交しないので、読みは完全には区別できない（Höhn–Smith–Lock 2021）。量子時計による較正が確率的になる理由の一つ（[D-0013](definitions/D-0013.md) の未解決の点）。 | [第 23 回の調査メモ]({SV}) |",
"Page–Wootters formalism":f"| Page–Wootters formalism | Page–Wootters の定式化 | 時計と系の全体の状態に拘束（ホイーラー–ドウィット方程式の類似）を課し、時計の読みで条件付けて系の時間発展を得る定式化。多時刻の統計は、測定ごとの結果を記憶系に記録させ、時計の一つの時刻でまとめて読むことで得られる（Giovannetti–Lloyd–Maccone 2015）。関係的な観測量の記述と同値であることが示されている（Höhn–Smith–Lock 2021。時計と系が相互作用しない場合）。 | [第 23 回の調査メモ]({SV}) |",
"quantum reference frame":f"| quantum reference frame | 量子参照系 | 量子系として扱う参照系。参照系の取り替えは、座標変換の重ね合わせとしてのユニタリで表され、もつれや重ね合わせは参照系に依存する。測定の結果の確率は参照系によらない（Giacomini–Castro-Ruiz–Brukner 2019）。参照系が大きく、よく局在していれば、古典的な（外部の）参照系による記述がよい近似になる（Loveridge–Miyadera–Busch 2018、Bartlett–Rudolph–Spekkens 2007）。 | [第 23 回の調査メモ]({SV}) |",
}
hdr=[i for i,l in enumerate(L) if l.startswith('| --- |')][0]
end=hdr+1
while end<len(L) and L[end].startswith('| '): end+=1
rows=L[hdr+1:end]
for k,v in new.items(): rows.append(v)
key=lambda r: r.split('|')[1].strip().lower().replace('–','-')
rows.sort(key=key)
L[hdr+1:end]=rows
open(p,'w').write('\n'.join(L))
# framework
p='framework.md'; s=open(p).read()
s=s.replace("最終更新
…（以下 1312 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
roadmap.md:3:最終更新: 2026-10-02（第 23 回。T-0019 の項目 3 を行った）
framework.md:3:最終更新: 2026-10-02（第 23 回。T-0019 の項目 3 の見立て（量子時計・量子参照系と較正の段階）を未解決の論点に加えた）
 framework.md | 4 ++--
 glossary.md  | 7 +++++--
 roadmap.md   | 5 +++--
 3 files changed, 10 insertions(+), 6 deletions(-)
```

</details>

<details><summary>ツール: Bash</summary>

```text
git diff glossary.md | grep '^[-+]' | cut -c1-80
```

</details>

<details><summary>結果: Bash</summary>

```text
--- a/glossary.md
+++ b/glossary.md
+| covariant time observable | 共変な時間観測量 | 時計のハミルト�
+| Page–Wootters formalism | Page–Wootters の定式化 | 時計と系の全
+| quantum reference frame | 量子参照系 | 量子系として扱う参照系
-| tester | テスター | 量子コム（ネットワーク）を確率に写�
-| T₀-ordered space | T₀ 順序空間 | 前順序付き空間で、x ≰ y �
+| tester | テスター | 量子コム（ネットワーク）を確率に写�
+| T₀-ordered space | T₀ 順序空間 | 前順序付き空間で、x ≰ y �
```

</details>

## Claude

用語一覧の並べ替えで、既存の 2 行の順序が入れ替わってしまったので、元に戻します。その後、まとめと `NEXT.md` を書きます。

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='glossary.md'; L=open(p).read().split('\n')
i=[k for k,l in enumerate(L) if l.startswith('| T₀-ordered space')][0]
j=[k for k,l in enumerate(L) if l.startswith('| tester |')][0]
L[i],L[j]=L[j],L[i]
open(p,'w').write('\n'.join(L))
EOF
git diff glossary.md | grep '^[-+]' | cut -c1-60
```

</details>

<details><summary>結果: Bash</summary>

```text
--- a/glossary.md
+++ b/glossary.md
+| covariant time observable | 共変な時間観測量 | �
+| Page–Wootters formalism | Page–Wootters の定式化 
+| quantum reference frame | 量子参照系 | 量子系と�
-| tester | テスター | 量子コム（ネットワーク
-| T₀-ordered space | T₀ 順序空間 | 前順序付き�
+| T₀-ordered space | T₀ 順序空間 | 前順序付き�
+| tester | テスター | 量子コム（ネットワーク
```

</details>

<details><summary>ツール: Bash</summary>

```text
L=$(git diff glossary.md | grep '^+| \(covariant\|Page\|quantum reference\)' | sed 's/^+//'); git checkout glossary.md; printf '%s\n' "$L" > /tmp/claude-0/-home-user/[ID]/scratchpad/rows.txt; python3 - <<'EOF'
rows=open('/tmp/claude-0/-home-user/[ID]/scratchpad/rows.txt').read().strip().split('\n')
p='glossary.md'; L=open(p).read().split('\n')
anchors={'covariant':'| coupling region','Page':'| parallel ordered locale','quantum reference':'| quantum de Finetti'}
for r in rows:
    for k,a in anchors.items():
        if r.startswith('| '+k):
            i=[n for n,l in enumerate(L) if l.startswith(a)][0]
            L.insert(i+1 if k!='Page' else i,r)
open(p,'w').write('\n'.join(L))
EOF
git diff glossary.md | grep '^[-+]' | cut -c1-50; grep -n "^| \(coupling\|covariant\|D\|Page\|parallel\|quantum de\|quantum ref\|quantum st\)" glossary.md | cut -c1-40
```

</details>

<details><summary>結果: Bash</summary>

```text
Updated 1 path from the index
--- a/glossary.md
+++ b/glossary.md
+| covariant time observable | 共変な時間観�
+| Page–Wootters formalism | Page–Wootters の
+| quantum reference frame | 量子参照系 | 量
22:| coupling region | 結合領域 | Fe
23:| covariant time observable | 共変�
75:| Page–Wootters formalism | Page–
76:| parallel ordered locale | 平行な
90:| quantum de Finetti theorem | 量子
91:| quantum reference frame | 量子参
92:| quantum strategy | 量子戦略 | �
```

</details>

## Claude

Now the summary and NEXT.md.

<details><summary>ツール: Write: /home/user/point-free-spacetime/summaries/2026-10-02_23_quantum-clocks-and-frames.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/summaries/2026-10-02_23_quantum-clocks-and-frames.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/summaries/2026-10-02_23_quantum-clocks-and-frames.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='NEXT.md'; s=open(p).read()
s=s.replace("最終更新: 2026-10-01（第 22 回セッションの後）","最終更新: 2026-10-02（第 23 回セッションの後）")
anchor="Harrow ほか 2010 の例 1 の数値の照合を、ユーザーの判断で結果 [R-0009](results/R-0009.md) として登録した。"
assert anchor in s
s=s.replace(anchor, anchor+"\n- 第 23 回：T-0019 の続き。ユーザーの判断で、項目 3（量子参照系・量子時計）を先に、arXiv 版の原典 7 件（Page–Wootters の定式化、関係的な量子力学、量子時計の時間の遅れ、量子参照系の取り替え、事象の時間的な局在、相対量、参照系と超選択則）で確かめた。見立てとして、既存の扱いはどれも (a) で書き直せ、論点は (a) の中で較正を決定的・確率的・事象ごとに位置を定めない、のどの段階まで許すかにある、とした（ユーザーの判断で、見立てとして記録するにとどめた。[まとめ](summaries/2026-10-02_23_quantum-clocks-and-frames.md)、[調査メモ](surveys/2026-10-02_23_quantum-clocks-and-frames.md)）。")
start=s.index("## 次のタスク"); end=s.index("## ユーザーにお願いしていること")
s=s[:start]+"""## 次のタスク

次のセッション（第 24 回の予定）では、[`roadmap.md`](roadmap.md) の **T-0019「量子・古典・混成の実験の扱いの先行研究の調査」の続き**を行う。T-0019 の後は段階 B（T-0004〜T-0007）である（[`CLAUDE.md`](CLAUDE.md) の「セッションの進め方」）。その後の順序、長期のタスク、未解決の論点は `roadmap.md` にある。

- 手がかりは、`roadmap.md` の「T-0019」の節と、[第 23 回の調査メモ](surveys/2026-10-02_23_quantum-clocks-and-frames.md)の 3〜5 節、[第 22 回の調査メモ](surveys/2026-10-01_22_combs-and-composites.md)の 4.4 節にある。
- 残りは、項目 2（Le Cam の理論の量子版。Buscemi、Jenčová、松本、Guţă–Kahn。文献は記憶による。未確認。主な文献は arXiv にあるはず）である。比べる対象を量子状態の族とするか、チャネル・測定器とするかを区別して調べる。
- 必要に応じて、第 23 回の見立ての段階 3 を支える因果的非分離性の文献（Oreshkov–Costa–Brukner 2012 など。未確認）を確かめる。
- 調査の後、ユーザーが判断すること：「量子的な観測」を (a) 量子系を測った古典的な記録（今の立場）と読むか、(b) 古典的な記録へ読み出す前の量子的な出力も実験の対象に含めると読むか。あわせて、第 23 回の見立てに沿って、(a) の中で較正（[D-0013](definitions/D-0013.md)）をどの段階（決定的・確率的・事象ごとに位置を定めない）まで許
…（以下 252 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
M NEXT.md
 M framework.md
 M glossary.md
 M roadmap.md
?? summaries/2026-10-02_23_quantum-clocks-and-frames.md
35 passed in 0.17s
```

</details>

## Claude

最後に対話ログを書き出します。

<details><summary>ツール: Bash</summary>

```text
python3 tools/export_log.py ~/.claude/projects/-home-user/[ID].jsonl logs/2026-10-02_23_quantum-clocks-and-frames.md --title "2026-10-02 第 23 回: 量子時計と量子参照系（較正の段階）" --since 2026-10-01T23:52:00Z --redact-file ../point-free-spacetime-private/redactions.txt 2>&1 | tail -3; wc -l logs/2026-10-02_23_quantum-clocks-and-frames.md; grep -v -e '^#' -e '^$' ../point-free-spacetime-private/redactions.txt | grep -iFcf - logs/2026-10-02_23_quantum-clocks-and-frames.md; grep -c -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}" logs/2026-10-02_23_quantum-clocks-and-frames.md; grep -o -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}" logs/2026-10-02_23_quantum-clocks-and-frames.md | sort | uniq -c | head
```

</details>
