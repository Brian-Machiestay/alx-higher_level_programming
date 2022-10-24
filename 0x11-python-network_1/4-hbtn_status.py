#!/usr/bin/python3
""" use the requests package to query a site"""

import requests
if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(str(res))))
    print('\t- content: {}'.format(res.text))
