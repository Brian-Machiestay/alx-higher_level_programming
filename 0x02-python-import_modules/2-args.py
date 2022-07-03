#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenth = len(sys.argv)
    if lenth == 1:
        print("{} arguments.".format(0))
    elif lenth == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(lenth - 1))
        for i in range(1, lenth):
            print("{}: {}".format(i, sys.argv[i]))
