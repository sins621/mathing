"""Deprecated: moved to `app.models.db` in the MVC refactor.

This file remains as a compatibility shim to avoid breaking old imports. Prefer
importing from `app.models.db` directly in new code.
"""
from app.models.db import (  # re-export for backward compatibility
    BaseModel,
    PracticeRegime,
    PracticeSession,
    db,
    initialize_db,
    shutdown_db,
)

__all__ = [
    "BaseModel",
    "PracticeRegime",
    "PracticeSession",
    "db",
    "initialize_db",
    "shutdown_db",
]
