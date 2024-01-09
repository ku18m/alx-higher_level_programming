#!/usr/bin/node
const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    const char = c || 'X';
    for (let row = 0; row < this.height; row++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
