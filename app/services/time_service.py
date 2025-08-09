"""Timing service that runs an exercise for a fixed duration.

The controller supplies a callable that asks a single question via a View and
returns True/False for correctness. This service measures time and aggregates
results, but does no I/O itself (keeps it outside the View layer).
"""
from __future__ import annotations

import time
from typing import Callable, Tuple


def run_for_duration(
    duration_minutes: int, ask_one_question: Callable[[], bool]
) -> tuple[int, int]:
    duration_seconds = duration_minutes * 60
    start_time = time.time()
    questions_asked = 0
    correct_answers = 0

    while time.time() - start_time < duration_seconds:
        if ask_one_question():
            correct_answers += 1
        questions_asked += 1

    return questions_asked, correct_answers


