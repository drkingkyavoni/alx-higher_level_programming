#!/usr/bin/python3
""" Module contains Base class testcases
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Class contains testcases for Base class
    """

    def test_base_class(self):
        """ Test cases for Base class
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
