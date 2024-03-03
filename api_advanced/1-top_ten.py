#!/usr/bin/python3
"""1-top_ten.py"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]
    elif response.status_code == 302:
        print("None")
    else:
        print("None")


if __name__ == "__main__":
    top_ten(sys.argv[1])
