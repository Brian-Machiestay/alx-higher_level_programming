#!/usr/bin/python3
low = list(range(97, 123))
upper = list(range(65, 91))
for i in range(25, -1, -1):
    a = chr(upper[i])
    b = chr(low[i])
    print("{}".format(a if i % 2 == 0 else b), end="")
