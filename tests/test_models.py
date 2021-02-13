"""Tests for DB models."""

from models import User


def test_user_repr_method() -> None:
    """Test that user info is displayed."""
    user = User(username="fakeuser", password="fakepass")
    assert user.__repr__() == r"<User: 'fakeuser'>"
