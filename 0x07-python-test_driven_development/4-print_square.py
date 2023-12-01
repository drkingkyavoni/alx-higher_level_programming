#!/usr/bin/python3
"""
    Module contains print_square
    Returns: None
    Test contained in tests/4-print_square.txt
"""


def print_square(size: int) -> None:
    if not isinstance(size, int) or \
     (not isinstance(size, float) and (size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#"*size)
