#!/usr/bin/node
import { argv } from 'node:process';

const len = argv.length;
if (len <= 2) console.log('No argument');
else if (len === 3) console.log('Argument found');
else console.log('Arguments found');
