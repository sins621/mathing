"""Database models (M in MVC).

This module defines the persistence layer using Peewee. It intentionally has no
knowledge of user interfaces (views) or orchestration logic (controllers).

Key entities:
- PracticeRegime: identifies a type of practice (e.g., Times Tables)
- PracticeSession: one run where a user practiced for some duration

The controller is responsible for creating sessions and persisting results.
"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from peewee import (
    AutoField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    TimeField,
)


# Single DB instance used by all models in this package
db = SqliteDatabase("mental_math.db")


class BaseModel(Model):
    class Meta:
        database = db


class PracticeRegime(BaseModel):
    id = AutoField()
    regime_name = TextField(unique=True)


class PracticeSession(BaseModel):
    id = AutoField()
    date = DateTimeField(default=datetime.now)
    practice_start = TimeField()
    practice_end = TimeField()
    total_questions = IntegerField()
    total_correct = IntegerField()
    regime = ForeignKeyField(PracticeRegime, backref="sessions")


def initialize_db() -> None:
    """Initialize DB tables. Call once at program startup.

    Kept here (in the model layer) so the controller simply calls a single
    function to prepare persistence.
    """
    db.connect(reuse_if_open=True)
    db.create_tables([PracticeSession, PracticeRegime], safe=True)


def shutdown_db() -> None:
    """Close DB connection at app shutdown."""
    if not db.is_closed():
        db.close()


