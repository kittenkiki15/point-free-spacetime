# 2026-09-29 第 15 回: QBism の先行研究（主体の間の一致）

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> 個人情報などは伏せ字にしています。ツールの呼び出しは要約の 1 行だけを残し、その中身と結果は、他者の文章の長い引用を避けるため、第 32 回に公開側から除きました（T-0027）。

## ユーザー

次のセッションを開始してください。

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

## Claude

第 15 回を始めます。PR #29 はマージ済みだったので、作業ブランチ `claude/zealous-keller-o7r1sv` を最新の `main` から作り直しました。今回扱うのは、[`NEXT.md`](point-free-spacetime/NEXT.md) の先頭のタスク、**T-0003「QBism の先行研究の調査」**です。

#### 最初の文献の確認（arXiv の要旨と書誌のみ。本文は未読）

| 文献 | 要旨から分かること |
| --- | --- |
| Caves–Fuchs–Schack 2002a（J. Math. Phys. 43, 4537） | 量子 de Finetti 定理（quantum de Finetti theorem）の初等的な証明。交換可能（exchangeable）な密度作用素の割り当てによって、トモグラフィーでいう「未知の量子状態」に操作的な定義を与える。実ヒルベルト空間では成り立たない |
| Caves–Fuchs–Schack 2002b（PRA 65, 022305） | 量子確率をベイズ確率として読む。量子状態トモグラフィーをベイズ推定として定式化する |
| Fuchs–Schack–Scudo 2004、Fuchs–Schack 2004 | 量子操作（プロセス）版の de Finetti 定理 |
| Caves–Fuchs–Schack 2007 | 確率 1 の予測も主体の信念による |
| Fuchs–Schack 2013（RMP 85, 1693） | ボルン則を、ダッチブックの整合性（Dutch-book coherence）に加わる規範的な規則として読む。SIC 測定（SIC measurement）を基準の測定とする |
| Fuchs–Mermin–Schack 2014（Am. J. Phys.） | QBism の入門。量子論の「非局所性」を解消する |
| Fuchs–Stacey 2019、Fuchs 2010 | 総説 |
| Timpson 2008 | 哲学からの批判的な検討（独我論という批判、説明の問題、主観的確率だけで足りるか） |
| Leifer–Spekkens 2013、Parzygnat–Russo 2022 | 量子の条件付き状態と、非可換なベイズの逆。第 14 回のマルコフ圏につながる |
| Blume-Kohout 2010 | ベイズ平均による状態推定（実務的な比較の対象） |

#### 比較の見立て（Claude の見立て。未検証）

1. **一致の扱い**：QBism では、確率や量子状態を個々の主体の信念とする。主体の間の一致は公理ではなく、量子 de Finetti 定理の下で、交換可能性を仮定した事後分布が近づく結果として現れる（記憶による。本文で確認が要る）。本プロジェクトの A-0007 は、一致の前提条件を前提として課している。
2. **推定の対象**：QBism の量子 de Finetti 定理は「未知の状態」を扱う。C-0003（統計の関数の推定と状態の推定の対応）のうち、状態の側の推定に当たる。本プロジェクトの統計の関数の推定は、SIC 表現（状態を、基準の測定の確率で表すもの）に近い。
3. **交換可能性**：第 09 回に「連続性と交換可能性は独立した条件」と訂正した点が、量子 de Finetti 定理の仮定と直接つながる。

#### 相談したいこと

進め方を決めたいので、次の 2 点を教えてください。

- **深さ**：第 14 回と同じく「要旨による確認と対応表まで」にしますか。それとも、中心の 2〜3 本（例: Caves–Fuchs–Schack 2002a・2002b、Fuchs–Schack 2013）の本文を読んで、定理の仮定と結論まで確かめますか。
- **重点**：次のどれを主軸にしますか。
  - (a) 主体の間の一致：A-0007 と、量子 de Finetti 定理の比較
  - (b) 推定の対象：C-0003 と、トモグラフィーや SIC 表現の比較
  - (c) 立場の違い：個人の信念か、主体の間の一致か（Timpson の批判も含む哲学的な比較）
  - (d) 第 14 回の圏論的な概観とのつながり（非可換なベイズの逆）

（ツール: ReadNotifications）

（ツール: ToolSearch: select:mcp__github__pull_request_read）

（ツール: mcp__github__pull_request_read）

## Claude

PR [kittenkiki15/point-free-spacetime#29](https://github.com/kittenkiki15/point-free-spacetime/pull/29) はマージ済みでした（21:41 UTC）。第 14 回はこれで終わりです。PR の通知の購読は自動で止まり、定期確認の予定も残っていません。

第 14 回の成果は次のとおりです。
- **調査メモと対応表**：フレームワークの各層を、圏論の言葉（対象・射・関手）で見直した対応表を作りました。
  - 骨組みは、マルコフ圏（層 1〜2）と、随伴の不動点としての整合条件（層 3〜5）です。
  - 状態の扱いは、モデル全体の圏としました。
- **文献の確認**：マルコフ圏の文献（Fritz ほか）、局所共変性、Bohr トポス、具体的な双対性を、要旨と書誌で確かめました。
- **候補**：定義と予想の候補は登録せず、ロードマップの T-0005・T-0006・T-0008・T-0009 に扱い先を記録しました。

次の第 15 回は、ロードマップの T-0003「QBism の先行研究の調査」です。`/clear` の後は、いつもどおり「次のセッションを開始してください」とだけ伝えていただければ始められます。

## ユーザー

「深さ」について、中心の 2〜3 本（例: Caves–Fuchs–Schack 2002a・2002b、Fuchs–Schack 2013）の本文を読んで、定理の仮定と結論まで確かめたいです。「重点」について、「(a) 主体の間の一致」に重点を置き、他は今後の調査対象として残しておいてください。

## Claude

第 15 回の冒頭で私が出した提案（「深さ」と「重点」の選択肢）を、セッション記録で確認します。

（ツール: Bash: Read session 15 dialogue so far）

（ツール: Bash: Check branch and download three papers）

（ツール: Bash: Rename PDFs to citation keys and extract text）

（ツール: Bash: Read CFS 2002a intro and classical theorem）

（ツール: Bash: Read CFS 2002a sections II-III）

## ユーザー

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   - The project (`/home/user/point-free-spacetime`, public; `/home/user/point-free-spacetime-private`, private) proceeds by sessions per CLAUDE.md: 1 session = 1 task from NEXT.md, dialogue in Japanese, at end: export log, write summary, update related files (glossary, symbols, references.bib, framework.md, roadmap.md, NEXT.md), commit (Japanese message, trailer lines), push branch `claude/zealous-keller-o7r1sv`, create PR to main, handle CI and cross-model review (gpt-6-sol) until merge; the user decides merge.
   - Sessions 11–14 are complete and merged (PR #24, #27, #28, #29).
   - Current: 第 15 回, task T-0003「QBism の先行研究の調査」. User's latest instruction (verbatim): 「深さ」について、中心の 2〜3 本（例: Caves–Fuchs–Schack 2002a・2002b、Fuchs–Schack 2013）の本文を読んで、定理の仮定と結論まで確かめたいです。「重点」について、「(a) 主体の間の一致」に重点を置き、他は今後の調査対象として残しておいてください。
   - (a) = 主体の間の一致：A-0007（予測分布の相互絶対連続性, Blackwell–Dubins）と量子 de Finetti 定理の比較. Others to leave as future: (b) 推定の対象 (C-0003 vs tomography/SIC), (c) 立場の違い (Timpson の批判等), (d) 第 14 回の圏論的概観とのつながり (非可換ベイズの逆: Leifer–Spekkens 2013, Parzygnat–Russo 2022).

2. Key Technical Concepts:
   - QBism, quantum de Finetti representation theorem (Hudson–Moody 1976; CFS elementary proof), exchangeability (symmetric + infinitely extendible), quantum Bayes rule, quantum-state tomography reinterpreted, agreement of future predictions, informationally complete / "sufficiently informative" measurements, POVM, real Hilbert spaces failure, Dutch-book coherence, SIC measurement (Fuchs–Schack 2013).
   - Project: A-0007 (mutual absolute continuity of predictive distributions), D-0005 (actual observable, posterior limits), C-0003, Blackwell–Dubins; distinction between posterior predictive agreement vs model-posterior agreement (from PR #29 review).
   - Earlier sessions: Markov categories, dual adjunction fixed points, D-0003 (X = ⨆ X_π, M_O = ℝ^{1+n}, d_O norm metric), D-0011 (occ_rec/occ_mod), C-0001/C-0007/C-0008, A-0009, A-0010, target-ID column, roadmap tasks T-0001..T-0015.

3. Files and Code Sections:
   - Private repo PDFs (new, not yet committed): `/home/user/point-free-spacetime-private/papers/caves2002definetti.pdf` (arXiv quant-ph/0104088), `caves2002bayes.pdf` (quant-ph/0106133), `fuchs2013.pdf` (arXiv:0906.2187). Citation keys intended to match public references.bib (keys to add: caves2002definetti, caves2002bayes, fuchs2013 — verify not already present).
   - Extracted text in scratchpad: `/tmp/claude-0/-home-user/[ID]/scratchpad/caves2002definetti.txt` (1483 lines; read 1–700), `caves2002bayes.txt` (419 lines; unread), `fuchs2013.txt` (3418 lines; unread).
   - Findings from CFS 2002a (Caves–Fuchs–Schack, "Unknown quantum states: the quantum de Finetti representation", J. Math. Phys. 43, 4537 (2002)):
     - Classical exchangeability: symmetric (Eq. 2.2) + extendible for any M (2.3) ⇒ unique representation p(x1..xN)=∫_{S_k}P(p) p_{x1}…p_{xN} dp (2.4), discrete k-valued; counterexample symmetric not exchangeable p(0,1)=p(1,0)=1/2.
     - Quantum: ρ^(N) symmetric (3.11–3.12) and exchangeable if for every M a symmetric ρ^(N+M) with tr_M ρ^(N+M)=ρ^(N) (3.13) ⇒ unique ρ^(N)=∫_{D_d}P(ρ)ρ^{⊗N}dρ (3.15–3.16), finite dimension d; extendibility excludes entanglement (GHZ example); fails on real Hilbert spaces.
     - Agreement (Intro, cites ref [40], likely CFS 2002b): two observers with exchangeable assignments and priors that never vanish (nonzero in a neighborhood of ρ_DK); quantum Bayes rule P(ρ|D_K)=P(D_K|ρ)P(ρ)/P(D_K) (1.3); for sufficiently informative measurements, as K→large, posterior peaks at ρ_DK regardless of prior; ∫P_i(ρ|D_K)ρ^{⊗N}dρ → ρ_DK^{⊗N} independent of i (1.4); tomography = observers coming to agreement on future predictions. This is stated informally in the intro — needs checking in CFS 2002b for precise hypotheses.
   - To be created: survey memo (e.g., `surveys/2026-09-29_15_qbism.md`, format per surveys/README.md, no long quotes), summary `summaries/2026-09-29_15_<topic>.md`, log `logs/2026-09-29_15_<topic>.md` (export with `--since 2026-09-29T21:45:42.469Z`), updates to references.bib, glossary.md, roadmap.md (T-0003 状態, future items (b)(c)(d)), NEXT.md (next T-0004), possibly framework.md, A-0007 notes.
   - Export command pattern: `python3 tools/export_log.py /root/.claude/projects/-home-user/[ID].jsonl logs/<file>.md --title "..." --redact-file ../point-free-spacetime-private/redactions.txt --since <ts>`; check `grep -v -e '^#' -e '^$' ../point-free-spacetime-private/redactions.txt | grep -iFcf - <log>` = 0.
   - Tests: `python3 -m pytest -q tools/tests` (33 tests), `python3 tools/deps_graph.py --check`.

4. Errors and fixes:
   - Context loss after /clear or compaction: user answered questions I couldn't see; fixed by reading the jsonl transcript with python to recover my earlier proposal (sessions 12, 14, 15).
   - Review-loop issues in PRs handled by fixing errors, recording detailing points in unresolved sections, and avoiding extra pushes when points were covered by existing items.
   - Stop hook requires pushing unpushed commits; used `git push -q -u origin claude/zealous-keller-o7r1sv` (force once when branch reset to main).

5. Problem Solving:
   - For session 15 the comparison thesis so far: CFS agreement requires exchangeability + prior positivity near the peak + informationally complete measurements, concluding convergence of posterior predictive (future-system states); A-0007 instead assumes mutual absolute continuity of predictive distributions (Blackwell–Dubins style) without exchangeability; A-0006 continuity ≠ exchangeability (noted in session 09). Need precise statements from CFS 2002b and Fuchs–Schack 2013.

6. All user messages (this conversation, user-role):
   - Session 11 start with handoff from session 10 (include PR #23 last comment D-0007 point).
   - AskUserQuestion answers: 各ファイルに移す; 圏論的概観→QBism→段階B→C-0001検証 order; 「目標の ID」欄を新設; T-0001 形式4桁ID.
   - 「確認しました。問題ありません。このセッションの対話を終えたいと思います。」
   - Session 12: 「C-0001 は、ご提案の方法で分割してください。…まずは候補 A でお願いします。」; priorities ok, re-evaluate all priorities when starting verification, 3-way split ok, A-0009 作業上 until review completes and next session starts; 「ご提案どおり残りは移して、このセッションの対話を終えたいと思います。」
   - Between sessions: D-0003 未解決の点を先に解決する提案; D-0011 は可能な実験の定義で C-0002 に依存すべき; 「今の文脈のまま第 13 回として始めてください。」; occ(e) for possible experiments needed, otherwise proceed; 「この内容で問題ありません。対話をここで終えたいと思います。」; 「6 回目のクロスモデルレビューの結果が来ました。ご確認ください。」
   - Session 14: 「1. はお勧めに賛同します。2. は対応表と文献の確認までにしたいです。3. はモデル全体の圏を取りたいです。」; 「確認しました。対話を終えて、セッションの終え方の手順に進んでください。」
   - Session 15: 「次のセッションを開始してください。」; 「深さ」について、中心の 2〜3 本（例: Caves–Fuchs–Schack 2002a・2002b、Fuchs–Schack 2013）の本文を読んで、定理の仮定と結論まで確かめたいです。「重点」について、「(a) 主体の間の一致」に重点を置き、他は今後の調査対象として残しておいてください。
   - Standing constraints (CLAUDE.md): Japanese responses; don't put long quotes/PDFs of others' works in public repo (PDFs in private `papers/<key>.pdf`); don't write personal-info fragments in search commands (use redactions.txt); never push to main directly; priority of conjectures decided with user; merge decided by user.

7. Pending Tasks:
   - Finish reading CFS 2002b (caves2002bayes.txt) and relevant parts of Fuchs–Schack 2013 (fuchs2013.txt), plus rest of CFS 2002a if needed, focusing on agreement hypotheses/conclusions.
   - Write survey memo for (a), recording (b)(c)(d) as future survey targets; add bib entries; glossary entries; commit PDFs in private repo; present milestone to user; then (when user ends) session-end procedure and PR, handle reviews.

8. Current Work:
   Reading the full text of CFS 2002a (done through line 700: sections I–III and start of IV) in scratchpad, extracting the exact definitions of exchangeability, the quantum de Finetti theorem statement (Eq. 3.15), and the informal agreement claim (Eqs. 1.3–1.4, citing [40]). Next files to read: caves2002bayes.txt and fuchs2013.txt.

9. Optional Next Step:
   Continue per the user's instruction「中心の 2〜3 本（例: Caves–Fuchs–Schack 2002a・2002b、Fuchs–Schack 2013）の本文を読んで、定理の仮定と結論まで確かめたいです。「重点」について、「(a) 主体の間の一致」に重点」: read `/tmp/claude-0/-home-user/[ID]/scratchpad/caves2002bayes.txt` (the precise quantum Bayes rule / agreement theorem and its hypotheses such as informational completeness and prior support), then grep fuchs2013.txt for de Finetti / agreement / intersubjectivity / Dutch book sections, then draft the survey memo comparing with A-0007 and report to the user in Japanese.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /root/.claude/projects/-home-user/[ID].jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

（ツール: Read: /tmp/claude-0/-home-user/[ID]/scratchpad/caves2002bayes.txt）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

## Claude

論文の本文の読み取りを終え、プロジェクトの A-0007 との対応を確かめています。

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Write: /home/user/point-free-spacetime/surveys/2026-09-29_15_qbism-agreement.md）

（ツール: Bash）

（ツール: Edit: /home/user/point-free-spacetime/surveys/2026-09-29_15_qbism-agreement.md）

## Claude

中心の文献の本文を読み、定理の仮定と結論を確かめました。調査メモの草稿は `surveys/2026-09-29_15_qbism-agreement.md` にあります。

#### 読んだ文献

例に挙げていただいた 3 本に加えて、次の 2 本も読みました。PDF は非公開側の `papers/` に置いています（まだコミットしていません）。

- Schack–Brun–Caves 2001「Quantum Bayes rule」：2 本の CFS 論文が、一致の主張の根拠として引いている論文です。
- Fuchs–Schack 2009「Priors in quantum Bayesian inference」：Fuchs–Schack 2013 が、一致しない例として引いている論文です。

#### 確かめたこと

1. **量子 de Finetti 定理（CFS 2002a）**
   - 仮定：有限次元の複素ヒルベルト空間で、状態が置換で不変であり、任意の個数の系へ置換不変のまま拡張できること（交換可能性）。
   - 結論：状態は $`\int P(ρ)\, ρ^{⊗N} dρ`$ の形にただ一通りに書けます。
   - 証明：情報的に完全な POVM を使って、古典の de Finetti 定理に帰着させます。
2. **量子ベイズ則（Schack–Brun–Caves 2001）**：事前の状態が交換可能なら、古典のベイズ則と同じ形の更新則が成り立ちます。これは証明付きの定理です。
3. **主体の間の一致**
   - 主張：交換可能性、情報的に完全な測定、事前分布が「データの指す状態の近傍で 0 でない」ことを仮定すると、将来の割り当てが一致する、というものです。
   - この主張には、読んだ 5 本のどれにも証明がなく、収束の意味（どの確率で、どの位相で）も正確には書かれていません。
   - Claude の見立てでは、古典の事後一致性（Doob・Schwartz 型）を当てはめたものと読めます。ただし原典では確かめていません。
4. **一致しない例**
   - $`σ_z`$ だけを測ると、$`σ_x`$ の予測には事前分布への依存が残ります（Schack–Brun–Caves 2001）。
   - 1 点に集中した事前分布、反帰納的な事前分布、2 系ずつの組を単位とする交換可能な事前分布では、同じ無限のデータから異なる結論になります（Fuchs–Schack 2009）。
   - Fuchs–Schack 2013 自体には一致の定理はありません。この 2009 年の例を引いて、「データだけでは状態は決まらない」と強調しています。

#### A-0007 との比較（Claude の補足）

- 交換可能で、測定が情報的に完全な場合は、「予測分布が互いに絶対連続」（A-0007）と「事前分布が互いに絶対連続」は同値になります。
- Fuchs–Schack 2009 の例は、どれも予測分布が互いに特異です。A-0007 は、ちょうどこれらの例を除いています。
- QBism は交換可能性と情報的に完全な測定を課して、状態の一致まで得ています。A-0007 はそれらを課さず、データの予測の一致だけを得ます。状態の一致に必要な条件は、D-0005 の「識別可能性・集中の条件」に分けています。両者は矛盾しません。

(b)〜(d) は、メモの 5 節に今後の調査対象として残しました。

#### ご相談

メモの 3.3 節の候補を、どこまで反映するか決めていただけますか。

1. **A-0007 の「注意」への追記**：交換可能で情報的に完全な場合の同値と、反例が対象外であることを書き加えます。
2. **D-0005 への記録**：情報的に完全な測定が識別可能性を与える先行例として、D-0005 に記録します。
3. **ロードマップへの追加**：事後一致性の原典（Doob・Schwartz）と Blackwell–Dubins 1962 の確認を、タスクとして加えます。

Claude のお勧めは 1〜3 のすべてを行うことですが、いかがでしょうか。

（ツール: Bash）

## Claude

ここまでの作業を、それぞれの作業ブランチ `claude/zealous-keller-o7r1sv` にコミットして push しました。未コミットのファイルは残っていません。

- **非公開リポジトリ**：読んだ論文 5 本の PDF（`papers/` の下）
- **公開リポジトリ**：調査メモの草稿 `surveys/2026-09-29_15_qbism-agreement.md`

PR はまだ作っていません。セッションの終わりに、決まった手順で作ります。

先ほどのご相談への回答をお待ちしています。メモの 3.3 節の候補のうち、どれを反映するかです。

1. A-0007 の「注意」への追記
2. D-0005 への記録
3. 事後一致性の原典の確認を、ロードマップのタスクに加えること

Claude のお勧めは 3 件すべてです。

## ユーザー

お勧めの「1〜3 のすべてを行う」でお願いします。

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

## Claude

3 件ともすべて反映し、作業ブランチにコミットして push しました。テスト（33 件）と依存関係の図の検査は通っています。

1. **A-0007 の「注意」**に 2 点を書き加えました（Claude の補足として明記）。
   - 結果の列が交換可能で、測定が情報的に完全な場合は、この前提が「事前分布が互いに絶対連続」と同値になること。
   - QBism の文献で一致しない例として挙がるものは、どれも予測分布が互いに特異で、この前提の対象外であること。
2. **D-0005 の「注意」**に、QBism の先行例を記録しました。
   - 情報的に完全な測定が識別可能性を与え、測っていない観測量の予測まで主体の間で一致する、とされていること。この主張の証明は文献中にありません。
   - $`σ_z`$ だけを測る場合は、$`σ_x`$ の予測に事前分布への依存が残ること。
3. **ロードマップ**では、新しいタスクを作らず、文献の確認を扱う既存の T-0014 に次の確認を加えました。
   - 事後一致性の定理（Doob・Schwartz）と Blackwell–Dubins 1962 の原典で、QBism の一致の主張を正確な定理の形にすること。
   - 1 の同値の証明と、Hudson–Moody 1976 の仮定を確かめること。

A-0007 と D-0005 の「履歴」には第 15 回の変更を書き、調査メモの 3.3 節は「反映した内容」に書き換えました。

(a) 主体の間の一致の調査は、ここで一区切りです。この回の対話を終える場合は、お知らせいただければ、セッションの終え方の手順（ログ、まとめ、関連ファイルの更新、PR の作成）に進みます。

## ユーザー

圏論的な視点でのフレームワークの概観と、QBism の文献調査を行っていただきました。未確定事項や予想の解決方法を検討するにあたり、有用な情報は得られたでしょうか？ また、それらの検討に際して「穴」となっているような調査不足の研究領域はあるでしょうか？ 今後の調査対象の研究分野を検討したいです。

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

## Claude

#### 1. 得られた有用な情報

**圏論的な概観（第 14 回）**は、未確定の事項を「どの問題として解けばよいか」に言い換える点で役立ちました。

- **再構成と整合条件（C-0002、D-0003、D-0006、T-0009）**：循環に見えていた整合条件は、「随伴の不動点を求める問題」と言い換えられる見込みが立ちました。解くための型（二つの関手、単位と余単位、三角恒等式）もはっきりしました。
- **推定と極限（D-0005、A-0007、T-0005・T-0006）**：ベイズの逆、コルモゴロフ積、ド・フィネッティの定理が、そのまま使える道具として揃っていることが分かりました。
- **状態の扱い**：「モデル全体の圏」を取ることで、状態を固定するかどうかの論点が整理されました。

**QBism の調査（第 15 回）**は、推定と一致の部分を具体的にしました。

- **A-0007 の位置づけ**：交換可能で、測定が情報的に完全な場合は、事前分布が互いに絶対連続であることと同値になります。一致しない既知の例は、どれも A-0007 の対象外です。A-0007 が強すぎず弱すぎない条件であることの傍証になりました。
- **識別可能性の役割（D-0005、C-0003）**：「測っていない観測量まで一致するには、情報的に完全な測定（識別可能性）が要る」ことを、具体例（$`σ_z`$ だけの測定）で確かめられました。C-0003（統計の関数の推定と状態の推定の一致）の仮定が妥当な方向にあることも裏付けられます。

**得られなかったこと**もあります。

- **一致の定理の正確な形**：QBism の文献には証明がなく、古典統計の定理に戻る必要があります。
- **位相**：どちらの調査も「位相を何にするか」（T-0004、D-0005 の極限の位相）には答えていません。ここが最大の空白です。
- **時空の側**：C-0001、C-0007、C-0008（局在、装置の領域、長さの尺度）には、ほぼ寄与していません。

#### 2. 調査が不足している領域（「穴」）

これまでの参考文献を確かめたところ、次の領域はまだ扱っていません。文献名は記憶によるもので、未確認です。

| 優先の見立て | 領域 | 関係する項目 | 期待できること |
| --- | --- | --- | --- |
| 高 | **統計的実験の比較と収束の理論**（Le Cam の不足度・距離、Blackwell の実験の比較、Torgersen） | T-0004、D-0005、D-0003（模倣の順序） | 「実験の族の極限」に使える、既存の位相と距離。第 14 回の「模倣」の順序の正体もこれにあたる |
| 高 | **操作的な確率論の枠組み**（一般化確率論 GPT：Hardy、Barrett、Chiribella–D'Ariano–Perinotti。Ludwig の公理的な量子力学） | D-0001〜D-0005、C-0003、C-0005 | 本プロジェクトの「実験 → 統計」は GPT の設定そのもので、状態空間を操作から再構成する先行研究が多い。Ludwig は、有限な実験から一様構造で完備化する計画を持ち、T-0004 と D-0005 に直結する |
| 高 | **ベイズ統計の事後一致性**（Doob、Schwartz、Diaconis–Freedman の不一致の例、Ghosal–van der Vaart） | C-0006、D-0005、A-0007（T-0014 に一部） | C-0006（事後分布が点に集中しない）の反例と、正確な条件 |
| 中 | **時空の因果構造からの再構成**（Malament、Hawking–King–McCarthy の定理。因果集合は一部調査済み） | C-0002、D-0007、T-0009 | 「観測から時空を再構成する」ときに、何の情報があれば幾何が決まるか |
| 中 | **相対論的な局在の不可能性の定理**（Newton–Wigner、Hegerfeldt、Malament の局在の定理） | C-0007、C-0008、D-0008 | C-0008（ポアンカレ共変な装置の領域は有界にできない）に近い既存の定理がある可能性 |
| 中 | **操作的な座標づけと参照系**（レーダー座標、Bondi の k 計算、量子参照系） | A-0010、D-0003 の整合条件 | 較正の写像 $`τ^O`$ と、観測者の取り替えの定式化 |
| 低〜中 | **計算可能解析とアルゴリズム的ランダムネス**（Weihrauch、Martin-Löf） | C-0004、A-0002 | 計算可能性から連続性が従う話（C-0004）。「ほとんど確実に」をデータ列ごとの主張に言い換える手段にもなる |
| 低 | 既に残した QBism の論点 (b)〜(d)、非可換ベイズの逆 | C-0003、第 14 回の概観 | — |

#### 3. お勧めの方針

最大の穴は「位相と極限」です。これは T-0004 から T-0006 の中心で、次の段階 B に直結します。そのため、表の上の 3 つを優先するのがよいと考えます。

1. Le Cam の理論
2. GPT と Ludwig
3. 事後一致性

3 つを別々に扱うより、「実験の族の位相と極限」という一つの調査タスクにまとめ、段階 B（T-0004）の前か、並行して置く案をお勧めします。時空の側の 3 つ（因果構造、局在の定理、参照系）は、段階 C・D（T-0009 など）の前に、別の調査タスクとして置くのが自然です。

ロードマップにどう登録するか（まとめ方、順序、今回のセッションで記録するか）について、ご意見をお聞かせください。

## ユーザー

まとめ方と優先順序は、お勧めの案でよいと思います。今回のセッションで記録してください。

（ツール: Read: /home/user/point-free-spacetime/roadmap.md）

（ツール: Bash）

（ツール: Bash）

## Claude

ロードマップ（`roadmap.md`）に記録し、コミットして push しました。テストは通っています。

**進める順序**は次のとおりにしました。

```math
\text{T-0003} \;→\; \text{T-0016} \;→\; \text{段階 B（T-0004〜T-0007）} \;→\; \text{T-0017} \;→\; \text{T-0008} \;→\; \text{段階 C（T-0009）} \;→\; \text{段階 D（T-0010）}
```

**追加したタスク**（文献は記憶によるもので、未確認と明記しています）

- **T-0016 実験の族の位相と極限の先行研究の調査**（段階 B の前）：次の 3 つの領域をまとめました。
  - Le Cam の理論と実験の比較
  - 一般化確率論（GPT）と Ludwig の公理的な量子力学
  - ベイズ統計の事後一致性
- **T-0017 時空の側の先行研究の調査**：次の 3 つの領域をまとめました。
  - 因果構造からの時空の再構成
  - 相対論的な局在の不可能性の定理
  - 操作的な座標づけと参照系

**T-0017 の位置**は、前回は「段階 C・D の前」とご提案しましたが、段階 B の後、T-0008（C-0001・C-0007・C-0008 の検証）の前に置きました。局在の不可能性の定理は、C-0007・C-0008 の検証に使える見込みがあるためです。段階 C・D の前であることは変わりません。T-0009 の直前がよろしければ、入れ替えます。

**その他の記録**

- **T-0003**：状態を「完了（第 15 回）」にしました。結果の要約と、残した論点 (b)〜(d) を書いています。
- **優先度が低〜中の候補**：計算可能解析とアルゴリズム的ランダムネス、QBism の残した論点 (b)〜(d) は、「保留している事項」に調査の候補として残しました。

対話を終える場合は、お知らせください。セッションの終え方の手順に進みます。

## ユーザー

対話を終えて、セッションの終え方の手順に進んでください。

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

（ツール: Bash）

## Claude

セッションの終え方の手順を進めています（参考文献・用語・フレームワークを更新済み。次はまとめと NEXT.md）。

（ツール: Write: /home/user/point-free-spacetime/summaries/2026-09-29_15_qbism-agreement.md）

## Claude

Now NEXT.md.

（ツール: Bash）

（ツール: Bash）

## Claude

Now export the log.

（ツール: Bash）
