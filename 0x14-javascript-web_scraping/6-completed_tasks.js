#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const Api = argv[2];
request(Api, function (error, response, body) {
  if (error) console.error(error);
  let count = 0;
  const finalobj = {};
  const parseBody = JSON.parse(body);
  for (let i = 1; i <= parseBody.length; i++) {
    for (const ob of parseBody) {
      if (ob.userId === i) {
        if (ob.completed === true) count++;
      }
    }
    if (count !== 0) finalobj[i] = count;
    count = 0;
  }
  console.log(finalobj);
});
