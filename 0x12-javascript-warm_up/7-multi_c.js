#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < Number(process.argv[2]); x++) {
    console.log('C is fun');
  }
}
