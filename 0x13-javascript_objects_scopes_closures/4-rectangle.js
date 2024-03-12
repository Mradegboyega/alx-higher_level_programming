#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // Create an empty object if conditions are not met
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print() {
    if (!this.width || !this.height) {
      return; // Do not print if the object is empty
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    // Exchange the width and height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    // Double the width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
