# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest

from som.vmobjects.double import Double
from som.vmobjects.object import Object


class DoubleTestCase(unittest.TestCase):

    def setUp(self):
        self.double = Double(Object(None), 5.5)

    def test_get_embedded_double(self):
        self.assertEqual(5.5, self.double.get_embedded_double())
