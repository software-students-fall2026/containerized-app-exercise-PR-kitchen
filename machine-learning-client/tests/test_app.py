"""Tests for the ML client HTTP endpoints."""


def test_health(client):
    """The health endpoint responds with ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


# TODO: tests for POST /detect
