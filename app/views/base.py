"""Abstract base for Views.

Defining a small interface allows the Controller to be agnostic to the UI
implementation (Console vs TUI). Swapping views becomes trivial.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple

from app.models.question import Question


class BaseView(ABC):
    @abstractmethod
    def select_practice_type(self) -> int:
        """Return 1 for Times Tables, 2 for Addition/Subtraction."""

    @abstractmethod
    def prompt_duration_minutes(self) -> int:
        """Duration of practice in minutes."""

    @abstractmethod
    def prompt_table_range(self) -> tuple[int, int]:
        """Return (min_value, max_value) for times tables."""

    @abstractmethod
    def prompt_num_digits(self) -> int:
        """Return the number of digits for add/sub questions."""

    @abstractmethod
    def ask_question(self, question: Question) -> bool:
        """Render the question and return True if user answers correctly."""

    @abstractmethod
    def show_summary(self, questions_asked: int, correct_answers: int) -> None:
        ...

    @abstractmethod
    def say_goodbye(self) -> None:
        ...


