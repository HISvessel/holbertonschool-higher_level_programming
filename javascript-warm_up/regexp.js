#!/bin/node

/* this script contains the basics of regular expressions*/ 

/* this creates regular expressions */ 
const re = /ab+c/;

const newRE = new RegExp("abc");

/* */

const planeString = "the latest plane designs evolved from slabcraft."

console.log(newRE.test(planeString)); /* test the planestring pattern against the regexp*/