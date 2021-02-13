"""Test app factory method."""

from pytest import MonkeyPatch
from app import create_app


def test_app_factory_method(monkeypatch: MonkeyPatch) -> None:
    """Test that application test settings are correct."""
    app = create_app(testing=True)
    assert app.testing

    class Recorder:
        dsn: str
        environment: str

    def fake_init(dsn: str, environment: str) -> None:
        Recorder.dsn = dsn
        Recorder.environment = environment

    monkeypatch.setattr("app.SENTRY_DSN", "http://fake.org")
    monkeypatch.setattr("sentry_sdk.init", fake_init)
    app = create_app()
    assert not app.testing
    assert Recorder.dsn == "http://fake.org"
    assert Recorder.environment == "dev"
