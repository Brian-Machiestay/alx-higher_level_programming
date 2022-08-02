#!/usr/bin/python3
"""creates no more empty geometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates a square"""
    def __init__(self, size):
        """instantiates this square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area"""
        return self.__size * self.__size
