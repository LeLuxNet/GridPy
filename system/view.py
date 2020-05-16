import importlib

from lib import led

view = -1


def get_app(name):
    return importlib.import_module("apps." + name).App()


def start_app(name):
    led.clear()
    get_app(name).run()
    next_view()


def next_view(next_id=-1):
    global view
    view = next_id
    print("View:", next_id)


def current():
    return view
