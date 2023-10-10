#!/usr/bin/python3
"""100-count"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keywords in the titles of hot articles from a subreddit"""
    if counts is None:
        counts = {}

    if subreddit is None:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-Agent"}

    params = {"after": after}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data").get("children")

    for post in posts:
        title = post.get("data").get("title").lower()
        for word in word_list:
            if title.count(word.lower()):
                if word in counts:
                    counts[word] += title.count(word.lower())
                else:
                    counts[word] = title.count(word.lower())

    after = data.get("data").get("after")
    if after is not None:
        return count_words(subreddit, word_list, after=after, counts=counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
