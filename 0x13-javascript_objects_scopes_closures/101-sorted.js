#!/usr/bin/node

const dict = require('./101-data.js');
const newdict = {};
const dct = dict.dict;
let newList = [];
for (const i in dct) {
  const val = dct[i];
  for (const j in dct) if (dct[j] === val) newList.push(j);
  newdict[val] = newList;
  newList = [];
}
console.log(newdict);
