#!/usr/bin/python3
"""
This module defines a Square class, which inherits from BaseGeometry,
and validates the size and calculates its area.
"""


class BaseGeometry:
    """
    A base class for geometric objects.
    """

    def area(self):
        """
        Raises an Exception if area is not implemented in a subclass.

        Raises:
            Exception: If not implemented in subclass
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.

        Args:
            name (str): The name to include in error messages.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(BaseGeometry):
    """
    A class representing a square, inheriting from BaseGeometry.
    The square validates its size and calculates its area.
    """

    def __init__(self, size):
        """
        Initialize a new square object with validated size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)

        # Private attribute with double underscores
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square in the format:
        [Square] <size>/<size>

        Returns:
            str: The string representation of the square.
        """
        return (f"[Square] {self.__size}/"
                f"{self.__size}")

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
