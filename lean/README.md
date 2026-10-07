# Lean による形式証明

Lean 4 と Mathlib を使って、対話で出てきた主張を形式的に検証します。

## ビルド

```sh
lake exe cache get   # Mathlib のビルド済みキャッシュを取得
lake build
```

## ルール

- 各定理の文書コメントに、対応する自然言語の主張と、関係する予想の ID（`C-NNNN`）を書きます。
- `sorry` を残したまま `main` に入れません（CI で検査しています）。
- Mathlib は Reservoir を使わず、`lakefile.toml` で GitHub の URL を直接指定しています。
