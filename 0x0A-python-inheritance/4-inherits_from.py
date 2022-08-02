#!/usr/bin/python3
"""this module checks instance"""


def inherits_from(obj, a_class):
    """checks is instance"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
