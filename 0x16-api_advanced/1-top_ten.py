#!/usr/bin/python3
"""This script queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""


import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers={"User-Agent": "My-User-Agent"},
                     allow_redirects=False)
    if r.status_code != 200:
        print("None")
    else:
        [print(child.get("data").get("title"))
         for child in r.json().get("data").get("children")]
