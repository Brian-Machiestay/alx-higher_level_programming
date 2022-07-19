#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    try:
        for i in range(0, list_length):
            try:
                a.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                a.append(0)
                print("division by 0")
                continue
            except TypeError:
                a.append(0)
                print("wrong type")
                continue
            except IndexError:
                a.append(0)
                print("out of range")
                continue
    finally:
        return a
