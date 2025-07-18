#!/usr/bin/node

const index = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(index)) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(index));
