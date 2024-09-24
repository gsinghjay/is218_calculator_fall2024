# calculator.py

from app.operations import addition, subtraction, multiplication, division

class Calculator:
    """Calculator Class that uses functions from operations module"""

    @staticmethod # do not have to instantiate a class
    def create():
        return Calculator()

    def add(self, a, b):
        """Add two numbers using the addition function from operations module."""
        return addition(a, b)

    def subtract(self, a, b):
        """Subtract two numbers using the subtraction function from operations module."""
        return subtraction(a, b)

    def multiply(self, a, b):
        """Multiply two numbers using the multiplication function from operations module."""
        return multiplication(a, b)

    def divide(self, a, b):
        """Divide two numbers using the division function from operations module."""
        return division(a, b)
