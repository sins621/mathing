"""Deprecated: legacy CLI entrypoint.

Kept for compatibility; new code should use `PracticeController` and a View
(`ConsoleView` or TUI) from the `app` package.
"""

from app.controllers.practice_controller import PracticeController
from app.views.console_view import ConsoleView


def start_practice() -> None:
    controller = PracticeController(view=ConsoleView())
    controller.run()
