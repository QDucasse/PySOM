# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest

from som.vmobjects.double import Double
from som.vmobjects.integer import Integer
from som.vmobjects.object import Object


class ObjectTestCase(unittest.TestCase):

    def setUp(self):
        self.object_integer = Object(None)
        self.object_integer._class = Integer

    def test_get_class(self):
        self.assertEqual(Integer, self.object_integer.get_class())

    def test_set_class(self):
        self.object_integer.set_class(Double)

    def test_get_field_name(self):
        pass

    def test_get_field_index(self):
        pass

    def test_get_number_of_fields(self):
        pass

    def test_get_default_number_of_fields(self):
        self.assertEqual(self.object_integer.NUMBER_OF_OBJECT_FIELDS,
                         self.object_integer._get_default_number_of_fields())

    def test_get_field(self):
        pass

    def test_set_field(self):
        pass

    def test_send(self):
        pass

    def test_send_does_not_understand(self):
        pass

    def test_send_unknown_global(self):
        pass

    def send_escaped_block(self):
        pass

    def test_str(self):
        self.assertEqual("a Integer", str(self.object_integer))
