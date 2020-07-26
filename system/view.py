import importlib

view = 2


def get_app(name):
    return importlib.import_module("apps." + name).App()


def start_app(name):
    next_view()
    get_app(name).run()


def next_view(next_id=1):
    global view
    view = next_id
    print("View:", view)


def current():
    return view
