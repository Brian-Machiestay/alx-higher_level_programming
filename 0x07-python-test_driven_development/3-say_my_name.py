#!/usr/bin/python3
""" this module prints
 a first name and a last name
"""


def say_my_name(first_name, last_name=""):
    """ this function
    prints the first and last name
    """

    if type(first_name) is not str and type(last_name) is not str:
        raise TypeError("first_name must be a string\n\
last_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
