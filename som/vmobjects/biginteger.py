# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""

from som.vmobjects.object import Object

class BigInteger(Object):
    '''
    Big integer representation to be used when using numbers bigger than 2147483647
    or smaller than -2147483646. The real value is hidden in as embedded.

    Parameters
    ----------
    nilObject: Object(None) or nil object equivalent.
    value: Actual integer value.
    '''
    def __init__(self, nilObject, value):
        Object.__init__(self, nilObject)
        self._embedded_biginteger = value

    def get_embedded_biginteger(self):
        '''
        Output the embedded big integer value.
        '''
        return self._embedded_biginteger

    def get_embedded_value(self):
        """
        Output the embedded big integer value. This method is polymorphic with Integer.
        """
        return self._embedded_biginteger
