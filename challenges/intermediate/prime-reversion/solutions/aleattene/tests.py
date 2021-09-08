
""" To start the tests, type from CLI: python tests.py """

import unittest
from solution import solve


class TestSolution(unittest.TestCase):

    def test_prime_numbers_from_pairs(self):
        self.assertEqual(solve(0, 20), 14)
        self.assertEqual(solve(2, 200), 457)
        self.assertEqual(solve(100, 200), 92)
        self.assertEqual(solve(2, 300), 794)
        self.assertEqual(solve(2, 2000), 17705)
        self.assertEqual(solve(2, 5000), 83742)
        self.assertEqual(solve(4, 5000), 83424)
        self.assertEqual(solve(100, 7500), 159608)
        self.assertEqual(solve(300, 8000), 166798)
        self.assertEqual(solve(1000, 9000), 168410)
        self.assertEqual(solve(2000, 9000), 124222)
        self.assertEqual(solve(3000, 9500), 105167)
        self.assertEqual(solve(5000, 10000), 59575)
        self.assertEqual(solve(9967, 10000), 1)
        self.assertEqual(solve(9968, 10000), 0)


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
