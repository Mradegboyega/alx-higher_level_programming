#!/usr/bin/node
const fs = require('fs'); // Import the filesystem module

// Retrieve the file path from the command line arguments
const filePath = process.argv[2];

// Function to read and print the file content
function readFileAndPrint(path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      // Print the error if one occurred
      console.error(err);
    } else {
      // Print the data if no error
      console.log(data);
    }
  });
}

// Call the function with the provided file path
if (filePath) {
  readFileAndPrint(filePath);
} else {
  console.log("Please provide a file path as an argument.");
}
