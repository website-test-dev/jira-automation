import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Tests for Calculator add and subtract methods."""

    def setUp(self):
        self.calc = Calculator()

    # add tests
    def test_add_two_positives(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(5, -2), 3)

    def test_add_two_negatives(self):
        self.assertEqual(self.calc.add(-4, -6), -10)

    # subtract tests
    def test_subtract_two_positives(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtract_two_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

if __name__ == '__main__':
    unittest.main()