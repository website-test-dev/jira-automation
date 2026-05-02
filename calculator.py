# calculator.py

import math

class Calculator:
    """A simple calculator class providing basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b.

        If b is zero, prints an error message and returns None.
        """
        if b == 0:
            print("Error: Cannot divide by zero")
            return None
        return a / b

    def sqrt(self, a):
        """Return the square root of a.

        If a is negative, prints an error message and returns None.
        """
        if a < 0:
            print("Error: Cannot take square root of a negative number")
            return None
        return math.sqrt(a)

    def power(self, a, b):
        """Return a raised to the power of b."""
        return a ** b

    def run_tests(self):
        """Run a set of example calculations and display the results."""
        print("Welcome to the Calculator")
        print(f"2 + 3 = {self.add(2, 3)}")
        print(f"5 - 2 = {self.subtract(5, 2)}")
        print(f"4 * 5 = {self.multiply(4, 5)}")
        # Example division test (optional)
        try:
            print(f"10 / 2 = {self.divide(10, 2)}")
        except ZeroDivisionError as e:
            print(e)

        # Power test
        print(f"2 ** 3 = {self.power(2, 3)}")

        # Square root tests
        print(f"sqrt(16) = {self.sqrt(16)}")
        print(f"sqrt(-4) = {self.sqrt(-4)}")

if __name__ == "__main__":
    calc = Calculator()
    calc.run_tests()
    # Test divide by zero
    calc.divide(10, 0)