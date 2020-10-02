# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""

from som.vmobjects.object import Object

class Array(Object):
    '''
    An array behavior.

    Parameters
    ----------
    nilObject: Object(None) or nil equivalent
    number_of_indexable_fields: int
    '''
    def __init__(self, nilObject, number_of_indexable_fields):
        Object.__init__(self, nilObject)

        # Private array of indexable fields
        self._indexable_fields = [nilObject] * number_of_indexable_fields

    '''
    Get the indexable field with the given index.

    Parameters
    ----------
    index: integer
    '''
    def get_indexable_field(self, index):
        return self._indexable_fields[index]

    '''
    Set the indexable field with the given index to the given value.

    Parameters
    ----------
    index: integer
    value: object
    '''
    def set_indexable_field(self, index, value):
        self._indexable_fields[index] = value

    '''
    Get the number of indexable fields in this array.
    '''
    def get_number_of_indexable_fields(self):
        return len(self._indexable_fields)

    '''
    Allocate a new array which has one indexable field more than this array.

    Parameters
    ----------
    value: object
    universe: Universe
        The universe the VM operates in.
    '''
    def copy_and_extend_with(self, value, universe):
        result = universe.new_array_with_length(self.get_number_of_indexable_fields() + 1)
        # Copy the indexable fields from this array to the new array
        self._copy_indexable_fields_to(result)
        # Insert the given object as the last indexable field in the new array
        result.set_indexable_field(self.get_number_of_indexable_fields(), value)
        # Return the new array
        return result

    '''
    Copy all indexable fields from this array to the destination array.

    Parameters
    ----------
    destination: Array
        Destination array the indexable fieslds will be copied in.
    '''
    def _copy_indexable_fields_to(self, destination):
        for i in range(self.get_number_of_indexable_fields()):
            destination.set_indexable_field(i, self.get_indexable_field(i))

    '''
    Equality operator. Compares length and the fields for equality.
    '''
    def __eq__(self, other):
        if self.get_number_of_fields() != other.get_number_of_fields():
            return False
        else:
            eq = True
            for i in range(self.get_number_of_fields()):
                eq = eq & (self.get_indexable_field(i) == other.get_indexable_field(i))
            return eq
