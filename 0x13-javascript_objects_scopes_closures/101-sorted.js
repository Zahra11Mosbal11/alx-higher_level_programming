#!/usr/bin/node
const dict = require('./101-data.js').dict;
let d_new = {};
for (let key in dict) {
  if (d_new[dict[key]] === undefined) {
    d_new[dict[key]] = [key];
  } else {
    d_new[dict[key]].push(key);
  }
}
console.log(d_new);
