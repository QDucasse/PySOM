# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""

class SymbolTable(object):
    '''
    A table of symbols mapping strings to their corresponding symbols.
    '''
    def __init__(self):
        self._map = {}

    def lookup(self, string):
        '''
        Lookup the given string in the hash map.

        Parameters
        ----------
        string: string
            String to lookup
        '''
        return self._map.get(string, None)

    def insert(self, symbol):
        '''
        Insert the given symbol into the hash map by associating the
        symbol associated string to the symbol itself

        Parameters
        ----------
        string: string
            String to lookup
        '''
        # Insert the given symbol into the hash map by associating the
        # symbol associated string to the symbol itself
        self._map[symbol.get_string()] = symbol
