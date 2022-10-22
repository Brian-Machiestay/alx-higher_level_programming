#!/usr/bin/python3
"""return the value of a specific header"""
import sys
import urllib.request as req

if __name__ == "__main__":
    res = req.Request(sys.argv[1])
    with req.urlopen(res) as ff:
        print(ff.headers.__getitem__("X-Request-Id"))
