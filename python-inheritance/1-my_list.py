#!/usr/bin/python3
"""
This module defines a class `MyList` that
inherits from the built-in `list` class.
The class adds an additional method `print_sorted` to print the list sorted in
ascending order.
"""


class MyList(list):
    """
    A subclass of the built-in `list` class that
    adds a method to print the list
    in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        This method does not modify the original list but creates a sorted copy
        and prints it.
        """
        print(sorted(self))
