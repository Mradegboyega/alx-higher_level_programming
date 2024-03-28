#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Take the URL from command line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the X-Request-Id header is present in the response
    if 'X-Request-Id' in response.headers:
        # Print the value of the X-Request-Id header
        print(response.headers['X-Request-Id'])
