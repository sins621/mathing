"""Console-based View implementation.

This view uses simple input()/print() for I/O. It contains input validation and
formatting, but no application logic.
"""
from __future__ import annotations

from app.models.question import Question
from app.views.base import BaseView


def _coerce_int(prompt: str) -> int:
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except Exception:
            print("Sorry, that wasn't a number. Try again.\n")


class ConsoleView(BaseView):
    def select_practice_type(self) -> int:
        return _coerce_int(
            "What would you like to practice?\n1: Times Tables\n2: Addition & Subtraction\n\n"
        )

    def prompt_duration_minutes(self) -> int:
        return _coerce_int("How long would you like to practice for (minutes)?\n\n")

    def prompt_table_range(self) -> tuple[int, int]:
        min_value = _coerce_int("What's the minimum number for the tables?\n\n")
        max_value = _coerce_int("What's the maximum number for the tables?\n\n")
        if min_value > max_value:
            min_value, max_value = max_value, min_value
        return min_value, max_value

    def prompt_num_digits(self) -> int:
        return _coerce_int("How many digits large should the number be?\n\n")

    def ask_question(self, question: Question) -> bool:
        user_answer = _coerce_int(question.prompt + "\n\n")
        if user_answer == question.correct_answer:
            print("Correct!\n")
            return True
        else:
            print(f"Sorry, the correct answer was {question.correct_answer}\n")
            return False

    def show_summary(self, questions_asked: int, correct_answers: int) -> None:
        print(f"You got {correct_answers}/{questions_asked} correct!")

    def say_goodbye(self) -> None:
        print("See you later")


