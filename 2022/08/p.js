#!/usr/bin/env node
const fs = require('fs');
const A = fs.readFileSync(0).toString().trim().split('\n');

function score(i, j) {
  let res = { edge: 0, scenic: 1 };
  for (let [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
    let vis = 0;
    for (let k = 1;; k++) {
      let h;
      try { h = A[i+dy*k][j+dx*k]; } catch (e) {}
      if (h === undefined) {
        res.edge = 1;
        break;
      }
      vis += 1;
      if (h >= A[i][j]) {
        break;
      }
    }
    res.scenic *= vis;
  }
  return res;
}

let ans1 = 0, ans2 = 0;
for (let i = 0; i < A.length; i++) {
  for (let j = 0; j < A[i].length; j++) {
    let sc = score(i, j);
    ans1 += sc.edge;
    ans2 = Math.max(ans2, sc.scenic);
  }
}
console.log(ans1, ans2);
