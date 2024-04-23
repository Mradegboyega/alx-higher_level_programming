#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

// Wedge Antilles character ID
const wedgeId = '18';

function countWedgeAppearances(url) {
  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to get data, status code:', response.statusCode);
      return;
    }

    let count = 0;
    const films = body.results;

    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        count++;
      }
    }

    console.log(count);
  });
}

countWedgeAppearances(apiUrl);
