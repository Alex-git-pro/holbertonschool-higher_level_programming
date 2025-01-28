#!/usr/bin/python3
"""
Defines a class Square with size validation and area calculation.

The `Square` class is initialized with a size and validates the type and 
value of the size to ensure it is a non-negative integer. It also includes 
a method to calculate the area of the square.

Attributes:
    __size (int): The size of the square. Initialized during object creation.

Methods:
    area(): Returns the area of the square, calculated as size * size.
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

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        This method takes a parameter `size` and assigns it to the private 
        attribute `__size` after validating its type and value.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        The area of the square is calculated as size * size.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
