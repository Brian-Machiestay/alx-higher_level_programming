#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenth = len(my_list)
    for i in range(lenth-1, -1, -1):
        print("{:d}".format(my_list[i]))
