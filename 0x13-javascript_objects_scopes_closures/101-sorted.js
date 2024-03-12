#!/usr/bin/node

const originalDict = require('./101-data').dict;

const newDict = Object.entries(originalDict).reduce((result, [userId, occurrences]) => {
  if (occurrences in result) {
    result[occurrences].push(userId);
  } else {
    result[occurrences] = [userId];
  }
  return result;
}, {});

console.log(newDict);
