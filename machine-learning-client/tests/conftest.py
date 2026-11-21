"""Shared pytest fixtures for the ML client."""

import pytest

from ml_client.app import create_app


@pytest.fixture(name="client")
def fixture_client():
    """A Flask test client for the ML client service."""
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()
