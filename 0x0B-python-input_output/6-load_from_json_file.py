#!/usr/bin/python3
"""writes serialized text to a file"""


import json


def load_from_json_file(filename):
    """writes serialized text to a file"""
    with open(filename, "r", encoding="UTF-8") as fi:
        text = fi.read()
    return json.loads(text)
