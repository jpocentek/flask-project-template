"""Application definition."""

import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension  # type: ignore

from db import db
from management import init_cli
from views import views

PROJECT_ROOT_PATH = os.environ["PROJECT_ROOT_PATH"]
TEMPLATE_DIR = os.path.join(PROJECT_ROOT_PATH, "templates")
STATIC_DIR = os.path.join(PROJECT_ROOT_PATH, "assets", "dist")
SENTRY_DSN = os.environ.get("SENTRY_DSN", None)
SENTRY_ENV = os.environ.get("SENTRY_ENV", "dev")

toolbar = DebugToolbarExtension()


def create_app(testing: bool = False) -> Flask:
    """Flask app factory."""
    app = Flask(
        __name__,
        template_folder=TEMPLATE_DIR,
        static_folder=STATIC_DIR,
    )
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        app.testing = True
        app.debug = False

    if SENTRY_DSN and not app.testing:
        import sentry_sdk  # pylint: disable=C0415

        sentry_sdk.init(dsn=SENTRY_DSN, environment=SENTRY_ENV)

    app.register_blueprint(views)

    db.init_app(app)
    init_cli(app)
    toolbar.init_app(app)

    return app
