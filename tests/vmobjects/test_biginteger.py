# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest

from som.vmobjects.biginteger import BigInteger
from som.vmobjects.integer import Integer
from som.vmobjects.object import Object


class BigIntegerTestCase(unittest.TestCase):

    def setUp(self):
        self.big_integer = BigInteger(Object(None), 30000000000)
        self.integer = Integer(Object(None), 3)

    def test_get_embedded_biginteger(self):
        self.assertEqual(30000000000, self.big_integer.get_embedded_biginteger())

    def test_get_embedded_value(self):
        self.assertEqual(30000000000, self.big_integer.get_embedded_value())

    def test_get_embedded_value_integer_and_big_integer(self):
        self.assertEqual(3, self.integer.get_embedded_value())
        self.assertEqual(30000000000, self.big_integer.get_embedded_value())
