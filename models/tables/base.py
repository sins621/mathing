from peewee import Model

from models.database import DatabaseManager


class BaseModel(Model):
    class Meta:
        database = DatabaseManager().db
