"""Application entrypoint wired to the MVC architecture.

Previously, this file handled DB setup and direct CLI prompts. It now
instantiates a Controller and a View implementation and lets them handle the
flow. This keeps responsibilities clean and demonstrates MVC in practice.
"""

from app.controllers.practice_controller import PracticeController
from app.views.tui_view import TUIView


def main() -> None:
    controller = PracticeController(view=TUIView())
    controller.run()


if __name__ == "__main__":
    main()
