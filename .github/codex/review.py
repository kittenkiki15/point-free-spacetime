#!/usr/bin/env python3
"""OpenAI の Responses API でレビューを生成する。

使い方:
    OPENAI_API_KEY=... python3 review.py <プロンプト.md> <出力.md>

モデルにはツール（ファイルの読み取りやコマンドの実行）を与えない。
API キーはこのスクリプトだけが使い、モデルからは参照できない。
"""

import json
import os
import sys
import urllib.request

API_URL = "https://api.openai.com/v1/responses"


def main() -> int:
    prompt_path, output_path = sys.argv[1], sys.argv[2]
    body = {
        "model": os.environ.get("REVIEW_MODEL", "gpt-6-sol"),
        "reasoning": {"effort": os.environ.get("REVIEW_EFFORT", "high")},
        "input": open(prompt_path, encoding="utf-8").read(),
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=900) as res:
        data = json.load(res)

    texts = [
        c["text"]
        for item in data.get("output", [])
        if item.get("type") == "message"
        for c in item.get("content", [])
        if c.get("type") == "output_text"
    ]
    if not texts:
        print(f"レビューの本文がありませんでした: status={data.get('status')}", file=sys.stderr)
        return 1
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(texts).strip() + "\n")
    usage = data.get("usage", {})
    print(f"input_tokens={usage.get('input_tokens')} output_tokens={usage.get('output_tokens')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
