"""Shared pytest fixtures (pytest-flask uses the ``app`` fixture)."""

import pytest

from app import create_app


@pytest.fixture(name="app")
def fixture_app():
    """The Flask app configured for testing."""
    return create_app({"TESTING": True})
