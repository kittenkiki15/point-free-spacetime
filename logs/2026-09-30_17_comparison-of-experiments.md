# 2026-09-30 第 17 回: 実験の比較と Le Cam の不足度

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> 個人情報などは伏せ字にしています。ツールの呼び出しは要約の 1 行だけを残し、その中身と結果は、他者の文章の長い引用を避けるため、第 32 回に公開側から除きました（T-0027）。

## ユーザー

次のセッションを開始してください。

（ツール: Bash: Check repo state and read NEXT.md）

（ツール: Bash: Compare branches with main in both repos）

## Claude

Both branches are already contained in main. I'll bring the working branches up to date with the latest main.

（ツール: Bash: Reset branches to main and read the T-0016 section）

（ツール: Bash: Read relevant survey sections for leads）

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

（ツール: Bash: Check ahead/behind status in both repos）

（ツール: Bash: Push updated branches in both repos）

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

（ツール: Bash: Extract text from the five comparison-of-experiments PDFs）

（ツール: Bash: Read Blackwell 1951 text）

（ツール: Read: /root/.claude/projects/-home-user/[ID]/tool-results/blhtfa1w1.txt）

## Claude

Blackwell 1951 は本文を読みました。次に、スキャン版の Blackwell 1953 を読みます。

（ツール: Read: /home/user/point-free-spacetime-private/papers/blackwell1953.pdf）

## Claude

Blackwell 1953 も読みました。次は Le Cam 1964（37 ページ）です。

（ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf）

（ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf）

（ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf）

（ツール: Read: /home/user/point-free-spacetime-private/papers/lecam1964.pdf）

## Claude

Le Cam 1964 を読み終えました。続けて、Shannon 1958 と Raginsky 2011 を読みます。

（ツール: Bash: Read Shannon 1958 text）

（ツール: Bash: Read Raginsky 2011 text）

（ツール: Read: /root/.claude/projects/-home-user/[ID]/tool-results/b8w9b84gi.txt）

## Claude

5 件をすべて読みました。報告の前に、プロジェクト側の対応箇所（D-0005 と、第 14 回の「模倣」）を確かめます。

（ツール: Bash: Read D-0005 and find mimicry references）

（ツール: Bash: Skim related definitions, assumptions, conjectures）

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

（ツール: Bash: Read summary format and previous summary/survey）

（ツール: Bash: Check survey index, bib entries, glossary terms）

（ツール: Bash: Inspect glossary headers and symbols table）

（ツール: Bash: List symbol sections）

（ツール: Bash: Read category and measurement symbol sections）

（ツール: Bash: Find mimicry definition in session 14 files）

## Claude

手順を確かめ、報告した見立てのうち「極限」の部分を証明の形で検算しました。これから調査メモを書きます。

（ツール: Write: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md）

（ツール: Edit: /home/user/point-free-spacetime/surveys/2026-09-30_17_comparison-of-experiments.md）

（ツール: Bash: Inspect roadmap structure）

（ツール: Bash: Move the unrequested Δ-convergence check to an outlook note）

（ツール: Bash: Find where mimicry issue lives in roadmap/framework）

## Claude

Roadmap と D-0005 を更新します。

（ツール: Bash: Update roadmap T-0016/T-0006 and D-0005 unresolved points）

（ツール: Bash: Add glossary and symbol entries）

（ツール: Bash: Check math guide rules on tables and norms）

（ツール: Bash: Read norm/absolute value rules）

## Claude

ノルムの書き方を、表の列区切りとぶつからない `\left\Vert … \right\Vert` にそろえます。

（ツール: Bash: Replace norm bars with Vert delimiters）

（ツール: Bash: Check remaining escaped bars and converted norms）

（ツール: Bash: Check framework.md update conventions）

（ツール: Bash: Read framework section around observables layer）

（ツール: Bash: Add section 4.3 to framework.md and regenerate graph）

## Claude

次に、対話ログを書き出します。

（ツール: Bash: Locate the session transcript file）

（ツール: Bash: Find session start timestamps and export tool options）

（ツール: Write: /home/user/point-free-spacetime/summaries/2026-09-30_17_comparison-of-experiments.md）

## Claude

Now NEXT.md.

（ツール: Bash: Update NEXT.md status and next task）

（ツール: Bash: Note user's review request and run tools tests）

## Claude

Tests pass. Exporting the log now (right before commit).

（ツール: Bash: Export dialogue log and check redactions）
