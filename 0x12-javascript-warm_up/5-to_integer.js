#!/usr/bin/node

require('process');
const argv = process.argv;
if (!parseInt(argv[2])) console.log('Not a number');
else console.log('My number: ' + parseInt(argv[2]));
