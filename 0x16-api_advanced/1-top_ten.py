#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user_agent = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=user_agent)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            data = response.json()
            children = data.get('data', {}).get('children', [])
            for post in children:
                print(post.get('data', {}).get('title'))
        except ValueError:
            print("Invalid JSON response from Reddit API")
    else:
        print(f"Error: HTTP status code {response.status_code}")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script_name.py subreddit_name")
    else:
        top_ten(argv[1])

