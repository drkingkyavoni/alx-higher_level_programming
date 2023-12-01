#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""


class Rectangle:
    """ class Square defines a square
        Args:
            width: int
            height: int
    """

    def __init__(self, width=0, height=0):
        """
            Initialize private width and height
            Args:
                width: int
                height: int
            Return: void
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Return: int
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
            Return: int
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
