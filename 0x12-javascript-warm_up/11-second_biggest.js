#!/usr/bin/node

let max = 0;
let lastMax = 0;
if (process.argv.length >= 3) {
  for (let index = 2; index < process.argv.length; index++) {
    const element = Number(process.argv[index]);
    if (element > max) {
      lastMax = max;
      max = element;
    }
    if (element > lastMax && element < max) {
      lastMax = element;
    }
  }
}
console.log(lastMax);
