#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None or my_list == []:
        return
    newl = list(set(my_list))
    count = 0
    for i in newl:
        count = count + i
    return count
