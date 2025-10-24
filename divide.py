#create divison operation : of any number

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def division(self):
        div = self.a / self.b
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by Zero (0)")
        else:
            print("Number divisible")
        return div
    

