# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""

from som.vmobjects.object import Object

class Double(Object):
    '''
    Double representation. The real value is hidden as an embedded instance variable.

    Parameters
    ----------
    nilObject: Object(None) or nil object equivalent.
    value: Actual double value.
    '''
    def __init__(self, nilObject, value):
        Object.__init__(self, nilObject)
        self._embedded_double = value

    def get_embedded_double(self):
        '''
        Output the embedded double value.
        '''
        return self._embedded_double
