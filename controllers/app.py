from models.database import DatabaseManager
from views.menu_view import MenuView


class AppController:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.menu_view = MenuView()
        # self.practice_session_repository =

    def run(self):
        self.db_manager.initialize()
        # Main app logic here
        while True:
            duration = self.menu_view.prompt_for_practice_duration()
            regime = self.menu_view.promt_for_regime_selection()

        self.cleanup()  # pyright: ignore

    def cleanup(self):
        self.db_manager.close()
