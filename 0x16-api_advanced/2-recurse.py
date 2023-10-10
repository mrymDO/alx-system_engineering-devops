#!/usr/bin/python3
"""2-recurse"""

import requests
import json


def recurse(subreddit, hot_list=[], after=None):
    """return a list that contains titles of hot articles for a subreddit"""
    if subreddit is None:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-Agent"}

    if after is not None:
        params = {'after': after}
    else:
        params = {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    else:
        data = response.json()
        posts = data.get("data").get("children")

        for post in posts:
            title = post.get("data").get("title")
            hot_list.append(title)

        after = data.get("data").get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
