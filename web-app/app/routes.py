"""Page routes for the web app."""

from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    """Landing page: choose the line or room workflow."""
    return render_template("index.html")


@bp.route("/line", methods=["GET", "POST"])
def line():
    """Workflow 1: count people in a line and estimate the wait."""
    # TODO (POST): send image to ML client, then estimates.estimate_wait_minutes().
    return render_template("line.html")


@bp.route("/room", methods=["GET", "POST"])
def room():
    """Workflow 2: count people in a room and estimate how busy it is."""
    # TODO (POST): send image to ML client, then estimates.busyness_level().
    return render_template("room.html")


@bp.get("/history")
def history():
    """Dashboard of past analyses stored in MongoDB."""
    # TODO: load recent results with db.get_recent_analyses().
    return render_template("history.html", analyses=[])
