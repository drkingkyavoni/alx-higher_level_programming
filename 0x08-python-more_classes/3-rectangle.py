#!/usr/bin/python3
"""
    Module contains class Rectangle
    Attributes:
        width: getter, setter
        height: getter, setter
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
            Initialize private width and height
            attributes:
                width: int
                height: int
            Return: void
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Return: __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Validate width as integer and greater than 0
            Return: void
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Return: __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Validate height as integer and greater than 0
            Return: void
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Function calculates the area of a rectangle
            Return: int
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Function calculates the perimeter of a rectangle
            Return: int
        """
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """
            Function to print str of class
            Return: str
        """
        return "\n".join(["#" * self.__width
                          for _ in range(self.__height)])

    def __repr__(self) -> str:
        """
            Function to print repr of class
            Return: str
        """
        return "<{}.{} object at {}>".format(
            self.__class__.__module__,
            self.__class__.__name__,
            hex(id(self))
        )
