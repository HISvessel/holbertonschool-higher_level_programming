#!/bin/node

/*This module is a followup to promises, to learn about its static metthods

Promise.all
Promise.allSettled
Promise.race
Promise.any*/

const promise1 = Promise.resolve('Hello, mum');
const promise2 = 10;
const promise3 = new Promise((resolve, reject) =>
setTimeout(resolve, 2000, 'Bye'));

Promise.all([promise1, promise2, promise3]).then(values => console.log(values))

