#!/usr/bin/python3
""" this module creates
an empty rectangle
"""


class Rectangle:
    """this class defines a rectangle"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """this instance method returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this instance method sets the value of the width"""
        self.__init__(value, self.__height)

    @property
    def height(self):
        """this method returns the height field"""
        return self.__height

    @height.setter
    def height(self, value):
        """this method sets he height field"""
        self.__init__(self.__width, value)

    def area(self):
        """this method returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns the str repres. of the rect."""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string = string + "#"
            if i != self.__height - 1:
                string = string + "\n"
        return string
