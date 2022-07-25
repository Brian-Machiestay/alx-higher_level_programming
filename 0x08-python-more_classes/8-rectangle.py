#!/usr/bin/python3
""" this module creates
an empty rectangle
"""


class Rectangle:
    """this class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """this instance method returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this instance method sets the value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this method returns the height field"""
        return self.__height

    @height.setter
    def height(self, value):
        """this method sets he height field"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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
                string = string + str(self.print_symbol)
            if i != self.__height - 1:
                string = string + "\n"
        return string

    def __repr__(self):
        """returns a string repres. of the rect. so eval can recreate"""
        string = "Rectangle("
        string = string + str(self.__width) + ", " + str(self.height) + ")"
        return string

    def __del__(self):
        """deletes an istance of this class"""
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
        del self

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the rect with biggest size"""
        if not(isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not(isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
