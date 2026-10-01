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

第 18 回に確かめた Ludwig（`ludwig1985`、第 I 章）の準備装置と登録装置の区別も、3 節の表に含める（[第 18 回の調査メモ](2026-09-30_18_limit-topology.md)の 5.2 節）。

## 2. 各文献での使われ方

### 2.1 Fewster–Verch（`fewster2020`）

- 測りたい量子場を「系（system）」、それを測るために結合させるもう一つの系を「プローブ（probe）」とよぶ。結合は、時空のコンパクトな「結合の領域（coupling region）」でだけ働く。
- 実験者（experimenter）がプローブを準備し、制御し、測定する手段を持つことは前提とし、測定問題は扱わない。扱うのは、測定の連鎖（measurement chain）の一つの環として、プローブの測定が系について何を告げるか、である。
- 時空は固定した（曲がっていてもよい）背景とし、量子重力での測定は扱わない。

### 2.2 Hardy（`hardy2001`）

- 実験家（experimentalist）は 3 種類の装置を持つ：準備装置（preparation device）、変換装置（transformation device）、測定装置（measurement apparatus）。
- どの装置にも、つまみ（knob）があり、つまみの設定（setting）で、準備する状態、行う変換、測る量を変える。測定装置は古典的な数を出力する。
- 量子・古典・その他のどの物理実験も、この形の実験とみなせる、とする。

### 2.3 Chiribella–D'Ariano–Perinotti（`chiribella2010`）

- 操作的確率論（operational-probabilistic theory）は、物理的な装置（physical device）で行える実験の集まりと、その結果の確率の予測からなる。
- 基本の概念は「系」と「試験（test）」である。試験は物理的な装置の 1 回の使用を表し、結果の集合で添字付けた事象の集まりである。系は、装置の入力と出力のポートに付けたラベルで、装置をつなぐ規則を定める。

### 2.4 Brunner ほか（`brunner2014`）

- ベル実験では、各者（Alice、Bob）が入力（測定の設定、measurement setting）$`x`$、$`y`$ を選び、出力 $`a`$、$`b`$ を得る。実験は、条件付き確率 $`p(ab \mid xy)`$ で記述する。入力と出力のラベルは約束にすぎない。

### 2.5 Fuchs–Mermin–Schack（`fuchs2014`）

- 確率は、agent が事象に割り当てるもので、その agent の個人的な信念の度合いを表す。agent は「行為する者」の意味である（代理人の意味ではない。原典の脚注）。
- 測定は、agent が世界に働きかける行為で、その agent に新しい経験（結果）を生む。量子状態の割り当ても agent の個人的な判断である。

### 2.6 Brukner（`brukner2018`）

- Wigner の友人の思考実験では、密閉した実験室の中で系を測定する者を「観測者（observer）」（友人）、実験室の外から実験室全体を量子系として扱う者を「超観測者（super-observer）」（Wigner）とよぶ。
- 結果は測定装置に記録され、友人の記憶に残る。友人は確定した結果を知覚する、ということだけを仮定する。

### 2.7 Rovelli（`rovelli1996`）

- 「観測者」は、意識を持つ系などの特別な系を指さない。ガリレイの相対性で「ある観測者に対する速度」と言うときの意味で使い、定まった運動状態を持つ任意の物理的な対象（机の上のランプでもよい）を指す。
- 量子力学は系と観測者を分けることを要するが、その境目の引き方には自由がある。同じ一連の出来事を、境目を変えた二つの記述で表せる（系 S と観測者 O の間で分ける記述と、S と O をまとめたものと別の観測者 P の間で分ける記述）。

### 2.8 Rovelli（`rovelli2002`）

- **部分観測量（partial observable）**：測定の手続きを対応させられ、数を与える物理量。**完全観測量（complete observable）**：理論が値（量子論では確率分布）を予測できる量。
- 振り子の例では、位置 $`q`$ と時刻 $`t`$ はどちらも部分観測量で、予測できるのは「時刻 $`t`$ での $`q`$」という完全観測量の族である。時刻 $`t`$ は時計で測る量である。
- 非相対論的な系では $`t`$ を独立な部分観測量、$`q`$ を従属な部分観測量と区別できるが、一般相対論的な文脈ではこの区別が失われる、とする。

### 2.9 Giacomini–Castro-Ruiz–Brukner（`giacomini2019`）

- 参照系は、どの実験室の状況でも、物理系によって実現される。例えば、剛体は空間的な距離を定める参照系になる。
- 観測者の実験室と装置が、別の観測者の実験室に対して位置の重ね合わせにある状況を考え、量子参照系（quantum reference frame）の間の変換を与える。状態の重ね合わせやもつれは、参照系に相対的な性質になる。

## 3. 語の対応表

2 節の整理である（第 18 回の Ludwig を含む）。

| 本プロジェクトで区別したい役割 | 既存研究での語 |
| --- | --- |
| 実験を行い、設定を選び、結果を得る者 | experimenter（Fewster–Verch）、experimentalist（Hardy）、agent（QBism）、observer（Wigner の友人。Brukner） |
| 結果から信念を更新する者 | agent（QBism） |
| 基準系（時間・空間の比較の基準） | observer（ガリレイの相対性の意味。Rovelli 1996）、reference frame（Giacomini ほか）。相対論の観測者（時間的な世界線と、その上の正規直交枠）は教科書の定義で、今回は原典を確かめていない |
| 装置 | probe（Fewster–Verch）、準備・変換・測定の装置（Hardy）、physical device と test（Chiribella ほか）、準備装置と登録装置（Ludwig）、measurement apparatus（Brukner） |
| 設定 | knob の setting（Hardy）、input・measurement setting（Brunner ほか） |
| 時計の読み | 部分観測量（Rovelli 2002） |
| 系と観測者・装置の境目 | 自由に動かせる（Rovelli 1996。Ludwig も準備と登録の切り分けが一意でないとする） |

## 4. プロジェクトへのつながり（Claude の見立て）

この節は、第 20 回の再編の**前**に検討した候補である。再編後の結論は、次のとおりである（ユーザーの判断。[まとめ](../summaries/2026-09-30_20_terms-setting-and-agents.md)）。

- 実験を行い、信念を更新する者は「主体」とし、観測者・装置と別の定義にした（[D-0012](../definitions/D-0012.md)）。「観測者」は基準系の意味だけに使い、実験と 1 対 1 に対応する世界線の区間とした（[D-0001](../definitions/D-0001.md)）。三つの語を「実際の～」と「可能な～」に分けた。
- 時計の読みの扱い（較正の写像）は、[D-0003](../definitions/D-0003.md) から [D-0013](../definitions/D-0013.md) に移し、実験ごとの写像 $`τ_e`$（準備の事象）・$`σ_e`$（登録の事象）とした。下の旧記号 $`τ^O_π`$・$`σ^O_π`$ と D-0003 への参照は、再編前のものである。

以下は、再編前に書いた候補である。

- **「観測者」の多義性は既存研究にもある。** 基準系の意味（Rovelli 1996、量子参照系、相対論）と、結果を知覚する者の意味（Wigner の友人）が並存している。本プロジェクトの「観測者」の二つの意味（基準系と、実験をする者。[roadmap.md](../roadmap.md) の T-0018 の節）は、この二つに対応する。
- **使い分けの候補**：実験をし、信念を更新する者は QBism に合わせて「主体（agent）」、基準系は相対論と Rovelli 1996 に合わせて「観測者（observer）」、物理系としての道具は「装置（apparatus、device）」とする。この案は、T-0018 の叩き台（第 20 回の冒頭の Claude の提案）と一致する。
- **設定の語**：Hardy の「つまみの設定」とベル実験の「測定の設定」は、D-0001 の設定 $`x ∈ X_π`$ と同じ役割である。第 20 回に行った「実験パラメータ」から「設定」への統一と合う。
- **時計の読みと D-0003**：Rovelli 2002 は、時計の読みを部分観測量とし、一般相対論的な文脈では独立な部分観測量（時刻）と従属な部分観測量の区別が失われるとする。本プロジェクトでは、時計の読みを設定（$`τ^O_π`$ の入力）にも結果（$`σ^O_π`$ の入力）にも置きうる（[D-0003](../definitions/D-0003.md) の未解決の点）。この区別が理論の上で本質的でないことの傍証になる。(A) の D-0003 の再編で参考にできる。
- **観測者は物理系か**：量子参照系の文献は、参照系を物理系として扱う。本プロジェクトの観測者（[A-0010](../assumptions/A-0010.md) の基準の時計と物差し）を、実際の実験の中の物理系（装置の一種）とみるか、可能な実験の記述のための理想化とみるかは、[D-0001](../definitions/D-0001.md)・[D-0002](../definitions/D-0002.md) との関係に関わる。ユーザーの判断で、(A) を行うときにこの点を明らかにする。
- **境目の自由**：Rovelli 1996 と Ludwig の、系と観測者・装置の境目を動かせるという扱いは、[A-0001](../assumptions/A-0001.md) の未解決の点（境界の取り方と実験の個別化）の先例になる。

## 5. 未確認の点

- 相対論の観測者の定義（時間的な世界線と正規直交枠）は、教科書の記憶による。
- Busch–Lahti–Mittelstaedt などの量子測定論の教科書での、系・プローブ・装置の用語は確かめていない。
- von Neumann の測定の連鎖とハイゼンベルクの切断は、Rovelli 1996 と Fewster–Verch の言及で確かめただけで、原典は確かめていない。
