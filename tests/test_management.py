"""Test for CLI management commands."""

from pytest import MonkeyPatch
from flask import Flask


def test_init_db_command(test_app: Flask, monkeypatch: MonkeyPatch):
    """Test init-db command."""
    runner = test_app.test_cli_runner()

    class Recorder:
        drop_called: bool = False
        create_called: bool = False

    def fake_drop_all() -> None:
        Recorder.drop_called = True

    def fake_create_all() -> None:
        Recorder.create_called = True

    monkeypatch.setattr("app.db.drop_all", fake_drop_all)
    monkeypatch.setattr("app.db.create_all", fake_create_all)
    result = runner.invoke(args=["init-db"])
    assert "Initialized database" in result.output
    assert Recorder.drop_called
    assert Recorder.create_called
