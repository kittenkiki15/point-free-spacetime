# 2026-10-02 第 24 回: 量子統計的実験・チャネルの比較と因果的非分離性

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> ツールの呼び出しは折りたたんで表示し、個人情報などは伏せ字にしています。

## ユーザー

次のセッションを開始してください。

<details><summary>ツール: Bash: NEXT.md とリポジトリの状態を確認</summary>

```text
cd /home/user/point-free-spacetime && cat NEXT.md && git status && git log --oneline -5 && git branch -a
```

</details>

<details><summary>結果: Bash: NEXT.md とリポジトリの状態を確認</summary>

```text
# 次のセッションでやること

最終更新: 2026-10-02（第 23 回セッションの後）

## 状況

- 第 01 回：リポジトリの運用ルールを決め、自動検証（Lean・Python・クロスモデルレビュー）を整えた。
- 第 02 回：点なし位相と論理・様相論理・因果・量子論のつながりを整理し、調査メモ・用語一覧・記号一覧・参考文献一覧を作った（[まとめ](summaries/2026-09-25_02_pointfree-logic.md)）。
- 第 03 回：Heunen–van der Schaaf の 2 本の論文メモを作り、「完備ブール代数の点はアトムと対応する」を Lean で形式化した（[まとめ](summaries/2026-09-25_03_ordered-locales.md)）。
- 第 04 回：第 03 回の結果をユーザーと確認し、論文メモを修正した。検証済みの主張を「結果」として管理する [`results/`](results/README.md) を作った（[まとめ](summaries/2026-09-25_04_review-and-results.md)）。
  - ユーザーの方針：予想の価値の主軸は、数学ではなく**物理学への寄与**（厳密な定義のない物理の概念や主張に数学的な定式化を与えることなど）に置く。
- 第 05 回：最小の長さと操作的な領域の構造について、おもちゃのモデルを多角的に検討した。最小の尺度の入れ方を型 I（小さい領域を捨てる）と型 II（余白に下限を置く）に分け、型 II を「膨張 $`N`$ による余白付きの包含が補間的でないこと」として点なしに表した。文献を調べ、数学の部分は既知と確認して結果 R-0006〜R-0008 に登録し、最初の予想 [C-0001](conjectures/C-0001.md)（優先度：高、[Issue #8](https://github.com/kittenkiki15/point-free-spacetime/issues/8)）を立てた（[まとめ](summaries/2026-09-26_05_minimal-scale.md)、[調査メモ](surveys/2026-09-26_05_subordination.md)）。
- 第 06 回：C-0001 を見直す前の先行研究の調査を行った。主張 4 と同じ型の no-go 型の結果（因果集合の非局所性、粒子の局在）、測定と局所性（Sorkin の不可能な測定、Fewster–Verch のプローブによる測定の枠組み）、最小の長さの観測者非依存性（DFR、Hossenfelder）を原典で確かめた。主張 4 は「単一の不変な関係」の no-go 定理として既知の型に属し、先行研究（Fewster–Verch の測定の構成の共変性など）から着想して、「区別」を観測者側のデータを添字にした族として扱う方針を立てた（見立て）。ユーザーの提案で、宇宙の有限性を赤外の上限として入れ、紫外と赤外の二つの尺度から実効的な尺度が現れるかを問う方向で、C-0001 を見直すことにした（[まとめ](summaries/2026-09-26_06_minimal-length-covariance.md)、[調査メモ](surveys/2026-09-26_06_minimal-length-covariance.md)）。
- 第 07 回：C-0001 の見直しに入る前に、用語「局所性」と「局在」
…（以下 11558 文字を省略）
```

</details>

<details><summary>ツール: Bash: main との関係を確認</summary>

```text
git fetch origin main claude/clever-planck-pr5kq1 2>&1 | tail -2; git log --oneline -3 origin/main; git merge-base --is-ancestor HEAD origin/main && echo merged; git diff --stat HEAD origin/main | tail -1; cd ../point-free-spacetime-private && git status -sb | head -2 && git fetch origin main 2>&1|tail -1; git log --oneline -2 origin/main; git log --oneline -2
```

</details>

<details><summary>結果: Bash: main との関係を確認</summary>

```text
fatal: couldn't find remote ref claude/clever-planck-pr5kq1
4238cba Merge pull request #44 from kittenkiki15/claude/clever-planck-pr5kq1
99d353a 第 22 回のクロスモデルレビューの詳細化の論点（適応的な設定の核の不変性と乱数の独立性）を A-0006 の未解決の点に記録した
9d21ed2 R-0009 に、記憶のない通信路を 2 回使う設定であることを明記した（第 22 回のクロスモデルレビューの詳細化の論点）
 13 files changed, 13 insertions(+), 2196 deletions(-)
## claude/clever-planck-pr5kq1...origin/claude/clever-planck-pr5kq1
   91dd8d1..7627198  main       -> origin/main
7627198 Merge pull request #14 from kittenkiki15/claude/clever-planck-pr5kq1
cdd152d 第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加した
cdd152d 第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加した
91dd8d1 Merge pull request #13 from kittenkiki15/claude/clever-planck-pr5kq1
```

</details>

<details><summary>ツール: ToolSearch: select:mcp__github__list_pull_requests</summary>

```text
（入力の本文は省略。項目: max_results, query）
```

</details>

<details><summary>結果: ToolSearch: select:mcp__github__list_pull_requests</summary>

```text
[tool_reference]
```

</details>

<details><summary>ツール: mcp__github__list_pull_requests</summary>

```text
（入力の本文は省略。項目: fields, owner, perPage, repo, state）
```

</details>

<details><summary>結果: mcp__github__list_pull_requests</summary>

```text
[{"head":{"ref":"claude/clever-planck-pr5kq1","repo":{"description":"点なし時空による物理学についての考察","full_name":"kittenkiki15/point-free-spacetime"},"sha":"ab105cdb5eccea15d98c182d5374e930be7df44a"},"merged":false,"merged_at":"2026-10-02T03:34:13Z","number":45,"state":"closed","title":"第 23 回：量子時計と量子参照系（T-0019 の項目 3、較正の段階）"},{"head":{"ref":"claude/clever-planck-pr5kq1","repo":{"description":"点なし時空による物理学についての考察","full_name":"kittenkiki15/point-free-spacetime"},"sha":"99d353adcf3f4f1ddfe9acd88943c2fd66cd3fe2"},"merged":false,"merged_at":"2026-10-01T15:18:15Z","number":44,"state":"closed","title":"第 22 回：T-0019 の項目 4・1（量子コムと一般化確率論の複合系）の調査"},{"head":{"ref":"claude/clever-planck-pr5kq1","repo":{"description":"点なし時空による物理学についての考察","full_name":"kittenkiki15/point-free-spacetime"},"sha":"99d3871882f4f05f6f88f5a3377d525389e9f87b"},"merged":false,"merged_at":"2026-10-01T11:21:13Z","number":43,"state":"closed","title":"第 21 回：適応的な設定の扱い、A-0012・A-0016・D-0013 の未解決の点、二者択一の前提の体系"}]
```

</details>

<details><summary>ツール: Bash: main を再取得して確認</summary>

```text
cd /home/user/point-free-spacetime && git fetch origin main 2>&1|tail -1; git log --oneline -2 origin/main; git merge-base --is-ancestor HEAD origin/main && echo merged
```

</details>

<details><summary>結果: Bash: main を再取得して確認</summary>

```text
4238cba..dda36f0  main       -> origin/main
dda36f0 Merge pull request #45 from kittenkiki15/claude/clever-planck-pr5kq1
ab105cd 第 23 回の 12 回目のクロスモデルレビューに対応：時計の周期性を全体の位相を除いた射影ユニタリ表現について述べると明記した
merged
```

</details>

## Claude

前回の PR がマージ済みか確認できたので、作業ブランチを最新の main から作り直します。

<details><summary>ツール: Bash: 両リポジトリのブランチを main から作り直し、T-0019 の節を読む</summary>

```text
git checkout -B claude/clever-planck-pr5kq1 origin/main 2>&1|tail -1; cd ../point-free-spacetime-private && git checkout -B claude/clever-planck-pr5kq1 origin/main 2>&1|tail -1; cd ../point-free-spacetime && sed -n '/^### T-0019/,/^### T-0020/p' roadmap.md | head -80
```

</details>

<details><summary>結果: Bash: 両リポジトリのブランチを main から作り直し、T-0019 の節を読む</summary>

```text
(use "git push" to publish your local commits)
  (use "git push" to publish your local commits)
### T-0019 量子・古典・混成の実験の扱いの先行研究の調査（第 19 回に追加）

第 19 回に、ユーザーの判断で追加した。フレームワークの要件として、量子的な観測と古典的な観測の両方と、その混成を「実験」として扱えるようにしたい（ユーザーの方針。量子重力理論への寄与という目的による）。T-0016 では、Le Cam の実験の理論（結果が古典的な記録の実験）と Ludwig の構成（有限個の効果による位相）を調べたが、この要件に直接答える部分は調べていない。

- 調べること（文献は記憶による。未確認。主な文献は arXiv にあるはず）：
  1. 一般化確率論（Hardy、Barrett、Chiribella–D'Ariano–Perinotti）：古典・量子・混成の状態空間と効果空間の区別、複合系の扱い、状態空間の再構成（T-0016 から移した）。[C-0003](conjectures/C-0003.md) との関係。
  2. Le Cam の理論の量子版（量子統計的実験の比較。Buscemi、Jenčová、松本、Guţă–Kahn の量子局所漸近正規性）。
  3. 量子参照系と量子時計（Page–Wootters、Giacomini–Castro-Ruiz–Brukner など）。T-0017 の「操作的な座標づけと参照系」と重なる部分は、ここでは次の問いに絞る。
  4. 逐次・適応的な実験の扱い（測定後の状態まで与える測定（instrument）の合成、量子コム（Chiribella–D'Ariano–Perinotti）・量子戦略（Gutoski–Watrous）・process tensor、チャネルの識別と推定での適応的な戦略と並列の戦略の違い）。(a) の立場で、適応的な設定（[D-0001](definitions/D-0001.md)）の結果の族の分布を、履歴を入力とする古典的な核の合成として書けるか。核で表す対象を、「固定した選び方の規則での記録の同時分布」と「選び方の規則を変えても整合する同じ過程の記述」に分けて調べる（実数値の有限個の結果なら、前者は通常の可測性の条件の下で条件付き分布の核に分解できるが、それだけでは後者を扱えるとは限らない。PR #43 のレビューの論点）。[D-0002](definitions/D-0002.md)（選び方の規則の定義域・可測性・無作為な選択）、[D-0004](definitions/D-0004.md)・[A-0006](assumptions/A-0006.md)・[D-0006](definitions/D-0006.md)（履歴を入力とする核）の未解決の点の材料にする（決めるのは T-0004〜T-0006）。適応的な設定は、(b) の判定基準の論点（量子的な出力を後の装置につなぐ場合）のうち、古典的な記録を次の装置へ渡す部分にあたる（第 21 回に、ユーザーの判断で加えた）。
  5. 複合のプロトコル $`π^M`$（[D-0001](definitions/D-0001.md) の注意。$`M`$ 個の部分装置で並列に観測し、同時に読み出す）の結果の同時分布と、一般化確率論・量子論の複合系の扱い（テンソル積、局所的な効果、もつれ）との対応（第 21 回に
…（以下 2889 文字を省略）
```

</details>

## Claude

前回（第 23 回）の PR #45 はマージ済みでした。両リポジトリの作業ブランチを最新の `main` から作り直しました。

#### 第 24 回の開始

`NEXT.md` によると、今回のタスクは **T-0019「量子・古典・混成の実験の扱いの先行研究の調査」の続き**です。残っているのは **項目 2：Le Cam の理論の量子版**です。

##### 今回の進め方の案

`NEXT.md` には「比べる対象を量子状態の族とするか、チャネル・測定器とするかを区別して調べる」とあります。この区別に沿って、候補の文献を 2 群に分けます。どれも記憶にもとづくもので、まだ原典で確かめていません。本文は arXiv 版で確かめます。

**群 A：状態の族（量子統計的実験）の比較**
- Buscemi 2012：量子統計モデルの比較と、十分性の同値条件。量子版の Blackwell–Sherman–Stein 定理。
- 松本：Le Cam の randomization criterion の量子版。
- Jenčová：量子の 2 値実験の比較と、量子版の不足度。

**群 B：チャネル・測定器の比較**
- Jenčová 2016 前後：量子チャネルと統計的実験の比較。
- Buscemi の「量子統計的射」（quantum statistical morphisms）と、チャネルの劣化可能性の順序。

**群 C：漸近論（極限）**
- Guţă–Kahn：量子局所漸近正規性（quantum LAN）。D-0005 の「族の極限」の量子版の候補です。

##### ご相談したいこと

1. **重点**：今回は群 A と群 B の対比（状態の比較の定理が、装置・チャネルの比較にどこまで当てはまるか）に重点を置き、群 C は要旨の確認にとどめる、という案でよいでしょうか。D-0005 の極限の位相とのつながりを重視するなら、群 C を厚くする手もあります。
2. **深さ**：第 22・23 回と同じく、中心の文献の本文で定理の仮定と結論を確かめ、調査メモにまとめる、でよいでしょうか。
3. **因果的非分離性**：Oreshkov–Costa–Brukner 2012 は前回の見立ての段階 3 を支えるために挙がっています。今回確かめますか、それとも後に回しますか。

方針が決まりしだい、文献の取得と確認を始めます。

<details><summary>ツール: Bash: 未 push のコミットの所在を確認</summary>

```text
git status -sb | head -1; cd ../point-free-spacetime-private && git status -sb | head -1; git log --oneline origin/claude/clever-planck-pr5kq1..HEAD
```

</details>

<details><summary>結果: Bash: 未 push のコミットの所在を確認</summary>

```text
## claude/clever-planck-pr5kq1...origin/main
## claude/clever-planck-pr5kq1...origin/main
7627198 Merge pull request #14 from kittenkiki15/claude/clever-planck-pr5kq1
```

</details>

<details><summary>ツール: Bash: 非公開リポジトリの作業ブランチを main に揃えて push</summary>

```text
git push -u origin claude/clever-planck-pr5kq1 2>&1 | tail -2
```

</details>

<details><summary>結果: Bash: 非公開リポジトリの作業ブランチを main に揃えて push</summary>

```text
* [new branch]      claude/clever-planck-pr5kq1 -> claude/clever-planck-pr5kq1
branch 'claude/clever-planck-pr5kq1' set up to track 'origin/claude/clever-planck-pr5kq1'.
```

</details>

<details><summary>ツール: Bash: 公開リポジトリの作業ブランチも push</summary>

```text
cd /home/user/point-free-spacetime && git push -u origin claude/clever-planck-pr5kq1 2>&1 | tail -1
```

</details>

<details><summary>結果: Bash: 公開リポジトリの作業ブランチも push</summary>

```text
branch 'claude/clever-planck-pr5kq1' set up to track 'origin/claude/clever-planck-pr5kq1'.
```

</details>

## Claude

フックが「push していないコミットがある」と警告したので、両リポジトリの作業ブランチを push しました。どちらも最新の `main` と同じ内容で、新しい変更はありません。

先ほどの 3 点のご相談への回答をお待ちしています。方針が決まりしだい、文献の取得と確認を始めます。

1. **重点**：群 A（量子状態の族の比較）と群 B（チャネル・測定器の比較）を対比することに重点を置き、群 C（量子局所漸近正規性）は要旨の確認にとどめる案でよいでしょうか。
2. **深さ**：第 22・23 回と同じく、中心の文献の本文で定理の仮定と結論を確かめ、調査メモにまとめる、でよいでしょうか。
3. **因果的非分離性**：Oreshkov–Costa–Brukner 2012 を今回確かめますか、それとも後に回しますか。

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
{"number":14,"title":"第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加","body":"第 23 回（公開リポジトリ kittenkiki15/point-free-spacetime#45）で読んだ論文 6 件の arXiv 版 PDF を、`papers/` に追加しました。あわせて、`papers/README.md` の一覧も更新しました。\n\n追加したファイルは次の 6 件です。\n\n- `giovannetti2015.pdf`\n- `castroruiz2020.pdf`\n- `hoehn2021.pdf`\n- `loveridge2018.pdf`\n- `smith2020.pdf`\n- `bartlett2007.pdf`\n\n`giacomini2019.pdf` は登録済みです。\n\n🤖 Generated with [Claude Code](https://claude.com/claude-code)\n\n[セッション URL]\n\n---\n_Generated by [Claude Code]([セッション URL])_","state":"closed","draft":false,"merged":true,"mergeable_state":"unknown","html_url":"https://github.com/kittenkiki15/point-free-spacetime-private/pull/14","user":{"login":"kittenkiki15","id":329015067,"profile_url":"https://github.com/kittenkiki15","avatar_url":"https://avatars.githubusercontent.com/u/329015067?v=4"},"merged_by":"kittenkiki15","head":{"ref":"claude/clever-planck-pr5kq1","sha":"cdd152d0367cf3bae73799401f393fc5a6463630","repo":{"full_name":"kittenkiki15/point-free-spacetime-private","description":"point-free-spacetime 用のプライベートリポジトリ"}},"base":{"ref":"main","sha":"91dd8d119cf39e8d37519dc2d9ca65eb097d7a06","repo":{"full_name":"kittenkiki15/point-free-spacetime-private","description":"point-free-spacetime 用のプライベートリポジトリ"}},"additions":6,"changed_files":7,"commits":1,"created_at":"2026-10-02T01:03:01Z","updated_at":"2026-10-02T03:34:39Z","closed_at":"2026-10-02T03:34:35Z","
…（以下 34 文字を省略）
```

</details>

<details><summary>ツール: mcp__claude-code-remote__unsubscribe_pr_activity</summary>

```text
（入力の本文は省略。項目: owner, pullNumber, repo）
```

</details>

<details><summary>結果: mcp__claude-code-remote__unsubscribe_pr_activity</summary>

```text
Unsubscribed from activity on kittenkiki15/point-free-spacetime-private#14. Webhook events for this PR will no longer be delivered.
```

</details>

## Claude

2 件の PR がどちらもマージされたので、第 23 回のセッションはここで終わりです。

- 公開リポジトリ：[kittenkiki15/point-free-spacetime#45](https://github.com/kittenkiki15/point-free-spacetime/pull/45)
- 非公開リポジトリ：[kittenkiki15/point-free-spacetime-private#14](https://github.com/kittenkiki15/point-free-spacetime-private/pull/14)

PR の通知も止めました。

次のセッション（第 24 回）では、`NEXT.md` にあるとおり、T-0019 の項目 2「Le Cam の理論の量子版」を扱います。その調査の後で、次の二つを判断していただく予定です。
- 「量子的な観測」を (a)・(b) のどちらの意味に読むか。
- (a) の中で、較正をどの段階まで許すか。

`/clear` でコンテキストを初期化してから、次のセッションを始めてください。

## ユーザー

以下の「ご相談したいこと」について、「1. 重点」は今回は群 A と群 B の対比に重点を置いてください。「2. 深さ」は、第 22・23 回と同じく、中心の文献の本文で定理の仮定と結論を確かめ、調査メモにまとめてください。「3. 因果的非分離性」は今回確かめてください。
***
前回の PR がマージ済みか確認できたので、作業ブランチを最新の main から作り直します。
前回（第 23 回）の PR #45 はマージ済みでした。両リポジトリの作業ブランチを最新の `main` から作り直しました。
第 24 回の開始
`NEXT.md` によると、今回のタスクは T-0019「量子・古典・混成の実験の扱いの先行研究の調査」の続きです。残っているのは 項目 2：Le Cam の理論の量子版です。
今回の進め方の案
`NEXT.md` には「比べる対象を量子状態の族とするか、チャネル・測定器とするかを区別して調べる」とあります。この区別に沿って、候補の文献を 2 群に分けます。どれも記憶にもとづくもので、まだ原典で確かめていません。本文は arXiv 版で確かめます。
群 A：状態の族（量子統計的実験）の比較

* Buscemi 2012：量子統計モデルの比較と、十分性の同値条件。量子版の Blackwell–Sherman–Stein 定理。
* 松本：Le Cam の randomization criterion の量子版。
* Jenčová：量子の 2 値実験の比較と、量子版の不足度。

群 B：チャネル・測定器の比較

* Jenčová 2016 前後：量子チャネルと統計的実験の比較。
* Buscemi の「量子統計的射」（quantum statistical morphisms）と、チャネルの劣化可能性の順序。

群 C：漸近論（極限）

* Guţă–Kahn：量子局所漸近正規性（quantum LAN）。D-0005 の「族の極限」の量子版の候補です。

ご相談したいこと

1. 重点：今回は群 A と群 B の対比（状態の比較の定理が、装置・チャネルの比較にどこまで当てはまるか）に重点を置き、群 C は要旨の確認にとどめる、という案でよいでしょうか。D-0005 の極限の位相とのつながりを重視するなら、群 C を厚くする手もあります。
2. 深さ：第 22・23 回と同じく、中心の文献の本文で定理の仮定と結論を確かめ、調査メモにまとめる、でよいでしょうか。
3. 因果的非分離性：Oreshkov–Costa–Brukner 2012 は前回の見立ての段階 3 を支えるために挙がっています。今回確かめますか、それとも後に回しますか。

方針が決まりしだい、文献の取得と確認を始めます。
フックが「push していないコミットがある」と警告したので、両リポジトリの作業ブランチを push しました。どちらも最新の `main` と同じ内容で、新しい変更はありません。
先ほどの 3 点のご相談への回答をお待ちしています。方針が決まりしだい、文献の取得と確認を始めます。

1. 重点：群 A（量子状態の族の比較）と群 B（チャネル・測定器の比較）を対比することに重点を置き、群 C（量子局所漸近正規性）は要旨の確認にとどめる案でよいでしょうか。
2. 深さ：第 22・23 回と同じく、中心の文献の本文で定理の仮定と結論を確かめ、調査メモにまとめる、でよいでしょうか。
3. 因果的非分離性：Oreshkov–Costa–Brukner 2012 を今回確かめますか、それとも後に回しますか。

2 件の PR がどちらもマージされたので、第 23 回のセッションはここで終わりです。

* 公開リポジトリ：[kittenkiki15/point-free-spacetime#45](https://github.com/kittenkiki15/point-free-spacetime/pull/45)
* 非公開リポジトリ：[kittenkiki15/point-free-spacetime-private#14](https://github.com/kittenkiki15/point-free-spacetime-private/pull/14)

PR の通知も止めました。
次のセッション（第 24 回）では、`NEXT.md` にあるとおり、T-0019 の項目 2「Le Cam の理論の量子版」を扱います。その調査の後で、次の二つを判断していただく予定です。

* 「量子的な観測」を (a)・(b) のどちらの意味に読むか。
* (a) の中で、較正をどの段階まで許すか。

`/clear` でコンテキストを初期化してから、次のセッションを始めてください。

## Claude

第 24 回として進めます。まず、ブランチの状態を確かめます。貼り付けていただいた文面によると、別のセッションですでにブランチを作り直して push しているようなので、その状態と食い違わないかを見ておきます。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git fetch -q origin && git log --oneline -3 origin/main | cat; git log --oneline -3 origin/claude/clever-planck-pr5kq1 | cat; git status -sb | head -2; cd ../point-free-spacetime-private && git fetch -q origin && git log --oneline -2 origin/main | cat; git log --oneline -2 origin/claude/clever-planck-pr5kq1 | cat
```

</details>

<details><summary>結果: Bash</summary>

```text
dda36f0 Merge pull request #45 from kittenkiki15/claude/clever-planck-pr5kq1
ab105cd 第 23 回の 12 回目のクロスモデルレビューに対応：時計の周期性を全体の位相を除いた射影ユニタリ表現について述べると明記した
9f98cfe 第 23 回の 11 回目のクロスモデルレビューに対応：A-0013 の普遍性について、時計の状態を設定に含めて保つ案と、対象ごとの核を許して主張を改める案を分けた
dda36f0 Merge pull request #45 from kittenkiki15/claude/clever-planck-pr5kq1
ab105cd 第 23 回の 12 回目のクロスモデルレビューに対応：時計の周期性を全体の位相を除いた射影ユニタリ表現について述べると明記した
9f98cfe 第 23 回の 11 回目のクロスモデルレビューに対応：A-0013 の普遍性について、時計の状態を設定に含めて保つ案と、対象ごとの核を許して主張を改める案を分けた
## claude/clever-planck-pr5kq1...origin/claude/clever-planck-pr5kq1
7627198 Merge pull request #14 from kittenkiki15/claude/clever-planck-pr5kq1
cdd152d 第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加した
7627198 Merge pull request #14 from kittenkiki15/claude/clever-planck-pr5kq1
cdd152d 第 23 回：量子時計・量子参照系の論文 6 件の PDF を追加した
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && git checkout -q -B claude/clever-planck-pr5kq1 origin/main && git log --oneline -1 | cut -c1-8; cd ../point-free-spacetime-private && git checkout -q -B claude/clever-planck-pr5kq1 origin/main && git log --oneline -1 | cut -c1-8; date -u +%FT%TZ
```

</details>

<details><summary>結果: Bash</summary>

```text
dda36f0 
7627198 
2026-10-02T03:49:40Z
```

</details>

<details><summary>ツール: Bash</summary>

```text
S=/tmp/claude-0/-home-user/[ID]/scratchpad/s24; mkdir -p $S; cd $S; q(){ curl -sS "https://export.arxiv.org/api/query?search_query=$1&max_results=5" | python3 -c "
import sys,re;t=sys.stdin.read()
for e in t.split('<entry>')[1:]:
  i=re.search(r'<id>http://arxiv.org/abs/(.*?)</id>',e).group(1)
  ti=re.sub(r'\s+',' ',re.search(r'<title>(.*?)</title>',e,re.S).group(1))
  au=', '.join(re.findall(r'<name>(.*?)</name>',e))[:80]
  j=re.search(r'<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>',e,re.S)
  print(i,'|',ti[:100],'|',au,'|',j.group(1) if j else '')"; echo; sleep 3; }
q 'au:Buscemi+AND+ti:comparison+AND+ti:sufficiency'
q 'au:Matsumoto+AND+ti:randomization+AND+ti:criterion'
q 'au:Jencova+AND+ti:comparison'
q 'au:Buscemi+AND+ti:degradable'
q 'au:Kahn+AND+ti:local+AND+ti:asymptotic+AND+ti:normality'
q 'au:Oreshkov+AND+ti:causal'
q 'au:Araujo+AND+ti:witnessing+AND+ti:causal'
```

</details>

<details><summary>結果: Bash</summary>

```text
Command did not complete within its 120s timeout and was moved to the background (ID: byk4ixya6). Output is being written to: /tmp/claude-0/-home-user/[ID]/tasks/byk4ixya6.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. To check interim output, use Read on that file path.
Session cwd remains /home/user/point-free-spacetime-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```

</details>

<details><summary>ツール: Bash</summary>

```text
sleep 60; cat /tmp/claude-0/-home-user/[ID]/tasks/byk4ixya6.output
```

</details>

<details><summary>結果（エラー）: Bash</summary>

```text
<tool_use_error>Blocked: sleep 60 followed by: cat /tmp/claude-0/-home-user/[ID]/tasks/byk4ixya6.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```

</details>

<details><summary>ツール: Read: /tmp/claude-0/-home-user/[ID]/tasks/byk4ixya6.output</summary>

```text
（入力の本文は省略。項目: file_path）
```

</details>

<details><summary>結果: Read: /tmp/claude-0/-home-user/[ID]/tasks/byk4ixya6.output</summary>

```text
1	
2	
3	
4	
5	
6
```

</details>

## Claude

arXiv の検索 API から結果が返ってこないので、記憶にある番号の要旨ページを直接確かめます。

<details><summary>ツール: Bash</summary>

```text
for id in 1004.3794 1012.2650 1512.07016 1511.08893 0804.3876 quant-ph/0512075 1105.4464 1506.03776 1506.05449 1208.4339 0907.0866; do printf "%s | " $id; curl -sS -m 20 "https://arxiv.org/abs/$id" | grep -o -E 'citation_title" content="[^"]*|citation_author" content="[^"]*|class="tablecell jref">[^<]*' | sed 's/.*content="//;s/.*jref">//' | head -4 | tr '\n' ';'; echo; done
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
curl -sS -m 30 "https://export.arxiv.org/api/query?search_query=ti:%22quantum%20binary%20experiments%22&max_results=5" | grep -o -E "<id>[^<]*|<title>[^<]*" | head; curl -sS -m 30 "https://export.arxiv.org/api/query?search_query=au:Jencova&max_results=60&sortBy=submittedDate&sortOrder=ascending" | python3 -c "
import sys,re;t=sys.stdin.read()
for e in t.split('<entry>')[1:]:
  print(re.search(r'<id>http://arxiv.org/abs/(.*?)</id>',e).group(1), re.sub(r'\s+',' ',re.search(r'<title>(.*?)</title>',e,re.S).group(1))[:90])" | grep -i "compar\|experiment\|sufficien\|blackwell\|channel"
```

</details>

<details><summary>結果: Bash</summary>

```text
curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received
```

</details>

<details><summary>ツール: Bash</summary>

```text
S=/tmp/claude-0/-home-user/[ID]/scratchpad/s24; mkdir -p $S; cd $S; for p in buscemi2012:1004.3794 matsumoto2010:1012.2650 jencova2016:1512.07016 buscemi2016:1511.08893 kahn2009:0804.3876 oreshkov2012:1105.4464 araujo2015:1506.03776 oreshkov2016:1506.05449; do k=${p%%:*}; id=${p#*:}; curl -sSL -m 60 -o $k.pdf "https://arxiv.org/pdf/$id" && pdftotext $k.pdf $k.txt; echo "$k $(wc -l < $k.txt) $(grep -m1 -o 'arXiv:[0-9.]*v[0-9]*' $k.txt)"; done
```

</details>

<details><summary>結果: Bash</summary>

```text
buscemi2012 1669 arXiv:1004.3794v4
matsumoto2010 2264 arXiv:1012.2650v7
jencova2016 1674 arXiv:1512.07016v2
buscemi2016 1187 arXiv:1511.08893v2
kahn2009 6274 arXiv:0804.3876v1
oreshkov2012 1819 arXiv:1105.4464v3
araujo2015 4208 arXiv:1506.03776v2
oreshkov2016 3341 arXiv:1506.05449v3
Shell cwd was reset to /home/user
```

</details>

## Claude

Buscemi 2012（群 A）から、主定理の仮定と結論を読みます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,60p buscemi2012.txt | grep -v "^\s*$" | head -40; grep -n -E "^(Theorem|Definition|Lemma|Corollary|Proposition|Remark) [0-9]" buscemi2012.txt | head -40
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 272,330p buscemi2012.txt; sed -n 505,560p buscemi2012.txt; sed -n 856,870p buscemi2012.txt; sed -n 1155,1240p buscemi2012.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1240,1300p buscemi2012.txt; sed -n 588,620p buscemi2012.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

## Claude

Buscemi 2012 の主定理を確かめました。次は松本 2010（randomization criterion の量子版）です。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,40p matsumoto2010.txt | grep -v "^\s*$"; grep -n -E "^(Theorem|Definition|Lemma|Corollary|Proposition|Remark|Example) ?[0-9.]*" matsumoto2010.txt | head -50
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 380,520p matsumoto2010.txt | grep -v "^\s*$" | head -110
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 520,560p matsumoto2010.txt | grep -v "^\s*$"; sed -n 770,860p matsumoto2010.txt | grep -v "^\s*$"; sed -n 1170,1200p matsumoto2010.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && grep -n -i "quantum experiment\|separable\|dim H <\|B1 (H)" matsumoto2010.txt | head -15; sed -n 300,330p matsumoto2010.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,30p jencova2016.txt | grep -v "^\s*$"; grep -n -E "^(Theorem|Definition|Lemma|Corollary|Proposition|Remark|Example) ?[0-9.]*" jencova2016.txt | head -40
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1000,1060p jencova2016.txt | grep -v "^\s*$"; sed -n 1185,1215p jencova2016.txt | grep -v "^\s*$"; sed -n 1240,1340p jencova2016.txt | grep -v "^\s*$"; sed -n 1510,1580p jencova2016.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

## Claude

Jenčová 2016 の主定理 1 を読みました。続けて、チャネルの不足度 $`δ(Φ, Ψ)`$ の定義と、前提の次元の条件を確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && grep -n -B2 -A6 "δ(Φ, Ψ) :=\|δ(Φ, Ψ) =\|deficiency" jencova2016.txt | sed -n 1,60p; grep -n -i "finite dimensional\|finite-dimensional" jencova2016.txt | head -5
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 823,880p jencova2016.txt | grep -v "^\s*$" | head -45; grep -n -i "without ancilla\|no ancilla\|K0 = C\|trivial ancilla" jencova2016.txt | head
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,40p buscemi2016.txt | grep -v "^\s*$" | head -30; grep -n -E "^(Theorem|Definition|Lemma|Corollary|Proposition|Remark|Example) ?[0-9.]*" buscemi2016.txt | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 172,300p buscemi2016.txt | grep -v "^\s*$"; sed -n 505,600p buscemi2016.txt | grep -v "^\s*$"; sed -n 975,995p buscemi2016.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

## Claude

Buscemi 2016 の命題 1 と系 1〜3 を確かめました。次は群 C の Kahn–Guţă 2009 です。ご指示どおり、要旨と主定理の主張だけを確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,40p kahn2009.txt | grep -v "^\s*$" | head -25; grep -n -E "^Theorem [0-9.]+" kahn2009.txt | head; 
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1451,1500p kahn2009.txt | grep -v "^\s*$" | head -40
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1380,1450p kahn2009.txt | grep -v "^\s*$" | grep -i -B2 -A3 "δ\|distinct\|eigenvalue" | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,200p oreshkov2012.txt | grep -v "^\s*$" | head -150
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 200,520p oreshkov2012.txt | grep -v "^\s*$" | head -200
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && grep -n -i "classical limit\|classical processes\|diagonal\|Closed laboratories (CL)\|(CL)" oreshkov2012.txt | head -12
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 515,560p oreshkov2012.txt | grep -v "^\s*$"; sed -n 170,200p oreshkov2012.txt | grep -v "^\s*$"
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

## Claude

次は Araújo ほか 2015（因果的非分離性の判定）です。

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,40p araujo2015.txt | grep -v "^\s*$" | head -30; grep -n -i "quantum switch\|cannot violate\|causal inequalit\|Definition\|witness is\|tripartite\|three parties" araujo2015.txt | head -50
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 562,700p araujo2015.txt | grep -v "^\s*$" | head -70
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && grep -n "VI\.\|cannot violate any causal inequality\|device-independent" araujo2015.txt | head; awk 'NR>=2050 && NR<=2200' araujo2015.txt | grep -v "^\s*$" | grep -i -B3 -A10 "switch" | head -60
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 1,40p oreshkov2016.txt | grep -v "^\s*$" | head -30; grep -n -i "Definition\|extensibl\|recursive\|causally separable if" oreshkov2016.txt | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && sed -n 30,45p oreshkov2016.txt; sed -n 600,660p oreshkov2016.txt | grep -i -B2 -A12 "Theorem\|canonical" | head -40; sed -n 1600,1625p oreshkov2016.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && grep -n "Theorem II.2" oreshkov2016.txt | head -3; awk '/Theorem II.2\. /{f=1} f{print; if(++n>30) exit}' oreshkov2016.txt; sed -n 273,300p oreshkov2016.txt
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

## Claude

9 件の要点を確かめ終えました。調査メモを書く前に、照合するプロジェクト側の記述（D-0005 の未解決の点、T-0005・T-0006）を確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && sed -n '/## 未解決の点/,/## 履歴/p' definitions/D-0005.md | cut -c1-500 | head -30; awk '/^### T-0005/,/^### T-0007/' roadmap.md | cut -c1-400 | head -30
```

</details>

<details><summary>結果: Bash</summary>

```text
## 未解決の点

- 極限の位相。コーシー性を使う場合の一様構造、すべてのコーシー列が収束するための完備性、極限を一つに定めるための分離性（ハウスドルフ性）か極限点の同値類を取る規則。候補として、Le Cam の実験の弱位相（推定の対象の有限部分集合ごとの不足度による位相。実験の型の空間はコンパクト・ハウスドルフ）がある（[第 18 回の調査メモ](../surveys/2026-09-30_18_limit-
- 部分列の選び方。結果を見てから選ぶ部分列は推定をゆがめうるので、結果によらずに選ぶか、選び方を尤度に組み込むか。
- 事後分布の集中の条件（測定の網羅性、識別可能性、一致性）。
- 事後分布を、応答関数の空間ではなく代数の元（観測量）の空間に置く場合の対応。
- 収束させる対象：実験の列か、各段階のデータから得る事後分布の列か。実験の設定と結果の空間はプロトコルごとに異なるので、実験そのものを共通の空間の元とみなす方法は決まっていない。
  - 第 17 回の候補（[調査メモ](../surveys/2026-09-30_17_comparison-of-experiments.md)の 7.1・7.2 節。Claude の見立て）：Le Cam の不足度と距離 $`Δ`$ は、推定の対象の集合 $`Θ`$ が共通なら、結果の空間が異なる実験を比べられ、$`Δ = 0`$ で割った実験の型は距離空間になる。$`Θ`$ を推定の対象の空間と読むか、設定の空間と読むかは決まっていない（第 19 回に、「パラメータ」を推定の対

## 履歴
### T-0005 尤度と同時分布、主体の間で共有するデータの空間

- [D-0004](definitions/D-0004.md)：複数回の結果の同時分布と尤度（条件付き独立を仮定するか）、推定の対象の区別。
- [A-0006](assumptions/A-0006.md)：交換可能性を別の前提として課すか。
- [A-0007](assumptions/A-0007.md)：予測分布を作る同時分布と尤度、主体の間で共有するデータの空間、適用範囲。前提を相互とするか片側とするか、フレームワークで採る一致の段階（第 16 回に加えた論点。ユーザーの判断で次に回した）。
- 弱い併合（Kalai–Lehrer 1994。文献は記憶による。未確認）：A-0007 の一致の段階の候補として、ここで調べる（第 19 回に T-0016 から移した）。

### T-0006 極限と事後分布の集中

- [D-0005](definitions/D-0005.md)：極限の位相（一様構造、完備性、分離性）、収束させる対象、部分列の選び方、事後分布の集中の条件、事後分布を置く空間。
- [D-0006](definitions/D-0006.md)（層 5）：予備的な検討にとどめる。実際の観測量の極限の位相を決めるときに、可能な観測量にも同じ取り方が使えるかを確かめる。層 5 の定義と前提そのものは T-0010 で扱う。
- 関係する予想：[C-0005](conjectures/C-0005.md)、[C-0006](conjectures/C-0006.md)。
- 第 17 回の候補（[調査メモ](surveys/2026-09-30_17_comparison-of-experiments.md)の 7 節）：実験を共通の空間に置く方法としての Le Cam の不足度（$`Θ`$ の読み方の二つ
…（以下 316 文字を省略）
```

</details>

## Claude

材料が揃ったので、調査メモを書きます。

<details><summary>ツール: Write: /home/user/point-free-spacetime/surveys/2026-10-02_24_quantum-comparison-and-causal-order.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/surveys/2026-10-02_24_quantum-comparison-and-causal-order.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/surveys/2026-10-02_24_quantum-comparison-and-causal-order.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /tmp/claude-0/-home-user/[ID]/scratchpad/s24 && grep -n "^Theorem [0-9]" araujo2015.txt; grep -n "Theorem 4" araujo2015.txt | head -3
```

</details>

<details><summary>結果: Bash</summary>

```text
（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）
```

</details>

## Claude

調査メモ `surveys/2026-10-02_24_quantum-comparison-and-causal-order.md` を書きました。8 件（群 A：2 件、群 B：2 件、群 C：1 件、因果的非分離性：3 件）について、定理の仮定と結論を arXiv 版の本文で確かめています。ただし群 C は、予定どおり要旨と主定理の主張の確認にとどめました。Jenčová の量子の 2 値実験の論文は、arXiv の番号を確かめられなかったので外しました。

#### 原典で確かめた主な結果

**群 A と群 B の対比**：どの定理も、「指定した類の課題での成績の比較」と「処理の写像の存在」が同値だと述べています。違いは、どんな課題を許すかと、それに対応する処理の類です。

| 許す課題 | 対応する処理 | 文献 |
| --- | --- | --- |
| 古典的な判定（POVM）だけ、補助系なし | 統計的射、または正写像（完全正値とは限らない） | Buscemi 2012 定理 3、松本 定理 13、Jenčová 命題 4、Buscemi 2016 命題 1 |
| 同じ課題で、比べられる側が可換 | CPTP 写像 | Buscemi 2012 命題 4、Buscemi 2016 系 1・3 |
| 量子の出力を持つ判定 | CPTP 写像 | 松本 定理 5 |
| 古典的な判定に補助系を加える | CPTP 写像 | Buscemi 2012 命題 5、Jenčová 定理 1・系 1 |

チャネルの比較は、入力に完全な状態の族を通した統計的実験の比較に帰着します（Jenčová 系 3）。

**群 C**：量子 LAN（Kahn–Guţă 定理 4.3）は、量子の Le Cam 距離が 0 に収束することとして述べられています。極限のモデルは、古典的なガウス分布と量子的なガウス状態の積です。

**因果的非分離性**：原典は二つの水準を区別しています。
- 相関の水準：装置に依存しない判定で、因果不等式を使います。
- 過程の水準：当事者の量子的な操作を信頼する判定で、因果の証人を使います。

量子スイッチは、過程の水準では因果的に非分離ですが、どの因果不等式も破れません（Araújo ほか 2015）。多者の因果的な過程は、厳密な半順序を値とする確率変数で定義されます。順序は確率的でよく、前の操作に応じて後の順序が変わる場合も含みます（Oreshkov–Giarmatzi 2016）。

#### 見立て（Claude によるもので、検証していません）

- 補助系を許した比較でも、比べる量は識別の成功確率という古典的な記録です。したがって (a) の立場でも、「補助系と合成した実験」を可能な実験に含めれば、装置を CPTP の水準で比べられます。含めなければ、比較は統計的射の水準にとどまります。第 22 回の判定基準 $`𝒯`$ の具体例です。
- 段階 3（事象ごとに位置を定めない）が問題になるのは、量子的な操作の特徴づけまで $`𝒯`$ に含める場合です。古典的な記録だけを比べる限り、量子スイッチの記録は確率的な因果順序で説明できます。この確率的な因果順序は、A-0016 を、順序が確率的で動的な場合に拡げた形と読めます。
- 量子の Le Cam 距離は、D-0005 の極限の位相の量子版の候補です。ただし、有限次元を仮定している文献が多く、連続の設定・結果に使うには確かめる必要があります。

これで、T-0019 の 5 項目の原典の確認は一通り終わりました。

<details><summary>ツール: AskUserQuestion</summary>

```text
（入力の本文は省略。項目: questions）
```

</details>

<details><summary>結果: AskUserQuestion</summary>

```text
Your questions have been answered: "調査メモの見立てを、どう扱いますか？"="記録して T-0019 を完了（推奨）". You can now continue with these answers in mind.
```

</details>

## Claude

見立てを未解決の点に記録し、T-0019 を完了にします。まず、ロードマップで T-0019 の状態がどこに書かれているかを確かめます。

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && grep -n "T-0019" roadmap.md | cut -c1-200 | head -20; grep -n "完了" roadmap.md | head -5 | cut -c1-150
```

</details>

<details><summary>結果: Bash</summary>

```text
3:最終更新: 2026-10-02（第 23 回。T-0019 の項目 3 を行った）
11:- 順序は、第 11 回にユーザーと相談して決めた（2 節）。第 13 回に、ユーザーの提案で T-0015（D-0003 の未解決の点の解決）を T-0002 の前に加えた。�
18:\text{T-0001} \;→\; \text{T-0015} \;→\; \text{T-0002} \;→\; \text{T-0003} \;→\; \text{T-0016} \;→\; \text{T-0018} \;→\; \text{T-0019} \;→\; \text{段階 B（T-0004〜T-0007）} \;→\
26:| （調査） | 量子・古典・混成の実験の扱い（一般化確率論、Le Cam の量子版、量子参照系） | T-0019 |
34:T-0015 は、番号は後から付けたが、順序は T-0001 の次である。T-0016 は T-0003 の次、T-0018 は T-0016 の次（第 16 回にユーザーと決めた）、T-0019 は T-0018 �
60:| T-0019 | 量子・古典・混成の実験の扱いの先行研究の調査（第 19 回に追加） | 調査 | なし | [D-0001](definitions/D-0001.md)、[D-0002](definitions/D-0002.md)、[D-000
69:  T0018 --> T0019["T-0019 量子・古典・混成の調査"]
85:図の矢印は、2 節の進める順序です。表の「前提のタスク」は、内容の上で先に要るものだけを書いています（例えば T-0003 は、内容の上では前提�
230:  - 一般化確率論（状態空間の再構成、古典・量子・混成の区別）→ 新しい調査のタスク T-0019
268:### T-0019 量子・古典・混成の実験の扱いの先行研究の調査（第 19 回に追加）
38:状態は、未着手・進行中・完了・保留のどれかです。
42:| T-0001 | 予想 C-0001 の見直し（第 12 回） | A | なし | [C-0001](conjectures/C-0001.md)、[C-0007](conjectures/C-0007.md)、[C-0008](c
43:| T-0002 | フレームワークの圏論的な概観（第 14 回） | A | T-0001 | [framework.md](framework.md) のすべての要素 | 完了 |
44:| T-0003 | QBism の先行研究の調査（第 15 回） | 調査 | なし | [D-0005](definitions/D-0005.md)、[A-0007](assumptions/A-0007.md)、[
56:| T-0015 | D-0003 の未解決の点の解決と、D-0011 を可能な実験の定義に改めること（第 13 回） | A | T-0001 | [D-0003](def
```

</details>

<details><summary>ツール: Bash</summary>

```text
sed -n 60p roadmap.md | rev | cut -c1-40 | rev; grep -n "^- 残り：項目 2" roadmap.md; grep -n "第 23 回の見立て" definitions/D-0013.md assumptions/A-0016.md | cut -c1-40; grep -n "第 17 回の候補" definitions/D-0005.md | cut -c1-40
```

</details>

<details><summary>結果: Bash</summary>

```text
Command did not complete within its 120s timeout and was moved to the background (ID: b8p0c5ey3). Output is being written to: /tmp/claude-0/-home-user/[ID]/tasks/b8p0c5ey3.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. To check interim output, use Read on that file path.
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
L=open('roadmap.md').read().split('\n')
print(L[59][-60:])
for i,l in enumerate(L):
    if l.startswith('- 残り：項目 2'): print(i+1,l[:80])
EOF
```

</details>

<details><summary>結果: Bash</summary>

```text
sumptions/A-0010.md)、[C-0003](conjectures/C-0003.md) | 進行中 |
284 - 残り：項目 2（Le Cam の理論の量子版）。見立ての段階 3 を支える因果的非分離性の文献（Oreshkov–Costa–Brukner 2012 など
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
SV="surveys/2026-10-02_24_quantum-comparison-and-causal-order.md"
SM="summaries/2026-10-02_24_quantum-comparison-and-causal-order.md"
# roadmap
p='roadmap.md'; L=open(p).read().split('\n')
assert L[59].endswith('| 進行中 |'); L[59]=L[59][:-len('| 進行中 |')]+'| 完了 |'
i=[k for k,l in enumerate(L) if l.startswith('- 残り：項目 2')][0]
L[i]=(f"- 第 24 回の進み具合（[調査メモ]({SV})、[まとめ]({SM})）：ユーザーの判断で、項目 2（Le Cam の理論の量子版）は群 A（状態の族の比較。Buscemi 2012、松本）と群 B（チャネル・装置の比較。Jenčová 2016、Buscemi 2016）の対比に重点を置き、群 C（量子 LAN。Kahn–Guţă 2009）は要旨と主定理の主張の確認にとどめた。あわせて、因果的非分離性（Oreshkov–Costa–Brukner 2012、Araújo ほか 2015、Oreshkov–Giarmatzi 2016）を原典で確かめた。見立てとして、比較の順序は許す判定・操作の類で決まり（古典的な判定だけなら統計的射の水準、補助系を許せば CPTP の水準）、因果的非分離性は相関の水準と過程の水準を分けて扱う、とした。これで 5 項目の原典の確認が一通り終わったので、ユーザーの判断で T-0019 を完了にした。\n"
      "- 残り（T-0019 の後）：(a)・(b) と、較正をどの段階まで許すかの判断は、ユーザーが次のセッションの最初に行う。Jenčová の量子の 2 値実験の比較と、前処理による比較は、必要になったときに確かめる。")
s='\n'.join(L)
import re
s=re.sub(r"最終更新: [^\n]*","最終更新: 2026-10-02（第 24 回。T-0019 を完了した）",s,count=1)
open(p,'w').write(s)
def app(p,anchor,text):
    s=open(p).read(); i=s.index(anchor); j=s.index('\n',i); s=s[:j]+text+s[j:]; open(p,'w').write(s)
# D-0005: append new bullet after the 第17回 candidate sub-bullet? add after the 'Le Cam の不足度' line: simpler append new bullet at end of 未解決 section
p='definitions/D-0005.md'; s=open(p).read()
i=s.index('## 履歴')
s=s[:i].rstrip('\n')+f"\n- 第 24 回の候補（[調査メモ]({'../'+SV})の 3.4 節。Claude の見立て）：量子の実験について、量子の Le Cam 距離（チャネルの不足度 $`δ(Φ, Ψ) = \\inf_α \\| Φ - α ∘ Ψ \\
…（以下 1190 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
1 failed, 34 passed in 0.27s
 assumptions/A-0016.md | 2 +-
 definitions/D-0005.md | 1 +
 definitions/D-0013.md | 2 +-
 roadmap.md            | 7 ++++---
 4 files changed, 7 insertions(+), 5 deletions(-)
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 -m pytest -q tools/tests 2>&1 | grep -E "Error|assert|FAILED" | head -10
```

</details>

<details><summary>結果: Bash</summary>

```text
>               assert (md.parent / target.split("#")[0]).exists(), (md, target)
E               AssertionError: (PosixPath('/home/user/point-free-spacetime/roadmap.md'), 'summaries/2026-10-02_24_quantum-comparison-and-causal-order.md')
E               assert False
tools/tests/test_framework.py:154: AssertionError
FAILED tools/tests/test_framework.py::test_links_exist - AssertionError: (Pos...
```

</details>

## Claude

見立てを記録し、T-0019 を「完了」にしました。

- **D-0005**：量子の Le Cam 距離を、極限の位相の量子版の候補として記録しました（量子 LAN は、この距離での収束の例です）。あわせて、残っている課題も書きました。
  - どの判定・操作の類で比べるかを決めること。
  - 原典の多くが有限次元を仮定していること。
- **D-0013**：段階 3 に含めるための追加の条件の候補を記録しました。因果的非分離性には「相関の水準」と「過程の水準」の二つがあり、段階 3 が問題になるのは、許す操作に量子的な操作の特徴づけを含める場合です。
- **A-0016**：Oreshkov–Giarmatzi の「確率的で動的な因果順序」を、この前提の拡張の候補として記録しました。段階 B で検討します。
- **`roadmap.md`**：T-0019 の状態を完了にし、第 24 回の進み具合を書きました。残りは次回の最初の判断で、(a)・(b) と、較正をどの段階まで許すかを決めていただきます。

`tools/tests` は 1 件だけ失敗しています。原因は、ロードマップからまだ書いていない第 24 回のまとめへリンクしていることです。まとめはセッションを終えるときに作るので、そこで解消されます。

対話を終える場合は、お知らせください。対話ログ・まとめ・関連ファイル（用語一覧、参考文献、`framework.md`、`NEXT.md`）を更新し、両方のリポジトリで PR を作ります。非公開リポジトリには PDF 8 件を追加します。

## Claude

フックの指示に従い、作業途中の変更をコミットして push します。非公開リポジトリには、今回の PDF 8 件と一覧の更新もここで加えます。

<details><summary>ツール: Bash</summary>

```text
git add -A && git commit -q -m "第 24 回（途中）：T-0019 の項目 2（量子統計的実験・チャネルの比較）と因果的非分離性の調査メモを追加し、D-0005・D-0013・A-0016 に見立てを記録して T-0019 を完了にした

Co-Authored-By: Claude Opus 5.5 <[メールアドレス]>
Claude-Session: [セッション URL]" && git push -q -u origin claude/clever-planck-pr5kq1 2>&1 | grep -v "^remote:"; git log --oneline -1 | cut -c1-8
cd ../point-free-spacetime-private && S=/tmp/claude-0/-home-user/[ID]/scratchpad/s24 && for k in buscemi2012 matsumoto2010 jencova2016 buscemi2016 kahn2009 oreshkov2012 araujo2015 oreshkov2016; do cp $S/$k.pdf papers/; done && python3 - <<'EOF'
p='papers/README.md'; s=open(p).read().rstrip('\n')
rows=[("buscemi2012","Buscemi, Comparison of quantum statistical models: equivalent conditions for sufficiency (2012)","arXiv:1004.3794v4（第 24 回に取得。Commun. Math. Phys. 310, 625）"),
("matsumoto2010","Matsumoto, A quantum version of randomization criterion (2010)","arXiv:1012.2650v7（第 24 回に取得）"),
("jencova2016","Jenčová, Comparison of quantum channels and statistical experiments (2016)","arXiv:1512.07016v2（第 24 回に取得）"),
("buscemi2016","Buscemi, Degradable channels, less noisy channels, and quantum statistical morphisms: an equivalence relation (2016)","arXiv:1511.08893v2（第 24 回に取得。Probl. Inf. Transm. 53, 201）"),
("kahn2009","Kahn–Guţă, Local asymptotic normality for finite dimensional quantum systems (2009)","arXiv:0804.3876v1（第 24 回に取得。Commun. Math. Phys. 289, 597）"),
("oreshkov2012"
…（以下 845 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
57fffea 
2d241dc 
0
```

</details>

## Claude

両方のリポジトリで、作業途中の変更をコミットして作業ブランチに push しました。PR はまだ作っていません。

- 公開リポジトリ（57fffea）：調査メモと、D-0005・D-0013・A-0016・ロードマップの更新です。
- 非公開リポジトリ（2d241dc）：第 24 回の論文の PDF 8 件と、`papers/README.md` の一覧の更新です。

公開リポジトリの `tools/tests` は、まだ 1 件だけ失敗します。ロードマップから、まだ書いていない第 24 回のまとめへリンクしているためです。セッションを終えるときにまとめを書けば解消します。

対話を終える場合はお知らせください。ログ・まとめ・関連ファイルを更新してから、PR を作ります。

## Claude

途中で止まっていた確認用のコマンド（ロードマップと定義の該当行を表示するもの）が、時間切れで打ち切られました。同じ確認は Python で済ませてあるので、作業への影響はありません。

対話を終える場合は、お知らせください。

## ユーザー

対話を終えてください。

## Claude

第 24 回を終えます。まず、対話ログを書き出す範囲を決めるために、第 24 回の最初の発言の時刻と、ほかのセッション記録の有無を確かめます。

<details><summary>ツール: Bash</summary>

```text
ls -la --time-style=+%FT%T ~/.claude/projects/-home-user/*.jsonl; cd ~/.claude/projects/-home-user && for f in *.jsonl; do python3 - "$f" <<'EOF'
import json,sys
for l in open(sys.argv[1]):
    try: d=json.loads(l)
    except: continue
    if d.get('type')=='user' and d.get('timestamp','')>'2026-10-02T03:30':
        c=d['message']['content']
        t=c if isinstance(c,str) else (c[0].get('text','') if isinstance(c,list) and c and c[0].get('type')=='text' else '')
        if t and not t.startswith('<'): print(sys.argv[1][:8], d['timestamp'], t[:60].replace('\n',' '))
EOF
done
```

</details>

<details><summary>結果: Bash</summary>

```text
-rw------- 1 root root  1420163 2026-10-02T00:01:15 /root/.claude/projects/-home-user/[ID].jsonl
-rw------- 1 root root   519760 2026-10-02T03:41:47 /root/.claude/projects/-home-user/[ID].jsonl
-rw------- 1 root root     2054 2026-10-01T15:23:15 /root/.claude/projects/-home-user/[ID].jsonl
-rw------- 1 root root 12325141 2026-10-02T06:54:57 /root/.claude/projects/-home-user/[ID].jsonl
-rw------- 1 root root  1184405 2026-10-01T11:42:13 /root/.claude/projects/-home-user/[ID].jsonl
1b224a2a 2026-10-02T03:35:52.557Z 次のセッションを開始してください。
1b224a2a 2026-10-02T03:36:28.723Z Stop hook feedback: [~/.claude/stop-hook-git-check.sh]: Ther
9ac91d3b 2026-10-02T03:35:52.557Z 次のセッションを開始してください。
9ac91d3b 2026-10-02T03:36:28.723Z Stop hook feedback: [~/.claude/stop-hook-git-check.sh]: Ther
9ac91d3b 2026-10-02T03:44:41.578Z Continue from where you left off.
9ac91d3b 2026-10-02T03:49:24.261Z 以下の「ご相談したいこと」について、「1. 重点」は今回は群 A と群 B の対比に重点を置いてください。「2. 深さ」
9ac91d3b 2026-10-02T04:11:04.095Z Stop hook feedback: [~/.claude/stop-hook-git-check.sh]: Ther
9ac91d3b 2026-10-02T06:54:33.578Z 対話を終えてください。
Shell cwd was reset to /home/user
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime && for k in buscemi2012 matsumoto2010 jencova2016 buscemi2016 kahn2009 oreshkov2012 araujo2015 oreshkov2016 guta2006; do printf "%s:%s " $k $(grep -c "{$k," references.bib); done; echo; grep -n "^| \(case\|causal\|process\|quantum\|state\|statistical\|local\)" glossary.md | cut -c1-50; sed -n 251p framework.md | cut -c1-80
```

</details>

<details><summary>結果: Bash</summary>

```text
buscemi2012:0 matsumoto2010:0 jencova2016:0 buscemi2016:0 kahn2009:0 oreshkov2012:0 araujo2015:0 oreshkov2016:0 guta2006:0 
14:| causal coverage | 因果被覆 | 順序付き
15:| causal hull | 因果的な包 | 集合 S の�
16:| causal site | 因果サイト | Christensen�
55:| local tomography | 局所トモグラフィ�
56:| locale | ロケール | フレームの圏の
57:| localic cones | 局所的な錐 | 順序付�
58:| locality | 局所性 | 局在したものど�
59:| localization | 局在 | 観測量・状態・
83:| process tensor | process tensor | 系に施�
88:| quantum Bayes rule | 量子ベイズ則 | 交
89:| quantum comb | 量子コム | 量子回路を
90:| quantum de Finetti theorem | 量子 de Finett
91:| quantum reference frame | 量子参照系 | �
92:| quantum strategy | 量子戦略 | 多ラウ�
- 量子的な観測と古典的な観測の両方と、その混成を「実験
```

</details>

<details><summary>ツール: Bash</summary>

```text
cat >> references.bib <<'EOF'

@article{buscemi2012,
  author  = {Buscemi, Francesco},
  title   = {Comparison of quantum statistical models: equivalent conditions for sufficiency},
  journal = {Communications in Mathematical Physics},
  volume  = {310},
  pages   = {625--647},
  year    = {2012},
  doi     = {10.1007/s00220-012-1421-3},
  eprint  = {1004.3794},
}

@misc{matsumoto2010,
  author  = {Matsumoto, Keiji},
  title   = {A quantum version of randomization criterion},
  year    = {2010},
  eprint  = {1012.2650},
  note    = {arXiv:1012.2650},
}

@misc{jencova2016,
  author  = {Jen{\v{c}}ov{\'a}, Anna},
  title   = {Comparison of quantum channels and statistical experiments},
  year    = {2016},
  eprint  = {1512.07016},
  note    = {arXiv:1512.07016},
}

@article{buscemi2016,
  author  = {Buscemi, Francesco},
  title   = {Degradable channels, less noisy channels, and quantum statistical morphisms: an equivalence relation},
  journal = {Problems of Information Transmission},
  volume  = {52},
  number  = {3},
  pages   = {201--213},
  year    = {2016},
  eprint  = {1511.08893},
}

@article{kahn2009,
  author  = {Kahn, Jonas and Gu{\c{t}}{\u{a}}, M{\u{a}}d{\u{a}}lin},
  title   = {Local asymptotic normality for finite dimensional quantum systems},
  journal = {Communications in Mathematical Physics},
  volume  = {289},
  pages   = {597--652},
  year    = {2009},
  doi     = {10.1007/s00220-009-0787-3},
  eprint  = {0804.3876},
}

@article{oreshkov2012,
  author  = {Ores
…（以下 1055 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>ツール: Bash</summary>

```text
for id in 1506.03776 1511.08893 1512.07016 1012.2650 1105.4464; do printf "%s | " $id; curl -sS -m 20 "https://arxiv.org/abs/$id" | grep -o -E 'class="tablecell jref">[^<]*|citation_doi" content="[^"]*|href="https://doi.org/[^"]*' | head -3 | tr '\n' ';'; echo; done
```

</details>

<details><summary>結果: Bash</summary>

```text
1506.03776 | citation_doi" content="10.1088/1367-2630/17/10/102001;href="https://doi.org/10.48550/arXiv.1506.03776;class="tablecell jref">New J. Phys. 17 (2015) 102001;
1511.08893 | citation_doi" content="10.1134/S0032946016030017;href="https://doi.org/10.48550/arXiv.1511.08893;class="tablecell jref">Problems of Information Transmission, volume 53, issue 3, pages 201-213 (October 2016);
1512.07016 | href="https://doi.org/10.48550/arXiv.1512.07016;
1012.2650 | href="https://doi.org/10.48550/arXiv.1012.2650;
1105.4464 | citation_doi" content="10.1038/ncomms2076;href="https://doi.org/10.48550/arXiv.1105.4464;class="tablecell jref">Nature Communications 3, 1092 (2012);
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='references.bib'; s=open(p).read()
a="  pages   = {201--213},\n  year    = {2016},\n  eprint  = {1511.08893},\n"
assert s.count(a)==1
s=s.replace(a,"  pages   = {201--213},\n  year    = {2016},\n  doi     = {10.1134/S0032946016030017},\n  eprint  = {1511.08893},\n  note    = {arXiv の書誌情報は volume 53 とするが、DOI に合わせて 52 とした},\n")
open(p,'w').write(s)
EOF
grep -A12 "{buscemi2016," references.bib | head -13
```

</details>

<details><summary>結果: Bash</summary>

```text
@article{buscemi2016,
  author  = {Buscemi, Francesco},
  title   = {Degradable channels, less noisy channels, and quantum statistical morphisms: an equivalence relation},
  journal = {Problems of Information Transmission},
  volume  = {52},
  number  = {3},
  pages   = {201--213},
  year    = {2016},
  doi     = {10.1134/S0032946016030017},
  eprint  = {1511.08893},
  note    = {arXiv の書誌情報は volume 53 とするが、DOI に合わせて 52 とした},
}
```

</details>

<details><summary>ツール: Bash</summary>

```text
cd /home/user/point-free-spacetime-private && sed -i 's/Probl. Inf. Transm. 53, 201）/Probl. Inf. Transm. 52, 201。arXiv の書誌情報は 53 とするが DOI に合わせた）/' papers/README.md && grep -c "Transm. 52" papers/README.md; cd ../point-free-spacetime && python3 - <<'EOF'
SV="surveys/2026-10-02_24_quantum-comparison-and-causal-order.md"
rows={
"| causal coverage":("before",f"| causal (non)separability | 因果的（非）分離性 | 過程行列（局所的な量子操作の確率を与える双線形の対象）が、因果順序の決まった過程の凸結合で書けること（2 者：$`W = q W^{{B ≼ A}} + (1 - q) W^{{A ≼ B}}`$。Oreshkov–Costa–Brukner 2012）。3 者以上では、前の操作の結果に応じて後の順序が変わる場合を含む、再帰的な分解で定める（Oreshkov–Giarmatzi 2016）。過程の水準の性質で、相関の水準の因果性（因果不等式）とは別である。量子スイッチは、因果的に非分離だが、因果不等式を破らない（Araújo ほか 2015）。 | [第 24 回の調査メモ]({SV}) |"),
"| process tensor":("before",f"| process matrix | 過程行列 | 各当事者の操作が量子の instrument で表されるとだけ仮定して、結果の同時確率を Choi 行列の双線形の式 $`P = \\mathrm{{Tr}}[W (M^A ⊗ M^B)]`$ で与える正の行列 $`W`$。量子コムの条件の一部を満たすが、因果順序の条件は課さない（Oreshkov–Costa–Brukner 2012）。 | [第 24 回の調査メモ]({SV}) |"),
"| quantum reference frame":("after",None),
}
p='glossary.md'; L=open(p).read().split('\n')
def ins(anchor,row,where):
    i=[k for k,l in enumerate(L) if l.startswith(anchor)][0]
    L.insert(i if where=='before' else i+1,row)
for a,(w,r) in rows.items():
    if r: ins(a,r,w)
ins("| quantum de Finetti theorem",f"| quantum local asymptotic normality | 量子局所漸近正規性（量子 LAN） | $`n`$ 個の同じ有限次元の系の状態 $`ρ^{{⊗n}}`$ のモデルが、局所的なパラメータの範囲で、古典的なガウス分布と量子的なガウス状態の積のモデルに、量子の Le Cam 距離の意味で収束すること（Kahn–Guţă 2009。CPTP チャネルで互いに近似する）。 | [第 24 回の調査メモ]({SV}) |","bef
…（以下 385 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
1
+| causal (non)separability | 因果的�
+| process matrix | 過程行列 | 各�
+| quantum local asymptotic normality | 
+| statistical morphism | 統計的射 |
```

</details>

## Claude

用語一覧に 4 語を加えました。「量子局所漸近正規性」の並び位置が、アルファベット順からずれていたので直します。

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='glossary.md'; L=open(p).read().split('\n')
i=[k for k,l in enumerate(L) if l.startswith('| quantum local asymptotic')][0]; r=L.pop(i)
j=[k for k,l in enumerate(L) if l.startswith('| quantum reference frame')][0]; L.insert(j,r)
open(p,'w').write('\n'.join(L))
EOF
grep -n "^| quantum\|^| statistical\|^| superse\|^| causal\|^| process" glossary.md | cut -c1-45
```

</details>

<details><summary>結果: Bash</summary>

```text
14:| causal (non)separability | 因果的（�
15:| causal coverage | 因果被覆 | 順序�
16:| causal hull | 因果的な包 | 集合 S
17:| causal site | 因果サイト | Christen
84:| process matrix | 過程行列 | 各当�
85:| process tensor | process tensor | 系に
90:| quantum Bayes rule | 量子ベイズ則 
91:| quantum comb | 量子コム | 量子回�
92:| quantum de Finetti theorem | 量子 de F
93:| quantum local asymptotic normality | 量
94:| quantum reference frame | 量子参照�
95:| quantum strategy | 量子戦略 | 多ラ
107:| statistical morphism | 統計的射 | �
108:| superselection rule | 超選択則 | �
```

</details>

## Claude

Now framework.md, the summary, and NEXT.md.

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
import re
SV="surveys/2026-10-02_24_quantum-comparison-and-causal-order.md"
p='framework.md'; s=open(p).read()
s=re.sub(r"最終更新: [^\n]*","最終更新: 2026-10-02（第 24 回。T-0019 を完了し、量子統計的実験・チャネルの比較と因果的非分離性の見立てを未解決の論点に加えた）",s,count=1)
a="(a) の中でも、較正（[D-0013](definitions/D-0013.md)）を決定的・確率的・事象ごとに位置を定めない、のどの段階まで許すかという論点が残る。"
assert s.count(a)==1
s=s.replace(a,a+f"第 24 回の見立て（[調査メモ]({SV})の 3・4 節）：装置・チャネルの比較の順序は、許す判定・操作の類で決まる（古典的な判定だけなら統計的射の水準、補助系との合成を許せば CPTP の水準。どちらも古典的な記録の確率で比べる）。因果的非分離性は、相関の水準（装置に依存しない）と過程の水準（量子的な操作を信頼する）を分けて扱う。T-0019 は第 24 回に完了し、(a)・(b) と較正の段階の判断は次に行う。")
open(p,'w').write(s)
EOF
grep -c "第 24 回の見立て" framework.md
```

</details>

<details><summary>結果: Bash</summary>

```text
1
```

</details>

<details><summary>ツール: Write: /home/user/point-free-spacetime/summaries/2026-10-02_24_quantum-comparison-and-causal-order.md</summary>

```text
（入力の本文は省略。項目: content, file_path）
```

</details>

<details><summary>結果: Write: /home/user/point-free-spacetime/summaries/2026-10-02_24_quantum-comparison-and-causal-order.md</summary>

```text
File created successfully at: /home/user/point-free-spacetime/summaries/2026-10-02_24_quantum-comparison-and-causal-order.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>ツール: Bash</summary>

```text
python3 - <<'EOF'
p='NEXT.md'; s=open(p).read()
s=s.replace("最終更新: 2026-10-02（第 23 回セッションの後）","最終更新: 2026-10-02（第 24 回セッションの後）")
i=s.index("- 第 23 回：T-0019 の続き。"); j=s.index("\n",i)
s=s[:j]+"\n- 第 24 回：T-0019 の項目 2（Le Cam の理論の量子版）と、因果的非分離性を、arXiv 版の原典 8 件で確かめた。ユーザーの判断で、群 A（状態の族の比較）と群 B（チャネル・装置の比較）の対比に重点を置いた。見立てとして、比較の順序は許す判定・操作の類で決まる（古典的な判定だけなら統計的射の水準、補助系との合成を許せば CPTP の水準）、因果的非分離性は相関の水準と過程の水準を分けて扱う、とした。T-0019 を完了にした（[まとめ](summaries/2026-10-02_24_quantum-comparison-and-causal-order.md)、[調査メモ](surveys/2026-10-02_24_quantum-comparison-and-causal-order.md)）。"+s[j:]
a=s.index("## 次のタスク"); b=s.index("## ユーザーにお願いしていること")
s=s[:a]+"""## 次のタスク

次のセッション（第 25 回の予定）では、まず **T-0019 の結果を踏まえた判断**をユーザーと行い、その後 [`roadmap.md`](roadmap.md) の段階 B（**T-0004** から。T-0004〜T-0007）に進む（[`CLAUDE.md`](CLAUDE.md) の「セッションの進め方」）。その後の順序、長期のタスク、未解決の論点は `roadmap.md` にある。

- ユーザーが判断すること（手がかりは、`roadmap.md` の「T-0019」の節と、第 22〜24 回の調査メモ）：
  1. 「量子的な観測」を、(a) 量子系を測った古典的な記録（今の立場）と読むか、(b) 古典的な記録へ読み出す前の量子的な出力も実験の対象に含めると読むか。(b) が要るかは、許す後続の操作の類 $`𝒯`$ を指定して判断する（[第 22 回の調査メモ](surveys/2026-10-01_22_combs-and-composites.md)の 3 節、[第 23 回の調査メモ](surveys/2026-10-02_23_quantum-clocks-and-frames.md)の 3.1 節）。
  2. (a) の中で、較正（[D-0013](definitions/D-0013.md)）を、決定的・確率的・事象ごとに位置を定めない、のどの段階まで許すか（第 23 回の調査メモの 3.2 節、[第 24 回の調査メモ](surveys/2026-10-02_24_quantum-comparison-and-causal-order.md)の 4 節）。
  3. 可能な実験に、補助系と合成した実験を含めるか（第 24 回の調査メモの 3.2 節。装置の比較の細かさと、求める因果性の水準が変わる）。
- 判断がセッションの一部で済むなら、続けて T-0004 に入るかをユーザーと相談する（1 セッション 1 タスクの原則に従い、判断だけで 1 回と
…（以下 193 文字を省略）
```

</details>

<details><summary>結果: Bash</summary>

```text
35 passed in 0.50s
```

</details>

## Claude

テストはすべて通りました。最後に対話ログを書き出し、論文の本文の抜粋を要約への参照に置き換えます。

<details><summary>ツール: Bash</summary>

```text
L=logs/2026-10-02_24_quantum-comparison-and-causal-order.md && python3 tools/export_log.py ~/.claude/projects/-home-user/[ID].jsonl $L --title "2026-10-02 第 24 回: 量子統計的実験・チャネルの比較と因果的非分離性" --since 2026-10-02T03:35:00Z --redact-file ../point-free-spacetime-private/redactions.txt && python3 - <<'EOF'
import re
p='logs/2026-10-02_24_quantum-comparison-and-causal-order.md'; s=open(p).read()
NOTE='（論文の本文の抜粋。著作権に配慮して省略した。確かめた内容は、調査メモ surveys/2026-10-02_24_quantum-comparison-and-causal-order.md の 2 節に要約している）'
keys=['buscemi2012','matsumoto2010','jencova2016','buscemi2016','kahn2009','oreshkov2012','araujo2015','oreshkov2016']
pat=re.compile(r'(<details><summary>ツール: Bash</summary>\n\n(`{3,})text\n)(.*?)(\n\2\n\n</details>\n\n<details><summary>結果: Bash[^<]*</summary>\n\n)(`{3,})text\n(.*?)\n\5\n', re.S)
n=0
def rep(m):
    global n
    if any(k+'.' in m.group(3) for k in keys) and any(w in m.group(3) for w in ('sed -n','grep','awk')):
        n+=1; return m.group(1)+m.group(3)+m.group(4)+m.group(5)+'text\n'+NOTE+'\n'+m.group(5)+'\n'
    return m.group(0)
s=pat.sub(rep,s)
pat2=re.compile(r'(<details><summary>結果: Bash[^<]*</summary>\n\n)(`{3,})text\n(.*?)\n\2\n', re.S)
def rep2(m):
    global n
    b=m.group(3)
    if NOTE in b: return m.group(0)
    eng=sum(1 for l in b.split('\n') if re.search(r'[a-z]+ [a-z]+ [a-z]+ [a-z]+', l))
    if eng>=8: n+=1; return m.group(1)+m.group(2)+'text\n'+NOTE+'\n'+m.group(2)+'\n'
    return m.group(0)
s=pat2.sub(rep2,s);
…（以下 323 文字を省略）
```

</details>
