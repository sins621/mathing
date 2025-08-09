"""Exercise generation service.

Responsible for creating `Question` objects (Model) without any I/O. The
Controller will request questions from here and pass them to a View to display
and collect answers.
"""
from __future__ import annotations

import random

from app.models.question import Question


def generate_times_table_question(min_value: int, max_value: int) -> Question:
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    return Question(prompt=f"What is {num1} * {num2}?", correct_answer=num1 * num2)


def generate_add_or_subtract_question(num_digits: int) -> Question:
    """Generate a simple addition OR subtraction question with the given size.

    - num_digits controls the magnitude (roughly 10**num_digits).
    - For subtraction, ensure non-negative results to keep UX simple.
    """
    upper = 10 ** num_digits - 1
    if upper < 1:
        upper = 9

    a = random.randint(1, upper)
    b = random.randint(1, upper)

    if random.choice([True, False]):
        # addition
        return Question(prompt=f"What is {a} + {b}?", correct_answer=a + b)
    else:
        # subtraction (non-negative)
        x, y = max(a, b), min(a, b)
        return Question(prompt=f"What is {x} - {y}?", correct_answer=x - y)


