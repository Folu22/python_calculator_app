#create divison operation : of any number

class Division:
    def __init__(self, *args):
        self.numbers = args

    def divide(self):
        if len(self.numbers) == 0:
            return None
        result = self.numbers[0]
        for num in self.numbers[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero")
            result /= num
        return result
    