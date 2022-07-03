#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no = len(sys.argv)
    count = 0
    if no == 1:
        print("{}".format(0))
    else:
        for i in range(1, no):
            count = count + int(sys.argv[i])
        print("{}".format(count))
