#!/usr/bin/python3
"""
This module contains a function `is_same_class` that checks if an object
is an instance of a specified class, without considering inheritance.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    This function returns True if the object is an instance of `a_class`
    and not an instance of a subclass. It does not consider inheritance
    when performing the check.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of `obj` with.

    Returns:
        bool: True if the object is an instance of the specified class,
              False otherwise.
    """
    return type(obj) is a_class
