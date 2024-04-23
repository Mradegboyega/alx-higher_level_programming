#!/usr/bin/node
const request = require('request');

// Retrieve the movie ID from the command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./3-starwars_title.js <movie ID>');
  process.exit(1);
}

// Construct the URL for the Star Wars API request
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch and print the movie title
function getMovieTitle(url) {
  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode === 200) {
      console.log(body.title);
    } else {
      console.log(`Failed to get data, status code: ${response.statusCode}`);
    }
  });
}

// Call the function with the constructed URL
getMovieTitle(apiUrl);
