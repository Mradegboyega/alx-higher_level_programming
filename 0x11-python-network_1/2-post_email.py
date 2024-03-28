#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Take the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data to be sent in the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Data should be bytes

    # Make a POST request and read the response
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_body = response.read()
        print(response_body.decode('utf-8'))
