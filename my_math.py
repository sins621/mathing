"""Deprecated: moved into services/views in MVC refactor.

Legacy interactive functions have been restructured as:
- Question generation -> `app.services.exercise_service`
- Asking/validating answers -> `app.views.console_view` (or TUI)
"""

from app.services.exercise_service import (
    generate_add_or_subtract_question,
    generate_times_table_question,
)

# Thin compatibility wrappers for old call sites. Prefer using the controller.


def practice_table(min_value: int, max_value: int) -> bool:
    from app.views.console_view import ConsoleView

    view = ConsoleView()
    return view.ask_question(generate_times_table_question(min_value, max_value))


def practice_addition_and_subtraction(num_digits: int) -> bool:
    from app.views.console_view import ConsoleView

    view = ConsoleView()
    return view.ask_question(generate_add_or_subtract_question(num_digits))
