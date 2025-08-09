"""PracticeController ties together the MVC layers.

High-level flow:
1) Initialize the DB (Model layer)
2) Ask the user (via View) what to practice and for how long
3) Generate questions (Service) and ask them through the View for a fixed time
4) Persist a summary PracticeSession (Model)

Swap the View implementation (Console vs TUI) without touching this logic.
"""
from __future__ import annotations

from datetime import datetime

from app.models import db as db_models
from app.models.db import PracticeRegime, PracticeSession
from app.models.question import Question
from app.services.exercise_service import (
    generate_add_or_subtract_question,
    generate_times_table_question,
)
from app.services.time_service import run_for_duration
from app.views.base import BaseView


class PracticeController:
    def __init__(self, view: BaseView) -> None:
        self.view = view

    def run(self) -> None:
        # 1) Init DB
        db_models.initialize_db()

        # 2) Collect configuration via the View
        choice = self.view.select_practice_type()
        duration = self.view.prompt_duration_minutes()

        # 3) Prepare question factory and regime metadata
        if choice == 1:
            min_value, max_value = self.view.prompt_table_range()

            def make_question() -> Question:
                return generate_times_table_question(min_value, max_value)

            regime_name = "Times Tables"
        elif choice == 2:
            num_digits = self.view.prompt_num_digits()

            def make_question() -> Question:
                return generate_add_or_subtract_question(num_digits)

            regime_name = "Addition & Subtraction"
        else:
            # Fallback for unexpected input; keep UX simple.
            self.view.say_goodbye()
            db_models.shutdown_db()
            return

        # 4) Build an ask-one-question callable that the timing service can use
        def ask_one() -> bool:
            return self.view.ask_question(make_question())

        practice_start_time = datetime.now()
        questions_asked, correct_answers = run_for_duration(duration, ask_one)
        practice_end_time = datetime.now()

        # 5) Persist a summary PracticeSession
        regime, _ = PracticeRegime.get_or_create(regime_name=regime_name)
        PracticeSession.create(
            practice_start=practice_start_time.time(),
            practice_end=practice_end_time.time(),
            total_questions=questions_asked,
            total_correct=correct_answers,
            regime=regime,
        )

        # 6) Show summary and shutdown
        self.view.show_summary(questions_asked, correct_answers)
        self.view.say_goodbye()
        db_models.shutdown_db()


