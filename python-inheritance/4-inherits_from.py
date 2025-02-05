#!/usr/bin/python3
"""
This module defines a function `inherits_from` that checks if an object
is an instance of a class that inherited (directly or indirectly) from
the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    This function returns True if the object is an instance of a subclass
    of the specified class (not the class itself), including subclasses
    that are inherited indirectly. It returns False if the object is an
    instance of the specified class itself.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of `obj` with.

    Returns:
        bool: True if the object is an instance of a subclass of the specified
              class (but not the class itself), False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
