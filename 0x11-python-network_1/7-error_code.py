#!/usr/bin/python3
"""check the error code"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code is not requests.code.ok:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
