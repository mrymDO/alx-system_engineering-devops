#!/usr/bin/python3
"""100-count"""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-Agent"}
    params = {"after": after} if after else {}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        for keyword in word_list:
            keyword = keyword.lower()
            if title.count(keyword):
                counts[keyword] = counts.get(keyword, 0) + title.count(keyword)

    new_after = data.get("data", {}).get("after")
    if new_after:
        return count_words(subreddit, word_list, counts, after=new_after)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for keyword, count in sorted_counts:
        if count > 0:
            print(f"{keyword}: {count}")
