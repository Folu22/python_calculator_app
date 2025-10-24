## create a math operation: addition that adds as many numbers as the user wants

class Addition:
    def __init__(self, *args):
        self.numbers = args

    def add(self):
        return sum(self.numbers)
