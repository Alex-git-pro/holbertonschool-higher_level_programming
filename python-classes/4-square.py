#!/usr/bin/python3
"""
Defines a class Square that represents a square.

The `Square` class allows you to set the size of the square with validation
for the type and value of the size, and also provides a method to calculate
the area of the square.

Attributes:
    __size (int): The size of the square. Initialized during object creation.

Methods:
    size: Property to get and set the size of the square.
    area(): Returns the area of the square, calculated as size * size.
"""

class Square:
    """
    A class representing a square.

    This class allows the creation of square objects with a size, and ensures
    that the size is a non-negative integer. The class also includes a method 
    to calculate the area of the square.

    Attributes:
        __size (int): The size of the square (private attribute).

    Args:
        size (int): The size of the square. Default is 0.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        The area of the square is calculated as size * size.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
