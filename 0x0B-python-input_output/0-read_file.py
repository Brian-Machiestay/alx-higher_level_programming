#!/usr/bin/python3
"""this module reads from a file"""


def read_file(filename=""):
    """this functions reads a file"""

    with open(filename, "r", encoding="UTF-8") as thisfile:
        print(thisfile.read(), end="")
