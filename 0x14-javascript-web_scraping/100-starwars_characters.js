#!/usr/bin/node
const request = require('request');
const argv = process.argv;
let starApi = 'https://swapi-api.hbtn.io/api/people/';
const id = argv[2];
const film = 'https://swapi-api.hbtn.io/api/films/' + id + '/';
while (starApi !== null) {
  request(starApi, function (error, response, body) {
    if (error) console.error(error);
    const parsedBody = JSON.parse(body);
    console.log(parsedBody);
    for (const obj of parsedBody.results) {
      if (obj.films.includes(film)) console.log(obj.name);
    }
    starApi = parsedBody.next;
  });
}
