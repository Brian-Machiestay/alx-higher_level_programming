#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newd = dict(a_dictionary)
    for key in list(newd):
        newd[key] = newd[key] * 2
    return newd
