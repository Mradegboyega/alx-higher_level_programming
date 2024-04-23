#!/usr/bin/node
const request = require('request');

// Retrieve the URL from the command-line arguments
const url = process.argv[2];

if (!url) {
  console.log('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Function to make a GET request and print the status code
function getStatus(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Call the function with the provided URL
getStatus(url);
