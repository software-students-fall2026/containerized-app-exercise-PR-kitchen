"""MongoDB access for the web app."""

from flask import current_app
from pymongo import MongoClient


def get_db():
    """Return a handle to the application database."""
    client = MongoClient(current_app.config["MONGO_URI"])
    return client[current_app.config["MONGO_DBNAME"]]


def get_recent_analyses(limit: int = 20) -> list[dict]:
    """Return the most recent analyses saved by the ML client."""
    # TODO: query the "analyses" collection, newest first.
    raise NotImplementedError
