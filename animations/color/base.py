class ColorGeneration:

    def generate(self):
        return None

    def generate_list(self, amount):
        colors = []
        for i in range(amount):
            colors.append(self.generate())
        return colors


class IndexColorGeneration(ColorGeneration):

    def __init__(self, max_index):
        self.max_index = max_index
        self.index = 0

    def generate(self):
        color = self.generate_index(self.index)
        self.index += 1
        if self.index >= self.max_index:
            self.index = 0
        return color

    def generate_index(self, index):
        return None
