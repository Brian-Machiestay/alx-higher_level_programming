#!/usr/bin/node
require('node:process');
const argv = process.argv;
const len = argv.length;
if (len === 2) { console.log('No argument'); } else if (len === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
