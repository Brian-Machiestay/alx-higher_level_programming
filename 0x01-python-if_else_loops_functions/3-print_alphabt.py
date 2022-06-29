#!/usr/bin/python3
for w in range(97, 123):
    if w == 101 or w == 113:
        continue
    print("{}".format(chr(w)), end="")
