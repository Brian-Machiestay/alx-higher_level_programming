#!/usr/bin/python3
"""this module is a unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this class subclasses a unittest"""

    def test_max_integer(self):
        """this text the max integer func"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([5]), 5)
