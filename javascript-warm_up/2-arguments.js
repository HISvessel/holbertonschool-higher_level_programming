#!/usr/bin/node
// arggument vectors are retrieved from the console's process
const argument = process.argv.length - 2;

// conditionals inside of parenthesis that go before function brackets
if (argument === 0) {
  console.log('No argument');
} else if (argument === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
