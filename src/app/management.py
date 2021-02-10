"""CLI management commands."""
import click
from flask import Flask
from flask.cli import with_appcontext

from .db import db


@click.command("init-db")
@with_appcontext
def init_db() -> None:
    """Initialize database."""
    # Import models so SQLAlchemy can
    # create tables for them.
    from .models import User  # pylint: disable=C0415,W0611

    db.drop_all()
    db.create_all()
    click.echo("Initialized database")


def init_cli(app: Flask) -> None:
    """Initialize all commands for app instance."""
    app.cli.add_command(init_db)
