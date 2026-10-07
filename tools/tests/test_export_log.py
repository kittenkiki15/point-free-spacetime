"""tools/export_log.py のテスト。公開前の伏せ字と、発言の抽出を確かめる。"""

import importlib.util
import json
from pathlib import Path

_path = Path(__file__).resolve().parents[1] / "export_log.py"
_spec = importlib.util.spec_from_file_location("export_log", _path)
export_log = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(export_log)


def convert_lines(tmp_path, lines, terms=()):
    f = tmp_path / "s.jsonl"
    f.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines), encoding="utf-8")
    return export_log.convert(f, "t", list(terms))


def user(content, **kw):
    return {"type": "user", "message": {"role": "user", "content": content}, **kw}


def assistant(text):
    return {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": text}]}}


def test_redacts_email_and_keys():
    aws = "AKIA" + "ABCDEFGHIJKLMNOP"
    text = f"mail a.b@example.com key sk-{'x' * 20} {aws}"
    out = export_log.redact(text)
    assert "example.com" not in out
    assert "sk-" not in out
    assert aws not in out


def test_redacts_uuid_case_insensitive():
    out = export_log.redact("id 3F2504E0-4F89-11D3-9A0C-0305E82C3301 and 3f2504e0-4f89-11d3-9a0c-0305e82c3301")
    assert out == "id [ID] and [ID]"


def test_redacts_terms_as_fixed_strings():
    out = export_log.redact("name foo[bar] and FOO[BAR]", ["foo[bar]"])
    assert out == "name [伏せ字] and [伏せ字]"


def test_keeps_user_text_starting_with_angle_bracket(tmp_path):
    out = convert_lines(tmp_path, [user("<div> で始まる発言")])
    assert "<div> で始まる発言" in out


def test_drops_system_messages(tmp_path):
    out = convert_lines(tmp_path, [
        user("<command-name>/clear</command-name>"),
        user("メタ情報", isMeta=True),
        user([{"type": "text", "text": "本文<system-reminder>内部</system-reminder>"}]),
    ])
    assert "clear" not in out
    assert "メタ情報" not in out
    assert "内部" not in out
    assert "本文" in out


def test_omits_tool_input_body(tmp_path):
    out = convert_lines(tmp_path, [{
        "type": "assistant",
        "message": {"role": "assistant", "content": [
            {"type": "tool_use", "id": "1", "name": "Write",
             "input": {"file_path": "a.md", "content": "秘密の本文"}},
        ]},
    }])
    assert "秘密の本文" not in out


def test_demotes_headings_outside_code(tmp_path):
    out = convert_lines(tmp_path, [assistant("# 見出し\n```\n# コード\n```")])
    assert "### 見出し" in out
    assert "\n# コード\n" in out


def test_since_skips_earlier_records(tmp_path):
    out = convert_lines(tmp_path, [
        {**user("前の回の発言"), "timestamp": "2026-09-25T10:00:00.000Z"},
        {**user("今回の発言"), "timestamp": "2026-09-25T11:02:28.903Z"},
    ])
    assert "前の回の発言" in out
    f = tmp_path / "s.jsonl"
    out = export_log.convert(f, "t", [], since="2026-09-25T11:02:28.903Z")
    assert "前の回の発言" not in out
    assert "今回の発言" in out


def test_since_compares_times_not_strings(tmp_path):
    convert_lines(tmp_path, [
        {**user("前の秒の発言"), "timestamp": "2026-09-25T11:02:27.999Z"},
        {**user("同じ秒の発言"), "timestamp": "2026-09-25T11:02:28.903Z"},
    ])
    f = tmp_path / "s.jsonl"
    # 秒精度の指定でも、同じ秒の小数秒付きの記録は「以降」に含まれる
    for since in ("2026-09-25T11:02:28Z", "2026-09-25T11:02:28+00:00", "2026-09-25T20:02:28+09:00"):
        out = export_log.convert(f, "t", [], since=since)
        assert "前の秒の発言" not in out
        assert "同じ秒の発言" in out


def test_since_and_until_select_one_session(tmp_path):
    convert_lines(tmp_path, [
        {**user("第 01 回の発言"), "timestamp": "2026-09-25T09:00:00Z"},
        {**user("第 02 回の発言"), "timestamp": "2026-09-25T11:02:28.903Z"},
        {**user("第 03 回の発言"), "timestamp": "2026-09-26T09:00:00.000Z"},
    ])
    f = tmp_path / "s.jsonl"
    out = export_log.convert(f, "t", [], since="2026-09-25T11:02:28.903Z", until="2026-09-26T09:00:00Z")
    assert "第 01 回の発言" not in out
    assert "第 02 回の発言" in out
    assert "第 03 回の発言" not in out


def test_untimed_records_are_excluded_with_warning(tmp_path, capsys):
    convert_lines(tmp_path, [
        {**user("時刻のある発言"), "timestamp": "2026-09-25T11:00:00Z"},
        user("時刻のない発言"),
        {"type": "summary", "summary": "発言でない記録"},  # 発言でない記録は警告の対象外
    ])
    f = tmp_path / "s.jsonl"
    # since だけ・until だけ・両方のいずれでも、時刻のない発言は出力せず警告する
    for kw in ({"since": "2026-09-25T10:00:00Z"}, {"until": "2026-09-25T12:00:00Z"},
               {"since": "2026-09-25T10:00:00Z", "until": "2026-09-25T12:00:00Z"}):
        out = export_log.convert(f, "t", [], **kw)
        assert "時刻のある発言" in out
        assert "時刻のない発言" not in out
        err = capsys.readouterr().err
        assert "警告" in err and "1 件" in err and "2 行目" in err


def test_untimed_records_are_kept_without_period(tmp_path, capsys):
    out = convert_lines(tmp_path, [user("時刻のない発言")])
    assert "時刻のない発言" in out
    assert capsys.readouterr().err == ""
