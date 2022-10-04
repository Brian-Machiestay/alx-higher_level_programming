#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) rev[j++] = list[i];
  return (rev);
};
