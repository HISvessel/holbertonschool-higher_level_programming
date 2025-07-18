#!/usr/bin/node

const count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing number of ocurrences');
}

for (let lines = 0; lines < count; lines++) {
  console.log('C is fun');
}
