# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest
from som.vm        import SymbolTable
from som.vmobjects import Symbol

class SymbolTableTestCase(unittest.TestCase):

    def setUp(self):
        self.table  = SymbolTable()
        self.symbol = Symbol(nilObject = False, value = "foo")

    def test_insert(self):
        self.assertIsNone(self.table.lookup("foo"))
        self.table.insert(self.symbol)
        self.assertEqual(self.symbol, self.table._map["foo"])

    def test_lookup(self):
        self.table.insert(self.symbol)
        self.assertEqual(self.table.lookup("foo"), self.symbol)

if __name__ == "__main__":
    unittest.main()
