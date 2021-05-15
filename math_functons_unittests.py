import unittest

from math_functions import gcd


class GcdTest(unittest.TestCase):
    def test_happy_flow(self):
        self.assertEqual(1, gcd(10, 2))
        self.assertEqual(1, gcd(11, 2))


if __name__ == '__main__':
    unittest.main()
