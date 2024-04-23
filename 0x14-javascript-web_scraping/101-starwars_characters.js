#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function printCharactersInOrder(movieId) {
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to fetch data, status code:', response.statusCode);
      return;
    }

    const characterUrls = body.characters;

    // Fetch character details in order and print their names
    characterUrls.forEach(characterUrl => {
      request(characterUrl, { json: true }, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }
        if (response.statusCode !== 200) {
          console.error('Failed to fetch data, status code:', response.statusCode);
          return;
        }

        console.log(body.name);
      });
    });
  });
}

printCharactersInOrder(movieId);
