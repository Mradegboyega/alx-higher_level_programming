#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file as the request body, and displays the body of the response

# Check if both URL and filename are provided as arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

# Send the POST request with curl and display the body of the response
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
