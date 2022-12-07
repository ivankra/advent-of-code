#!/usr/bin/env node
const fs = require('fs');
const input = fs.readFileSync(0).toString();

class Node {
    constructor(parent = null) {
        this.parent = parent;
        this.dirs = {};
        this.files = {};
    }

    cd(name) {
        if (this.dirs[name] === undefined) {
            this.dirs[name] = new Node(this);
        }
        return this.dirs[name];
    }

    *visit() {
        this.total = Object.values(this.files).reduce((a,b) => a+b, 0);
        for (const dir of Object.values(this.dirs)) {
            yield* dir.visit();
            this.total += dir.total;
        }
        yield this;
    }
};

const root = new Node();
let cur = root;
for (let line of input.trim().split('\n')) {
    let tok = line.split(' ');
    if (tok[0] == '$') {
        if (tok[1] == 'cd') {
            if (tok[2] == '/') {
                cur = root;
            } else if (tok[2] == '..') {
                cur = cur.parent;
            } else {
                cur = cur.cd(tok[2]);
            }
        }
    } else if (tok[0] == 'dir') {
        cur.cd(tok[1]);
    } else {
        cur.files[tok[1]] = parseInt(tok[0]);
    }
}

const dirs = [...root.visit()];
let ans1 = 0, ans2 = 10**100;
for (const dir of dirs) {
    if (dir.total <= 100000) {
        ans1 += dir.total;
    }
    let f = 70000000 - root.total + dir.total;
    if (f >= 30000000) {
        ans2 = Math.min(ans2, dir.total);
    }
}
console.log(ans1, ans2);
