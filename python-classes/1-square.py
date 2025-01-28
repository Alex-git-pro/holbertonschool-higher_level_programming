#!/usr/bin/python3
"""
Defines a class Square that represents a square.

This module defines a `Square` class that is initialized with a size 
parameter. It currently only stores the size of the square as a private 
attribute (`__size`), and it does not yet have methods to compute other 
properties, such as area or perimeter.

Attributes:
    __size (int): The size of the square, initialized when the object is created.

Todo:
    * Implement a method to calculate the area of the square.
    * Implement a method to calculate the perimeter of the square.
    * Add validation to ensure the size is a positive integer.
"""

class Square:
    """
    A class that defines a square.

    The square is initialized with a size. This class currently only has an
    attribute to store the size, but future methods can be added for more
    functionality.

    Attributes:
        __size (int): The size of the square (private attribute).

    Args:
        size (int): The size of the square. It is assigned to the private
            attribute `__size`.

    Todo:
        * Add getter and setter for the size attribute.
        * Add validation to ensure the size is positive.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        This method takes a parameter `size` and assigns it to the private
        attribute `__size`.

        Args:
            size (int): The size of the square. This value is stored
                as a private attribute.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        if size <= 0:
            raise ValueError("size must be a positive integer")
        self.__size = size
