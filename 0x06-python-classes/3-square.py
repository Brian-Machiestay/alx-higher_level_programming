#!/usr/bin/python3
"""creates a square module and instantiates it"""


class Square:
    """the square class"""
    def __init__(self, size=0):
        """instantiates the size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
