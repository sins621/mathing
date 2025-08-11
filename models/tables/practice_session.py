from datetime import datetime

from base import (
    AutoField,
    BaseModel,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    TimeField,
)
from practice_regime import PracticeRegime


class PracticeSession(BaseModel):
    id = AutoField()
    date = DateTimeField(default=datetime.now)
    practice_start = TimeField()
    practice_end = TimeField()
    total_questions = IntegerField()
    total_correct = IntegerField()
    regime = ForeignKeyField(PracticeRegime, backref="regime")

    @classmethod
    def create_session(cls, regime_id, start_time, end_time, questions, correct):
        return cls.create(
            regime=regime_id,
            practice_start=start_time,
            practice_end=end_time,
            total_questions=questions,
            total_correct=correct,
        )
