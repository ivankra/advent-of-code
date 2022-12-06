const fs = require('fs');

const text = fs.readFileSync(0).toString().trim();

function solve(m) {
  for (let k = m; k + m <= text.length; k++) {
    let a = Array.from(text.slice(k - m, k));
    a.sort();
    let good = true;
    for (let i = 1; i < m; i++) {
      good &= a[i-1] != a[i];
    }
    if (good) {
      return k;
    }
  }
}

console.log(solve(4), solve(14));
