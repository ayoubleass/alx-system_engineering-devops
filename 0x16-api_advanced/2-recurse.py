#!/usr/bin/python3
"""This script queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    r = requests.get(url, headers={"User-Agent": "My-User-Agent"})
    if r.status_code >= 300:
        return None
    childrens = r.json().get("data").get("children")
    hot_list = hot_list + [child.get("data").get("title")
                           for child in childrens]
    if not r.json().get("data").get("after"):
        return hot_list
    return recurse(subreddit, hot_list, r.json().get("data").get("after"))
