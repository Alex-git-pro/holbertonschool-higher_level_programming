#!/usr/bin/python3
"""
Defines a class Square that represents a square.

This module defines a `Square` class which initializes the size of the square 
with a given value. It validates the type and value of the size parameter to 
ensure it is a non-negative integer.

Attributes:
    __size (int): The size of the square. Initialized during object creation.

Todo:
    * Implement a method to calculate the area of the square.
    * Implement a method to calculate the perimeter of the square.
"""

class Square:
    """
    A class that defines a square.

    This class is initialized with a size. The constructor validates that the
    size is an integer and that it is greater than or equal to 0. If the size 
    is invalid, an exception is raised.

    Attributes:
        __size (int): The size of the square (private attribute).

    Args:
        size (int): The size of the square. It is assigned to the private 
            attribute `__size`.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is negative.
    """
