#!/usr/bin/python3
"""this module writes to a file"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, "w", encoding="UTF-8") as fi:
        count = fi.write(text)
    return count
