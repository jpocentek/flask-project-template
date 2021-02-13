"""Test fixtures and config."""

from typing import Generator
import pytest
from app import create_app, db


@pytest.fixture
def test_app() -> Generator:
    """Setup test app."""
    app = create_app(testing=True)
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield app
