#!/bin/usr/python3
"""this module prints
a square
"""


def print_square(size):
    """ this function
    prints a square using #
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size != 0:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
