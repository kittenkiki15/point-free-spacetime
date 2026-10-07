"""tools/live_log.py と、共通の変換（export_log.convert_records）のテスト。

1 ターンごとの対話ログ（T-0025 の 1）で、発言の集め方と公開前の検査を確かめる。
"""

import importlib.util
import json
import sys
from pathlib import Path

_tools = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_tools))
_spec = importlib.util.spec_from_file_location("live_log", _tools / "live_log.py")
live_log = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(live_log)
export_log = live_log.export_log


def write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows), encoding="utf-8")


CWD = "/work"


def user(text, ts, uuid, sid="s1", cwd=CWD):
    return {"type": "user", "uuid": uuid, "sessionId": sid, "timestamp": ts, "cwd": cwd,
            "message": {"role": "user", "content": text}}


def assistant(blocks, ts, uuid, sid="s1"):
    return {"type": "assistant", "uuid": uuid, "sessionId": sid, "timestamp": ts,
            "message": {"role": "assistant", "content": blocks}}


def queued(text, ts, uuid, kind="human", source="q-src", sid="s1"):
    return {"type": "attachment", "uuid": uuid, "sessionId": sid, "timestamp": ts,
            "attachment": {"type": "queued_command", "prompt": text, "source_uuid": source,
                           "origin": {"kind": kind}}}


REPO_CWD = CWD + "/point-free-spacetime"


def touch(sid):
    """そのセッションがリポジトリの下で作業した記録（期間の外。セッションの確認に使う）。"""
    return user("<command-name>/x</command-name>", "2026-01-01T00:00:00Z", f"touch-{sid}", sid=sid, cwd=REPO_CWD)


def assistant_cwd(row):
    row["cwd"] = CWD
    return row


def test_collect_merges_files_dedupes_and_sorts(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        touch("s1"), touch("s2"),
        user("前の回", "2026-10-06T00:00:00Z", "u0"),
        user("一つ目", "2026-10-06T01:00:00Z", "u1"),
        assistant_cwd(assistant([{"type": "text", "text": "三つ目"}], "2026-10-06T03:00:00Z", "a3")),
    ])
    write(tmp_path / "-work" / "b.jsonl", [
        user("一つ目", "2026-10-06T01:00:00Z", "u1"),  # 別のファイルに写された同じ行
        user("二つ目", "2026-10-06T02:00:00Z", "u2", sid="s2"),
    ])
    rows = live_log.collect(tmp_path, "2026-10-06T00:30:00Z", workdir=Path(CWD))
    assert [r["uuid"] for r in rows] == ["u1", "u2", "a3"]


def test_collect_ignores_other_projects_and_other_cwd(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        touch("s1"),
        user("この研究の発言", "2026-10-06T01:00:00Z", "u1"),
        user("同じディレクトリの記録だが、作業ディレクトリが外", "2026-10-06T01:00:01Z", "u2", cwd="/other"),
    ])
    write(tmp_path / "-other" / "b.jsonl", [
        user("別のプロジェクトの同時刻の私的な発言", "2026-10-06T01:00:00Z", "x1", cwd="/other"),
    ])
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD))
    assert [r["uuid"] for r in rows] == ["u1"]


def test_public_log_keeps_utterances_only_with_time_and_branch():
    rows = [
        user("質問", "2026-10-06T01:00:00Z", "u1"),
        assistant([{"type": "text", "text": "答え"},
                   {"type": "tool_use", "id": "t1", "name": "Bash", "input": {"command": "ls 秘密のコマンド"}}],
                  "2026-10-06T01:00:05Z", "a1"),
        {"type": "user", "uuid": "r1", "sessionId": "s1", "timestamp": "2026-10-06T01:00:06Z",
         "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "t1", "content": "結果の本文"}]}},
        user("別の分岐の発言", "2026-10-06T01:01:00Z", "u2", sid="s2"),
    ]
    out = export_log.convert_records(rows, "t", include_tools=False, show_time=True, header=[])
    assert "質問" in out and "答え" in out and "別の分岐の発言" in out
    assert "秘密のコマンド" not in out and "結果の本文" not in out
    assert "## ユーザー（2026-10-06 01:00:00 UTC、記録 1）" in out
    assert "## ユーザー（2026-10-06 01:01:00 UTC、記録 2）" in out


def test_queued_human_messages_are_kept_and_others_dropped():
    rows = [
        queued("途中に送った発言", "2026-10-06T01:00:00Z", "q1"),
        queued("<task-notification>通知</task-notification>", "2026-10-06T01:00:01Z", "q2", kind="system"),
        # 通常の発言としても記録されたもの（source_uuid が一致）は二重に出さない
        queued("二重の発言", "2026-10-06T01:00:02Z", "q3", source="u9"),
        user("二重の発言", "2026-10-06T01:00:03Z", "u9"),
        user("Stop hook feedback:\n[~/.claude/stop-hook-git-check.sh]: 未コミットの変更があります", "2026-10-06T01:00:04Z", "u10") | {"isMeta": True},
    ]
    out = export_log.convert_records(rows, "t", include_tools=False, show_time=True, header=[])
    assert "途中に送った発言" in out
    assert "通知" not in out
    assert out.count("二重の発言") == 1
    assert "Stop hook" not in out


def test_check_accepts_ordinary_log(monkeypatch):
    monkeypatch.setattr(live_log, "is_commit", lambda t: t == "9712480f20ea7ebfd4743de5bd246cab42c7cd24")
    text = "# t\n\n> 見出し\n\n## ユーザー\n\nコミット 9712480f20ea7ebfd4743de5bd246cab42c7cd24 を確かめる。\n"
    assert live_log.check(text, ["伏せる語"], header_lines=1) == []


def test_check_flags_terms_contacts_secrets_and_quotes():
    key = "Ab3" + "xYz9Qw8Er7Ty6Ui5Op4As3Df2Gh1Jk0Lz"
    quote = "\n".join(["> 引用の行"] * 9)
    english = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    text = f"# t\n\n伏せる語 と 03-1234-5678 と {key}\n\n{quote}\n\n{english}\n"
    problems = live_log.check(text, ["伏せる語"], header_lines=0)
    joined = "\n".join(problems)
    assert "伏せ字の語句" in joined
    assert "電話番号" in joined
    assert "高エントロピー" in joined
    assert "引用のブロック" in joined
    assert "日本語をほとんど含まない" in joined


def test_check_flags_long_english_inside_code_blocks():
    english = "\n".join(["the quick brown fox jumps over the lazy dog"] * 20)
    text = f"# t\n\n```text\n{english}\n```\n"
    assert any("日本語をほとんど含まない" in p for p in live_log.check(text, [], header_lines=0))


def test_check_flags_known_key_formats_even_if_short():
    aws = "AKIA" + "ABCDEFGHIJKLMNOP"  # 20 文字（高エントロピーの検査の長さに届かない）
    assert any("既知の形式" in p for p in live_log.check(f"キー {aws}", [], header_lines=0))


def test_slug_is_restricted():
    assert live_log.SLUG.fullmatch("operations-improvement")
    for bad in ("Name", "a_b", "日本語", "a--b", "-a", "a/b"):
        assert not live_log.SLUG.fullmatch(bad)


def test_commit_and_push_resends_unpushed_commit(tmp_path):
    import subprocess

    def run(*args, cwd):
        subprocess.run(args, cwd=cwd, check=True, capture_output=True)

    remote, work = tmp_path / "remote.git", tmp_path / "work"
    run("git", "init", "-q", "--bare", str(remote), cwd=tmp_path)
    run("git", "init", "-q", "-b", "work-branch", str(work), cwd=tmp_path)
    for k, v in (("user.name", "t"), ("user.email", "t@example.invalid"), ("commit.gpgsign", "false")):
        run("git", "config", k, v, cwd=work)
    run("git", "remote", "add", "origin", str(remote), cwd=work)
    (work / "logs").mkdir()
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    assert "push した" in live_log.commit_and_push(work, ["logs/a.md"], "m1")
    # push に失敗した状態を作る（コミットだけを進める）
    (work / "logs" / "a.md").write_text("2\n", encoding="utf-8")
    run("git", "commit", "-q", "-am", "m2", cwd=work)
    # 内容が変わらなくても、未 push のコミットを送る
    assert "push した" in live_log.commit_and_push(work, ["logs/a.md"], "m3")
    assert "変更なし" in live_log.commit_and_push(work, ["logs/a.md"], "m4")


def test_check_rows_names_the_message_and_overrides_resolve_it():
    english = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    rows = [user("ふつうの発言", "2026-10-06T01:00:00Z", "u1"),
            user(english, "2026-10-06T01:01:00Z", "u2")]
    problems = live_log.check_rows(rows, [], {})
    assert len(problems) == 1 and "u2" in problems[0]
    # 誤検出として確認済みにする
    assert live_log.check_rows(rows, [], {"u2": {"approve": "自分の英文"}}) == []
    # 要約で置き換える
    replaced = live_log.apply_overrides(rows, {"u2": {"replace": "英文の論文の一節を引用した（要約）"}})
    assert live_log.check_rows(replaced, [], {}) == []
    out = export_log.convert_records(replaced, "t", include_tools=False, header=[])
    assert "quick brown fox" not in out and "要約に置き換えた" in out
    assert rows[1]["message"]["content"] == english  # もとの行は変えない


def test_collect_excludes_sibling_projects_under_workdir(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        touch("s1"),
        user("親ディレクトリでの発言", "2026-10-06T01:00:00Z", "u1"),
        user("公開リポジトリでの発言", "2026-10-06T01:00:01Z", "u2", cwd=CWD + "/point-free-spacetime/tools"),
        user("非公開リポジトリでの発言", "2026-10-06T01:00:02Z", "u3", cwd=CWD + "/point-free-spacetime-private"),
        user("兄弟の別プロジェクトの発言", "2026-10-06T01:00:03Z", "x1", cwd=CWD + "/other-project"),
        user("名前の前方が一致するだけの別ディレクトリ", "2026-10-06T01:00:04Z", "x2",
             cwd=CWD + "/point-free-spacetime-other"),
    ])
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD))
    assert [r["uuid"] for r in rows] == ["u1", "u2", "u3"]


def test_approve_skips_only_quote_checks():
    english = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    key = "Ab3" + "xYz9Qw8Er7Ty6Ui5Op4As3Df2Gh1Jk0Lz"
    rows = [user(f"{english} {key}", "2026-10-06T01:00:00Z", "u1")]
    problems = live_log.check_rows(rows, [], {"u1": {"approve": "自分の英文"}})
    assert len(problems) == 1 and "高エントロピー" in problems[0]


def test_approve_tokens_skips_only_the_approved_high_entropy_string():
    """approve_tokens は、ハッシュが一致する高エントロピーの文字列だけを通す（T-0027 の 2）。"""
    key = "Ab3" + "xYz9Qw8Er7Ty6Ui5Op4As3Df2Gh1Jk0Lz"
    other = "Zq9" + "wErT5yUi7oPa1sDf3gHj6kLz8xCv2bNm"
    h = live_log.token_hash(key)
    assert len(h) < 32 and not live_log.check(f"ハッシュ {h}", [], header_lines=0)  # ハッシュ自体は検査に掛からない
    rows = [user(f"URL の一部 {key}", "2026-10-06T01:00:00Z", "u1")]
    held = live_log.check_rows(rows, [], {})
    assert len(held) == 1 and h in held[0] and key not in held[0]  # 保留の表示はハッシュだけ
    assert live_log.check_rows(rows, [], {"u1": {"approve_tokens": {h: "誤検出"}}}) == []
    # 承認は、その発言の、その文字列にしか効かない
    assert live_log.check_rows(rows, [], {"u2": {"approve_tokens": {h: "誤検出"}}})
    rows2 = [user(f"{key} と {other}", "2026-10-06T01:00:00Z", "u1")]
    left = live_log.check_rows(rows2, [], {"u1": {"approve_tokens": {h: "誤検出"}}})
    assert len(left) == 1 and live_log.token_hash(other) in left[0] and h not in left[0]
    # 電話番号などは、承認では通らない（既知の形式のキーとメールアドレスは、変換のときに伏せ字になる）
    phone = "0312345678"
    rows3 = [user(f"電話 {phone}", "2026-10-06T01:00:00Z", "u1")]
    assert live_log.check_rows(rows3, [], {"u1": {"approve": "x", "approve_tokens": {live_log.token_hash(phone): "x"}}})


def _private(tmp_path, monkeypatch):
    """非公開リポジトリの代わり（CI には非公開リポジトリがない）。"""
    private = tmp_path / "private"
    private.mkdir(exist_ok=True)
    (private / "redactions.txt").write_text("# 語句なし\n", encoding="utf-8")
    monkeypatch.setattr(live_log, "PRIVATE", private)


def test_start_retries_closing_previous_session(tmp_path, monkeypatch):
    import argparse
    state = tmp_path / "live.json"
    state.write_text(json.dumps({"number": 1, "slug": "a", "title": "t", "since": "2026-10-01T00:00:00Z",
                                 "date": "2026-10-01"}), encoding="utf-8")
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    results = iter([1, 0, 0])  # 1 回目の同期は保留、2 回目は成功、3 回目は新しい回の同期
    calls = []

    def fake_sync(a):
        calls.append(json.loads(state.read_text(encoding="utf-8")))
        return next(results)

    monkeypatch.setattr(live_log, "cmd_sync", fake_sync)
    a = argparse.Namespace(number=2, slug="b", title="t2", since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("前の回の同期が失敗したら、新しい回を始めない")
    except SystemExit:
        pass
    assert json.loads(state.read_text(encoding="utf-8"))["number"] == 1  # 新しい回の状態は書かない
    assert live_log.cmd_start(a) == 0  # やり直すと、前の回の同期を再試行する
    assert [c["number"] for c in calls] == [1, 1, 2]
    assert calls[1]["until"] == "2026-10-02T00:00:00Z"


def test_collect_excludes_sessions_not_confirmed_as_this_project(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        touch("s1"),
        user("この研究の発言", "2026-10-06T01:00:00Z", "u1"),
        # 同じ親ディレクトリから始めた、別の会話（リポジトリの下で作業していない）
        user("別の会話の発言", "2026-10-06T01:00:01Z", "x1", sid="other"),
    ])
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD))
    assert [r["uuid"] for r in rows] == ["u1"]


def test_collect_and_convert_keep_queued_message_without_cwd(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        touch("s1"),
        queued("cwd のない途中の発言", "2026-10-06T01:00:00Z", "q1"),  # queued() の行には cwd がない
        queued("確認できないセッションの途中の発言", "2026-10-06T01:00:01Z", "q2", sid="other"),
    ])
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD))
    out = export_log.convert_records(rows, "t", include_tools=False, header=[])
    assert "cwd のない途中の発言" in out
    assert "確認できないセッション" not in out


def test_log_name_validates_date_and_stays_in_logs():
    ok = {"date": "2026-10-06", "number": 29, "slug": "a-b"}
    assert live_log.log_name(ok) == "2026-10-06_29_a-b.md"
    for bad in ({**ok, "date": "../example"}, {**ok, "date": "2026-13-01"}, {**ok, "slug": "../x"},
                {**ok, "number": "29"}):
        try:
            live_log.log_name(bad)
            raise AssertionError(bad)
        except SystemExit:
            pass


def test_hex_tokens_are_suspicious_except_commit_sha(monkeypatch):
    sha = "9712480f20ea7ebfd4743de5bd246cab42c7cd24"
    monkeypatch.setattr(live_log, "is_commit", lambda t: t == sha)
    assert not live_log.looks_secret(sha)  # 実在するコミットの SHA
    assert live_log.looks_secret("f" * 40)  # 同じ形でも、コミットでなければ疑う
    assert live_log.looks_secret("0123456789abcdef0123456789abcdef")  # 32 文字の 16 進数
    assert live_log.looks_secret("a" * 64)


def test_interrupt_marker_only_with_tools():
    rows = [user([{"type": "text", "text": "[Request interrupted by user for tool use]"}], "2026-10-06T01:00:00Z", "u1")]
    assert "中断" not in export_log.convert_records(rows, "t", include_tools=False, header=[])
    assert "中断" in export_log.convert_records(rows, "t", header=[])


def _git_repo(tmp_path):
    import subprocess

    def run(*args, cwd):
        subprocess.run(args, cwd=cwd, check=True, capture_output=True)

    remote, work = tmp_path / "remote.git", tmp_path / "work"
    run("git", "init", "-q", "--bare", str(remote), cwd=tmp_path)
    run("git", "init", "-q", "-b", "work-branch", str(work), cwd=tmp_path)
    for k, v in (("user.name", "t"), ("user.email", "t@example.invalid"), ("commit.gpgsign", "false")):
        run("git", "config", k, v, cwd=work)
    run("git", "remote", "add", "origin", str(remote), cwd=work)
    (work / "logs").mkdir()
    return work, run


def test_push_refuses_unpushed_history_that_fails_checks(tmp_path):
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("最初\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    # 検査を通った版をコミットしたが push に失敗し、その後に伏せる語を登録した、という状況
    (work / "logs" / "a.md").write_text("伏せる語\n", encoding="utf-8")
    run("git", "commit", "-q", "-am", "m2", cwd=work)
    (work / "logs" / "a.md").write_text("[伏せ字]\n", encoding="utf-8")
    try:
        live_log.commit_and_push(work, ["logs/a.md"], "m3", verify=live_log.history_problems(["伏せる語"]))
        raise AssertionError("未 push の履歴に伏せる語があれば push しない")
    except SystemExit as e:
        assert "公開できない版" in str(e)
    # この呼び出しで作ったコミット（m3）は取り消してある
    log = subprocess_out(work, "git", "log", "--format=%s")
    assert log.split() == ["m2", "m1"]


def subprocess_out(cwd, *args):
    import subprocess
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


def test_failed_push_rolls_back_the_new_commit(tmp_path):
    work, run = _git_repo(tmp_path)
    run("git", "remote", "set-url", "origin", str(tmp_path / "missing.git"), cwd=work)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    import time as _time
    sleep = live_log.time.sleep
    live_log.time.sleep = lambda s: None
    try:
        try:
            live_log.commit_and_push(work, ["logs/a.md"], "m1")
            raise AssertionError("push に失敗するはず")
        except SystemExit as e:
            assert "取り消した" in str(e)
    finally:
        live_log.time.sleep = sleep
    assert subprocess_out(work, "git", "rev-list", "--all").strip() == ""


def test_lost_messages_detects_dropped_utterances():
    old = "## ユーザー（2026-10-06 01:00:00 UTC、記録 1）\n\na\n\n## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nb\n"
    # 記録の番号が変わっても、発言者と時刻が同じなら同じ発言とみなす
    same = old.replace("記録 1", "記録 2") + "## ユーザー（2026-10-06 02:00:00 UTC、記録 2）\n\nc\n"
    assert live_log.lost_messages(old, same) == []
    shrunk = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nb\n"
    assert live_log.lost_messages(old, shrunk) == ["ユーザー（2026-10-06 01:00:00 UTC）"]


def test_collect_accepts_registered_session_without_repo_cwd(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        user("親ディレクトリのままの会話", "2026-10-06T01:00:00Z", "u1", sid="s9"),
    ])
    assert live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD)) == []
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), known_sessions={"s9"})
    assert [r["uuid"] for r in rows] == ["u1"]


def test_history_check_includes_quotes_except_the_checked_version():
    quote = "\n".join(["> 引用の行"] * 15)  # 公開側の見出しの引用（3 行）より後に、8 行以上続く
    old = f"# t\n\n{quote}\n"
    verify = live_log.history_problems([], checked={old})
    assert verify(old) == []  # 今の版（確認済み）と同じ中身は除く
    assert any("引用のブロック" in p for p in verify(old + "\n追記\n"))


def test_lost_messages_counts_same_second_messages():
    two = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\na\n\n## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nb\n"
    one = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\na\n"
    assert live_log.lost_messages(two, one) == ["Claude（2026-10-06 01:00:05 UTC）"]


def test_unpushed_history_includes_merge_commits(tmp_path):
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    run("git", "checkout", "-q", "-b", "side", cwd=work)
    (work / "logs" / "a.md").write_text("side\n", encoding="utf-8")
    run("git", "commit", "-q", "-am", "side", cwd=work)
    run("git", "checkout", "-q", "work-branch", cwd=work)
    (work / "logs" / "a.md").write_text("main\n", encoding="utf-8")
    run("git", "commit", "-q", "-am", "main", cwd=work)
    subprocess_run_ok = __import__("subprocess").run(["git", "merge", "-q", "side", "-m", "merge"], cwd=work,
                                                     capture_output=True)
    assert subprocess_run_ok.returncode != 0  # 競合する
    # 競合の解決で、どちらの親にもない内容（伏せる語）を入れたマージコミット
    (work / "logs" / "a.md").write_text("伏せる語\n", encoding="utf-8")
    run("git", "commit", "-q", "-am", "merge", cwd=work)
    (work / "logs" / "a.md").write_text("[伏せ字]\n", encoding="utf-8")
    run("git", "commit", "-q", "-am", "fix", cwd=work)
    texts = [t for _, _, t in live_log.unpushed_log_versions(work, "work-branch")]
    assert "伏せる語\n" in texts


def test_phone_numbers_without_separators():
    for t in ("電話は08012345678です", "0312345678", "+819012345678"):
        assert any("電話番号" in p for p in live_log.check(t, [], header_lines=0)), t
    for t in ("0123456789abcdef0123", "2026-10-06T01:00:00Z", "12345678901"):
        assert not any("電話番号" in p for p in live_log.check(t, [], header_lines=0)), t


def test_lost_messages_detects_replaced_body():
    old = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nA\n"
    new = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nB\n"
    assert live_log.lost_messages(old, new) == ["Claude（2026-10-06 01:00:05 UTC）"]
    assert live_log.lost_messages(old, old.replace("記録 1", "記録 2")) == []
    assert live_log.lost_messages(old, old + "\n<details>ツールの結果</details>\n") == []


def test_collect_reports_untimed_messages(tmp_path):
    untimed_row = user("時刻のない発言", None, "u2")
    del untimed_row["timestamp"]
    write(tmp_path / "-work" / "a.jsonl", [touch("s1"), user("発言", "2026-10-06T01:00:00Z", "u1"), untimed_row])
    untimed = []
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), untimed=untimed)
    assert [r["uuid"] for r in rows] == ["u1"]
    assert [d["uuid"] for d in untimed] == ["u2"]


def test_secret_detection_for_two_character_classes():
    assert live_log.looks_secret("Q7X2M9K4P1Z8W3R6T5Y0V2N8B4C6D1F3")  # 英大文字と数字だけ
    assert live_log.looks_secret("q7x2m9k4p1z8w3r6t5y0v2n8b4c6d1f3g")  # 区切りのない小文字と数字
    assert not live_log.looks_secret("summaries/2026-10-06_29_operations-improvement")  # パス


def test_untimed_non_message_attachment_is_ignored(tmp_path):
    note = {"type": "attachment", "uuid": "n1", "sessionId": "s1", "cwd": CWD,
            "attachment": {"type": "queued_command", "prompt": "<task-notification>x</task-notification>",
                           "origin": {"kind": "system"}}}
    write(tmp_path / "-work" / "a.jsonl", [touch("s1"), note])
    untimed = []
    live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), untimed=untimed)
    assert untimed == []


def test_history_checks_file_names_of_deleted_files(tmp_path):
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    (work / "logs" / "secret-name.md").write_text("x\n", encoding="utf-8")
    run("git", "add", "logs/secret-name.md", cwd=work)
    run("git", "commit", "-q", "-m", "m2", cwd=work)
    run("git", "rm", "-q", "logs/secret-name.md", cwd=work)
    run("git", "commit", "-q", "-m", "m3", cwd=work)
    try:
        live_log.commit_and_push(work, ["logs/a.md"], "m4", verify=live_log.history_problems(["secret-name"]))
        raise AssertionError("履歴のファイル名に伏せる語があれば push しない")
    except SystemExit as e:
        assert "ファイル名" in str(e)


def test_start_continues_when_previous_records_are_lost(tmp_path, monkeypatch, capsys):
    import argparse
    state = tmp_path / "live.json"
    state.write_text(json.dumps({"number": 1, "slug": "a", "title": "t", "since": "2026-10-01T00:00:00Z",
                                 "date": "2026-10-01"}), encoding="utf-8")
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    results = iter([live_log.LOSS, 0])
    monkeypatch.setattr(live_log, "cmd_sync", lambda a: next(results))
    a = argparse.Namespace(number=2, slug="b", title="t2", since="2026-10-02T00:00:00Z", date=None)
    assert live_log.cmd_start(a) == 0
    assert json.loads(state.read_text(encoding="utf-8"))["number"] == 2
    assert "回収できなかった" in capsys.readouterr().err


def test_indented_quotes_are_counted():
    quote = "\n".join(["  > 字下げした引用の行"] * 9)
    assert any("引用のブロック" in p for p in live_log.check(f"# t\n\n{quote}\n", [], header_lines=0))
    quote = "\n".join(["- > 箇条書きの中の引用"] * 9)
    assert any("引用のブロック" in p for p in live_log.check(f"# t\n\n{quote}\n", [], header_lines=0))


def test_missing_versus_changed_messages():
    old = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nA\n\n## ユーザー（2026-10-06 01:00:09 UTC、記録 1）\n\nB\n"
    changed = old.replace("\nA\n", "\n[伏せ字]\n")
    assert live_log.lost_messages(old, changed) and not live_log.missing_messages(old, changed)
    dropped = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nA\n"
    assert live_log.missing_messages(old, dropped) == ["ユーザー（2026-10-06 01:00:09 UTC）"]


def test_start_stops_when_previous_bodies_changed(tmp_path, monkeypatch):
    import argparse
    state = tmp_path / "live.json"
    state.write_text(json.dumps({"number": 1, "slug": "a", "title": "t", "since": "2026-10-01T00:00:00Z",
                                 "date": "2026-10-01"}), encoding="utf-8")
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    monkeypatch.setattr(live_log, "cmd_sync", lambda a: live_log.CHANGED)
    a = argparse.Namespace(number=2, slug="b", title="t2", since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("本文が変わったら新しい回を始めない")
    except SystemExit:
        pass
    assert json.loads(state.read_text(encoding="utf-8"))["number"] == 1


def test_start_checks_metadata_before_writing(tmp_path, monkeypatch):
    import argparse
    state = tmp_path / "live.json"
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    monkeypatch.setattr(live_log, "PRIVATE", tmp_path / "private")
    (tmp_path / "private").mkdir()
    (tmp_path / "private" / "redactions.txt").write_text("伏せる語\n", encoding="utf-8")
    monkeypatch.setattr(live_log, "cmd_sync", lambda a: 0)
    a = argparse.Namespace(number=2, slug="b", title="伏せる語 の回", since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("タイトルが検査に当たれば書かない")
    except SystemExit:
        pass
    assert not state.exists()


def test_start_refuses_without_redactions(tmp_path, monkeypatch):
    import argparse
    monkeypatch.setattr(live_log, "STATE", tmp_path / "live.json")
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    monkeypatch.setattr(live_log, "PRIVATE", tmp_path / "missing")
    a = argparse.Namespace(number=2, slug="b", title="t", since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("redactions.txt がなければ止まる")
    except SystemExit as e:
        assert "redactions.txt" in str(e)


def test_sync_push_refuses_unpushed_non_log_commits(tmp_path):
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    (work / "tool.py").write_text("x = 1\n", encoding="utf-8")
    run("git", "add", "tool.py", cwd=work)
    run("git", "commit", "-q", "-m", "work", cwd=work)
    (work / "logs" / "a.md").write_text("2\n", encoding="utf-8")
    try:
        live_log.commit_and_push(work, ["logs/a.md"], "m2", verify=live_log.history_problems([]))
        raise AssertionError("ログ以外の未 push のコミットがあれば push しない")
    except SystemExit as e:
        assert "logs/ 以外" in str(e)
    assert subprocess_out(work, "git", "log", "--format=%s").split() == ["work", "m1"]


def test_sync_push_ignores_merged_history_with_stale_branch_ref(tmp_path):
    """前の PR のマージでリモートの作業ブランチが消え、追跡参照だけが古いまま残っていても、
    main に入ったマージのコミットを未 push の作業とみなさない（T-0027 の 1）。"""
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    (work / "tool.py").write_text("x = 1\n", encoding="utf-8")
    run("git", "add", "tool.py", cwd=work)
    run("git", "commit", "-q", "-m", "work", cwd=work)
    run("git", "push", "-q", "origin", "work-branch", cwd=work)
    # PR のマージ：main にマージのコミットを作り、リモートの作業ブランチを消す（追跡参照は残る）
    run("git", "checkout", "-q", "-b", "main", "HEAD~1", cwd=work)
    (work / "other.py").write_text("y = 1\n", encoding="utf-8")
    run("git", "add", "other.py", cwd=work)
    run("git", "commit", "-q", "-m", "other", cwd=work)
    run("git", "merge", "-q", "--no-ff", "work-branch", "-m", "merge", cwd=work)
    run("git", "push", "-q", "origin", "main", cwd=work)
    run("git", "push", "-q", "origin", "--delete", "work-branch", cwd=work)
    run("git", "update-ref", "refs/remotes/origin/work-branch", "main^2", cwd=work)
    run("git", "checkout", "-q", "-B", "work-branch", "origin/main", cwd=work)
    run("git", "branch", "-q", "-D", "main", cwd=work)
    assert live_log.unpushed_non_log_commits(work, "work-branch") == []
    (work / "logs" / "a.md").write_text("2\n", encoding="utf-8")
    assert "push した" in live_log.commit_and_push(work, ["logs/a.md"], "m2",
                                                   verify=live_log.history_problems([]))


def test_body_changed_even_with_missing_messages():
    old = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nA\n\n## ユーザー（2026-10-06 01:00:09 UTC、記録 1）\n\nB\n"
    both = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\n[伏せ字]\n"  # 一件は本文が変わり、一件は消えた
    assert live_log.missing_messages(old, both) and live_log.body_changed(old, both)
    only_missing = "## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\nA\n"
    assert not live_log.body_changed(old, only_missing)


def test_start_refuses_mismatched_until(tmp_path, monkeypatch):
    import argparse
    state = tmp_path / "live.json"
    state.write_text(json.dumps({"number": 1, "slug": "a", "title": "t", "since": "2026-10-01T00:00:00Z",
                                 "until": "2026-10-02T00:00:00Z", "date": "2026-10-01"}), encoding="utf-8")
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    monkeypatch.setattr(live_log, "cmd_sync", lambda a: 0)
    a = argparse.Namespace(number=2, slug="b", title="t2", since="2026-10-03T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("前の回の until と --since が違えば止まる")
    except SystemExit as e:
        assert "一致しない" in str(e)


def test_queued_message_kept_when_matching_user_row_is_not_output():
    rows = [
        queued("途中に送った発言", "2026-10-06T01:00:00Z", "q1", source="u1"),
        user("メタ情報の行", "2026-10-06T01:00:01Z", "u1") | {"isMeta": True},
    ]
    out = export_log.convert_records(rows, "t", include_tools=False, header=[])
    assert "途中に送った発言" in out and "メタ情報の行" not in out


def test_start_checks_new_metadata_before_closing_previous(tmp_path, monkeypatch):
    import argparse
    state = tmp_path / "live.json"
    prev = {"number": 1, "slug": "a", "title": "t", "since": "2026-10-01T00:00:00Z", "date": "2026-10-01"}
    state.write_text(json.dumps(prev), encoding="utf-8")
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    (tmp_path / "private" / "redactions.txt").write_text("伏せる語\n", encoding="utf-8")
    calls = []
    monkeypatch.setattr(live_log, "cmd_sync", lambda a: calls.append(1) or 0)
    a = argparse.Namespace(number=2, slug="b", title="伏せる語 の回", since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("新しい回の情報が検査に当たれば止まる")
    except SystemExit:
        pass
    assert calls == [] and json.loads(state.read_text(encoding="utf-8")) == prev  # 前の回は閉じていない


def test_queued_message_kept_when_matching_user_row_is_outside_period():
    rows = [
        queued("途中に送った発言", "2026-10-06T01:00:00Z", "q1", source="u1"),
        user("途中に送った発言", "2026-10-06T03:00:00Z", "u1"),  # 期間の外（次の回）
    ]
    out = export_log.convert_records(rows, "t", until="2026-10-06T02:00:00Z", include_tools=False, header=[])
    assert out.count("途中に送った発言") == 1


def test_sync_holds_when_no_user_message_is_collected(tmp_path, monkeypatch):
    import argparse
    repo, private = tmp_path / "repo", tmp_path / "private"
    (repo / "logs").mkdir(parents=True)
    private.mkdir()
    (private / "redactions.txt").write_text("# なし\n", encoding="utf-8")
    state = repo / "logs" / "live.json"
    state.write_text(json.dumps({"number": 1, "slug": "a", "title": "t", "since": "2026-10-06T00:00:00Z",
                                 "date": "2026-10-06"}), encoding="utf-8")
    for k, v in (("REPO", repo), ("PRIVATE", private), ("STATE", state), ("OVERRIDES", private / "o.json"),
                 ("SESSIONS", private / "s.json")):
        monkeypatch.setattr(live_log, k, v)
    monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    a = argparse.Namespace(projects=tmp_path / "projects", no_push=True, allow_loss=False)
    assert live_log.cmd_sync(a) == live_log.HELD
    assert not (repo / "logs" / "2026-10-06_01_a.md").exists()


def test_queued_message_is_kept_across_two_syncs():
    first = [queued("途中に送った発言", "2026-10-06T01:00:00Z", "q1", source="u1")]
    later = first + [user("途中に送った発言", "2026-10-06T01:00:30Z", "u1")]
    a = export_log.convert_records(first, "t", include_tools=False, show_time=True, header=[])
    b = export_log.convert_records(later, "t", include_tools=False, show_time=True, header=[])
    assert b.count("途中に送った発言") == 1
    assert live_log.lost_messages(a, b) == []  # 先に公開した時刻と表示が保たれる


def test_string_interrupt_marker_is_not_an_utterance():
    rows = [user("[Request interrupted by user]", "2026-10-06T01:00:00Z", "u1")]
    out = export_log.convert_records(rows, "t", include_tools=False, header=[])
    assert "Request interrupted" not in out and "ユーザー" not in out


def _start_env(tmp_path, monkeypatch, prev):
    state = tmp_path / "live.json"
    state.write_text(json.dumps(prev), encoding="utf-8")
    monkeypatch.setattr(live_log, "STATE", state)
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    monkeypatch.setattr(live_log, "cmd_sync", lambda a: 0)
    return state


def test_start_same_number_requires_same_info(tmp_path, monkeypatch):
    import argparse
    prev = {"number": 2, "slug": "b", "title": "t2", "since": "2026-10-02T00:00:00Z", "date": "2026-10-02"}
    state = _start_env(tmp_path, monkeypatch, prev)
    same = argparse.Namespace(number=2, slug="b", title="t2", since="2026-10-02T00:00:00Z", date=None)
    assert live_log.cmd_start(same) == 0
    other = argparse.Namespace(number=2, slug="c", title="t2", since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(other)
        raise AssertionError("同じ番号で別の情報なら止まる")
    except SystemExit:
        pass
    assert json.loads(state.read_text(encoding="utf-8")) == prev


def test_start_validates_since_fully_and_order(tmp_path, monkeypatch):
    import argparse
    prev = {"number": 1, "slug": "a", "title": "t", "since": "2026-10-02T00:00:00Z", "date": "2026-10-02"}
    state = _start_env(tmp_path, monkeypatch, prev)
    for since in ("2026-10-03Tbad", "2026-10-01T00:00:00Z"):  # 時刻として不正、前の回より前
        a = argparse.Namespace(number=2, slug="b", title="t2", since=since, date=None)
        try:
            live_log.cmd_start(a)
            raise AssertionError(since)
        except SystemExit:
            pass
        assert json.loads(state.read_text(encoding="utf-8")) == prev


def test_collect_keeps_distinct_rows_without_uuid(tmp_path):
    a = queued("一つ目の途中の発言", "2026-10-06T01:00:00Z", None, source="s-a")
    b = queued("二つ目の途中の発言", "2026-10-06T01:00:00Z", None, source="s-b")
    for r in (a, b):
        del r["uuid"]
        r["cwd"] = CWD
    write(tmp_path / "-work" / "a.jsonl", [touch("s1"), a, b, dict(a)])  # 最後は同じ行の写し
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD))
    assert sorted(r["attachment"]["prompt"] for r in rows) == ["一つ目の途中の発言", "二つ目の途中の発言"]


def test_sidechain_queued_does_not_hide_user_row():
    side = queued("同じ発言", "2026-10-06T01:00:00Z", "q1", source="u1") | {"isSidechain": True}
    rows = [side, user("同じ発言", "2026-10-06T01:00:30Z", "u1")]
    out = export_log.convert_records(rows, "t", include_tools=False, header=[])
    assert out.count("同じ発言") == 1


def test_output_predicates_match_conversion():
    side = queued("x", "2026-10-06T01:00:00Z", "q1") | {"isSidechain": True}
    claude = assistant([{"type": "text", "text": "Claude の発言"}], "2026-10-06T01:00:00Z", "a1")
    assert not export_log.is_output_queued(side)
    assert not export_log.is_output_user(claude)
    assert export_log.is_output_queued(queued("y", "2026-10-06T01:00:00Z", "q2"))
    assert export_log.is_output_user(user("z", "2026-10-06T01:00:00Z", "u3"))


def test_sync_holds_when_only_claude_messages_are_collected(tmp_path, monkeypatch):
    import argparse
    repo, private, projects = tmp_path / "repo", tmp_path / "private", tmp_path / "projects"
    (repo / "logs").mkdir(parents=True)
    private.mkdir()
    (private / "redactions.txt").write_text("# なし\n", encoding="utf-8")
    state = repo / "logs" / "live.json"
    state.write_text(json.dumps({"number": 1, "slug": "a", "title": "t", "since": "2026-10-06T00:00:00Z",
                                 "date": "2026-10-06"}), encoding="utf-8")
    for k, v in (("REPO", repo), ("PRIVATE", private), ("STATE", state), ("OVERRIDES", private / "o.json"),
                 ("SESSIONS", private / "s.json")):
        monkeypatch.setattr(live_log, k, v)
    monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    row = assistant([{"type": "text", "text": "Claude の発言だけ"}], "2026-10-06T01:00:00Z", "a1")
    monkeypatch.setattr(live_log, "collect", lambda *x, **k: [row])  # 集まったのが Claude の発言だけの場合
    a = argparse.Namespace(projects=projects, no_push=True, allow_loss=False)
    assert live_log.cmd_sync(a) == live_log.HELD


def test_untimed_row_without_session_is_reported(tmp_path):
    row = user("時刻もセッションもない発言", None, "u2", cwd=REPO_CWD)
    del row["timestamp"], row["sessionId"]
    write(tmp_path / "-work" / "a.jsonl", [touch("s1"), user("発言", "2026-10-06T01:00:00Z", "u1"), row])
    untimed = []
    live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), untimed=untimed)
    assert [d["uuid"] for d in untimed] == ["u2"]


def test_start_refuses_long_english_title(tmp_path, monkeypatch):
    import argparse
    monkeypatch.setattr(live_log, "STATE", tmp_path / "live.json")
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    title = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    a = argparse.Namespace(number=2, slug="b", title=title, since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("長い英文のタイトルは書かない")
    except SystemExit:
        pass
    assert not (tmp_path / "live.json").exists()


def test_override_on_user_row_applies_to_output_queued_row():
    english = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    rows = [queued(english, "2026-10-06T01:00:00Z", "q1", source="u1"), user(english, "2026-10-06T01:00:30Z", "u1")]
    replaced = live_log.apply_overrides(rows, {"u1": {"replace": "英文の一節（要約）"}})
    public = export_log.convert_records(replaced, "t", include_tools=False, show_time=True, header=[])
    assert "quick brown fox" not in public and "英文の一節（要約）" in public
    assert live_log.check_rows(replaced, [], {"u1": {"replace": "英文の一節（要約）"}}) == []


def test_override_by_content_id_for_row_without_uuid():
    english = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    row = queued(english, "2026-10-06T01:00:00Z", None)
    del row["uuid"]
    problems = live_log.check_rows([row], [], {})
    rid = live_log.row_id(row)
    assert rid.startswith("h-") and rid in problems[0] and live_log.row_id(dict(row)) == rid
    replaced = live_log.apply_overrides([row], {rid: {"replace": "要約"}})
    public = export_log.convert_records(replaced, "t", include_tools=False, header=[])
    assert "quick brown fox" not in public and "要約" in public


def test_current_session_is_not_guessed(monkeypatch):
    monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    assert live_log.current_session() is None  # 更新時刻などから推測しない
    assert live_log.current_session("explicit") == "explicit"
    monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "env-session")
    assert live_log.current_session() == "env-session"


def test_output_row_without_session_is_reported(tmp_path):
    row = user("セッションのない発言", "2026-10-06T01:00:01Z", "u2", cwd=REPO_CWD)
    del row["sessionId"]
    write(tmp_path / "-work" / "a.jsonl", [touch("s1"), user("発言", "2026-10-06T01:00:00Z", "u1"), row])
    untimed = []
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), untimed=untimed)
    assert [d["uuid"] for d in rows] == ["u1"] and [d["uuid"] for d in untimed] == ["u2"]


def test_secret_detection_beyond_path_like_tokens():
    assert live_log.looks_secret("QWERTYUIOPASDFGHJKLZXCVBNMQAZWSXEDCRFV")  # 英大文字だけ
    assert live_log.looks_secret("q7x2m9k4/p1z8w3r6t5y0v2n8b4c6d1f3g=")  # 小文字・数字に / と =
    assert not live_log.looks_secret("tools/tests/test_live_log-extra_files")  # パスの形


def test_unconfirmed_session_messages_are_reported_and_registry_resolves(tmp_path):
    write(tmp_path / "-work" / "a.jsonl", [
        touch("s1"),
        user("確かめた会話", "2026-10-06T01:00:00Z", "u1"),
        user("同期しなかった分岐の発言", "2026-10-06T01:00:01Z", "u2", sid="s2"),
    ])
    unconfirmed = []
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), unconfirmed=unconfirmed)
    assert [r["uuid"] for r in rows] == ["u1"] and [d["uuid"] for d in unconfirmed] == ["u2"]
    # 登録簿で、この研究の会話と確かめた場合
    unconfirmed = []
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), known_sessions={"s2"},
                            unconfirmed=unconfirmed)
    assert [r["uuid"] for r in rows] == ["u1", "u2"] and unconfirmed == []
    # 登録簿で、除くと決めた場合
    unconfirmed = []
    rows = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), excluded_sessions={"s2"},
                            unconfirmed=unconfirmed)
    assert [r["uuid"] for r in rows] == ["u1"] and unconfirmed == []


def test_registry_reads_included_and_excluded(tmp_path, monkeypatch):
    reg = tmp_path / "s.json"
    reg.write_text(json.dumps(["a", "!b"]), encoding="utf-8")
    monkeypatch.setattr(live_log, "SESSIONS", reg)
    assert live_log.load_sessions() == {"a"} and live_log.load_excluded() == {"b"}


def test_text_only_markers_are_not_dropped():
    rows = [user("Stop hook feedback とは何ですか？", "2026-10-06T01:00:00Z", "u1"),
            # 印（isMeta）のない行は、フックの通知の形でもユーザーの発言として残す
            user("Stop hook feedback:\n[~/.claude/x.sh]: 貼り付けた通知について質問です", "2026-10-06T01:00:01Z", "u2"),
            user("Stop hook feedback:\n[~/.claude/x.sh]: 本物の通知", "2026-10-06T01:00:02Z", "u3") | {"isMeta": True},
            user("[Request interrupted by user] と表示されたのはなぜですか", "2026-10-06T01:00:03Z", "u4"),
            user("[Request interrupted by user]", "2026-10-06T01:00:04Z", "u5")]
    out = export_log.convert_records(rows, "t", include_tools=False, header=[])
    assert "とは何ですか" in out and "貼り付けた通知" in out and "なぜですか" in out
    assert "本物の通知" not in out and out.count("Request interrupted") == 1


def test_start_checks_raw_title_for_quotes(tmp_path, monkeypatch):
    import argparse
    monkeypatch.setattr(live_log, "STATE", tmp_path / "live.json")
    monkeypatch.setattr(live_log, "REPO", tmp_path)
    _private(tmp_path, monkeypatch)
    title = "\n".join(["> 引用の行"] * 12)
    a = argparse.Namespace(number=2, slug="b", title=title, since="2026-10-02T00:00:00Z", date=None)
    try:
        live_log.cmd_start(a)
        raise AssertionError("引用の行が続くタイトルは書かない")
    except SystemExit:
        pass
    assert not (tmp_path / "live.json").exists()


def test_broken_lines_are_reported(tmp_path, monkeypatch):
    monkeypatch.setattr(live_log.time, "sleep", lambda s: None)
    path = tmp_path / "-work" / "a.jsonl"
    path.parent.mkdir(parents=True)
    rows = [touch("s1"), user("発言", "2026-10-06T01:00:00Z", "u1")]
    path.write_text(json.dumps(rows[0], ensure_ascii=False) + "\n{壊れた行\n"
                    + json.dumps(rows[1], ensure_ascii=False) + "\n{書き込み途中", encoding="utf-8")
    broken = []
    got = live_log.collect(tmp_path, "2026-10-06T00:00:00Z", workdir=Path(CWD), broken=broken)
    assert [r["uuid"] for r in got] == ["u1"]
    assert broken == ["a.jsonl の 2 行目", "a.jsonl の 4 行目"]


def test_project_dirs_include_repo_subdirectories(tmp_path):
    work = Path("/work")
    for name in ("-work", "-work-point-free-spacetime", "-work-point-free-spacetime-sim",
                 "-work-point-free-spacetime-private-papers", "-work-other", "-elsewhere"):
        (tmp_path / name).mkdir()
    names = [d.name for d in live_log.project_dirs(tmp_path, work)]
    assert names == ["-work", "-work-point-free-spacetime", "-work-point-free-spacetime-private-papers",
                     "-work-point-free-spacetime-sim"]


def test_history_checks_japanese_file_names(tmp_path):
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    (work / "logs" / "伏せる語の記録.md").write_text("x\n", encoding="utf-8")
    run("git", "add", "logs", cwd=work)
    run("git", "commit", "-q", "-m", "m2", cwd=work)
    run("git", "rm", "-q", "logs/伏せる語の記録.md", cwd=work)
    run("git", "commit", "-q", "-m", "m3", cwd=work)
    try:
        live_log.commit_and_push(work, ["logs/a.md"], "m4", verify=live_log.history_problems(["伏せる語"]))
        raise AssertionError("履歴の日本語のファイル名に伏せる語があれば push しない")
    except SystemExit as e:
        assert "ファイル名" in str(e) and "伏せる語の記録.md" in str(e)


def test_history_is_checked_before_advising_normal_push(tmp_path):
    work, run = _git_repo(tmp_path)
    (work / "logs" / "a.md").write_text("1\n", encoding="utf-8")
    live_log.commit_and_push(work, ["logs/a.md"], "m1")
    (work / "logs" / "a.md").write_text("伏せる語\n", encoding="utf-8")  # 未 push のログの版
    run("git", "commit", "-q", "-am", "log", cwd=work)
    (work / "tool.py").write_text("x = 1\n", encoding="utf-8")  # その後のふだんの作業
    run("git", "add", "tool.py", cwd=work)
    run("git", "commit", "-q", "-m", "work", cwd=work)
    (work / "logs" / "a.md").write_text("[伏せ字]\n", encoding="utf-8")
    try:
        live_log.commit_and_push(work, ["logs/a.md"], "m2", verify=live_log.history_problems(["伏せる語"]))
        raise AssertionError("止まるはず")
    except SystemExit as e:
        # ふだんの push を案内する前に、履歴の公開できない版を知らせる
        assert "公開できない版" in str(e) and "ふだんの push" not in str(e)


def test_exclusive_lock_blocks_concurrent_runs(tmp_path):
    import subprocess
    import sys
    lock = tmp_path / "x.lock"
    with live_log.exclusive_lock(lock):
        # 別のプロセスからは、ロックを持っている間は取れない
        code = ("import fcntl,sys; f=open(sys.argv[1],'a')\n"
                "try:\n fcntl.flock(f, fcntl.LOCK_EX|fcntl.LOCK_NB); print('got')\n"
                "except BlockingIOError: print('blocked')")
        out = subprocess.run([sys.executable, "-c", code, str(lock)], capture_output=True, text=True).stdout
        assert out.strip() == "blocked"
        # 同じプロセスの別の取得も、待った後に止まる
        try:
            with live_log.exclusive_lock(lock, timeout=0.3):
                raise AssertionError("取れないはず")
        except SystemExit:
            pass
    with live_log.exclusive_lock(lock, timeout=0.3):  # 放した後は取れる
        pass


def test_check_rows_skips_user_row_hidden_by_queued():
    english = " ".join(["the quick brown fox jumps over the lazy dog"] * 20)
    q = queued(english, "2026-10-06T01:00:00Z", "q1", source="u1")
    rows = [q, user(english, "2026-10-06T01:00:30Z", "u1")]
    overrides = {"q1": {"replace": "要約"}}
    assert live_log.check_rows(live_log.apply_overrides(rows, overrides), [], overrides) == []


def test_lost_messages_prefers_exact_matches():
    def log(*bodies):
        return "".join(f"## Claude（2026-10-06 01:00:05 UTC、記録 1）\n\n{b}\n\n" for b in bodies)
    assert live_log.lost_messages(log("A", "AB"), log("AB", "AC")) == []
    assert live_log.lost_messages(log("A", "AB"), log("AB", "X")) == ["Claude（2026-10-06 01:00:05 UTC）"]


def test_rows_without_uuid_are_checked_when_queued_has_no_source():
    q = queued("途中の発言", "2026-10-06T01:00:00Z", None)
    del q["uuid"], q["attachment"]["source_uuid"]
    u = user("電話は " + "090" + " 1234 5678 です", "2026-10-06T01:00:30Z", None)
    del u["uuid"]
    problems = live_log.check_rows([q, u], [], {})
    assert any("電話番号" in p for p in problems)
    out = export_log.convert_records([q, u], "t", include_tools=False, header=[])
    assert "途中の発言" in out and "です" in out


def test_phone_numbers_with_spaces():
    t = "090" + " 1234 5678"
    assert any("電話番号" in p for p in live_log.check(t, [], header_lines=0))
    assert not any("電話番号" in p for p in live_log.check("2026-10-06 04:01:27 UTC", [], header_lines=0))
