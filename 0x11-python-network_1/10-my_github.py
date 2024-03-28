#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    # Take username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Construct the URL for the GitHub API to get user information
    url = f"https://api.github.com/users/{username}"

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response as JSON
        user_data = response.json()
        # Display the user ID
        print("Your GitHub user ID:", user_data["id"])
    else:
        # If the request was not successful, print an error message
        print("Failed to retrieve user ID. HTTP status code:", response.status_code)
