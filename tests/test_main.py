'''My Calculator Test'''
from app.main import addition, subtraction, multiplication, division, pytest

def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction Function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''Multiplication Function'''
    assert multiplication(2,2) == 4

def test_division():
    '''Division Function'''
    assert division(2,2) == 1

def test_division_by_zero_exception():
    '''Division Function testing that I get the exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
