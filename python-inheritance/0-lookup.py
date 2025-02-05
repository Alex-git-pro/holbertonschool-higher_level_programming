#!/usr/bin/python3
"""
This module contains the function `lookup` that returns the list of attributes
and methods of an object.

Function:
    lookup(obj): Returns a list of all attributes
    and methods of the given object.

Args:
    obj (any): The object whose attributes and methods are to be retrieved.

Returns:
    list: A list of strings representing the names
    of the attributes and methods
          of the object.
"""


def lookup(obj):
    return dir(obj)
