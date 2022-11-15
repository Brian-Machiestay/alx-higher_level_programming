#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const starApi = argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/' + 18 + '/';
request(starApi, function (error, response, body) {
  if (error) console.error(error);
  let count = 0;
  for (const obj of JSON.parse(body).results) {
    if (obj.characters.includes(character)) count++;
  }
  console.log(count);
});
