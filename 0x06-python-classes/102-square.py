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

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        self.__init__(value)

    def __eq__(self, other):
        """compares two square objects"""
        return self.__size == other.__size

    def __ne__(self, other):
        """if two of this object are not equal"""
        return self.__size != other.__size

    def __lt__(self, other):
        """if this is less than the other methods"""
        return self.__size < other.__size

    def __le__(self, other):
        """check less equals"""
        return self.__size <= other.__size

    def __gt__(self, other):
        """check greater than"""
        return self.__size > other.__size

    def __ge__(self, other):
        """check greater or equal to"""
        return self.__size >= other.__size
