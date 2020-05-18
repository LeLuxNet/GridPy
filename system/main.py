from lib import button
from system import view

apps = ["drawer", "animations", "tictactoe", "snake", "connectfour", "flashlight"]


def quit():
    button.cleanup()


def run():
    while view.current() == 0:
        pass
    selected = apps[view.current() - 1]
    view.start_app(selected)
