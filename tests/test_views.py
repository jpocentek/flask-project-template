"""Tests for views."""

from flask import Flask


def test_index(test_app: Flask) -> None:
    """Test that index page returns 200 OK."""
    response = test_app.test_client().get("/")
    assert response.status_code == 200
    assert b"<h1>Flask Demo</h1>" in response.data


def test_ping(test_app: Flask) -> None:
    """Test that healthcheck returns OK."""
    assert test_app.test_client().get("/ping").status_code == 200
