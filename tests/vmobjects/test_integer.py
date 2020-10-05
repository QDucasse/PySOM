# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest

from som.vmobjects.biginteger import BigInteger
from som.vmobjects.integer import Integer
from som.vmobjects.object import Object


class IntegerTestCase(unittest.TestCase):

    def setUp(self):
        self.integer = Integer(Object(None), 3)
        self.big_integer = BigInteger(Object(None), 30000000000)

    def test_get_embedded_integer(self):
        self.assertEqual(3, self.integer.get_embedded_integer())

    def test_get_embedded_value_integer_and_big_integer(self):
        self.assertEqual(3, self.integer.get_embedded_value())
        self.assertEqual(30000000000, self.big_integer.get_embedded_value())

    def test_string_representation(self):
        self.assertEqual("3", str(self.integer))

    def test_value_fits(self):
        self.assertTrue(Integer.value_fits(3))
        self.assertFalse(Integer.value_fits(-2147483647))
        self.assertFalse(Integer.value_fits(2147483648))
