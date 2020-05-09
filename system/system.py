import importlib
from time import sleep

from lib import button, led, char

view = -1


def _init():
    led.show_image("assets/logo.png")
    sleep(2)
    led.clear()


def _quit():
    button.cleanup()


def run():
    if view == -1:
        _drawer()
    elif view == 0:
        # Animations
        pass
    elif view == 1:
        start_app("tictactoe")


def start_app(name):
    importlib.import_module("apps." + name)
    next_view()


def _drawer():
    char.gliding_text("GridPy Test")
    next_view(1)


def next_view(id=-1):
    global view
    view = id


_init()

while True:
    run()

_quit()
