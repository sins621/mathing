"""TUI View implementation using npyscreen.

This swaps the Console I/O with a simple terminal UI. The Controller does not
change; only the View is replaced.

Note: `npyscreen` uses an application loop. We keep this minimal and
blocking for simplicity.
"""
from __future__ import annotations

import npyscreen

from app.models.question import Question
from app.views.base import BaseView


class _InputApp(npyscreen.NPSAppManaged):
    def onStart(self):  # type: ignore[override]
        pass


def _get_number(prompt: str) -> int:
    """Simple helper to collect an integer from the user via a popup form."""
    value_holder: dict[str, int] = {"value": 0}

    class NumberForm(npyscreen.ActionPopup):
        def create(self):  # type: ignore[override]
            self.value = self.add(npyscreen.TitleText, name=prompt)

        def on_ok(self):  # type: ignore[override]
            try:
                value_holder["value"] = int(self.value.value)
            except Exception:
                value_holder["value"] = 0
            finally:
                self.parentApp.setNextForm(None)

        def on_cancel(self):  # type: ignore[override]
            self.parentApp.setNextForm(None)

    app = _InputApp()
    app.addForm("MAIN", NumberForm)
    app.run()
    return value_holder["value"]


def _message(msg: str) -> None:
    class MessageForm(npyscreen.ActionPopup):
        def create(self):  # type: ignore[override]
            self.add(npyscreen.Pager, values=[msg])

        def on_ok(self):  # type: ignore[override]
            self.parentApp.setNextForm(None)

        def on_cancel(self):  # type: ignore[override]
            self.parentApp.setNextForm(None)

    app = _InputApp()
    app.addForm("MAIN", MessageForm)
    app.run()


class TUIView(BaseView):
    def select_practice_type(self) -> int:
        return _get_number(
            "What would you like to practice? 1=Times Tables, 2=Add/Sub"
        )

    def prompt_duration_minutes(self) -> int:
        return _get_number("How many minutes?")

    def prompt_table_range(self) -> tuple[int, int]:
        min_value = _get_number("Min table value")
        max_value = _get_number("Max table value")
        if min_value > max_value:
            min_value, max_value = max_value, min_value
        return min_value, max_value

    def prompt_num_digits(self) -> int:
        return _get_number("How many digits?")

    def ask_question(self, question: Question) -> bool:
        user_answer = _get_number(question.prompt)
        if user_answer == question.correct_answer:
            _message("Correct!")
            return True
        else:
            _message(f"Sorry, the correct answer was {question.correct_answer}")
            return False

    def show_summary(self, questions_asked: int, correct_answers: int) -> None:
        _message(f"You got {correct_answers}/{questions_asked} correct!")

    def say_goodbye(self) -> None:
        _message("See you later")


