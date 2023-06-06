#!/usr/bin/python3
"""Queries reddit api for num of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    resp = requests.get(url, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        return 0
    return resp.json().get('data').get('subscribers')
