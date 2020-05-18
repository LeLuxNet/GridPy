class BaseApp:

    def __init__(self, name):
        self.name = name

    def run(self):
        raise Exception('App not implemented')