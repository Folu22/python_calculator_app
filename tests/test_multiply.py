#Test the multiplication functionality in multiply.py
from multiply import Multiplication

multiply = Multiplication(1, 2, 3, 4, 5)

def test_multiply():
    assert multiply.multiply() == 120

print(test_multiply)