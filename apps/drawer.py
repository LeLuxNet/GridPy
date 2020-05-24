from lib import app
from system import view


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Drawer")
        self.viewed = 0

    def run(self):
        pass
