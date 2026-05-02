import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """Create a Calculator instance before each test."""
        self.calc = Calculator()

    # Tests for the add method
    def test_add_positive_numbers(self):
        """Adding two positive numbers should return their sum."""
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_negative_numbers(self):
        """Adding two negative numbers should return their sum."""
        result = self.calc.add(-3, -7)
        self.assertEqual(result, -10)

    def test_add_mixed_sign_numbers(self):
        """Adding a positive and a negative number should return the correct result."""
        result = self.calc.add(8, -3)
        self.assertEqual(result, 5)

    # Tests for the subtract method
    def test_subtract_positive_numbers(self):
        """Subtracting a smaller positive number from a larger one should return the difference."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_subtract_negative_numbers(self):
        """Subtracting a negative number should effectively add its absolute value."""
        result = self.calc.subtract(-5, -2)
        self.assertEqual(result, -3)

    def test_subtract_mixed_sign_numbers(self):
        """Subtracting a positive number from a negative number should return the correct negative result."""
        result = self.calc.subtract(-3, 5)
        self.assertEqual(result, -8)


if __name__ == "__main__":
    unittest.main()