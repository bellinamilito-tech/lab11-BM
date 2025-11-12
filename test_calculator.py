# https://github.com/bellinamillito-tech/lab11-BM
# Partner 1: Bellina
# Partner 2: Bellina

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, -5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
