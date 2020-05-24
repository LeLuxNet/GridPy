from lib import button
from system import view

apps = ["drawer",  # 1
        "animations",  # 2
        "tictactoe",  # 3
        "connectfour",  # 4
        "snake",  # 5
        "flashlight",  # 6
        "test_card"]  # 7


def run():
    while view.current() == 0:
        pass
    selected = apps[view.current() - 1]
    view.start_app(selected)
