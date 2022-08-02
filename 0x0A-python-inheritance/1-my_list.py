#!/usr/bin/python3
"""this module creates a subclass of a list"""


class MyList(list):
    """this class subclasses a list object"""

    def print_sorted(self):
        """this function prints a list in sorted order"""
        this = self[:]
        this.sort()
        print(this)
