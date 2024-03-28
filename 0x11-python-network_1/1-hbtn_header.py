#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # The first command-line argument is the script name, so the URL is the second
    url = sys.argv[1]

    # Using 'with' for automatic resource management
    with urllib.request.urlopen(url) as response:
        # Each header can be accessed like a dictionary
        # The 'get' method is used to avoid exceptions if the header doesn't exist
        request_id = response.getheader('X-Request-Id')
        print(request_id)
