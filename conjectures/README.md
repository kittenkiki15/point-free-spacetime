# 予想の一覧

対話の中で出てきた未検証の主張を「予想」として管理します。
1 件 1 ファイル（`C-NNNN.md`）で、書式は [`_template.md`](_template.md) のとおりです。

## 評価の段階

| 項目 | 高 | 中 | 低 |
| --- | --- | --- | --- |
| 確度 | 成り立つと強く見込まれる | どちらともいえない | 成り立たない見込みが強い |
| 重要度 | 成り立てば考察全体の方向を左右する | 個別の論点に効く | 補助的・興味本位 |
| 検証費用 | 数日以上、または新しい道具が必要 | 数時間〜1 日程度 | 1 セッション内で済む |

優先度（高・中・低）は、上の評価をもとに対話の中で決めます。

## 状態

`未着手` → `検証中` → `証明済み`・`反証済み`・`数値的に支持`・`保留`

- `証明済み`：数学的な証明がある場合に限る（Lean による形式証明、または対話・文献中の証明）。
- `反証済み`：反例がある場合（数値実験で見つけた反例を含む）。
- `数値的に支持`：数値実験などで支持されているが、証明はない場合。証明済みとは区別する。

## 一覧

優先度の高い順に並べます。

| ID | 予想 | 確度 | 重要度 | 検証費用 | 優先度 | 状態 | Issue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [C-0007](C-0007.md) | 局在の限界から、装置の占める領域の上下限が導かれる | 低 | 高 | 高 | 中 | 未着手 | [#25](https://github.com/kittenkiki15/point-free-spacetime/issues/25) |
| [C-0001](C-0001.md) | 長さ空間の尺度 ℓ の膨張の余白付きの包含は補間的でなく、離散化と区別できる | 高 | 中 | 低 | 中 | 未着手 | [#8](https://github.com/kittenkiki15/point-free-spacetime/issues/8) |
| [C-0008](C-0008.md) | ポアンカレ共変な装置の占める領域は有界にできない | 高 | 中 | 中 | 中 | 未着手 | [#26](https://github.com/kittenkiki15/point-free-spacetime/issues/26) |
| [C-0003](C-0003.md) | 情報的に完全なプロトコルの族の下では、統計の関数の推定と状態の推定の極限が一致する | 高 | 中 | 低 | 中 | 未着手 | [#17](https://github.com/kittenkiki15/point-free-spacetime/issues/17) |
| [C-0004](C-0004.md) | 実験プロトコルを計算可能な手続きとして形式化すると、連続性の意味での等価原理が従う | 高 | 中 | 中 | 中 | 未着手 | [#18](https://github.com/kittenkiki15/point-free-spacetime/issues/18) |
| [C-0006](C-0006.md) | 等価原理の下でも、事後分布が点に収束しない場合がある | 高 | 中 | 低 | 中 | 未着手 | [#20](https://github.com/kittenkiki15/point-free-spacetime/issues/20) |
| [C-0002](C-0002.md) | 可能な実験は、再構成した観測量の時空の中でモデル化できる | 中 | 高 | 高 | 低 | 未着手 | [#16](https://github.com/kittenkiki15/point-free-spacetime/issues/16) |
| [C-0005](C-0005.md) | 実験から得る可算集合の閉包が、観測量の全体を含む物理的に自然な条件がある | 中 | 中 | 中 | 低 | 未着手 | [#19](https://github.com/kittenkiki15/point-free-spacetime/issues/19) |
| [C-0009](C-0009.md) | 較正の普遍性から、観測者の取り替えはローレンツ変換かガリレイ変換になる | 高 | 高 | 高 | 低 | 未着手 | [#37](https://github.com/kittenkiki15/point-free-spacetime/issues/37) |
| [C-0010](C-0010.md) | 比較の実験で取り替えを与える体系では、較正の普遍性は検証できる条件に言い換えられる | 中 | 中 | 中 | 低 | 未着手 | [#38](https://github.com/kittenkiki15/point-free-spacetime/issues/38) |
| [C-0011](C-0011.md) | 比較の取り替えが経路に依らず、全域へ整合的に広げられるなら、観測者の取り替えは群の作用で記述できる | 中 | 高 | 高 | 低 | 未着手 | [#39](https://github.com/kittenkiki15/point-free-spacetime/issues/39) |
| [C-0012](C-0012.md) | 可能な実験の観測も、観測者の座標時刻で、登録が準備より前にない | 高 | 中 | 中 | 低 | 未着手 | [#40](https://github.com/kittenkiki15/point-free-spacetime/issues/40) |
| [C-0013](C-0013.md) | 可能な実験でも較正の普遍性が成り立つ | 中 | 中 | 中 | 低 | 未着手 | [#41](https://github.com/kittenkiki15/point-free-spacetime/issues/41) |
