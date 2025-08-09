from cli import start_practice
from db import PracticeRegime, PracticeSession, db


def initialize_db():
    db.connect()
    db.create_tables([PracticeSession, PracticeRegime], safe=True)


def main():
    initialize_db()
    start_practice()
    db.close()


if __name__ == "__main__":
    main()
