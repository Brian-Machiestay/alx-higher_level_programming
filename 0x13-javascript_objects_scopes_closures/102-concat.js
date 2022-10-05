#!/usr/bin/node

require('process');
const fs = require('fs');
const argv = process.argv;
fs.readFile(argv[2].toString(), 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(argv[4].toString(), data, (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
fs.readFile(argv[3].toString(), 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  fs.appendFile(argv[4].toString(), data, (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
