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

    def my_print(self):
        """prints the square"""
        thissize = self.size
        if thissize == 0:
            print()
        else:
            for i in range(0, thissize):
                for j in range(0, thissize):
                    print("#", end="")
                print()
