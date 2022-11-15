#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

const file = argv[2];
const str = argv[3];
fs.writeFile(file, str, (err) => {
  if (err) console.error(err);
});
