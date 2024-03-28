#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Set the default value of q as an empty string
    q = "" if len(sys.argv) < 2 else sys.argv[1]

    # Data to be sent in the POST request
    data = {'q': q}

    # Send a POST request to the URL with the q parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Parse the JSON response
        json_response = response.json()

        if json_response:
            # If the JSON is not empty, display the id and name
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            # If the JSON is empty, display "No result"
            print("No result")
    except ValueError:
        # If the JSON is not properly formatted, display "Not a valid JSON"
        print("Not a valid JSON")
