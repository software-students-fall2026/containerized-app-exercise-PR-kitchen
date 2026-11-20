"""HTTP service that the web app calls to analyze an image."""

import os

from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()


def create_app() -> Flask:
    """Create and configure the ML client Flask app."""
    app = Flask(__name__)

    @app.get("/health")
    def health():
        """Liveness check used by docker-compose / the web app."""
        return jsonify(status="ok")

    @app.post("/detect")
    def detect():
        """Count the people in an uploaded image and store the result.

        Expected request: multipart/form-data with an ``image`` file plus a
        ``mode`` field (``"line"`` or ``"room"``).
        """
        # TODO: read image from request.files, call detector.count_people(),
        #       call db.save_result(), and return the saved result as JSON.
        return jsonify(error="not implemented"), 501

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("ML_CLIENT_PORT", 5001)))
