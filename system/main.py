from lib import button, char
from system import view


def quit():
    button.cleanup()


def run():
    if view.current() == -1:
        _drawer()
    elif view.current() == 0:
        # Animations
        pass
    elif view.current() == 1:
        view.start_app("tictactoe")
    elif view.current() == 2:
        view.start_app("flashlight")


def _drawer():
    char.gliding_text("GridPy Test", fade_out=True)
    view.next_view(1)
