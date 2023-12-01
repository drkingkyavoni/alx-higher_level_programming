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
        Attributes:
            area
            perimeter
            __str__
            __repr__
    """

    number_of_instances: int = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize private width and height
            Attributes:
                width: int
                height: int
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Print string when instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))

    @property
    def width(self):
        """ Set property width as private
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Validate width as integer and greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Set property height as private
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Validate height as integer and greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Function calculates the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Function calculates the perimeter of a rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """ Function to print str of class
        """
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self) -> str:
        """ Function to print repr of class
        """
        return "{}({}, {})".format(
            eval('self.__class__.__name__'),
            self.__width,
            self.__height
        )

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Function returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ Function returns a new Rectangle instance with
            width == height == size
        """
        cls.height, cls.width = size, size
        return Rectangle(cls.height, cls.width)
