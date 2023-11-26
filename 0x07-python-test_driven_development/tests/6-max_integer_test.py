#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Test if input parameters are valid
        Return exception
    """
    def TestMaxIntegerValues(self):
        # check the value of the function is valid
        with self.assertRaises(TypeError):
            max_integer((2, 3))
            max_integer([[], []])
            max_integer([None])
            max_integer('b')
            max_integer(2.0)
            max_integer([1, (2, 3), 4.0])
            max_integer([{'a': 2}, 4.0, 1])
            max_integer([1, 'a', 3.0])
            max_integer([1, 2.0, 3.0])
            max_integer([None, 2.0, 3.0])
            max_integer([1/0, 2])

    """
        Test for null input parameters and assert output values
    """
    def TestMaxIntegerResultsNullValue(self):
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    """
        Test for valid input parameters and assert output values
    """
    def TestMaxIntegerResults(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1e10, -3e11, -4e12, -2e13]), -1e10)
        self.assertEqual(max_integer([1e10, 3e11, 4e12, 2e13]), 2e13)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([1, -1]), 1)
        self.assertEqual(max_integer([-1, 1]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)
