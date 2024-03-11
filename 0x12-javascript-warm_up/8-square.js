#!/usr/bin/node
let i;
let j;
const x = process.argv[2];
const isInt = parseInt(x);

if (isNaN(isInt)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    let row = '';
    for (j = 0; j < x; j++) {
      row += 'X ';
    }
    console.log(row);
  }
}
