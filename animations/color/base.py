class ColorGeneration:

    def generate(self):
        return None

    def generate_list(self, amount):
        colors = []
        for i in range(amount):
            colors.append(self.generate())
        return colors
