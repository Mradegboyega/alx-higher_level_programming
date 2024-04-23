#!/usr/bin/node
const fs = require('fs'); // Import the filesystem module

// Get command-line arguments for the file path and the string to write
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Function to write a string to a file
function writeStringToFile(path, content) {
  fs.writeFile(path, content, 'utf8', (err) => {
    if (err) {
      // If an error occurs, print the error object
      console.error(err);
    } else {
      // Optionally, print a success message or do nothing on success
      console.log('File written successfully');
    }
  });
}

// Check if both arguments are provided
if (filePath && contentToWrite) {
  writeStringToFile(filePath, contentToWrite);
} else {
  console.log('Usage: ./1-writeme.js <file path> "<text to write>"');
}
