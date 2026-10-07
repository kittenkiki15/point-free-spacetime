# 未解決の点

定義・前提の「未解決の点」と、予想の「詳細化の論点」の一つひとつを、1 件 1 ファイル（`questions/Q-NNNN.md`）で管理します（第 28 回に方針を、第 30 回に仕組みを決めた。T-0025 の 5）。

- 一度にすべては移しません。段階 B 以降に触れたものから順に、タスクに割り当てたものだけを移します（第 28 回のユーザーの判断）。移していない論点は、これまでどおり親のファイルの節に書きます。
- 書式は [`_template.md`](_template.md) です。表の項目は、親の ID（定義・前提・予想）・割り当てたタスク・状態・Issue・初出・解決した回です。本文は「論点」と「経緯」です。
- **状態などの内容はファイルが正本**です。議論は、Q ごとの GitHub の Issue（タイトルは `[Q-NNNN] <論点の短い名前>`）に置きます。
- 状態は、未解決・解決・取り下げのどれかです。
- 論点を Q に移したら、本文の正本は Q のファイルになります（移す前は、親のファイルの節が正本です）。親のファイルの「未解決の点」（予想では「詳細化の論点」）の該当する箇条を、Q へのリンク 1 行（リンク先は `../questions/Q-NNNN.md`、その後に「：論点の短い名前」）に置き換えます。
- 次のことを `tools/tests/test_framework.py` で検査します。
  - 親の ID のファイルがあり、親のファイルの節から Q へのリンクがあること（双方向のリンク）。
  - 未解決の Q が、未完了のタスク（一つ）に割り当てられていること。割り当てたタスクの「関係する ID」に、親の ID があること。
  - Q の Issue の欄が、Issue へのリンクの形式であること。Issue の表示の番号とリンク先の番号が一致し、タスクと Q の間で同じ Issue を使わないこと（Issue が実在するかと、その開閉は検査しない。セッションの終わりに Claude が照合する）。
  - 「割り当てたタスク」の欄が、状態によらず、あるタスクのファイルへのリンク（`../tasks/T-NNNN.md`）一つであること。
  - 一覧の各列（論点・親の ID・割り当てたタスク・状態・Issue）が、Q のファイルと一致すること。
- 解決・取り下げにした Q へのリンクの行は、親のファイルの節に残っても、割り当て漏れの検査では論点として数えません。ただし、行が「Q へのリンク」と「：Q の名前」だけからなる場合に限ります（ほかの問いを書き足した行は、論点として数えます）。
- Issue の番号は、タスク・Q・予想の間で重複しないことを検査します。

## 一覧

| ID | 論点 | 親の ID | 割り当てたタスク | 状態 | Issue |
| --- | --- | --- | --- | --- | --- |
| [Q-0001](Q-0001.md) | 結果の統計の空間の位相と、等価原理の「近い」の意味 | [D-0004](../definitions/D-0004.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#33](https://github.com/kittenkiki15/point-free-spacetime/issues/33) |
| [Q-0002](Q-0002.md) | 可能な実験の状態の集合の位相と、座標の同相性 | [D-0014](../definitions/D-0014.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#34](https://github.com/kittenkiki15/point-free-spacetime/issues/34) |
| [Q-0003](Q-0003.md) | 許す状態（ボレル確率測度・正規状態） | [D-0014](../definitions/D-0014.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#35](https://github.com/kittenkiki15/point-free-spacetime/issues/35) |
| [Q-0004](Q-0004.md) | 状態を値とする設定・結果の上の較正の可測構造 | [D-0014](../definitions/D-0014.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#36](https://github.com/kittenkiki15/point-free-spacetime/issues/36) |
| [Q-0005](Q-0005.md) | コンパクト性を課す対象 | [A-0005](../assumptions/A-0005.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#37](https://github.com/kittenkiki15/point-free-spacetime/issues/37) |
| [Q-0006](Q-0006.md) | 「一様に有界」の範囲 | [A-0005](../assumptions/A-0005.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#38](https://github.com/kittenkiki15/point-free-spacetime/issues/38) |
| [Q-0007](Q-0007.md) | 結果の空間の意味 | [D-0004](../definitions/D-0004.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#39](https://github.com/kittenkiki15/point-free-spacetime/issues/39) |
| [Q-0008](Q-0008.md) | 時計や物差しの読みでない結果の座標を、共通の空間に写す方法 | [D-0003](../definitions/D-0003.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#40](https://github.com/kittenkiki15/point-free-spacetime/issues/40) |
| [Q-0009](Q-0009.md) | 設定に含める資源の量は、予算か実際の消費量か | [A-0004](../assumptions/A-0004.md) | [T-0004](../tasks/T-0004.md) | 未解決 | [#41](https://github.com/kittenkiki15/point-free-spacetime/issues/41) |
