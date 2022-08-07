#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """returns the dict of this obj instance for serialization"""
    return obj.__dict__
