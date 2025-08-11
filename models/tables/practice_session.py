from datetime import datetime

from peewee import AutoField, DateTimeField, ForeignKeyField, IntegerField, TimeField

from models.tables.base import BaseModel
from models.tables.practice_regime import PracticeRegime


class PracticeSession(BaseModel):
    id = AutoField()
    date = DateTimeField(default=datetime.now)
    practice_start = TimeField()
    practice_end = TimeField()
    total_questions = IntegerField()
    total_correct = IntegerField()
    regime = ForeignKeyField(PracticeRegime, backref="regime")
