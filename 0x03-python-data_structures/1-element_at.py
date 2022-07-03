#!/usr/bin/python3
def element_at(my_list, idx):
    lenth = len(my_list)
    if idx < 0 or idx > lenth - 1:
        return None
    return my_list[idx]
