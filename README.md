# point-free-spacetime

点なし時空（point-free spacetime）による物理学についての考察です。

時空を「点の集合」としてではなく、開集合のなす束（フレーム）や、それを双対圏で捉えた空間（ロケール）のように、点を基本データとしない構造として扱う、点なし位相（point-free topology）の考え方を物理学に応用する可能性を、ユーザーと Claude（Anthropic の AI）との対話を通して探ります。

その中心として、「観測」と「実験」の定式化から点なし時空を基礎づけるフレームワークを作ります。最新版は [`framework.md`](framework.md) にあります。

## 成果物

| 成果物 | 場所 |
| --- | --- |
| 対話ログ | [`logs/`](logs/) |
| 対話のまとめ | [`summaries/`](summaries/) |
| 参考文献の調査メモ | [`surveys/`](surveys/) |
| 用語一覧 | [`glossary.md`](glossary.md) |
| 記号一覧 | [`symbols.md`](symbols.md) |
| 参考文献一覧 | [`references.bib`](references.bib) |
| フレームワーク（最新版） | [`framework.md`](framework.md) |
| ロードマップ（最新版） | [`roadmap.md`](roadmap.md) |
| 定義の一覧 | [`definitions/`](definitions/) |
| 前提（仮定）の一覧 | [`assumptions/`](assumptions/) |
| 予想（未検証の主張）の一覧 | [`conjectures/`](conjectures/) |
| 検証済みの結果の一覧 | [`results/`](results/) |
| Lean 4 による形式証明 | [`lean/`](lean/) |
| Python による数値実験 | [`sim/`](sim/) |

## 現状（2026-10-03。第 28 回の時点）

- フレームワークの最初の段階（段階 A。実験と観測の基本の定義、主体・観測者・装置の区別、量子・古典・混成の実験の扱い）を終えたところです。実験と観測量の層を詳しくする段階 B のうち、最初のタスク（T-0020）は済んでいます。運用の改善（T-0025）の後、段階 B の残りのタスクに進みます（[`roadmap.md`](roadmap.md)）。
- 定義 14 件、前提 16 件、予想 13 件、検証済みの結果 9 件、調査メモ 15 件があります。
- 結果は、既知の数学の形式化（Lean）や文献の照合が中心で、**新しい定理と言えるものはまだありません**。予想はすべて未検証です。
- 段階 A までの振り返りは [`docs/retrospective-stage-A.md`](docs/retrospective-stage-A.md) にあります。

## 読み始めるには

| 目的 | 最初に読むもの |
| --- | --- |
| 何をしようとしているか知りたい | [`framework.md`](framework.md)（構成の 6 つの層と、定義・前提・予想の依存関係の図） |
| 先行研究のサーベイとして使いたい | [`surveys/README.md`](surveys/README.md) の「テーマ別の索引」 |
| 各回の議論の要点を追いたい | [`summaries/`](summaries/)（各回のまとめ。短く、人が読む前提で書いています） |
| 判断の根拠をたどりたい | [`logs/`](logs/)（対話ログ。公開できる範囲で処理した、PR を作るまでの対話の記録で、人が読むことは前提にしていません。PR を作った後の経緯は、各 PR で追えます） |
| 研究の進め方（AI との共同研究の運用）を知りたい | [`CLAUDE.md`](CLAUDE.md)、[`docs/review-procedure.md`](docs/review-procedure.md)、振り返りの 2・3 節 |

次に取り組む予定のタスクは [`NEXT.md`](NEXT.md) にあります。
運用ルールの詳細は [`CLAUDE.md`](CLAUDE.md) を参照してください。

## 注意

- 対話ログとまとめには、AI が生成した内容が含まれます。検証済みの結果と、予想・推測とを区別して書くようにしていますが、内容の正しさは保証しません。
- 形式証明（Lean）は GitHub Actions で自動的に検証しています。ただし、形式化が元の主張を正しく表しているかは、別途確認が必要です。

## ライセンス

[CC0 1.0 Universal](LICENSE)。ただし、引用している他者の文章や書誌情報の権利は、それぞれの権利者に帰属します。
