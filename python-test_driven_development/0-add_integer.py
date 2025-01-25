#!/usr/bin/python3
"""
Module to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
    - a : an integer or float
    - b : an integer or float (default is 98)

    If a or b is not an integer or float, raise TypeError.

    Returns:
    - The sum of a and b as an integer.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
