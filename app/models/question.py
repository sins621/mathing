"""Question data object (part of the Model layer).

In MVC, a question is a simple data structure with no knowledge of how it will
be asked (View) or when/why it is generated (Controller).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    correct_answer: int


