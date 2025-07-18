#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log("Missing size");
};

for (let vertical = 0; vertical < size; vertical++) {
  console.log('X'.repeat(size));
}
