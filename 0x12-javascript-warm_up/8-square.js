#!/usr/bin/node
let i;
let j;
const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing or invalid size');
} else {
  for (i = 0; i < parseInt(x); i++) {
    let row = '';
    for (j = 0; j < parseInt(x); j++) {
      row += 'X ';
    }
    console.log(row);
  }
}
