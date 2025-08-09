from datetime import datetime

from peewee import *  # pyright: ignore

db = SqliteDatabase("mental_math.db")


class BaseModel(Model):
    class Meta:
        database = db


class PracticeRegime(BaseModel):
    id = AutoField()
    regime_name = TextField()


class PracticeSession(BaseModel):
    id = AutoField()
    date = DateTimeField(default=datetime.now)
    practice_start = TimeField()
    practice_end = TimeField()
    total_questions = IntegerField()
    total_correct = IntegerField()
    regime = ForeignKeyField(PracticeRegime, backref="regime")
