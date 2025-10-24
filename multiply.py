#create a multiplication operation : of any number

class Multiplication:
    def __init__(self, *args):
        self.numbers = args

    def multiply(self):
        result = 1
        for num in self.numbers:
            result *= num
        return result