# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest

from som.vm.universe import Universe
from som.vmobjects.array import Array
from som.vmobjects.object import Object


class ArrayTestCase(unittest.TestCase):

    def setUp(self):
        # Universe definition
        self.universe = Universe()
        # Array definition, 5 strings "bar"
        self.array = Array(Object(None), 5)
        for i in range(4):
            self.array.set_indexable_field(i, "bar")
        # Extended array definition, 5 strings "bar" followed by a string "foo"
        self.extended_array = Array(Object(None), 6)
        for i in range(4):
            self.extended_array.set_indexable_field(i, "bar")
        self.extended_array.set_indexable_field(5, "foo")

    def test_get_set_indexable_field(self):
        self.array.set_indexable_field(1, "foo")
        self.assertEqual("foo", self.array.get_indexable_field(1))

    def test_get_number_of_indexable_fields(self):
        self.assertEqual(5, self.array.get_number_of_indexable_fields())

    def test_copy_and_extend_with(self):
        extended_array = self.array.copy_and_extend_with("foo", self.universe)
        self.assertEqual(self.extended_array, extended_array)

    def test_copy_indexable_fields_to(self):
        # Populate a destination array with erroneous data to ensure it is overwritten
        destination = Array(Object(None), 5)
        for i in range(4):
            destination.set_indexable_field(i, "foo")
        self.array._copy_indexable_fields_to(destination)
        self.assertEqual(self.array, destination)
