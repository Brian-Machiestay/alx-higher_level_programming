#!/usr/bin/node

require('process');
function factorial (num) {
  if (num === 0) return (1);
  return (num * factorial(num - 1));
}
const argv = parseInt(process.argv[2]);
if (!argv) console.log(1);
else console.log(factorial(argv));
