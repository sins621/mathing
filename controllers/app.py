from models.database import DatabaseManager


class AppController:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def run(self):
        self.db_manager.initialize()
        # Main app logic here
        self.cleanup()

    def cleanup(self):
        self.db_manager.close()
