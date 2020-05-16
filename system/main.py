from lib import button, char, led
from system import view


def quit():
    button.cleanup()


def run():
    if view.current() == 1:
        _drawer()
    elif view.current() == 2:
        # Animations
        pass
    elif view.current() == 11:
        view.start_app("tictactoe")
    elif view.current() == 12:
        view.start_app("flashlight")


def _drawer():
    led.clear()
    char.gliding_text("GridPy Test", fade_in=True, fade_out=True)
    view.next_view(11)
