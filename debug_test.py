"""Debug script to see what actually happens in the test."""

import sys

sys.path.insert(0, "src")

from calculator.calculator import Calculator

# Replicate the test conditions
calc = Calculator()
a = 100000000
b = 10

print(f"Input values: a={a}, b={b}")
print(f"Expected operation: {a} / {b}")

try:
    result = calc.divide(a, b)
    print(f"Result: {result}")
    print(f"Type: {type(result)}")
    print("No exception was raised!")
except ValueError as e:
    print(f"ValueError raised: {e}")
except Exception as e:
    print(f"Other exception raised: {type(e).__name__}: {e}")
