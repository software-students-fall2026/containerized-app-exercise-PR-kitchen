"""Flask web app for estimating line wait times and restaurant busyness."""

import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app(test_config: dict | None = None) -> Flask:
    """Application factory."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        MONGO_URI=os.environ.get("MONGO_URI", "mongodb://localhost:27017"),
        MONGO_DBNAME=os.environ.get("MONGO_DBNAME", "prkitchen"),
        ML_CLIENT_URL=os.environ.get("ML_CLIENT_URL", "http://localhost:5001"),
    )
    if test_config:
        app.config.update(test_config)

    from . import routes  # pylint: disable=import-outside-toplevel

    app.register_blueprint(routes.bp)
    return app
