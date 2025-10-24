#Buiding the calculator app main module that imports all operations

from add import Addition
from subtract import Subtraction
from multiply import Multiplication
from divide import Division

class Calculator:
    def __init__(self):
        self.addition = Addition
        self.subtraction = Subtraction
        self.multiplication = Multiplication
        self.division = Division

    def calculate(self, operation, *args):
        if operation == 'add':
            return self.addition(*args).add()
        elif operation == 'subtract':
            return self.subtraction(*args).subtract()
        elif operation == 'multiply':
            return self.multiplication(*args).multiply()
        elif operation == 'divide':
            return self.division(*args).divide()
        else:
            raise ValueError("Invalid operation")
        
if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.calculate('add', 1, 2, 3, 4, 5))
    print("Subtraction:", calc.calculate('subtract', 10, 2, 3))
    print("Multiplication:", calc.calculate('multiply', 1, 2, 3, 4))
    print("Division:", calc.calculate('divide', 100, 2, 5)) 
    