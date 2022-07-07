#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if a_dictionary == dict():
        return
    count = a_dictionary[list(a_dictionary)[0]]
    for key in list(a_dictionary):
        if a_dictionary[key] > count:
            count = a_dictionary[key]
            keyf = key
    return key
