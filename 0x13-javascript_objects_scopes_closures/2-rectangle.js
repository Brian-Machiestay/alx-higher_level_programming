#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!w || w === 0 || w < 0) return;
    if (!h || h === 0 || h < 0) return;
    this.width = w;
    this.height = h;
  }
};
