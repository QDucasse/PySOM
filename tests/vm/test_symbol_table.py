# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest
from som.vm import SymbolTable

class SymbolTableTestCase(unittest.TestCase):

    def setup(self):
        self.table  = SymbolTable()
        self.symbol = Symbol(nilObject = false, "foo")

    def test_insert(self):
        self.table.insert(self.symbol)
        self.assertEqual(self.symbol, self.table.lookup("foo"))
