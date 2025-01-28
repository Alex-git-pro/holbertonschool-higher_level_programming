#!/usr/bin/python3
"""
Defines a class Square with size and position attributes.

The `Square` class allows you to set the size of the square with validation
for the type and value of the size, as well as a position attribute that 
controls where the square is printed. The class provides methods for 
calculating the area of the square and printing the square with a specified 
position.

Attributes:
    __size (int): The size of the square (private attribute).
    __position (tuple): A tuple of two non-negative integers representing
                         the position of the square when printed.

Methods:
    size: Property to get and set the size of the square.
    position: Property to get and set the position of the square.
    area(): Returns the area of the square, calculated as size * size.
    my_print(): Prints the square with a given position, using '#' characters.
"""

class Square:
    """
    A class representing a square with a specific size and position.

    This class allows the creation of square objects with a size, and ensures
    that the size is a non-negative integer. The class also includes methods
    to calculate the area of the square and print it with a specified position.

    Attributes:
        __size (int): The size of the square (private attribute).
        __position (tuple): The position of the square when printed. A tuple
                             of two non-negative integers.

    Args:
        size (int): The size of the square. Default is 0.
        position (tuple): A tuple representing the position. Default is (0, 0).

    Raises:
        TypeError: If size is not an integer or position is not a tuple of two
                   positive integers.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a valid tuple.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): A tuple of two non-negative integers representing
                           the position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
             not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        The area of the square is calculated as size * size.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character, starting from the given position.

        The square is printed line by line. The position of the square is 
        determined by the position attribute, which indicates how many lines 
        and spaces to print before the actual square starts.

        Example:
            If size is 4 and position is (2, 1), the output will be:
            
            (2 blank lines)
            (1 space for indentation) ####
            (1 space for indentation) ####
            (1 space for indentation) ####
            (1 space for indentation) ####

        If the size is 0, just prints a new line.

        """
        if self.__size == 0:
            print()
            return

        # Print empty lines based on the vertical position
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square with leading spaces
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
