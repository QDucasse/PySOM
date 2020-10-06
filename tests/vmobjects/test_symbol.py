# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""


import unittest
from som.vmobjects.object import Object
from som.vmobjects.symbol import Symbol

class SymbolTestCase(unittest.TestCase):

    def setUp(self):
        self.symbol = Symbol(Object(None), "test")
        unary_signature_strings = [
            "size", "addTwo", "use", "call",
            "parse", "hash", "notify", "setUp",
            "weight", "isOk", "isNotOk", "create"
        ]
        self.unary_signature_symbols = [Symbol(Object(None),string) for string in unary_signature_strings]

        binary_signature_chars = [
            "~", "&", "|", "*", "/",
            "@", "+", "-", "=", ">",
            "<", ",", "%", "\\"
        ]
        self.binary_signature_symbols = [Symbol(Object(None),char) for char in binary_signature_chars]

        keyword2_signature_strings = [
            "at:put:", "remove:from:", "add:withKey:",
            "choose:from:", "add:from:", "choose:and:"
        ]
        self.keyword2_signature_symbols = [Symbol(Object(None),string) for string in keyword2_signature_strings]

        keyword3_signature_strings = [
            "at:put:and:", "choose:divide:andAddTo:",
            "add:to:andNotify:", "parse:addTo:export:"
        ]
        self.keyword3_signature_symbols = [Symbol(Object(None),string) for string in keyword3_signature_strings]

    def test_get_string(self):
        self.assertEqual("test", self.symbol.get_string())

    # ====
    def test_is_binary_signature_binary_symbol(self):
        for symbol in self.binary_signature_symbols:
            self.assertTrue(symbol.is_binary_signature())

    def test_is_binary_signature_unary_symbol(self):
        for symbol in self.unary_signature_symbols:
            self.assertFalse(symbol.is_binary_signature())

    def test_is_binary_signature_keyword2_symbol(self):
        for symbol in self.keyword2_signature_symbols:
            self.assertFalse(symbol.is_binary_signature())

    def test_is_binary_signature_keyword3_symbol(self):
        for symbol in self.keyword3_signature_symbols:
            self.assertFalse(symbol.is_binary_signature())
    # ====
    # ====
    def test_determine_number_of_signature_arguments_unary_symbol(self):
        for symbol in self.unary_signature_symbols:
            self.assertEqual(1,symbol._determine_number_of_signature_arguments())

    def test_determine_number_of_signature_arguments_binary_symbol(self):
        for symbol in self.binary_signature_symbols:
            self.assertEqual(2,symbol._determine_number_of_signature_arguments())

    def test_determine_number_of_signature_arguments_keyword2_symbol(self):
        for symbol in self.keyword2_signature_symbols:
            self.assertEqual(3,symbol._determine_number_of_signature_arguments())

    def test_determine_number_of_signature_arguments_keyword3_symbol(self):
        for symbol in self.keyword3_signature_symbols:
            self.assertEqual(4,symbol._determine_number_of_signature_arguments())
    # ====
    # ====
    def test_get_number_of_signature_arguments_unary_symbol(self):
        for symbol in self.unary_signature_symbols:
            self.assertEqual(1,symbol.get_number_of_signature_arguments())

    def test_get_number_of_signature_arguments_binary_symbol(self):
        for symbol in self.binary_signature_symbols:
            self.assertEqual(2,symbol.get_number_of_signature_arguments())

    def test_get_number_of_signature_arguments_keyword2_symbol(self):
        for symbol in self.keyword2_signature_symbols:
            self.assertEqual(3,symbol.get_number_of_signature_arguments())

    def test_get_number_of_signature_arguments_keyword3_symbol(self):
        for symbol in self.keyword3_signature_symbols:
            self.assertEqual(4,symbol.get_number_of_signature_arguments())
    # ====

    def test_str(self):
        self.assertEqual("#test", str(self.symbol))
