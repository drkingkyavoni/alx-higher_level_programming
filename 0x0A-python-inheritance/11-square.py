#!/usr/bin/python3
""" Module contains Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class
    """
    def __init__(self, size):
        """ function initializes Square class
        Args:
            int: size
        Returns:
            None
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ function calculates area of square
        Returns:
            int: area of square
        """
        return self.__size ** 2

    def __str__(self):
        """ function that prints string representation
        Returns:
            str: string rep of Square
        """
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__size, self.__size)
