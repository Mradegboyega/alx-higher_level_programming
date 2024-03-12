#!/usr/bin/node

const ParentSquare = require('./5-square'); // Assuming the file is named 5-square.js

class Square extends ParentSquare {
  constructor(size) {
    super(size); // Call the constructor of the parent class (Square)
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X'; // Use 'X' if the character is undefined
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
