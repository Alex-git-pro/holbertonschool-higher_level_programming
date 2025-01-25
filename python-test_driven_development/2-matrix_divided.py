#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (integer or float) used as divisor.

    Returns:
        A new matrix where each element is the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
        TypeError: If rows of matrix are not of the same size.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(elm, (int, float)) for row in matrix
               for elm in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(elm / div, 2) for elm in row] for row in matrix]
