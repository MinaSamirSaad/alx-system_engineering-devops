#!/usr/bin/python3
"""AdvancedAPI"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns the hotest title recursivly"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "random user"
    }
    params = {
        "after": after,
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if req.status_code != 200:
        return None if not hot_list else hot_list
    res = req.json().get('data')
    after = res.get('after')
    children = res.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
