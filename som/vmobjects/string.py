# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""


from som.vmobjects.object import Object

class String(Object):
    '''
    String representation with an embedded value. The real value is hidden as an
    embedded instance variable.

    Parameters
    ----------
    nilObject: Object(None) or nil object equivalent.
    value: Actual string value.
    '''
    def __init__(self, nilObject, value):
        Object.__init__(self, nilObject)
        self._string = value

    def get_embedded_string(self):
        '''
        Output the embedded string value.
        '''
        return self._string

    def __str__(self):
        '''
        String representation. The actual string object between double quotes.
        '''
        return "\'" + self._string + "\'"
