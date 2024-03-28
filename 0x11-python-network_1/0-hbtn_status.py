#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
using the urllib package.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # The 'with' statement ensures resources are cleaned up promptly after use
    with urllib.request.urlopen(url) as response:
        # Read the body of the response
        body = response.read()
        print("Body response:")
        # Print the type of the body
        print("\t- type:", type(body))
        # Print the content of the body
        print("\t- content:", body)
        # Print the UTF-8 representation of the body
        print("\t- utf8 content:", body.decode('utf-8'))
