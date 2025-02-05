#!/usr/bin/python3
"""
This module defines a base class for geometric shapes, `BaseGeometry`,
and a derived class, `Rectangle`, which represents a rectangle.

The `BaseGeometry` class provides methods for validating integer values
and calculating areas (although the area method is a placeholder).

The `Rectangle` class validates its width and height and provides methods
for calculating the area and representing the rectangle as a string.
"""


class BaseGeometry:
    """
    A base class for geometric objects.
    """

    def area(self):
        """
        Raises an exception if the area method
        is not implemented in a subclass.

        This method serves as a placeholder for
        subclasses to implement specific
        area calculation methods.

        Raises:
            Exception: If not implemented in a subclass.
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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle,
    inheriting from BaseGeometry.

    This class validates the width and height,
    calculates the area of the
    rectangle, and provides a string
    representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new rectangle object
        with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height
            is not an integer.
            ValueError: If width or height
            is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes with double underscores
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of
        the rectangle in the format:
        [Rectangle] <width>/<height>

        Returns:
            str: The string representation
            of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates and returns the area
        of the rectangle.

        Returns:
            int: The area of the
            rectangle (width * height).
        """
        return self.__width * self.__height
