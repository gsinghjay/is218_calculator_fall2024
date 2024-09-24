"""Unit tests for the Calculator class."""

import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_addition(calculator, a, b, expected):
    """Test addition method of Calculator."""
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 5, -5),
    (5.5, 2.5, 3.0),
])
def test_subtraction(calculator, a, b, expected):
    """Test subtraction method of Calculator."""
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 100, 0),
    (2.5, 4, 10.0),
])
def test_multiplication(calculator, a, b, expected):
    """Test multiplication method of Calculator."""
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-4, -2, 2),
    (5, 2, 2.5),
])
def test_division(calculator, a, b, expected):
    """Test division method of Calculator."""
    assert calculator.divide(a, b) == expected

@pytest.mark.parametrize("a, b, exception", [
    (10, 0, ZeroDivisionError),
    (0, 0, ZeroDivisionError),
])
def test_division_by_zero(calculator, a, b, exception):
    """Test division method for division by zero."""
    with pytest.raises(exception):
        calculator.divide(a, b)
