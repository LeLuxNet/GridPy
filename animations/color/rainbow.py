from animations.color import base
from lib import colors


class RainbowGeneration(base.IndexColorGeneration):

    def generate_index(self, index):
        hue = index / self.max_index
        return colors.hsv(hue, 1, 1)
