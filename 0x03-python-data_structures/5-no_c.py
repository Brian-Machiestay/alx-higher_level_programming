#!/usr/bin/python3
def no_c(my_string):
    lent = len(my_string)
    a = ""
    for i in range(0, lent):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        a = a + my_string[i]
    return a
