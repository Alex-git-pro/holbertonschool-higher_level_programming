#!/usr/bin/python3
"""
This module defines a BaseGeometry class for geometric operations and
a Rectangle class that inherits from BaseGeometry to represent a rectangle.

The BaseGeometry class includes:
- `area`: A placeholder method that raises an exception
if not implemented by a subclass.
- `integer_validator`: A method to validate
if a value is a positive integer.

The Rectangle class inherits from BaseGeometry and provides:
- `__init__`: Initializes a rectangle with validated width and height.
- `__str__`: Returns a string representation of the rectangle.
- `area`: Calculates the area of the rectangle.
"""


class BaseGeometry:
    """
    A base class for geometric objects.

    This class serves as a base for geometric shapes and provides
    functionality for validating integer values and calculating areas.
    """

    def area(self):
        """
        Raises an Exception if the area method is
        not implemented in a subclass.

        This method should be overridden by subclasses to calculate the area
        of specific geometric shapes.

        Raises:
            Exception: If not implemented in a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.

        This method checks whether the provided value is an integer and if
        it is greater than zero. It raises appropriate
        exceptions if validation fails.

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
    A class representing a rectangle, inheriting from BaseGeometry.

    This class validates the width and height of the rectangle and provides
    methods to calculate its area and represent it as a string.
    """

    def __init__(self, width, height):
        """
        Initialize a new rectangle object with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes with double underscores
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format:
        Rectangle: <width> - <height>

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle: {self.__width} - {self.__height}"

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height
