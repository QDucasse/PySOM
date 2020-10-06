# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""


import unittest
from som.vmobjects.object import Object
from som.vmobjects.string import String

class StringTestCase(unittest.TestCase):

    def setUp(self):
        self.string = String(Object(None), "test")

    def test_get_embedded_string(self):
        self.assertEqual("test", self.string.get_embedded_string())

    def test_str(self):
        self.assertEqual("\'test\'", str(self.string))
