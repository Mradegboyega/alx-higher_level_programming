#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL, and displays
the body of the response. Manages urllib.error.HTTPError exceptions to print
"Error code:" followed by the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Attempt to open the URL and read the response
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print("Error code:", e.code)
