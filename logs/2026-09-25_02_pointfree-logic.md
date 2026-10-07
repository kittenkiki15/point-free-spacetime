# 2026-09-25 第 02 回: 点なし位相と論理・様相論理、先行研究の発見

> この記録は Claude Code のセッション記録から `tools/export_log.py` で自動変換したものです。
> 個人情報などは伏せ字にしています。ツールの呼び出しは要約の 1 行だけを残し、その中身と結果は、他者の文章の長い引用を避けるため、第 32 回に公開側から除きました（T-0027）。

## ユーザー

「6. 次にできること」でご提案いただいた順で進めてよいと思います。

一点質問です。点なし位相は論理学との関連が深いように思いますが、具体的にはどのような論理との関連になりますか？ また、量子論とのつながりは、背景として論理学とのつながりとも関連するのでしょうか？

## Claude

はい、その順で進めましょう。確認ですが、私の返答には「6. 次にできること」という見出しはなかったので、`NEXT.md` の「考察の出発点」の候補の順と理解しました。

1. 点なし位相の基礎
2. 既存研究の調査
3. 物理学で「点」が問題になる場面の洗い出し

違っていたら教えてください。以下、ご質問にお答えします。参考文献は記憶に基づいて挙げています。`references.bib` に登録するときに書誌情報を確認します。

#### 1. 点なし位相とつながる論理

**結論：主に直観主義論理（intuitionistic logic）と、幾何学的論理（geometric logic）です。**

##### (a) フレームは直観主義論理の代数

- フレームは、順序集合として見ると**完備ハイティング代数**（complete Heyting algebra）と同じものです。
- ハイティング代数は、直観主義命題論理の代数的な意味論です。ブール代数が古典論理の代数であるのと同じ関係です。
- 位相空間の開集合で読むと、次の対応になります。
  - 論理積 ∧ は共通部分 ∩、論理和 ∨ は合併 ∪ に対応します。
  - 否定 ¬U は「U の補集合の内部」です。
  - たとえば実数直線で U = (0, ∞) とすると、¬U = (−∞, 0) です。U ∪ ¬U は点 0 を含まないので、全体になりません。つまり**排中律が成り立ちません**。
- McKinsey–Tarski（1944 年ごろ）は、直観主義命題論理が位相空間の開集合による意味論に対して完全であることを示しました。

##### (b) 幾何学的論理：開集合は「観測で確かめられる命題」

- フレームの演算は、**有限個の論理積**と**任意個の論理和**です。
- これは「有限回の観測で確かめられる命題」の論理と一致します。
  - 有限個の観測をすべて行えば、有限個の論理積を確かめられます。
  - どれか一つが成り立つと確かめれば、無限個の論理和も確かめられます。
  - 無限個の論理積や否定は、有限回の観測では確かめられません。
- この見方は Vickers の *Topology via Logic*（1989）で体系的に展開されています。
- この見方では、ロケールは「命題的な幾何学的理論のモデルの空間」になり、ロケールの点は、その理論のモデル（すべての命題に一貫した真偽を割り当てる方法）に対応します。
  - 点を持たないのに自明でないロケールがあります。これは「矛盾はないのに、集合論的なモデルを持たない理論」に対応します。
  - たとえば「ℕ から ℝ への全射」の理論がそうです。そのような全射は存在しませんが、理論には矛盾がありません。
  - **「点がない」ことは、論理的には「無矛盾だがモデルがない」ことを意味します。**これが点なし位相の核心の一つです。

##### (c) ストーン双対性とトポス

- 論理と空間の対応は、次のような階層をなします（Stone 1936〜、Johnstone *Stone Spaces* 1982）。

| 論理側の代数 | 空間側 |
| --- | --- |
| ブール代数（古典論理） | ストーン空間 |
| 分配束 | スペクトル空間 |
| フレーム | ロケール（ソバー空間） |

- ロケール上の層はトポスをなします。トポスの内部論理は、高階の直観主義論理です。
- ロケールの理論は選択公理なしで展開できます。たとえばチコノフの定理のロケール版は選択公理を使いません。構成的数学との相性が良いのも、この論理との関係によります。

#### 2. 量子論とのつながりも、論理が背景にあるか

**結論：はい、論理が背景にあります。ただし、二つの異なる流れがあり、点なし位相と相性が良いのは後者です。**

##### (a) 古典的な「量子論理」：点なし位相とは緊張関係

- Birkhoff–von Neumann（1936）の量子論理では、命題はヒルベルト空間の閉部分空間で、それらは**オーソモジュラー束**をなします。
- この束は**分配律を満たしません**。一方、フレームの定義の核心は分配律です（前回 Lean で検証したものです）。
- したがって、伝統的な量子論理は、そのままでは点なし位相の枠組みに入りません。

##### (b) トポス的アプローチ：量子系の状態空間は「点のないロケール」

Isham–Butterfield（1998〜）、Döring–Isham（2008）、Heunen–Landsman–Spitters（2009、Bohrification）の流れです。

1. 量子系の可換部分代数（同時に測定できる観測量の組、つまり古典的な「文脈」）をすべて集め、包含関係で順序付けます。
2. その上の（前）層のトポスの中では、量子系が**内部的には可換な**C\*-代数に見えます。
3. 構成的なゲルファント双対性（Banaschewski–Mulvey、Coquand–Spitters）により、その「スペクトル」がトポスの中のロケールとして得られます。
4. **このロケールは一般に点を持ちません。これはコッヘン–シュペッカーの定理と同値です。**すべての観測量に矛盾なく値を割り当てる方法（隠れた変数による大域的な値付け）がないことが、「状態空間に点がない」ことに対応します。
5. このときの論理は、分配的な**直観主義論理**です。量子論理の非分配性は、文脈ごとの古典論理を貼り合わせる構造に置き換わります。

1(b) の「無矛盾だがモデルがない理論」と、ちょうど同じ形をしています。

##### (c) クォンタール：非可換な「点なし空間」

- Mulvey（1986）は、フレームの非可換版として**クォンタール**（quantale）を導入しました。
  - 交わり ∧ を、可換とは限らない積に置き換えたものです。
  - 非可換な C\*-代数のスペクトルを捉えようとする試みです。
- クォンタールは線形論理とも関係しています。Abramsky–Vickers（1993）は、観測の論理との関係を論じています。

#### このプロジェクトへの示唆

- 「開集合＝観測で確かめられる命題」という見方は、時空の点なし化に物理的な動機を与えます。有限の精度でしか位置を確かめられない、という考え方です。
- 量子論での「点がないこと＝コッヘン–シュペッカー」と、時空の「点がない」ことを同じ枠組みで扱えるかは、有望な問いに見えます。考察が進んだら、予想として立てる候補になりそうです。

最初のトピック「点なし位相の基礎」でも、この論理の観点（ハイティング代数、幾何学的論理、ストーン双対性）を軸に整理するのがよさそうです。今回出てきた用語（ハイティング代数、幾何学的論理、オーソモジュラー束、クォンタールなど）と文献は、このセッションの終わりに用語一覧と参考文献一覧に登録します。

## ユーザー

「6. 次にできること」について、あなたの出力を再掲します。

```
6. 次にできること
* この整理を surveys/（たとえば surveys/pointfree-topology-basics.md）と glossary.md に書き残し、基本文献を references.bib に登録する。候補は Johnstone『Stone Spaces』(1982)、Johnstone「The point of pointless topology」(1983)、Picado–Pultr『Frames and Locales』(2012)、Vickers『Topology via Logic』(1989) です。
* Lean で、Mathlib に何があるかを確かめる。Order.Frame や、TopologicalSpace.Opens がフレームであることなどがあるはずです。そのうえで、たとえば「完備ブール代数の点はアトムと対応する」を形式化してみる。
* 物理での「点」の問題（候補の 2）に進み、「時空の性質のうち、点がないと表せないものはあるか」を最初の予想の候補にする。
```


もう一点質問させてください。物理学における因果を論理で扱おうとすると、様相論理が必要になるように思うのですが、様相論理との相性がよいのは、上記の (a) (b) (c) のいずれでしょうか？ または直接は関係しないでしょうか？

## Claude

#### 「6. 次にできること」について

再掲ありがとうございます。この出力は、私の見えている会話の範囲にはありませんでした。私から見えない部分の会話での出力だと思われます。前回、別の候補と取り違えてしまい、失礼しました。

再掲いただいた順で進めます。

1. 基礎の整理を `surveys/` と `glossary.md` に書き残し、基本文献を `references.bib` に登録する。
2. Mathlib にあるものを確かめ、「完備ブール代数の点はアトムと対応する」を形式化する。
3. 物理学での「点」の問題に進み、最初の予想の候補を立てる。

#### 様相論理との相性

「上記の (a)(b)(c)」は、前回の論理側（1 の (a) ハイティング代数、(b) 幾何学的論理、(c) ストーン双対性とトポス）と、量子側（2 の (a)〜(c)）の両方に付けていたので、両方についてお答えします。

**結論：直接に関係します。最も相性が良いのは論理側の (a) と (c)、量子側では (b)（トポス的アプローチ）です。** さらに、因果構造は点なしの形で**時制論理**（tense logic、時間についての様相論理）として素直に書けます。

##### 1. 位相と様相論理はもともと一体

- **(a) ハイティング代数 ↔ S4**
  - McKinsey–Tarski は、様相論理 S4 の □ を「内部をとる操作」と読むと、S4 がちょうど位相空間の論理になることを示しました。
  - 直観主義論理は、ゲーデル–McKinsey–Tarski の翻訳で S4 に埋め込めます。「p が直観主義的に真」を「□p が真」と読む翻訳です。
  - つまり、開集合の論理（直観主義論理）は、もともと様相論理の一部分です。
- **(c) トポスでの様相**
  - フレーム上の**核**（nucleus）は、様相演算子 ○ の一種です。次の3つを満たし、「遅延論理」（lax logic）の様相にあたります。
    - p → ○p
    - ○○p → ○p
    - ○(p ∧ q) ↔ ○p ∧ ○q
  - 核は部分ロケールと一対一に対応し、トポスでは**ローヴェア–ティアニー位相**（Lawvere–Tierney topology）という名前で現れます。
  - 点なし位相には、様相が最初から内在しているといえます。
- **(c) ストーン双対性は様相論理の標準的な道具**
  - 様相論理の代数的な意味論（演算子付きブール代数）と、その空間側（関係付きストーン空間）の対応は、Jónsson–Tarski と Esakia による、ストーン双対性の拡張です。
- **(b) 幾何学的論理にも様相がある**
  - 点なし版のべき集合である**パワーロケール**（Vietoris ロケールなど）は、□ と ◇ に対応します。Abramsky の *Domain Theory in Logical Form*（1991）や、Vickers の仕事にあります。
  - ただし、因果とのつながりは (a)・(c) ほど直接的ではありません。

##### 2. 因果を点なしで扱う：時制論理として

- 普通の様相論理の意味論（クリプキ意味論）は、「点」と「点どうしの関係」を使います。
  - Goldblatt（1980）は、ミンコフスキー時空で因果関係（因果的未来にあること）を関係にとると、その様相論理が **S4.2** になることを示しました。
  - これは点に基づく結果です。
- 点なしで書くには、関係の代わりに**開集合に働く演算子**を使います。
  - 開集合 U に対して、その時間的未来 I⁺(U) も開集合です。したがって I⁺ は、フレームからフレームへの写像です。
  - I⁺ は任意個の合併を保ちます。I⁺(⋃ Uᵢ) = ⋃ I⁺(Uᵢ) です。これは ◇（「いつか未来で成り立ちうる」）の性質です。
  - 合併を保つ写像には、必ず右随伴があります。それが □ 型の演算子（「過去のすべてで成り立つ」）になります。
  - この「未来の ◇」と「過去の □」の随伴の組は、Prior の**時制論理**の構造（F ⊣ H、P ⊣ G）そのものです。
- まとめると、**因果構造は、フレームの上の随伴な様相演算子の組として、点を使わずに表せます**。
- 同じ方向の先行研究として、Christensen–Crane *Causal sites as quantum geometry*（2005）があります。点ではなく「領域」と、領域間の因果関係から出発して時空を組み立てる試みで、このプロジェクトに近いので調査の候補になります。

##### 3. 量子側

- **(b) トポス的アプローチ：最も相性が良い**
  - 文脈（可換部分代数）の順序集合の上の前層トポスでは、内部論理の意味論（クリプキ–ジョワイヤル意味論）が、文脈の順序を関係とするクリプキ意味論そのものになります。
  - 「より細かい文脈のすべてで成り立つ」という様相的な構造が、最初から組み込まれています。
  - Döring–Isham の daseinisation（命題を各文脈で近似する操作）も、随伴で定義される様相的な操作です。
- **(c) クォンタール**：線形論理の指数演算子 !・? は S4 型の様相です。ただし、因果との関係は間接的です。
- **(a) 伝統的な量子論理**：非分配の束の上の様相は扱いにくく、相性は良くありません。

#### このプロジェクトへの示唆（予想の候補）

- 前回の「量子論で点がない（コッヘン–シュペッカー）」に加えて、**「時空の因果構造は、点なしの時制論理で完全に表せるか」**という問いが立ちます。
- 点に基づく Goldblatt の結果（S4.2）が、点なしの演算子 I⁺ とその随伴だけで再現できるかは、具体的で検証しやすい候補です。Lean で形式化するにもちょうどよい規模に見えます。
- もう一つ、「点に基づく意味論では区別できないが、点なしでは区別できる因果構造」があるかも、面白い問いです。これは「6. 次にできること」の 3（点がないと表せない性質）とつながります。

どちらも、今の時点では私の見立てです。確度や優先度は、1 の基礎の整理を終えてから一緒に評価しましょう。

#### 次の作業

ご指示があれば、1（`surveys/`・`glossary.md`・`references.bib`）に着手します。前回と今回の論理・様相論理の整理も、ここに含めます。文献には、再掲の4点に加えて、次の6点を候補として登録します。

- McKinsey–Tarski（1944）
- Goldblatt（1980）
- Isham–Butterfield（1998）
- Heunen–Landsman–Spitters（2009）
- Christensen–Crane（2005）
- Birkhoff–von Neumann（1936）

書誌情報は記憶に頼らず、登録時に確認します。

## ユーザー

はい。「1（surveys/・glossary.md・references.bib）」に着手してください。

## Claude

まず作業ブランチを最新の `main` から作り直し、そのあと文献の書誌情報を確認します。

（ツール: Bash: Sync branch to main and test bibliographic API access）

## Claude

Crossref と arXiv の API には、この環境から接続できませんでした。そこで、Web 検索で書誌情報を1件ずつ確認します。

（ツール: ToolSearch: select:WebSearch,WebFetch）

（ツール: WebSearch: Johnstone "The point of pointless topology" Bulletin of the American Mathematical Society 1983 volume 8 pages）

（ツール: WebSearch: Picado Pultr "Frames and Locales: Topology without points" Birkhäuser 2012 Frontiers in Mathematics DOI）

（ツール: WebSearch: Johnstone "Stone Spaces" Cambridge Studies in Advanced Mathematics 3 1982 ISBN）

（ツール: WebSearch: Vickers "Topology via Logic" Cambridge Tracts in Theoretical Computer Science 5 1989）

（ツール: WebSearch: McKinsey Tarski "The algebra of topology" Annals of Mathematics 1944 45 141-191）

（ツール: WebSearch: Goldblatt "Diodorean modality in Minkowski spacetime" Studia Logica 1980 39 219）

## Claude

6件を確認しました。Johnstone（1983）の DOI は検索結果の中で食い違っていたので、出版元のページで確かめます。残りの4件も調べます。

（ツール: WebFetch: https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-8/issue-1/The-point-of-pointless-topology/bams/1183550014.full）

（ツール: WebSearch: Birkhoff von Neumann "The logic of quantum mechanics" Annals of Mathematics 1936 37 823）

（ツール: WebSearch: Isham Butterfield "A topos perspective on the Kochen-Specker theorem I" International Journal of Theoretical Physics 1998 37 2669）

（ツール: WebSearch: Heunen Landsman Spitters "A topos for algebraic quantum theory" Communications in Mathematical Physics 2009 291 63）

（ツール: WebSearch: Christensen Crane "Causal sites as quantum geometry" Journal of Mathematical Physics 2005 46）

（ツール: WebSearch: Heunen Schaaf "Ordered locales" Journal of Pure and Applied Algebra）

（ツール: WebSearch: "Causal coverage in ordered locales and spacetimes" Journal of Mathematical Physics 2026 authors）

（ツール: WebFetch: https://pubs.ams.org/journals/bull/1983-08-01/S0273-0979-1983-15092-9）

（ツール: WebSearch: "A topos perspective on the Kochen-Specker theorem" Isham Butterfield doi 10.1023）

（ツール: WebSearch: "Causal sites as quantum geometry" doi 10.1063）

（ツール: WebFetch: https://www.ams.org/journals/bull/1983-08-01/S0273-0979-1983-15080-2/）

（ツール: WebSearch: "S0273-0979-1983-15080-2" pointless topology Johnstone）

（ツール: WebFetch: https://arxiv.org/abs/2510.17417）

（ツール: WebFetch: https://arxiv.org/abs/2303.03813）

（ツール: Write: /home/user/point-free-spacetime/surveys/topic-pointfree-topology-basics.md）

## Claude

数式ガイドでは `\mathbf` を避けることになっているので（Chrome で太字にならないため）、`\mathrm` に置き換えます。続いて `references.bib` を書きます。

（ツール: Bash: Fix math macros and register 12 references）

## Claude

`references.bib` が BibTeX として正しく読めるかを確かめます。

（ツール: Bash: Validate references.bib with pybtex）

## Claude

12件すべて正しく読めました。次に用語一覧を更新します。既存の4語に今回の用語を加え、英語のアルファベット順に並べ直します。

（ツール: Bash: Rewrite glossary with new sorted entries）

## Claude

22語になりました。作業を失わないよう、ここまでをコミットして push しておきます。PR はセッションの終わりにまとめて作ります。

（ツール: Bash: Commit and push survey, glossary, references）

## Claude

「6. 次にできること」の 1 が終わりました。コミットして push 済みで、PR はセッションの終わりにまとめて作ります。

#### 作ったもの
- **調査メモ** [`surveys/topic-pointfree-topology-basics.md`](surveys/topic-pointfree-topology-basics.md)
  - 基本概念と、論理・様相論理・因果（時制論理）・量子論とのつながりを8節にまとめました。
  - 文献で確かめていない事項には「未確認」「見立て」と付けています。
  - ファイル名は、`surveys/README.md` の決まりに合わせて `topic-` で始めました。ご提案の名前 `pointfree-topology-basics.md` とは少し違います。
- **参考文献** `references.bib`：12件を登録しました。
  - 書誌情報は、Web 検索で出版元やデータベースの記載を確かめたものです。
  - 確認できなかった DOI は書いていません。
  - BibTeX として正しく読めることも確かめました。
- **用語一覧** `glossary.md`：18語を追加し、全22語をアルファベット順に並べ直しました。

#### 重要な発見：本題そのものの先行研究
文献を確認する途中で、**Heunen と van der Schaaf** の2本の論文が見つかりました。点なし位相で相対論の因果構造を扱う研究で、このプロジェクトの主題に最も近い先行研究です。

- ***Ordered locales***（J. Pure Appl. Algebra、2024）
  - ロケールに因果的な順序を加えた「順序付きロケール」を定義しています。
  - 時空（因果の向きの付いた空間）との間に、ストーン双対性と同じ形の対応を作っています。
- ***Causal coverage in ordered locales and spacetimes***（J. Math. Phys.、2026年8月）
  - 相対論の因果論を点なしで展開しています。
  - Christensen–Crane の「因果サイト」を改良したものです。
  - 層の条件を「決定論的な時間発展」として解釈しています。

前回挙げた予想の候補（点なしの時制論理で因果構造を表せるか）の一部は、すでにこれらで扱われている可能性があります。**3（予想の候補を立てる）の前に、この2本を読むべきです**。PDF を入手していただければ、非公開リポジトリの `papers/` に置いたうえで、論文メモを作ります。どちらも arXiv で公開されています（2303.03813 と 2510.17417）。

#### 前回の説明の訂正
時間的未来の演算子 I⁺ の読み方を間違えていました。

- x ∈ I⁺(U) は「x の**過去**のどこかで U が成り立った」という意味です。したがって I⁺ は**過去の ◇**にあたります。
- その右随伴は**未来の □**（「これから先ずっと成り立つ」）です。
- 随伴の組が時制論理の構造になるという結論は変わりません。調査メモには正しい形で書きました。

#### 次の作業
次は 2（Mathlib にあるものを確かめ、「完備ブール代数の点はアトムと対応する」を Lean で形式化する）に進めます。先に Heunen–van der Schaaf の論文メモに取りかかることもできます。どちらから進めましょうか。

## ユーザー

@"/root/.claude/uploads/[ID]/b9f9cc14-s00220-009-0865-6.pdf" @"/root/.claude/uploads/[ID]/2bab7b15-9803055v4.pdf" @"/root/.claude/uploads/[ID]/49d93b7e-2510.17417v1.pdf" @"/root/.claude/uploads/[ID]/20db784c-1-s2.0-S0022404924000513-main.pdf" @"/root/.claude/uploads/[ID]/380513bf-S0273-0979-1983-15080-2.pdf" 調査メモのファイル名について、`summaries/` のファイル `2026-09-25_01_repo-rules.md` と同様に、ファイル名の先頭に日付と番号を付けてほしいです。時系列で調査内容を追えるようにしたいです。

参考文献について、ダウンロード可能な論文の PDF を入手しました。5件添付します。他に調査対象にしたい論文や書籍があれば、お知らせください。

用語一覧と一緒に、記号一覧もあるとよいと思いました。いかがでしょうか？

## Claude

まず、添付いただいた5件の PDF がどの論文かを、それぞれの1ページ目で確かめます。

（ツール: Bash: Identify each uploaded PDF by its first page）

（ツール: Bash: Install pypdf and extract first-page text）

## Claude

Python のライブラリがこの環境で動かなかったので、ファイルを読む機能で各 PDF の1ページ目を確認します。

（ツール: Read: /root/.claude/uploads/[ID]/b9f9cc14-s00220-009-0865-6.pdf）

（ツール: Read: /root/.claude/uploads/[ID]/2bab7b15-9803055v4.pdf）

（ツール: Read: /root/.claude/uploads/[ID]/49d93b7e-2510.17417v1.pdf）

（ツール: Read: /root/.claude/uploads/[ID]/20db784c-1-s2.0-S0022404924000513-main.pdf）

（ツール: Read: /root/.claude/uploads/[ID]/380513bf-S0273-0979-1983-15080-2.pdf）

（ツール: Bash: Install poppler and print first-page text of PDFs）

## Claude

5件とも、想定どおりの論文でした。`Ordered locales` の DOI は検索では確認できなかったので、PDF の本文から拾います。

（ツール: Bash: Extract DOI of Ordered locales from PDF）

## Claude

これで `Ordered locales` の DOI も確認できました。PDF を非公開リポジトリの `papers/` に、引用キーの名前で置きます。

（ツール: Bash: Add 5 PDFs to private repo and push）

（ツール: Bash: Rename survey and update links; view docs to edit）

（ツール: Bash: Update naming rule, CLAUDE.md, README, and bib DOI）

## Claude

続いて記号一覧 `symbols.md` を作ります。これまでに調査メモと Lean のコードで使った記号を、Lean での書き方と合わせて載せます。

（ツール: Write: /home/user/point-free-spacetime/symbols.md）

## Claude

Lean の列に書いた名前が、今の Mathlib に本当にあるかを確かめます。

（ツール: Bash: Verify Mathlib names used in symbols list）

（ツール: Bash: Commit and push rename and symbols list）

## Claude

ご依頼の3点に対応し、両リポジトリに push しました。PR はセッションの終わりにまとめて作ります。

#### 1. 調査メモのファイル名
- `surveys/2026-09-25_02_pointfree-topology-basics.md` に改名しました（今回を第 02 回としています）。用語一覧からのリンクも直しました。
- `surveys/README.md` の命名規則を、次のように改めました。
  - 論文のメモ：`YYYY-MM-DD_NN_<引用キー>.md`
  - テーマのメモ：`YYYY-MM-DD_NN_<テーマ>.md`
  - 同じ論文を後のセッションで読み直したときは、既存のメモを更新し、冒頭に更新したセッションを追記します。

#### 2. 論文の PDF（5件）
1ページ目で5件とも正しい論文であることを確かめ、非公開リポジトリの `papers/` に引用キーの名前で置きました。`papers/README.md` には、出版社版か arXiv 版かの一覧も書きました。

| ファイル | 版 |
| --- | --- |
| `heunen2024.pdf`（Ordered locales） | 出版社版 |
| `heunen2026.pdf`（Causal coverage） | arXiv 版 v1 |
| `heunen2009.pdf`（A topos for algebraic quantum theory） | 出版社版 |
| `isham1998.pdf`（Topos perspective on Kochen–Specker I） | arXiv 版 v4 |
| `johnstone1983.pdf`（The point of pointless topology） | 出版社版 |

検索では確認できなかった `Ordered locales` の DOI も、PDF から確認して `references.bib` に追加しました。

#### 3. 記号一覧
よい考えだと思い、[`symbols.md`](symbols.md) を作りました。
- 記号ごとに、読み方、意味、Lean（Mathlib）での書き方、初出を載せています。
- 分野は、順序と束、位相とロケール、圏論、様相・時制論理、因果構造の5つで、計26項目です。
- Lean の列の名前は、すべて Mathlib に存在することを確かめました。文書の数式と Lean のコードを見比べるときの対応表にもなります。
- `CLAUDE.md` の「セッションの終え方」で、更新する対象に記号一覧を加えました。

#### 4. 追加の調査候補
まだ登録も書誌情報の確認もしていません。登録するときに確認します。

**A. 本題に直結（優先して読みたいもの）**
- Kronheimer–Penrose, *On the structure of causal spaces*（1967）：時空の因果構造を公理化した古典で、順序付きロケールの源流の一つです。
- Malament（1977）、Hawking–King–McCarthy（1976）：因果構造が時空の位相や共形構造を決めるという定理です。「点なしで因果から時空を復元できるか」の出発点になります。
- Minguzzi, *Lorentzian causality theory*（Living Reviews in Relativity、2019）：因果論の総説で、Heunen–van der Schaaf を読むときの参照用です。
- Hirsch–McLean, *Temporal logic of Minkowski spacetime*（arXiv:2010.01321）：Goldblatt の結果（S4.2）の後継研究です。
- Döring–Isham, *A topos foundation for theories of physics* I–IV（J. Math. Phys.、2008）：トポス的アプローチの本論です。

**B. 教科書（参照用）**
- Mac Lane–Moerdijk, *Sheaves in Geometry and Logic*（1992）：トポスと層、内部論理の標準的な教科書です。

**C. 背景（必要になったら）**
- 構成的ゲルファント双対性：Banaschewski–Mulvey（2006）、Coquand–Spitters（2009）
- クォンタール：Mulvey（1986）、Abramsky–Vickers（1993）
- 様相論理の双対性：Jónsson–Tarski、Esakia
- Whitehead 流の「領域に基づく幾何学」（mereotopology）：点ではなく領域から空間を組み立てる、哲学・論理学側の伝統です。本プロジェクトの発想に近い系譜です。

#### 次の作業
いただいた PDF で、Heunen–van der Schaaf の2本の論文メモから始めるのがよいと考えています。2本は本題に最も近く、予想の候補の一部がすでに解かれているかを先に確かめる必要があるためです。そのあと、元の 2（Lean での形式化）に進みます。この順でよろしいでしょうか。

## ユーザー

はい。その順で進めてください。ここでいったん、PR を作成してマージし、セッションを終了するのがよいと思いますが、いかがでしょうか？

## Claude

はい、よい区切りだと思います。セッションを終える手順を進めます。

1. 対話ログとまとめを書き出す
2. `NEXT.md` を更新する
3. 両リポジトリで PR を作る

一つ課題があります。セッション記録のファイルは第 01 回と共通なので、そのまま変換すると第 01 回の内容も入ってしまいます。そこで、変換スクリプトに「指定した時刻以降だけを書き出す」オプションを加えます。まず、第 02 回の最初の発言の時刻を調べます。

（ツール: Bash: Find timestamp of session 02's first message）

（ツール: Bash: View convert and main functions）

（ツール: Bash: Add --since option to export_log with test）

## Claude

テストも通りました。`CLAUDE.md` の手順にこのオプションを追記し、まとめと `NEXT.md` を書きます。

（ツール: Bash: Document --since in CLAUDE.md）

（ツール: Write: /home/user/point-free-spacetime/summaries/2026-09-25_02_pointfree-logic.md）

（ツール: Write: /home/user/point-free-spacetime/NEXT.md）

## Claude

最後に対話ログを書き出し、伏せ字の漏れがないか検査します。

（ツール: Bash: Export session 02 log and check for leaks）
