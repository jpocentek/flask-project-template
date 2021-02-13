"""Test app factory method."""

from flask import Flask
from app import create_app


def test_app_factory_method() -> None:
    """Test that application test settings are correct."""
    app = create_app()
    assert not app.testing
    app = create_app(testing=True)
    assert app.testing


def test_index(test_app: Flask) -> None:
    """Test that index page returns 200 OK."""
    assert test_app.test_client().get("/").status_code == 200


def test_ping(test_app: Flask) -> None:
    """Test that healthcheck returns OK."""
    assert test_app.test_client().get("/ping").status_code == 200
