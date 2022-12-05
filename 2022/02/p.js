#!/usr/bin/env node
const fs = require('fs');

const text = fs.readFileSync(0).toString();

function beaten(a, b) {
  return b == a + 1 || (b == 1 && a == 3);
}

let ans1 = 0, ans2 = 0;

text.trim().split('\n').map(line => {
  const [as, bs] = line.split(' ');
  a = {'A': 1, 'B': 2, 'C': 3}[as];
  b1 = {'X': 1, 'Y': 2, 'Z': 3}[bs];
  for (const b of [1, 2, 3]) {
    let score = b, outcome = 'X';
    if (beaten(a, b)) {
      score += 6;
      outcome = 'Z';
    } else if (a == b) {
      score += 3;
      outcome = 'Y';
    }

    if (b == b1) {
      ans1 += score;
    }
    if (outcome == bs) {
      ans2 += score;
    }
  }
});

console.log(ans1, ans2);
