#!/usr/bin/node

const superSquare = require('./5-square.js');
module.exports = class Square extends superSquare {
  charPrint (c) {
    if (!c) this.print();
    else {
      let square = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) square = square + c;
        if (i < this.height - 1) square = square + '\n';
      }
      console.log(square);
    }
  }
};
