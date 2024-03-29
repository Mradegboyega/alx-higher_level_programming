#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing "You got me!" in the body of the response

# Send the request with curl and set the data in the request body
curl -sX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "http://0.0.0.0:5000/catch_me"
