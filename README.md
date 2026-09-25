# point-free-spacetime

点なし時空（point-free spacetime）による物理学についての考察です。

時空を「点の集合」としてではなく、開集合の束（フレーム / ロケール）のような点を持たない構造として扱う、点なし位相（point-free topology）の考え方を物理学に応用する可能性を、ユーザーと Claude（Anthropic の AI）との対話を通して探ります。

## 成果物

| 成果物 | 場所 |
| --- | --- |
| 対話ログ | [`logs/`](logs/) |
| 対話のまとめ | [`summaries/`](summaries/) |
| 参考文献の調査メモ | [`surveys/`](surveys/) |
| 用語一覧 | [`glossary.md`](glossary.md) |
| 参考文献一覧 | [`references.bib`](references.bib) |
| 予想（未検証の主張）の一覧 | [`conjectures/`](conjectures/) |
| Lean 4 による形式証明 | [`lean/`](lean/) |
| Python による数値実験 | [`sim/`](sim/) |

次に取り組む予定のタスクは [`NEXT.md`](NEXT.md) にあります。
運用ルールの詳細は [`CLAUDE.md`](CLAUDE.md) を参照してください。

## 注意

- 対話ログとまとめには、AI が生成した内容が含まれます。検証済みの結果と、予想・推測とを区別して書くようにしていますが、内容の正しさは保証しません。
- 形式証明（Lean）は GitHub Actions で自動的に検証しています。ただし、形式化が元の主張を正しく表しているかは、別途確認が必要です。

## ライセンス

[CC0 1.0 Universal](LICENSE)。ただし、引用している他者の文章や書誌情報の権利は、それぞれの権利者に帰属します。
