#!/usr/bin/python3
""" this module print a text with
two lines after . ? :
"""


def text_indentation(text):
    """ this function does exactly
    what is described in the module
    """

    chars = ".?:"
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in chars:
            print(text[i], end="\n\n")
            i = i + 2
            continue
        print(text[i], end="")
        i = i + 1
