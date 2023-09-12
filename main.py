


import calculator

def test_addition():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtraction():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, -1) == 0

def test_multiplication():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(-2, 4) == -8

def test_division():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(10, 5) == 2
    assert calculator.divide(0, 5) == 0

def test_divide_by_zero():
    try:
        calculator.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

