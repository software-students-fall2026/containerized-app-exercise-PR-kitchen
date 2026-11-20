"""MongoDB access for the ML client."""

import os

from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
MONGO_DBNAME = os.environ.get("MONGO_DBNAME", "prkitchen")


def get_db():
    """Return a handle to the application database."""
    return MongoClient(MONGO_URI)[MONGO_DBNAME]


def save_result(mode: str, people_count: int, metadata: dict) -> str:
    """Save one analysis result and return its id as a string."""
    # TODO: insert into the "analyses" collection with a timestamp.
    raise NotImplementedError
