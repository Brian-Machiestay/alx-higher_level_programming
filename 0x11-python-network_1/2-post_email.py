#!/usr/bin/python3
"""return the value of a specific header"""
import sys
import urllib.request as req

if __name__ == "__main__":
    res = req.Request(sys.argv[1], method="POST")
    res.data = {"email": sys.argv[2]}
    with req.urlopen(res) as ff:
        print(ff.read())
