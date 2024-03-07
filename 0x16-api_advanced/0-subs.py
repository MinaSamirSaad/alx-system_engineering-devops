#!/usr/bin/python3
"""
    quering the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
        Function that queries the Reddit API and returns the number
        of subscribers.
        @subreddit: suscriptors
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        return 0
    jreq = request.json()

    if 'data' in jreq:
        return jreq.get("data").get("subscribers")
    else:
        return 0
