"""Tests for the page routes."""


def test_index(client):
    """The landing page loads."""
    assert client.get("/").status_code == 200


# TODO: tests for /line, /room and /history (mock the ML client and MongoDB).
