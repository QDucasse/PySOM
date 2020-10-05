# -*- coding: utf-8 -*-
"""
@author: Stefan Marr
Reformating - Quentin DUCASSE
"""

import abc

class Invokable(abc.ABC):
    '''
    A common abstract class for methods and primitives.
    '''

    @abc.abstractmethod
    def is_primitive(self):
        '''
        Tells whether this is a primitive.
        '''
        raise NotImplementedError()

    @abc.abstractmethod
    def invoke(self, frame, interpreter):
        '''
        Invoke this invokable object in a given frame.

        Parameters
        ----------
        frame: Frame
        interpreter: Interpreter
        '''
        raise NotImplementedError()

    @abc.abstractmethod
    def get_signature(self):
        '''
        Get the signature for this invokable object.
        '''
        raise NotImplementedError()

    @abc.abstractmethod
    def get_holder(self):
        '''
        Get the holder for this invokable object.
        '''
        raise NotImplementedError()

    @abc.abstractmethod
    def set_holder(self, value):
        '''
        Set the holder for this invokable object.

        Parameters
        ----------
        value: holder object.
        '''
        raise NotImplementedError()
