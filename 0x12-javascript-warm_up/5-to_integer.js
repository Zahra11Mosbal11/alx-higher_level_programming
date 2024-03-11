#!/usr/bin/node
const arg = process.argv[2];
const isInt = parseInt(arg);
if (isNaN(isInt)) {
  console.log('Not a number');
} else {
  console.log('My number:', isInt);
}
