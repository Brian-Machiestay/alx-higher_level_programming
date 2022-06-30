#!/usr/bin/python3
def uppercase(str):
    low = list(range(97, 123))
    upper = list(range(65, 91))
    for i in str:
        j = ord(i)
        print("{}".format(chr(upper[low.index(j)])) if j in low else i, end="")
    print()
