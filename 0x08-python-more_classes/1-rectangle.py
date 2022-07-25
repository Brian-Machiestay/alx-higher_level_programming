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
