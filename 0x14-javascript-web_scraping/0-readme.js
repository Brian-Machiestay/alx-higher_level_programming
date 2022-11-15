#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

const arg1 = argv[2];
fs.readFile(arg1, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
