# 2026-09-29 第 14 回: フレームワークの圏論的な概観

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> 個人情報などは伏せ字にしています。ツールの呼び出しは要約の 1 行だけを残し、その中身と結果は、他者の文章の長い引用を避けるため、第 32 回に公開側から除きました（T-0027）。

## ユーザー

次のセッションを開始してください。

（ツール: Bash: Read NEXT.md and git state）

（ツール: Bash: Check whether branch is merged into main）

## Claude

PR #28 はマージ済みなので、作業ブランチを最新の `main` から作り直します。

（ツール: Bash: Reset branch to main and read T-0002 section）

（ツール: Bash: Locate T-0002 in roadmap）

（ツール: Bash: Read T-0002 details and framework）

（ツール: Bash: Read definitions D-0001 to D-0008）

## Claude

第 14 回のセッションを始めます。

#### 確認した状況

- PR #28（第 13 回）はマージ済みでした。作業ブランチ `claude/zealous-keller-o7r1sv` を最新の `main` から作り直しました。
- 今回のタスクは、[`roadmap.md`](roadmap.md) の **T-0002「フレームワークの圏論的な概観」** です。成果物は調査メモと、`framework.md` への概観の節の追加です。

#### 最初のたたき台：各層を圏論の言葉で見る（見立て）

定義 D-0001〜D-0011 を読み直しました。そのうえで、それぞれに当てはまりそうな既存の圏論の枠組みを挙げます。文献との対応はまだ原典で確かめておらず、すべて見立てです。

**(a) 層 1〜2：実験と応答関数 → マルコフ圏（Markov category）**
- 応答関数 $`p_π : X_π → \mathrm{Prob}(Y_π)`$ は、確率的な写像（マルコフ核）です。つまり、ジリー・モナド（Giry monad）のクライスリ圏（Kleisli category）、または Fritz のマルコフ圏 $`\mathsf{Stoch}`$ での射 $`X_π → Y_π`$ そのものになります。
- 対象をプロトコル、射を「あるプロトコルを別のプロトコルで模倣すること」（設定の変換と、結果の後処理）とすると、実験の圏が得られます。後処理による比較は、統計的実験のブラックウェル順序（Blackwell order）に当たります。
- 第 11 回のレビューの論点（状態や装置のモデルを固定するか）は、次のように言い換えられます。**状態を固定すると、応答関数の割り当ては実験の圏から $`\mathsf{Stoch}`$ への一つの関手になる。状態も動かすと、そのような関手（モデル）全体の圏を考えることになる**（ローヴェア流の関手的意味論 / functorial semantics）。
- ベイズの逆（Bayesian inversion）、ド・フィネッティの定理、コルモゴロフ積（無限のデータ列）も、マルコフ圏の中で定式化されています（Cho–Jacobs、Fritz–Gonda–Perrone、Fritz–Rischel）。このため、D-0005 の「事後分布の極限」と A-0007 を同じ言葉で書ける可能性があります。

**(b) 局在 D-0008：領域の上の関手 → 代数的場の量子論（AQFT）のネット**
- $`R ↦ 𝒪(R)`$ が単調であることは、$`M_O`$ の開集合の順序集合から集合（あるいは代数）の圏への関手であることに当たります。これは Haag–Kastler のネットの等方性（isotony）と同じ形です。
- 観測者の取り替えまで含めると、Brunetti–Fredenhagen–Verch の局所共変な場の理論（時空の圏から代数の圏への関手）の形に近づきます。C-0008（ポアンカレ共変性との緊張）は、「この関手が観測者の亜群（groupoid）の作用と両立するか」という問いとして書けます。

**(c) 層 3：観測量から空間への再構成 → 双対性と随伴**
- 可換の場合の基準は、ゲルファント双対性（可換 C* 代数と、コンパクト・ハウスドルフ空間の反対圏）と、フレームとロケールの双対性 $`\mathsf{Loc} = \mathsf{Frm}^{\mathrm{op}}$` です。
- 非可換の場合の点なしの再構成としては、**Bohr トポス**（Heunen–Landsman–Spitters）が有力な候補です。可換な部分代数（文脈）の順序集合の上の前層トポスの中で、内部のゲルファント・スペクトルをロケールとして得るもので、D-0007 の「入力に可換性の関係が要る」という未解決の点に直接対応します。

**(d) 整合条件 → 双対的な随伴の不動点**
- 位相空間とフレームの間の随伴 $`𝒪 ⊣ \mathrm{pt}`$ は、不動点（sober な空間と spatial なフレーム）の上で同値になります。一般の双対性も、多くは「双対的な随伴を不動点に制限したもの」として得られます（Porst–Tholen の concrete duality）。
- D-0003 の整合条件（再構成したモデルが較正の写像を再現する）と、D-0006 の不動点の条件は、「実験の側と空間の側の間の随伴を作り、その単位と余単位が同型になる対象」として定式化できる見込みがあります。

**(e) 層 1・6：膨張 → ガロア接続**
- 膨張 $`N`$（D-0009）は上限を保つので、右随伴である収縮（erosion）を持ちます。R-0008（オープニングの不動点は膨張の像）は、この随伴から一般に従う事実の特別な場合です。D-0011 の $`N_{\mathrm{occ}}`$ も同じ形で扱えます。

#### 相談したいこと

1. **どの観点を主軸にするか。** 私のお勧めは、(a) マルコフ圏と (d) 随伴の不動点を骨組みにして、(b)(c) をその上に載せる形です。(a) で層 1〜2 を、(d) で層 3〜5 の循環（C-0002 と D-0006）と整合条件を、一つの言葉で書けるためです。
2. **深さ。** 今回は、各層の「対象・射・関手」の対応表と、文献の確認（上に挙げた論文を arXiv で原典に当たる）までにして、新しい定義や予想の登録は候補として挙げるだけにするか。それとも、例えば「実験の圏」を作業上の定義として登録するところまで進めるか。
3. **状態の扱い（第 11 回のレビューの論点）。** 状態を固定して関手を一つ取るか、モデル全体の圏を取るか。フレームワークの「観測量の推定」は後者（どのモデルかを推定する）に近いと思いますが、ご意見を伺いたいです。

どの方向で進めるか、ご指示をください。

（ツール: Bash: Push branch synced to main）

## Claude

作業ブランチ `claude/zealous-keller-o7r1sv` を push しました。未 push だったコミットは、最新の `main` にある PR #28 のマージコミットだけです。今回の作業の変更はまだありません。

先ほどの 3 点についてのご判断をお待ちしています。

1. 主軸にする観点。私のお勧めは、マルコフ圏と、随伴の不動点としての整合条件を骨組みにする形です。
2. 今回どこまで進めるか。対応表と文献の確認までにするか、「実験の圏」などを作業上の定義として登録するところまで進めるか。
3. 状態の扱い。状態を固定して関手を一つ取るか、モデル全体の圏を取るか。

## ユーザー

1. はお勧めに賛同します。2. は対応表と文献の確認までにしたいです。3. はモデル全体の圏を取りたいです。

## Claude

「1.」「2.」「3.」の質問は、この会話の記録にはありません。別の会話（第 14 回）で出したものかもしれないので、セッション記録とリポジトリを確認します。

（ツール: Bash: Look for the session 14 questions in transcripts）

## Claude

第 14 回の冒頭の提案が記録に残っていました。回答をいただいた 3 点の前提になっている提案の本文を確認します。

（ツール: Bash: Read session 14 dialogue so far）

（ツール: Bash: List existing bib keys and surveys）

（ツール: ToolSearch: select:WebFetch,WebSearch）

## Claude

文献の原典を arXiv で確認します。

（ツール: WebFetch: https://arxiv.org/abs/1908.07021）

（ツール: WebFetch: https://arxiv.org/abs/1709.00322）

（ツール: WebFetch: https://arxiv.org/abs/2010.07416）

（ツール: WebFetch: https://arxiv.org/abs/1912.02769）

（ツール: WebFetch: https://arxiv.org/abs/2105.02639）

（ツール: WebFetch: https://arxiv.org/abs/math-ph/0112041）

（ツール: WebFetch: https://arxiv.org/abs/0709.4364）

（ツール: WebSearch: Porst Tholen "Concrete dualities" Category Theory at Work 1991 dual adjunction fixed points）

（ツール: WebSearch: Giry 1982 "A categorical approach to probability theory" Lecture Notes in Mathematics 915 DOI）

（ツール: Bash: Check bib entries and survey format）

（ツール: WebFetch: https://arxiv.org/abs/2204.02284）

（ツール: WebSearch: Lawvere "Functorial semantics of algebraic theories" Reprints in Theory and Applications of Categories No. 5 2004）

## Claude

文献の原典（arXiv の要旨ページと書誌）を確かめられました。これをもとに、調査メモ（対応表を含む）を書きます。

（ツール: Write: /home/user/point-free-spacetime/surveys/2026-09-29_14_categorical-overview.md）

## Claude

次に、参考文献一覧に今回の文献を登録し、`framework.md` に概観の節を加えます。

（ツール: Bash: View bib tail and framework sections）

（ツール: Bash: Add bib entries and framework overview section）

（ツール: Bash: Add glossary entries, commit, push WIP）

## Claude

ご判断に沿って T-0002 を進めました。成果は作業中のコミット 8181390 として push してあります。

#### 成果物

- **調査メモ**：[`surveys/2026-09-29_14_categorical-overview.md`](surveys/2026-09-29_14_categorical-overview.md)
  - 各層の「対象・射・関手」の対応表（2 節）
  - 状態の扱い：モデル全体の圏（3 節）
  - 随伴の不動点としての整合条件（4 節）
  - 定義・予想の候補（5 節。登録はしていません）
- **`framework.md`**：「4.1 圏論的な概観」の節を加えました。
- **参考文献一覧**：9 件を追加しました（Giry、Lawvere、Fritz、Cho–Jacobs、Fritz–Rischel、Fritz–Gonda–Perrone、Fritz–Gonda–Perrone–Rischel、Brunetti–Fredenhagen–Verch、Porst–Tholen）。Heunen–Landsman–Spitters は登録済みでした。
- **用語一覧**：マルコフ圏、ジリー・モナド、ベイズの逆、関手的意味論、双対的な随伴を加えました。

#### 文献の確認

各論文の要旨ページと書誌で、次の点を確かめました。本文は読んでいないので、定理番号や定義の正確な形は未確認です。

- マルコフ圏の文献群は、本プロジェクトが要する道具をそろえています。
  - 条件付けと十分統計量（Fritz 2020）
  - ベイズの逆（Cho–Jacobs）
  - 無限積と 0-1 法則（Fritz–Rischel）
  - ド・フィネッティの定理（Fritz–Gonda–Perrone）
  - 統計的実験の比較、つまりブラックウェル–シャーマン–スタインの定理（Fritz–Gonda–Perrone–Rischel）
- 局所共変な場の量子論は、「時空の圏から代数の圏への関手」として定義されています（Brunetti–Fredenhagen–Verch）。
- Bohr トポスは、可換な部分代数を貼り合わせたトポスの中で、スペクトルをロケールとして得るものです（Heunen–Landsman–Spitters）。

#### 状態の扱い：モデル全体の圏（見立て）

- 一つのモデルは、実験の圏から $`\mathsf{Stoch}`$ への関手です。モデル全体は、自然変換を射とする関手の圏になります。
- D-0005 の推定は「どのモデルか」の推定にあたり、事前・事後分布はモデルのパラメータ付け $`Θ`$（応答関数の空間）の上に置きます。
- 状態を固定する見方は、この圏の一つの対象を選ぶ特別な場合として含まれます。

#### 候補として記録したもの（登録していません）

- **定義の候補**：「実験の圏」と「モデルの圏」
- **予想の候補**
  - 再構成と記述し直しが随伴をなし、整合条件を満たす組がその不動点と一致する。
  - 実際の観測量の極限を圏論的に定式化すると、ブラックウェル–デュビンスの定理の圏論版が得られる。

内容をご確認ください。直したい点がなければ、ロードマップ（T-0002 を完了、次は T-0003 の QBism の調査）と `NEXT.md` を更新し、セッションの終え方の手順に進みます。

Sources:
- [Fritz 2020 (arXiv:1908.07021)](https://arxiv.org/abs/1908.07021)
- [Cho–Jacobs (arXiv:1709.00322)](https://arxiv.org/abs/1709.00322)
- [Fritz–Gonda–Perrone–Rischel (arXiv:2010.07416)](https://arxiv.org/abs/2010.07416)
- [Fritz–Rischel (arXiv:1912.02769)](https://arxiv.org/abs/1912.02769)
- [Fritz–Gonda–Perrone (arXiv:2105.02639)](https://arxiv.org/abs/2105.02639)
- [Brunetti–Fredenhagen–Verch (arXiv:math-ph/0112041)](https://arxiv.org/abs/math-ph/0112041)
- [Heunen–Landsman–Spitters (arXiv:0709.4364)](https://arxiv.org/abs/0709.4364)
- [Giry 1982 (Springer)](https://link.springer.com/chapter/10.1007/BFb0092872)
- [Lawvere, Functorial Semantics (TAC Reprints No. 5)](http://www.tac.mta.ca/tac/reprints/articles/5/tr5abs.html)
- [Porst–Tholen, Concrete dualities（nLab の duality の項）](https://ncatlab.org/nlab/show/duality)

## ユーザー

確認しました。対話を終えて、セッションの終え方の手順に進んでください。

## Claude

セッションの終え方の手順に進みます。まず、ロードマップと `NEXT.md` の現状を確認します。

（ツール: Bash: Check roadmap and NEXT state）

（ツール: Bash: Update roadmap and NEXT.md）

## Claude

Next, the summary.

（ツール: Bash: Write summary and run tests）

（ツール: Bash: Export session 14 log and check redactions）
