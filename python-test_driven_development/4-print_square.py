#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of size 'size' using the character '#'.

    Arguments:
    size -- the size (length of the side) of the square

    If `size` is not an integer, raises TypeError with the message "size must be an integer".
    If `size` is a float and less than 0, raises TypeError with the message "size must be an integer".
    If `size` is less than 0, raises ValueError with the message "size must be >= 0".
    """
    if type(size) != int:
        if type(size) == float:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
