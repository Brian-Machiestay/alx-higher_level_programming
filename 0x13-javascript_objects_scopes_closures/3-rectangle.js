#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!w || w === 0 || w < 0) return;
    if (!h || h === 0 || h < 0) return;
    this.width = w;
    this.height = h;
  }

  print () {
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) square = square + 'X';
      if (i < this.height - 1) square = square + '\n';
    }
    console.log(square);
  }
};
