#!/usr/bin/node

require('process');
const argv = process.argv;
const size = parseInt(argv[2]);
let square = '';
if (!size) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) square = square + 'X';
    if (i < size - 1) square = square + '\n';
  }
  if (size > 0) console.log(square);
}
