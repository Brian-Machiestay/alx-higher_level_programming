#!/usr/bin/python3
"""writes serialized text to a file"""


import json


def save_to_json_file(my_obj, filename):
    """writes serialized text to a file"""
    with open(filename, "w", encoding="UTF-8") as fi:
        fi.write(json.dumps(my_obj))
