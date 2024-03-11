#!/usr/bin/node
let i;
const x = process.argv[2];
const isInt = parseInt(x);

if (isNaN(isInt)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
