#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const url = argv[2];

request(url, function (error, response, body) {
  if (error) console.error(error);
  console.log('code:', response.statusCode);
});
