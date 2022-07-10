#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for element in list(a_dictionary):
        if a_dictionary[element] == value:
            del(a_dictionary[element])
    return a_dictionary
