#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const id = argv[2];
const starApi = 'https://swapi-api.hbtn.io/api/films/' + id + '/';
request(starApi, function (error, response, body) {
  if (error) console.error(error);
  console.log(JSON.parse(body).title);
});
