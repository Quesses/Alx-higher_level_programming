#!/usr/bin/node
const dict = require('./101-data').dict;
const dicKeys = Object.keys(dict);
const dicVals = Object.values(dict);
const result = {};
let match;
for (let i = 0; i < dicVals.length; i++) {
  result[JSON.stringify(dicVals[i])] = [];
  // filter dicKeys for if each key in dict[key] matches dicVals[i]
  match = dicKeys.filter(key => dict[key] === dicVals[i]);
  match.forEach(item => result[JSON.stringify(dicVals[i])].push(item));
}
console.log(result);
