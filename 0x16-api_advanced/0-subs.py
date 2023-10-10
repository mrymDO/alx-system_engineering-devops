#!/usr/bin/python3
"""0-sub"""

import requests
import json

def number_of_subscribers(subreddit):
    """return total subscribers for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    total_subscribers = data['data']['subscribers']
    return total_subscribers
