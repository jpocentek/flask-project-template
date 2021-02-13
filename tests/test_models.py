"""Tests for DB models."""

from flask import Flask
from models import User


def test_model_table(test_app: Flask) -> None:
    """Test that we can query User model."""
    with test_app.app_context():
        assert not User.query.all()  # An empty list should be returned


def test_user_repr_method() -> None:
    """Test that user info is displayed."""
    user = User(username="fakeuser", password="fakepass")
    assert user.__repr__() == r"<User: 'fakeuser'>"
