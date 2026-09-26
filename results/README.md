# 検証済みの結果の一覧

対話の中で検証した主張を「結果」として管理します。未検証の主張を扱う[予想の一覧](../conjectures/README.md)とは別に、本プロジェクトの成果物として一覧にします。
1 件 1 ファイル（`R-NNNN.md`）で、書式は [`_template.md`](_template.md) のとおりです。

## 登録の基準

次のいずれかで検証した主張を登録します。予想（`C-NNNN`）が証明・反証されたときも、ここに登録して予想ファイルから R-ID へリンクします。

- **Lean**：`lean/` での形式証明（`sorry` なし）。
- **テスト**：`sim/` のテストによる確認。有限の場合の総当たりや具体的な反例は、その範囲では証明にあたる。数値実験による支持にとどまるものは、種類を「数値的に支持」とする。
- **自然言語の証明**：対話・調査メモ・文献中の証明。証明はファイルの中に書くか、所在を示す。

既知の結果を形式化したものも登録してよい。その場合は、種類の欄と「検証」の節に**既知の結果の形式化**であることと、出典を明記する。

## 種類

| 種類 | 意味 |
| --- | --- |
| 定理・命題・系 | 数学的な証明がある主張。重さに応じて使い分ける |
| 反例 | ある主張が成り立たないことを、具体的な例で示したもの |
| 数値的に支持 | 数値実験で支持されているが、証明はないもの |

## 対応付けの規則

- Lean の定理の文書コメントと、テストの docstring に、対応する R-ID を書く（例：`結果 R-0002`）。
- 各ファイルに、主張を自然言語で述べている箇所（まとめ・調査メモ）へのリンクを書く。

## 一覧

| ID | 結果 | 種類 | 検証 | 成果物 | 初出 |
| --- | --- | --- | --- | --- | --- |
| [R-0001](R-0001.md) | フレームの点と素元は一対一に対応する | 命題 | Lean | [`BooleanPoints.lean`](../lean/PointFreeSpacetime/BooleanPoints.lean)：`ptEquivPrime` | 第 03 回 |
| [R-0002](R-0002.md) | 完備ブール代数の点とアトムは一対一に対応する | 定理 | Lean | [`BooleanPoints.lean`](../lean/PointFreeSpacetime/BooleanPoints.lean)：`ptEquivAtom` | 第 03 回 |
| [R-0003](R-0003.md) | アトムを持たない完備ブール代数は点を持たない | 系 | Lean | [`BooleanPoints.lean`](../lean/PointFreeSpacetime/BooleanPoints.lean)：`isEmpty_pt_of_forall_not_isAtom` | 第 03 回 |
| [R-0004](R-0004.md) | 平行性の不等式 (f±) ならば共役 | 命題 | Lean、テスト | [`Conjugate.lean`](../lean/PointFreeSpacetime/Conjugate.lean)：`conjugate_of_fpm`、[`test_conjugate.py`](../sim/tests/test_conjugate.py)：`test_f_pm_implies_conjugate_on_small_lattices` | 第 04 回 |
| [R-0005](R-0005.md) | フレームでは、共役ならば (f±) とは限らない | 反例 | テスト | [`test_conjugate.py`](../sim/tests/test_conjugate.py)：`test_five_element_counterexample` | 第 04 回 |
| [R-0006](R-0006.md) | 余白付きの包含の補間性と、識別の関係の推移性（点の場合。既知の結果の形式化） | 命題 | Lean | [`Tolerance.lean`](../lean/PointFreeSpacetime/Tolerance.lean)：`marginSub_interpolates_iff` | 第 05 回 |
| [R-0007](R-0007.md) | 膨張による余白付きの包含の補間性（点なし版。既知の事実の言い直し） | 命題 | Lean | [`Tolerance.lean`](../lean/PointFreeSpacetime/Tolerance.lean)：`margin_interpolates_iff` | 第 05 回 |
| [R-0008](R-0008.md) | オープニングの不動点は膨張の像（既知の結果の形式化） | 命題 | Lean | [`Tolerance.lean`](../lean/PointFreeSpacetime/Tolerance.lean)：`opening_fixed_iff_mem_range` | 第 05 回 |
