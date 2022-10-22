#!/usr/bin/python3
"""use the urllib module to fetch a webpage"""
import urllib.request as req


fetched = req.Request('https://alx-intranet.hbtn.io/status')
with req.urlopen(fetched) as ff:
    content = ff.read()
    print("Body response:")
    print("    -type: {}".format(type(content)))
    print("    -content: {}".format(content))
    print("    -utf8 content: {}".format(content.decode('utf-8')))
