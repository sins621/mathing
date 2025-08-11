from peewee import SqliteDatabase


class DatabaseManager:
    _instance = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._db = SqliteDatabase("mental_math.db")
        return cls._instance

    @property
    def db(self):
        return self._db

    def initialize(self):
        assert self._db is not None, "Database not initialized"
        self._db.connect()
        from models.tables.practice_regime import PracticeRegime
        from models.tables.practice_session import PracticeSession

        self._db.create_tables([PracticeRegime, PracticeSession], safe=True)

    def close(self):
        if self._db and not self._db.is_closed():
            self._db.close()
