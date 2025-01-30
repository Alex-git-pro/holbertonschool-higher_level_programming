#!/usr/bin/python3

class Rectangle:
    """
    A class that defines a rectangle with width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with the given width and height.
        Increments the class attribute 'number_of_instances'
        each time a new instance is created.

        Args:
            width (int): the width of the rectangle (default 0)
            height (int): the height of the rectangle (default 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): the new width of the rectangle.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): the new height of the rectangle.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: the area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
            int: the perimeter (2 * (width + height))
            or 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of
        the rectangle with print_symbol characters.

        Returns:
            str: a string representing the rectangle
            or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_line = str(self.print_symbol) * self.__width
        return "\n".join([rectangle_line] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of
        the rectangle that can be used to recreate it.

        Returns:
            str: a string that can be used to recreate the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the class attribute `number_of_instances`
        each time an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): the first rectangle.
            rect_2 (Rectangle): the second rectangle.

        Raises:
            TypeError: if either rect_1 or rect_2 is not
            an instance of Rectangle.

        Returns:
            Rectangle: the rectangle with the biggest area
            or rect_1 if areas are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
