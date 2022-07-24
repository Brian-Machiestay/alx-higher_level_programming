#!/usr/bin/python3
"""this module adds two integers
defines the function add_integer
which adds two integers

"""


def add_integer(a, b=98):
    """this function adds two integers
    takes the integer values a and b and adds them

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    thisa = int(a)
    thisb = int(b)
    return thisa + thisb
