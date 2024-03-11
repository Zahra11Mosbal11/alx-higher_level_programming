#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const integers = process.argv.slice(2).map(arg => parseInt(arg)).filter(num => !isNaN(num));
  integers.sort((a, b) => b - a);
  if (integers.length < 2) {
    console.log(0);
  } else {
    console.log(integers[1]);
  }
}
