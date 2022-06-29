#!/usr/bin/python3
def uppercase(str):
    low = list(range(97, 123))
    upper = list(range(65, 91))
    for i in str:
        if ord(i) in low:
            print("{}".format(chr(upper[low.index(ord(i))])), end="")
            continue
        print("{}".format(i), end="")
