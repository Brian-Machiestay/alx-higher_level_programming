#!/usr/bin/node

const list = require('./100-data.js');
console.log(list.list);
let i = 0;
const newList = list.list.map(x => x * i++);
console.log(newList);
