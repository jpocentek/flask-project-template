"""Test fixtures and config."""

from typing import Generator
import pytest
from app import create_app


@pytest.fixture
def test_app() -> Generator:
    """Setup test app."""
    application = create_app(testing=True)
    yield application
    # Teardown goes here...
