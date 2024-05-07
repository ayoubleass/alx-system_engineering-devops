#!/usr/bin/python3
"""This script has a function that
Returns the number of subscribers for a given subreddit"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code >= 300 or r.status_code < 200:
        return 0
    return "{}".format(r.json().get('data').get('subscribers'))
