"""Static views."""

from typing import Tuple
from flask import render_template, Blueprint

from db import db

views = Blueprint("views", __name__)


@views.route("/", methods=("GET",))
def index() -> str:  # pylint: disable=W0612
    """Main index page."""
    return render_template("index.html")


@views.route("/ping", methods=("GET",))
def ping() -> Tuple[str, int]:  # pylint: disable=W0612
    """Health check"""
    result = db.session.execute("SELECT 1")
    result.fetchone()
    return "", 200
