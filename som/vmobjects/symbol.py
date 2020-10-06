# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""


from som.vmobjects.object import Object

class Symbol(Object):
    '''
    Representation of a symbol. A symbol is composed of a string attribute and is
    recognisable in Smalltalk due to the '#' at the beginning. A symbol can be
    anything from a character to a string to a method name.

    Parameters
    ----------
    nilObject: Object(None) or nil object equivalent.
    value: String representation.
    '''
    def __init__(self, nilObject, value):
        Object.__init__(self, nilObject)
        self._string = value
        self._number_of_signature_arguments = self._determine_number_of_signature_arguments() # updated later

    def get_string(self):
        '''
        Get the string associated to this symbol
        '''
        return self._string

    def _determine_number_of_signature_arguments(self):
        '''
        Determine the number of signature arguments by first checking if the
        symbol is a binary method, then it counts the number of colons.

        Example:
        #+       --> 2 (binary operator)
        #at:put: --> 3 (keyword operator)
        #at:     --> 2 (keyword operator)
        #size    --> 1 (unary operator)
        '''
        # Check for binary signature
        if self.is_binary_signature():
            return 2
        else:
            # Count the colons in the signature string
            number_of_colons = 0

            # Iterate through every character in the signature string
            for c in self._string:
                if c == ':':
                    number_of_colons += 1

            # The number of arguments is equal to the number of colons plus one
            return number_of_colons + 1

    def get_number_of_signature_arguments(self):
        '''
        Outputs the number of signature arguments determined with
        _determine_number_of_signature_arguments() used when the object is
        created.
        '''
        return self._number_of_signature_arguments

    def is_binary_signature(self):
        '''
        Checks if the signature is the one of a binary operator.
        '''
        # Check the individual characters of the string
        for c in self._string:
            if (c != '~' and c != '&' and c != '|' and c != '*' and c != '/' and
                c != '@' and c != '+' and c != '-' and c != '=' and c != '>' and
                c != '<' and c != ',' and c != '%' and c != '\\'):
                return False
        return True

    def __str__(self):
        '''
        String representation: # followed by the embedded string.
        '''
        return "#" + self._string
