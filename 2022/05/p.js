#!/usr/bin/env node
const fs = require('fs');

const text = fs.readFileSync(0).toString();

function parseDrawing(drawing) {
  const lines = drawing.split('\n');
  const n = lines[lines.length - 1].trim().split(/\s+/).length;
  let stacks = Array(n).fill().map(_ => []);
  for (let i = lines.length - 2; i >= 0; i--) {
    for (let j = 1, k = 0; j < lines[i].length; j += 4, k++) {
      if (lines[i][j] != ' ') {
        stacks[k].push(lines[i][j]);
      }
    }
  }
  return stacks;
}

function solve(part) {
  const [drawing, instr] = text.split('\n\n');
  let stacks = parseDrawing(drawing);
  for (const line of instr.split('\n')) {
    const m = line.match(/^move (\d+) from (\d) to (\d)$/);
    const k = parseInt(m[1]);
    const i = parseInt(m[2]) - 1;
    const j = parseInt(m[3]) - 1;
    if (part == 1) {
      for (let r = 0; r < k; r++) {
        stacks[j].push(stacks[i].pop());
      }
    } else {
      let els = stacks[i].splice(stacks[i].length - k);
      stacks[j] = stacks[j].concat(els);
    }
  }
  return stacks.map(s => s[s.length-1]).join('');
}

console.log(solve(1), solve(2));
