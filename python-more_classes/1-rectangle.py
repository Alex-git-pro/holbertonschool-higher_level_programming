#!/usr/bin/python3
"""
Module that defines a class Rectangle
"""



class Rectangle:
    """
    A class to define a rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with width and height

        Args:
            width (int) -> the width of the rectangle (default 0)
            height (int) -> the height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrives the width of the rectangle

        Return:
            int: the width of the rectanfgle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): the new width of the rectangle

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retives the height of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): the new height of the rectangle

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
