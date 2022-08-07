#!/usr/bin/python3
"""this deserializes a string"""


import json


def from_json_string(my_str):
    """does the real stuff"""
    return(json.loads(my_str))
