"""Deprecated: input validation moved into View implementations.

Legacy helpers kept for compatibility; new code should prefer view-level
validation (e.g., `ConsoleView._coerce_int`).
"""


def choice_is_number(value) -> bool:  # pragma: no cover - legacy
    try:
        int(value)
        return True
    except Exception:
        return False


def validate_number(value) -> int:  # pragma: no cover - legacy
    while not choice_is_number(value):
        value = input("Sorry, you didn't input a valid option, try again.\n\n")
    return int(value)
