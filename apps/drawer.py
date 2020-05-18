from lib import app
from system import view


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Drawer")

    def run(self):
        view.next_view(3)
