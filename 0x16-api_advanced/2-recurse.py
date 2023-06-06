#!/usr/bin/python3
"""query reddit api"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    """recursively return list containing hot post titles for a given sub"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced:project:\
                    v1.0.0 (by /u/firdaus_cartoon_jr)"
                    }
    params = {
            'after':after,
            'count':count,
            'limit':100
            }
    resp = requests.get(url, headers=headers, params=params,
            allow_redirects=False)
    if resp.status_code in (302, 404):
        return 404
    resp_json = resp.json()
    after = resp_json.get('data').get('after')
    count += resp_json.get('data').get('dist')
    if count == 0:
        return None
    for post in resp_json.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, count=count, after=after)
