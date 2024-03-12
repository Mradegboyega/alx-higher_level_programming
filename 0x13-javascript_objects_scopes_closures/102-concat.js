#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

try {
  const content1 = fs.readFileSync(sourceFile1, 'utf-8');
  const content2 = fs.readFileSync(sourceFile2, 'utf-8');
  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destinationFile, concatenatedContent);

  console.log(`Files "${sourceFile1}" and "${sourceFile2}" successfully concatenated to "${destinationFile}".`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
