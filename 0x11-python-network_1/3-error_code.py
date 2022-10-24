#!/usr/bin/python3
"""return the value of a specific header"""
import sys
import urllib.request as req
import urllib.error

if __name__ == "__main__":
    res = req.Request(sys.argv[1])
    try:
        with req.urlopen(res) as ff:
            print(ff.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
