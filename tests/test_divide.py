#Testing the division function
import pytest
from divide import Division

def test_divide_positive_numbers():
    operation = Division(100, 2, 5)
    assert operation.divide() == 10

def test_divide_by_zero():
    operation = Division(10, 0)
    with pytest.raises(ValueError):
        operation.divide()

def test_divide_no_numbers():
    operation = Division()
    assert operation.divide() is None

def test_divide_single_number():
    operation = Division(50)
    assert operation.divide() == 50

def test_divide_negative_numbers():
    operation = Division(-100, 2, -5)
    assert operation.divide() == 10

print(test_divide_positive_numbers)
print(test_divide_by_zero)
print(test_divide_no_numbers)
print(test_divide_single_number)
print(test_divide_negative_numbers)
print("All division tests passed.")

