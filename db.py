from datetime import datetime

from peewee import *  # pyright: ignore

db = SqliteDatabase("mental_math.db")


class BaseModel(Model):
    class Meta:
        database = db


class PracticeSession(BaseModel):
    id = AutoField(PrimaryKeyField)
    date = DateTimeField(datetime)


class PracticeRegime(BaseModel):
    id = AutoField(PrimaryKeyField)


db.connect()
db.create_tables([PracticeSession, PracticeRegime])
db.close()
