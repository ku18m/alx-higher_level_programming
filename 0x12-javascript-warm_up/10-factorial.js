#!/usr/bin/node

function factorial (a) {
  if (a > 1) {
    a *= factorial(a - 1);
  }
  return a;
}

if (isNaN(Number(process.argv[2])) || Number(process.argv[2]) < 0) {
  console.log(1);
} else {
  console.log(factorial(Number(process.argv[2])));
}
