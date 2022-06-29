#!/usr/bin/python3
for w in range(0, 9):
    for i in range(1, 10):
        if w == 8 and i == 9:
            print("{}".format(89))
            continue
        print("{}{}, ".format(w, i), end="")
