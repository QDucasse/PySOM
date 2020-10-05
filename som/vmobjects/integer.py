# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""


from som.vmobjects.object import Object

class Integer(Object):
    '''
    Integer representation to be used with numbers smaller than 2147483647 or
    bigger than -2147483646. The real value is hidden as an embedded instance
    variable.

    Parameters
    ----------
    nilObject: Object(None) or nil object equivalent.
    value: Actual integer value.
    '''
    def __init__(self, nilObject, value):
        Object.__init__(self, nilObject)
        self._embedded_integer = value

    def get_embedded_integer(self):
        '''
        Output the embedded double value.
        '''
        return self._embedded_integer

    def get_embedded_value(self):
        '''
        This Method is the same as get_embedded_integer() but is polymorphic
        with BigInteger.
        '''
        return self._embedded_integer

    def __str__(self):
        '''
        String representation corresponds to the actual integer in str form.
        '''
        return str(self._embedded_integer)

    @classmethod
    def value_fits(cls, value):
        '''
        Checks if the given integer is in the range of the Integer class. A
        false output means the integer should be handled by a BigInteger.

        Parameters
        ----------
        value: int
        '''
        return value <= 2147483647 and value > -2147483646
