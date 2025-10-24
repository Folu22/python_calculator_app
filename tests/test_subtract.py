#testing the subtract function
from subtract import Subtraction
import unittest

class TestSubtraction(unittest.TestCase):
    def test_subtract_two_numbers(self):
        operation = Subtraction(10, 5)
        self.assertEqual(operation.subtract(), 5)

    def test_subtract_multiple_numbers(self):
        operation = Subtraction(20, 5, 3, 2)
        self.assertEqual(operation.subtract(), 10)

    def test_subtract_no_numbers(self):
        operation = Subtraction()
        self.assertEqual(operation.subtract(), 0)

    def test_subtract_single_number(self):
        operation = Subtraction(15)
        self.assertEqual(operation.subtract(), 15)

if __name__ == '__main__':
    unittest.main()
