#!/usr/bin/python3
# use the request package to fetch a url
import requests
if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(str(res))))
    print('\t- content: {}'.format(res.text))
