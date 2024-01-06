#!/usr/bin/python3
"""
Unittests for max_integer function
"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -5, -2, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -3, 5, -2, 4]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Failed for empty list")

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42, "Failed for single element list")

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_mixed_types(self):
        with self.assertRaises(TypeError, msg="Failed for mixed types"):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()

