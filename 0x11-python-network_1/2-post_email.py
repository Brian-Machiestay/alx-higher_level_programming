#!/usr/bin/python3
"""return the value of a specific header"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    res = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(res) as ff:
        print(ff.read().decode('utf-8'))
