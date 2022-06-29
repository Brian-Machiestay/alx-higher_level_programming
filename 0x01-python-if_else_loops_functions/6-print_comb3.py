#!/usr/bin/python3
count = 1
for w in range(0, 9):
    for i in range(count, 10):
        if w == 8 and i == 9:
            print("{}".format(89))
            continue
        print("{}{}, ".format(w, i), end="")
    count = count + 1
