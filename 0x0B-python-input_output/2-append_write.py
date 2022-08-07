#!/usr/bin/python3
"""this module appends to a file"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, "a", encoding="UTF-8") as fi:
        count = fi.write(text)
    return count
