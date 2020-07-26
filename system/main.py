from system import view

apps = ["drawer",  # 1
        "animations",  # 2
        "tictactoe",  # 3
        "connectfour",  # 4
        "snake",  # 5
        "flashlight",  # 6
        "test_card"]  # 7


def run():
    if view.current() == 0:
        view.next_view(-1)
        while view.current() == -1:
            pass
        return
    selected = apps[view.current() - 1]
    view.start_app(selected)
