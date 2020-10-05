# -*- coding: utf-8 -*-
"""
@author: Quentin DUCASSE
"""

import unittest

from som.vmobjects.block import Block
from som.vmobjects.object import Object


class BlockTestCase(unittest.TestCase):
    def setUp(self):
        self.method = 0
        self.context = 0
        self.block = Block(Object(None), )

    def test_number_of_block_fields(self):
        self.assertEqual(Object.NUMBER_OF_BLOCK_FIELDS, )
