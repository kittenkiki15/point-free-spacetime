# 次のセッションでやること

最終更新: 2026-09-25（第 02 回セッションの終わり）

## 状況

- 第 01 回：リポジトリの運用ルールを決め、自動検証（Lean・Python・クロスモデルレビュー）を整えた。
  - 最終的な方式のクロスモデルレビュー（`pull_request_target`・Responses API）は、PR #2 で動作を確認済み。
- 第 02 回：点なし位相と論理・様相論理・因果・量子論のつながりを整理し、調査メモ・用語一覧・記号一覧・参考文献一覧を作った。
  - 詳細は [`summaries/2026-09-25_02_pointfree-logic.md`](summaries/2026-09-25_02_pointfree-logic.md) と [`surveys/2026-09-25_02_pointfree-topology-basics.md`](surveys/2026-09-25_02_pointfree-topology-basics.md)。
  - 本プロジェクトに最も近い先行研究として、Heunen–van der Schaaf の順序付きロケールの 2 本（`heunen2024`・`heunen2026`）を見つけた。PDF は非公開リポジトリの `papers/` にある。

## 次のタスク（この順で進める）

1. **Heunen–van der Schaaf の論文メモを作る**。
   - `heunen2024`（Ordered locales）と `heunen2026`（Causal coverage in ordered locales and spacetimes）を読み、`surveys/YYYY-MM-DD_NN_heunen2024.md` などに論文メモを書く。
   - 調査メモ 7 節の予想の候補（点なしの時制論理、点がないと表せない因果構造、量子と時空の点のなさの統一）が、既に扱われているかを確かめる。
   - 新しい用語・記号を用語一覧・記号一覧に加える。
2. **Lean で「完備ブール代数の点はアトムと対応する」を形式化する**。
   - Mathlib にある関連する定義（`Order.Frame`、`TopologicalSpace.Opens`、`Locale`、`FrameHom`、完全素フィルター、アトムなど）を確かめてから始める。
   - 調査メモ 1 節の証明の概略を参照。
3. **物理学での「点」の問題に進み、最初の予想を立てる**。確度・重要度・検証費用・優先度は対話で評価する。

## ユーザーにお願いしていること

- [ ] （任意）追加の調査候補の PDF の入手。候補は調査メモの末尾と、第 02 回のまとめの「未解決の論点」を参照。
- [ ] （任意）`main` ブランチの保護ルールで、PR と CI の成功を必須にする。

## 未解決の論点

- 調査メモの未確認事項（正則開集合の例、$`ℕ → ℝ`$ の全射の例の典拠など）。
