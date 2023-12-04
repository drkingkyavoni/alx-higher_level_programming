#!/usr/bin/python3
""" Module contains class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """ function that instantiates the class
        Returns:
            void
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ function prints area of rectangle
        Returns:
            int: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ function prints string
        Returns:
            str: formatted string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
