#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class, which serves as a base for
geometry-related operations. It includes methods for validating integers
and a placeholder method for calculating the area of geometric shapes.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class is meant to be subclassed by other classes that implement
    specific geometric operations, such as calculating the area of shapes.
    The `area` method must be overridden by subclasses, and the
    `integer_validator` method ensures that
    values used in geometry calculations
    are valid positive integers.
    """

    def area(self):
        """
        Raises an exception if the area method is not implemented.

        This method is a placeholder intended to be overridden by subclasses
        that represent specific geometric shapes. If a subclass does not
        implement this method, an exception is raised to indicate the missing
        implementation.

        Raises:
            Exception: If the method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.

        This method checks if the provided value is an integer and greater
        than zero. It raises appropriate exceptions if the value is not an
        integer or is less than or equal to zero.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
