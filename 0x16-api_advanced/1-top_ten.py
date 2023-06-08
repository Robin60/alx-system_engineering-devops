#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced:project:\
                    v1.0.0 (by /u/firdaus_cartoon_jr)"
                    }
    params = {
             "limit": 10
             }
    resp = requests.get(url, allow_redirects=False, headers=headers,
                        params=params)
    if resp.status_code in (302, 404):
        print("None")
        return
    else:
        res = resp.json().get("data")
        [print(r.get("data").get("title")) for r in res.get("children")]
