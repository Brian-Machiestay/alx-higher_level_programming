#!/usr/bin/python3
""" post an email"""
import requests
import sys

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(res.text)
