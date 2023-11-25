#!/usr/bin/python3

"""
    This module contains  a matrix_divided function
    Return: list
    Tested in tests/2-matrix_divided.txt
"""


def matrix_divided(matrix: list, div):
    """
        Returns a matrix divided by a non-zero number
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(set([len(row) for row in matrix])) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if any(not isinstance(elem, (int, float))
           for row in matrix for elem in row):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    return [[round(elem / div, 2) for elem in row] for row in matrix]
