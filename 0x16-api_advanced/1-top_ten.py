#!/usr/bin/python3
"""AdvancedAPI"""
import requests


def top_ten(subreddit):
    """Returns the top 10 hotest posts for a given subreddit"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "random user"
    }
    params = {
        "limit": 10
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if req.status_code != 200:
        print('None')
    else:
        res = req.json().get('data').get('children')
        for children in res:
            print(children.get('data').get('title'))
