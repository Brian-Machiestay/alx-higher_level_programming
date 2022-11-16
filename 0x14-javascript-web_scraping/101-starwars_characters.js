#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const id = argv[2];
const film = 'https://swapi-api.hbtn.io/api/films/' + id + '/';
async req(film) {
  request(film, function (error, response, body) {
    if (error) console.error(error);
    const parsedBody = JSON.parse(body);
    for (const obj of parsedBody.characters) {
      await request(obj, function (error, response, bo) {
        if (error) console.error(error);
        console.log(JSON.parse(bo).name);
      });
    }
  })
};
req(film);
