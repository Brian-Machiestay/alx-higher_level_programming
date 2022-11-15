#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const fs = require('fs');

const url = argv[2];
const file = argv[3];
request(url, function (error, response, body) {
  if (error) console.error(error);
  const content = body;
  fs.writeFile(file, content, (err) => {
    if (err) console.error(err);
  });
});
