# ---------------------------------------------------------
# Name: Shahnaj Latif
# QCC ID: (add your QCC ID here)
# ET574 - Homework 5 - Math Library Tests
# ---------------------------------------------------------

import unittest
from my_math import fibonacci, mean, factorial

class TestMyMath(unittest.TestCase):

    # ----- fibonacci -----
    def test_fibonacci_basic(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_errors(self):
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(-1)
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(3.5)
        with self.assertRaises((TypeError, ValueError)):
            fibonacci("7")

    # ----- mean -----
    def test_mean_basic(self):
        self.assertAlmostEqual(mean([1, 2, 3]), 2.0)
        self.assertAlmostEqual(mean([1.5, 2.5]), 2.0)
        self.assertAlmostEqual(mean([0, 0, 0, 0]), 0.0)

    def test_mean_mixed_and_single(self):
        self.assertAlmostEqual(mean([42]), 42.0)
        self.assertAlmostEqual(mean([1, 2.0, 3]), 2.0)

    def test_mean_errors(self):
        with self.assertRaises((ValueError, ZeroDivisionError)):
            mean([])
        with self.assertRaises((TypeError, ValueError)):
            mean([1, "two", 3])

    # ----- factorial -----
    def test_factorial_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_errors(self):
        with self.assertRaises((TypeError, ValueError)):
            factorial(-3)
        with self.assertRaises((TypeError, ValueError)):
            factorial(4.2)
        with self.assertRaises((TypeError, ValueError)):
            factorial("10")


if __name__ == "__main__":
    unittest.main(verbosity=2)
