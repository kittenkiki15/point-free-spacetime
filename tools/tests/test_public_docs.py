"""公開側の Markdown（logs/ を除く）に、対話ログと同じ個人情報・秘密情報・長い引用の検査を掛ける（第 32 回。
T-0027 のリリース前の確認でユーザーと決めた）。

対話ログ（logs/）は tools/live_log.py の sync が、公開の前に同じ検査を掛ける。ここでは、調査メモ・まとめなど
ふだんの作業で書くファイルに掛ける。伏せ字の語句（非公開リポジトリの redactions.txt）は CI からは読めないので、
ここでは照合せず、形の検査（メールアドレス・電話番号・既知の形式のキー・高エントロピーの文字列・長い引用）だけを行う。
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import live_log  # noqa: E402

LINK_TARGET = re.compile(r"\]\(([^)]*)\)")
# ID のリンクだけのセル。リンク先は、クエリ・断片のない相対パスに限る（クエリにキーを入れたものは除かない）
ID_LINK_CELL = re.compile(r"^(\[[DACRTQ]-\d{4}\] +(\.\./)*[\w/.-]*[DACRTQ]-\d{4}\.md[、,〜 ]*)+$")


def keep_query(m) -> str:
    """リンク先は、相対リンクも外部の URL も検査に残す（パスやクエリにキーなどが入り得るため。PR #73 の
    レビュー）。リポジトリに実在するファイルのパスは、検査の前に repo_paths で除くので、ファイル名の誤検出は起きない。
    リンクの記号だけを空白にして、表示文字とリンク先を別の語にする。"""
    return "] " + m.group(1)


def prepared(text: str) -> str:
    """検査の前に、誤検出のもとになる部分を除く。リンクの記号（リンク先は残し、実在する
    ファイルのパスは後段の repo_paths で除く）と、表の中の ID のリンクだけのセル（ID のリンクが並ぶ表は、日本語をほとんど含まない長い段落とみなされやすい）を除く。表のほかの
    セルは、行のまま残して検査する（文章の表を長い引用の検査から外さないため。PR #73 のレビュー）。"""
    out = []
    for line in text.splitlines():
        line = LINK_TARGET.sub(keep_query, line)
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            line = "| " + " | ".join(c for c in cells if not ID_LINK_CELL.fullmatch(c)) + " |"
        out.append(line)
    return "\n".join(out)


def repo_paths() -> list[str]:
    """リポジトリのファイルのパス（拡張子を除いた形も）。ファイル名（例：retrospective-stage-A）は、大文字を含むと
    高エントロピーの文字列とみなされるので、実在するファイルのパスは除いてから検査する。"""
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True).stdout.decode()
    paths = [p for p in out.split("\0") if p]
    # 相対リンクはディレクトリを省いて書くので、ファイル名（拡張子つき・なし）も加える
    names = {q for p in paths for q in (p, p.rsplit(".", 1)[0], p.rsplit("/", 1)[-1], p.rsplit("/", 1)[-1].rsplit(".", 1)[0])}
    return sorted((q for q in names if len(q) >= 8), key=len, reverse=True)


def public_markdown() -> list[Path]:
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--cached", "--others", "--exclude-standard",
                          "*.md"], capture_output=True, check=True).stdout.decode("utf-8")
    return [ROOT / p for p in out.split("\0") if p and not p.startswith("logs/") and (ROOT / p).is_file()]


def test_public_markdown_passes_the_log_checks():
    problems, paths = {}, repo_paths()
    for f in public_markdown():
        text = prepared(f.read_text(encoding="utf-8"))
        for p in paths:
            text = text.replace(p, "")
        bad = live_log.check(text, [], header_lines=0)
        if bad:
            problems[str(f.relative_to(ROOT))] = bad
    assert problems == {}


def test_prepared_text_still_detects_quotes_and_secrets():
    # リンク先と表を除いても、本文の長い引用と、本文に書いたキーの形の文字列は検出する
    quote = "\n".join("> " + "The quick brown fox jumps over the lazy dog again and again." for _ in range(12))
    assert live_log.check(prepared(quote), [], header_lines=0)
    assert live_log.check(prepared("鍵は " + "ghp_" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8" + " だった"), [],
                          header_lines=0)
    # URL のクエリに入れたキーは検出する
    assert live_log.check(prepared("[資料](https://example.org/x?token=" + "ghp_" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8)"),
                          [], header_lines=0)
    # 相対リンクのパスや、表の中のリンクの表示文字に入れたキーも検出する
    key = "ghp_" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8"
    assert live_log.check(prepared(f"[資料](../surveys/{key}.md)"), [], header_lines=0)
    assert live_log.check(prepared(f"| 項目 | [{key}](../definitions/D-0001.md) |"), [], header_lines=0)
    assert live_log.check(prepared(f"| 項目 | [D-0001](../definitions/D-0001.md?token={key}) |"), [], header_lines=0)
    # 外部の URL のパスに入れたキーも検出する
    assert live_log.check(prepared("[資料](https://files.example.org/share/" + "ghp_" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8)"),
                          [], header_lines=0)
    # 短いセルに分けて表に貼った英文も、行のまま長い引用の検査に掛かる
    table = "\n".join("| " + " | ".join(["The quick brown fox jumps over the lazy dog"] * 3) + " |" for _ in range(8))
    assert live_log.check(prepared(table), [], header_lines=0)
    # 表の行の ID のリンクの並びは、長い引用とみなさない
    row = "| 依存する ID | " + "、".join(f"[D-{n:04d}](../definitions/D-{n:04d}.md)" for n in range(1, 40)) + " |"
    assert live_log.check(prepared(row), [], header_lines=0) == []
