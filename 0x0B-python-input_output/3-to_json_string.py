#!/usr/bin/python3
"""this module serializes a string"""


import json


def to_json_string(my_obj):
    """does the real stuff"""
    return json.dumps(my_obj)
