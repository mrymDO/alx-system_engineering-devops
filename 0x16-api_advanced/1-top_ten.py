#!/usr/bin/python3
"""1-top_ten"""

import requests


def top_ten(subreddit):
    """print titles of first 10 posts in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-Agent"}
    allow_redirects = False
    response = requests.get(
            url, headers=headers, allow_redirects=allow_redirects)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children'][:10]

            for post in posts:
                title = post['data']['title']
                print(title)
        except KeyError:
            print(None)
    else:
        print(None)
