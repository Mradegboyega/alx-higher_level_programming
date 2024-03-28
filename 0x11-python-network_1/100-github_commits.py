#!/usr/bin/python3
"""
A Python script that retrieves and prints the 10 most recent commits
of a repository from GitHub using its API.
"""

import requests
import sys

if __name__ == "__main__":
    # Take repository name and owner name from command-line arguments
    repository = sys.argv[1]
    owner = sys.argv[2]

    # URL for the GitHub API to fetch commits
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Get the JSON data from the response
        commits = response.json()

        # Iterate over the 10 most recent commits
        for commit in commits[:10]:
            # Extract SHA and author name from each commit
            sha = commit['sha']
            author_name = commit['commit']['author']['name']

            # Print the SHA and author name
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print("Error:", e)
