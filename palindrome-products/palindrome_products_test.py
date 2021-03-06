"""
Notes regarding the implementation of smallest_palindrome and
largest_palindrome:

Both functions must take two keyword arguments:
    max_factor -- int
    min_factor -- int, default 0

Their return value must be a tuple (value, factors) where value is the
palindrome itself, and factors is an iterable containing both factors of the
palindrome in arbitrary order.
"""

import unittest

from palindrome_products import smallest_palindrome, largest_palindrome


class PalindromesTests(unittest.TestCase):

    def test_largest_palindrome_from_single_digit_factors(self):
        value, factors = largest_palindrome(max_factor=9)
        self.assertEqual(value, 9)
        self.assertIn(set(factors), [{1, 9}, {3, 3}])

    def test_largest_palindrome_from_double_digit_factors(self):
        value, factors = largest_palindrome(max_factor=99, min_factor=10)
        self.assertEqual(value, 9009)
        self.assertEqual(set(factors), {91, 99})

    def test_smallest_palindrome_from_double_digit_factors(self):
        value, factors = smallest_palindrome(max_factor=99, min_factor=10)
        self.assertEqual(value, 121)
        self.assertEqual(set(factors), {11})


    def test_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest_palindrome(max_factor=999, min_factor=100)
        self.assertEqual(value, 906609)
        self.assertEqual(set(factors), {913, 993})

    def test_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = smallest_palindrome(max_factor=999, min_factor=100)
        self.assertEqual(value, 10201)
        self.assertEqual(set(factors), {101, 101})


if __name__ == '__main__':
    unittest.main()
