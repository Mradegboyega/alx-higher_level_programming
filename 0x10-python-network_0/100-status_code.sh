#!/bin/bash
# This script sends a request to a URL and displays only the status code of the response

# Send the request using curl and store the exit code
curl -s -o /dev/null -w "%{http_code}" "$1"
