#!/usr/bin/node

require('process');
const argv = process.argv;
function add (a, b) {
  return (a + b);
}
const first = argv[2];
const second = argv[3];
console.log(add(parseInt(first), parseInt(second)));
