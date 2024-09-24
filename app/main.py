# main.py

from calculator import Calculator

# Create an instance of the Calculator class
calc = Calculator()

# Perform calculations
a = 10
b = 5

print(f"{a} + {b} = {calc.add(a, b)}")
print(f"{a} - {b} = {calc.subtract(a, b)}")
print(f"{a} * {b} = {calc.multiply(a, b)}")
print(f"{a} / {b} = {calc.divide(a, b)}")
