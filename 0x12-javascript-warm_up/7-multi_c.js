#!/usr/bin/node

require('process');
const argv = process.argv;
if (!parseInt(argv[2])) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < parseInt(argv[2]); i++) console.log('C is fun');
}
