#!/usr/bin/python3
""" Module contains pascal_triangle function
"""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers
    representing the Pascal’s triangle
    """
    arr = [[1 for _ in range(i+1)] for i in range(n)]

    arr2 = []
    for i in range(n):
        arr2.append(arr[i])
        for j in range(1, i):
            arr2[i][j] = arr[i-1][j-1] + arr[i-1][j]
    return arr2
