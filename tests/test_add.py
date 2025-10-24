#Test the addition functionality in add.py
from add import Addition


add = Addition(1, 2, 3, 4, 5)
def test_add():
    assert add.add() == 15

print(test_add)

