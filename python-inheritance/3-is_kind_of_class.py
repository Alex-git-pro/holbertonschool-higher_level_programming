#!/usr/bin/python3
"""
This module contains a function `is_kind_of_class` that checks if an object
is an instance of a specified class or a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    This function considers inheritance, so it returns True if the object
    is an instance of the specified class or if it is an instance of any
    subclass of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of `obj` with.

    Returns:
        bool: True if the object is an instance of the specified class,
              or an instance of a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
