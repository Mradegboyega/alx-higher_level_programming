#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

function downloadContentToFileSync(url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to fetch data, status code:', response.statusCode);
      return;
    }

    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  });
}

downloadContentToFileSync(url, filePath);
