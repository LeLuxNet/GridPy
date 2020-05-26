from animations.color import base
from lib import colors


class RandomGeneration(base.ColorGeneration):

    def generate(self):
        return colors.random_color()


class DifferentRandomGeneration(base.ColorGeneration):

    def __init__(self, difference):
        self.difference = difference
        self.previous = None

    def generate(self):
        while True:
            color = colors.random_color()
            if self.previous is None or \
                    self._enough_dif(self.previous.red, color.red) or \
                    self._enough_dif(self.previous.green, color.green) or \
                    self._enough_dif(self.previous.blue, color.blue):
                self.previous = color
                return color

    def _enough_dif(self, old, new):
        return old - new > self.difference or new - old > self.difference
