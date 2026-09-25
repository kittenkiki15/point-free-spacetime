# 用語一覧

英語の原語を併記しています。項目は英語の原語のアルファベット順です。

| 英語 | 日本語 | 説明 | 初出 |
| --- | --- | --- | --- |
| atom | アトム | 束で、0 のすぐ上にある元（0 と自分の間に他の元がない元）。完備ブール代数の点は、アトムと一対一に対応する。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| completely prime filter | 完全素フィルター | 任意の結び ⋁S が属するなら、S のある元が属するフィルター。ロケールの点と一対一に対応する。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| frame | フレーム | 任意の結びと有限の交わりを持ち、有限の交わりが任意の結びに対して分配する完備束。位相空間の開集合全体はフレームになる。 | [第 01 回](summaries/2026-09-25_01_repo-rules.md) |
| geometric logic | 幾何学的論理 | 有限の論理積、任意の論理和、存在量化（と等号）だけを使う論理。命題的な幾何学的論理（有限の論理積と任意の論理和だけ）は、有限回の観測で確かめられる命題の論理と解釈でき、フレームはその代数である。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| Heyting algebra | ハイティング代数 | 含意を持つ束で、直観主義命題論理の代数的意味論。フレームは、順序集合としては完備ハイティング代数と同じものである。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| intuitionistic logic | 直観主義論理 | 排中律を仮定しない論理。位相空間の開集合で解釈でき、否定は補集合の内部になる。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| Kochen–Specker theorem | コッヘン–シュペッカーの定理 | 次元 3 以上のヒルベルト空間で記述される量子系では、すべての観測量に、関数関係を保って矛盾なく値を割り当てることはできない、という定理（2 次元では成り立たない）。トポス的アプローチでは、スペクトル前層に大域切断がないことと同値になる。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| locale | ロケール | フレームの圏の反対圏の対象。点を基本データとしない「空間」として扱う（点を持たないとは限らない）。 | [第 01 回](summaries/2026-09-25_01_repo-rules.md) |
| modal logic S4 | 様相論理 S4 | □p → p と □p → □□p などを公理とする様相論理。□ を内部をとる操作と読むと、位相空間の論理になる（McKinsey–Tarski）。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| nucleus | 核 | フレーム上の写像 j で、a ≤ j(a)、j(j(a)) ≤ j(a)、j(a ∧ b) = j(a) ∧ j(b) を満たすもの。部分ロケールと一対一に対応し、様相演算子の一種とみなせる。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| ordered locale | 順序付きロケール | ロケールに順序（前順序）の構造を加えたもの（Heunen–van der Schaaf）。前順序付き位相空間の点なし版であり、応用として相対論の因果順序を点なしで扱える。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| orthomodular lattice | オーソモジュラー束 | 直交補を持つ束で、分配律より弱いオーソモジュラー律を満たすもの。ヒルベルト空間の閉部分空間全体がなし、伝統的な量子論理の代数である。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| point (of a locale) | （ロケールの）点 | ロケールの圏で、終対象（一点空間に対応するロケール）からロケール L への射。フレームの言葉では、逆向きのフレーム準同型 L → {0, 1} にあたる。完全素フィルターや素元と一対一に対応する。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| point-free topology | 点なし位相 | 点ではなく開集合の束（フレーム）を基本として位相を扱う理論。pointless topology とも呼ぶ。 | [第 01 回](summaries/2026-09-25_01_repo-rules.md) |
| proof assistant | 定理証明支援系 | 証明を形式的に記述し、計算機で正しさを検証するソフトウェア。本プロジェクトでは Lean 4 を使う。 | [第 01 回](summaries/2026-09-25_01_repo-rules.md) |
| quantale | クォンタール | 任意の結びを持つ完備束に、結合的で、各変数について任意の結びを保つ積（可換とは限らない）を備えた構造。フレームは、積を交わりにとった特別な場合である。非可換な空間の候補として Mulvey が導入した。線形論理と関係する。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| sober space | ソバー空間 | 既約な閉集合がちょうど一つの点の閉包になっている位相空間。ソバー空間の圏と空間的ロケールの圏は同値になる。ハウスドルフ空間はソバーである。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| spatial locale | 空間的ロケール | 点が十分にあり、点の集合の位相空間の開集合フレームとして表せるロケール。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| Stone duality | ストーン双対性 | 論理側の代数（ブール代数、分配束、フレームなど）と、空間（ストーン空間、スペクトル空間、ロケールなど）の間の双対性。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| sublocale | 部分ロケール | ロケールの「部分空間」。部分集合ではなく、核によって与えられる。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| tense logic | 時制論理 | 過去・未来についての様相演算子（P・F・H・G）を持つ様相論理。点なしの因果構造は、フレーム上の随伴な演算子の組 P ⊣ G、F ⊣ H として表せる見込みがある。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
| topos | トポス | 集合の圏のようにふるまう圏。ロケール上の層の圏はトポスであり、その内部論理は高階の直観主義論理である。 | [基礎の調査メモ](surveys/2026-09-25_02_pointfree-topology-basics.md) |
