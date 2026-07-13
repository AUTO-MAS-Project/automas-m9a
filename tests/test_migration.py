from types import SimpleNamespace

from automas_script_maafw_pack_m9a.migration import _build_user_payload


def test_user_migration_does_not_emit_script_connection_overrides() -> None:
    payload = _build_user_payload(
        raw_user={
            "Info": {
                "Name": "M9A 用户",
                "Controller": "legacy-adb",
                "Resource": "legacy-resource",
            },
            "Task": {"Queue": []},
            "Data": {},
            "Notify": {},
        },
        interface=SimpleNamespace(task=[], option={}),
    )

    assert payload["Info"] == {"Name": "M9A 用户"}
    assert "Controller" not in payload["Info"]
    assert "Resource" not in payload["Info"]
