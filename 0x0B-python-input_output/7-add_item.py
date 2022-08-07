#!/usr/bin/python3
"""this module adds all args to a list and saves to a file"""

if __name__ == "__main__":

    import sys
    import json
    from os import path
    load_j = __import__('6-load_from_json_file').load_from_json_file
    save_j = __import__('5-save_to_json_file').save_to_json_file

    listobj = []
    count = 0
    for i in sys.argv:
        if count == 0:
            count = count + 1
            continue
        listobj.append(i)
        count = count + 1

    try:
        obj = load_j("add_item.json")
    except(Exception):
        open("add_item.json", "w", encoding="UTF-8")
        obj = open("add_item.json", "r", encoding="UTF-8")
        obj = obj.read()

    if obj == "":
        save_j(listobj, "add_item.json")
    else:
        obj = list(obj)
        obj.extend(listobj)
        save_j(obj, "add_item.json")
