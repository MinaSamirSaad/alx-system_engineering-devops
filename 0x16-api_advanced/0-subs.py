#!/usr/bin/python3
"""AdvancedAPI"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of suscribers"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "random user"
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
        allow_redirects=False
    )
    if req.status_code >= 300:
        return 0
    try:
        res = req.json().get('data', None).get('subscribers', None)
        return res if res else 0
    except Exception as e:
        return 0
