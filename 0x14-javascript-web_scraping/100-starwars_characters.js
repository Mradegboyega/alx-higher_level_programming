#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function printCharacters(movieId) {
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to fetch data, status code:', response.statusCode);
      return;
    }

    console.log(body.title);
    console.log();

    const characters = body.characters;

    // Fetch character details and print their names
    characters.forEach(characterUrl => {
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

printCharacters(movieId);
