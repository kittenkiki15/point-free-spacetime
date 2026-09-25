# CLAUDE.md — 運用ルール

このリポジトリは、点なし時空（point-free spacetime）による物理学についての考察を、ユーザーと Claude の対話を中心に進めるプロジェクトの公開用リポジトリです。
Claude はこのファイルのルールに従って作業します。

## セッションの始め方

1. まず [`NEXT.md`](NEXT.md) を読み、前回までの状況と次にやるべきタスクを確認する。
2. 必要に応じて、直近の `summaries/` と、優先度の高い予想（[`conjectures/README.md`](conjectures/README.md)）を読む。
3. 作業ブランチを最新の `main` から作る（または既存の作業ブランチに `main` を取り込む）。

## セッションの終え方

ユーザーがセッションの終了を告げたら（または区切りのよいところで）、次を行う。

1. **対話ログ**：セッション記録（`~/.claude/projects/<作業ディレクトリ>/<セッション ID>.jsonl`）を変換し、`logs/` に置く。
   ```sh
   python3 tools/export_log.py <セッション.jsonl> logs/YYYY-MM-DD_NN_<話題>.md \
     --title "YYYY-MM-DD 第 NN 回: <話題>" \
     --redact-file ../point-free-spacetime-private/redactions.txt
   ```
   - `redactions.txt`（非公開リポジトリ）には、個人情報の断片など、公開リポジトリに書けない伏せ字の語句を置く。新しい語句が出てきたら追記する。
   - 変換後は、伏せ字の漏れ（メールアドレス、API キー、他者の文章の長い引用など）がないか確認する。`grep -v '^#' <redactions.txt> | grep -icf - <ログ>` が 0 になること。
   - 個人情報の断片を、検索コマンドなどに直接書かない（ログに残るため）。検索には `redactions.txt` を使う。
   - ログはコミット直前に書き出すので、それ以降のやりとり（PR の作成など）は次回のログの冒頭に含めなくてよい。
2. **まとめ**：同じファイル名で `summaries/` にまとめを書く（書式は [`summaries/README.md`](summaries/README.md)）。
3. **関連ファイルの更新**：用語一覧、参考文献一覧、予想の一覧などを、そのセッションの内容に合わせて更新する。
4. **`NEXT.md` の更新**：次のセッションでやるべきタスクと、未解決の論点を書く。
5. 日本語のコミットメッセージでコミットし、作業ブランチを push して `main` への PR を作る。

セッションの後、ユーザーは `/clear` でコンテキストを初期化する。次のセッションで必要な情報は、すべてリポジトリ（特に `NEXT.md`）に残しておくこと。

## リポジトリの分担

| リポジトリ | 公開 | 置くもの |
| --- | --- | --- |
| `point-free-spacetime`（ここ） | 公開（CC0 1.0） | 対話ログ、まとめ、調査メモ、用語一覧、参考文献一覧、予想、Lean と Python のコード |
| `point-free-spacetime-private` | 非公開 | 論文の PDF など他者の著作物、公開に向かないメモ |

### 著作権と公開範囲

- 公開側には、他者の文章の長い引用、図、PDF を置かない。書誌情報と、必要最小限の短い引用（出典を明記）にとどめる。
- 対話ログに論文の本文が長く入った場合は、公開前に要約へ置き換える。
- 論文の PDF は非公開側の `papers/<引用キー>.pdf` に置く。引用キーは公開側の [`references.bib`](references.bib) と揃える。

## ディレクトリ構成

| パス | 内容 |
| --- | --- |
| [`NEXT.md`](NEXT.md) | 次のセッションでやるべきタスク |
| [`logs/`](logs/) | 対話ログ（セッション記録を変換したもの。1 セッション 1 ファイル） |
| [`summaries/`](summaries/) | 対話のまとめ（ログと同じファイル名） |
| [`surveys/`](surveys/) | 参考文献の調査メモ（論文ごと・テーマごと） |
| [`glossary.md`](glossary.md) | 用語一覧 |
| [`references.bib`](references.bib) | 参考文献一覧（BibTeX） |
| [`conjectures/`](conjectures/) | 予想（1 件 1 ファイル）と一覧 |
| [`lean/`](lean/) | Lean 4 + Mathlib による形式証明 |
| [`sim/`](sim/) | Python による数値実験 |
| [`docs/`](docs/) | 運用上の資料（[数式の書き方](docs/math-guide.md) など） |
| [`tools/`](tools/) | 補助スクリプト |

ファイル名の日付は `YYYY-MM-DD`、同じ日の複数セッションは `_01`、`_02` と番号を付ける。

## 言語と表記

- 文書は日本語を基本とする。
- 用語一覧では英語の原語を併記する（例: locale / ロケール）。本文でも、初出の専門用語には英語を併記する。
- 数式は [`docs/math-guide.md`](docs/math-guide.md) に従う。要点は次のとおり。
  - ブロック数式は ` ```math ` コードブロック、インライン数式は `` $`...`$ `` で書く。
  - 日本語と数式の境目には半角スペースを入れる。
  - 絶対値は `\left| x \right|`、特殊な文字は Unicode 文字（ℝ、𝐄 など）を直接書く。
  - 関数名と変数の間には `\,` を入れる（`\sin\,x`）。数式ではないドル記号は `\$` と書く。

## 予想の管理

未検証の主張は「予想」として [`conjectures/`](conjectures/) で管理する。

- 1 件 1 ファイル（`conjectures/C-NNNN.md`）。書式は [`conjectures/_template.md`](conjectures/_template.md)。
- **確度**・**重要度**・**検証費用**は、それぞれ「高・中・低」の段階で評価する。
- **優先度**（高・中・低）は、対話の中でユーザーと相談して決める。Claude が独断で決めない。
- 予想の**内容と評価**はファイルで、**作業の進み具合と議論**は GitHub の Issue で管理する。
  - Issue のタイトルは `[C-NNNN] <予想の短い名前>` とし、予想ファイルに Issue 番号を書く。
  - Issue には優先度に応じて `priority:high` などのラベルを付ける。
  - 予想の**状態**（未着手・検証中・証明済みなど）は予想ファイルを正本とする。Issue を開く・閉じるときは、予想ファイルと一覧表の状態も同じコミットで更新する。
- 予想を追加・更新したら、[`conjectures/README.md`](conjectures/README.md) の一覧表も更新する。

## 検証

### Lean（形式証明）

- [`lean/`](lean/) に置く。Mathlib は `lakefile.toml` で GitHub の URL を直接指定する（この環境では Reservoir にアクセスできないため）。
- 各定理の文書コメントに、対応する自然言語の主張と、関係する予想の ID を書く。
- `sorry` を残したまま `main` に入れない（CI で検査する）。
- Lean が保証するのは「形式化した命題が正しい」ことだけなので、形式化が元の主張を正しく表しているかはまとめの中で確認する。
- ローカルでの確認手順：
  ```sh
  cd lean
  lake exe cache get   # Mathlib のビルド済みキャッシュを取得
  lake build
  ```
  elan（Lean のバージョン管理ツール）が入っていない場合は、先に次を実行する。
  ```sh
  curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none
  export PATH="$HOME/.elan/bin:$PATH"
  ```

### Python（数値実験）

- [`sim/`](sim/) に置く。依存関係は `sim/pyproject.toml` で管理し、乱数のシードを固定する。
- 結果（図や数値）には、生成したスクリプトとパラメータを記録する。
- 確認手順：`cd sim && pip install -e '.[dev]' && python -m pytest`

## Git の運用

- `main` に直接 push しない。作業ブランチから `main` への PR を作る。
- コミットメッセージは日本語で書く。
- PR を作ると、次の GitHub Actions が動く。
  - `lean.yml`：Lean のビルドと `sorry` の検査
  - `python.yml`：Python のテスト
  - `codex-review.yml`：OpenAI のモデル（`gpt-6-sol`）によるクロスモデルレビュー（リポジトリの Secret `OPENAI_API_KEY` が必要）。対話の生ログ（`logs/`）は修正しないので、レビューの対象外とする
- レビューの指摘には、対応するか、対応しない理由を返信する。
