#!/usr/bin/env node
const fs = require('fs');

const text = fs.readFileSync('input.txt').toString();

let sums = text.split('\n\n').map(block => {
  let nums = block.trim().split('\n').map(x => parseInt(x));
  return nums.reduce((acc, val) => acc + val, 0);
});

sums = new Int32Array(sums).sort().reverse();
console.log(sums[0]);
console.log(sums.slice(0, 3).reduce((a, x) => a + x));
