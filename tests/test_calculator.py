import pytest

from calculator.calculator import Calculator, DivisionByZeroError

@pytest.fixture
def calculator():
    return Calculator()

def test_division_by_zero_raises(calculator):
    """geforderter Test für eine Exception"""
    with pytest.raises(DivisionByZeroError):
        calculator.divide(1, 0)

def test_add(calculator):
    assert calculator.add(3, 2) == 5

def test_add_zero(calculator):
    assert calculator.add(0, 0) == 0

def test_add_negative(calculator):
    assert calculator.add(-2, 3) == 1

def test_subtract(calculator):
    assert calculator.subtract(3, 2) == 1

def test_subtract_zero(calculator):
    assert calculator.subtract(0, 0) == 0

def test_subtract_negative(calculator):
    assert calculator.subtract(-2, 3) == -5

def test_multiply(calculator):
    assert calculator.multiply(3, 2) == 6

def test_multiply_zero(calculator):
    assert calculator.multiply(9999, 0) == 0

def test_multiply_negative(calculator):
    assert calculator.multiply(-9999, 0) == 0

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2

def test_divide_negative(calculator):
    assert calculator.divide(-9, 3) == -3

def test_is_even(calculator):
    assert calculator.is_even(10) == True

def test_is_odd(calculator):
    assert calculator.is_even(11) == False