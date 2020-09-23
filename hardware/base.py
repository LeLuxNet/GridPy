from lib import cords
from lib.colors import Color


class LedLib:

    def set_pixel(self, pos: cords.Cords, color: Color):
        pass

    def show(self):
        pass


class ButtonLib:

    def setup(self, pin):
        pass

    def pressed(self, pin):
        return False

    def cleanup(self):
        pass
