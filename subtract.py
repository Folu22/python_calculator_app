# create a math operation: subtraction that subtracts as many numbers as the user wants

class Subtraction:
    def __init__(self, *args):
        self.numbers = args

    def subtract(self):
        if len(self.numbers) == 0:
            return 0
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result
    

        