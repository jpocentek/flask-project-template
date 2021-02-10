"""Application definition."""

import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension  # type: ignore

from .db import db
from .management import init_cli


def create_app(testing: bool = False) -> Flask:
    """Flask app factory."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DebugToolbarExtension(app)

    if testing:
        app.testing = True
        app.debug = False

    db.init_app(app)
    init_cli(app)

    return app
