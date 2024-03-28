#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status using the
`requests` library. It displays the body of the response.
"""

import requests

if __name__ == "__main__":
    # Sending a GET request to the URL
    response = requests.get('https://alx-intranet.hbtn.io/status')
    # Extracting the content of the response
    content = response.text  # 'text' returns the content as a string

    # Displaying the required information
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
