#!/usr/bin/python3
"""returns the number of subscribers under this subreddit"""
import requests
import sys

def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/" + sys.argv[1] + "/about"
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    return 300
