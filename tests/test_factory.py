"""Test app factory method."""

from app import create_app


def test_app_factory_method() -> None:
    """Test that application test settings are correct."""
    app = create_app()
    assert not app.testing
    app = create_app(testing=True)
    assert app.testing
