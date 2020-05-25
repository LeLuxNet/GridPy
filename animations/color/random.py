from animations.color import base
from lib import colors


class RandomGeneration(base.ColorGeneration):

    def generate(self):
        return colors.random_color()
