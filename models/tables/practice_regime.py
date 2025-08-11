from peewee import AutoField, TextField

from models.tables.base import BaseModel


class PracticeRegime(BaseModel):
    id = AutoField()
    regime_name = TextField()
