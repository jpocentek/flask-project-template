"""DB models."""
from .db import db


class User(db.Model):
    """Represents a user in system."""

    __tablename__: str = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(94), nullable=False)

    def __repr__(self) -> str:
        return "<User: %r>" % self.username
