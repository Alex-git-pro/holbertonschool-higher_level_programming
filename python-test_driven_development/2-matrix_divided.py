#!/usr/bin/python3
"""
Module to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Parameters:
    - matrix : a list of lists of integers or floats
    - div : a number (integer or float)

    Returns:
    A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats,
               if rows of the matrix have different sizes,
               if div is not a number.
    ZeroDivisionError: If div is 0.

    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]
    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> matrix_divided([[1, 2], [3, 4]], 'a')
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats"
                )

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [
        [
            round(elem / div, 2) for elem in row
        ]
        for row in matrix
    ]
