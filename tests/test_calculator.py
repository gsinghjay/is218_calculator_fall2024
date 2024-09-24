import pytest
from app.calculator import Calculator

# Fixture for the Calculator instance
@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator.create()

# Parameterized test for addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_addition(calc, a, b, expected):
    """Test addition method of Calculator."""
    assert calc.add(a, b) == expected

# Parameterized test for subtraction
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 5, -5),
    (5.5, 2.5, 3.0),
])
def test_subtraction(calc, a, b, expected):
    """Test subtraction method of Calculator."""
    assert calc.subtract(a, b) == expected

# Parameterized test for multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 100, 0),
    (2.5, 4, 10.0),
])
def test_multiplication(calc, a, b, expected):
    """Test multiplication method of Calculator."""
    assert calc.multiply(a, b) == expected

# Parameterized test for division
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-4, -2, 2),
    (5, 2, 2.5),
])
def test_division(calc, a, b, expected):
    """Test division method of Calculator."""
    assert calc.divide(a, b) == expected

# Parameterized test for division by zero
@pytest.mark.parametrize("a, b, exception", [
    (10, 0, ZeroDivisionError),
    (0, 0, ZeroDivisionError),
])
def test_division_by_zero(calc, a, b, exception):
    """Test division method for py tdivision by zero."""
    with pytest.raises(exception):
        calc.divide(a, b)
