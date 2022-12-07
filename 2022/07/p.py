#!/usr/bin/env python
import sys
from pathlib import Path

class Node:
    def __init__(self, parent, path):
        self.parent = parent
        self.path = path
        self.dirs = {}
        self.files = {}

    def subdir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Node(self, self.path / name)
        return self.dirs[name]

    def rec(self):
        self.total = sum(self.files.values())
        for d in self.dirs.values():
            yield from d.rec()
            self.total += d.total
        yield self


root = cur = Node(None, Path('/'))
for line in sys.stdin:
    tok = line.strip().split()
    if tok[0] == '$':
        if tok[1] == 'cd':
            if tok[2] == '/':
                cur = root
            elif tok[2] == '..':
                cur = cur.parent
            else:
                cur = cur.subdir(tok[2])
    elif tok[0] == 'dir':
        cur.subdir(tok[1])
    else:
        cur.files[tok[1]] = int(tok[0])

all_dirs = list(root.rec())
ans1 = sum(d.total for d in all_dirs if d.total <= 100000)
ans2 = root.total + 1
for d in all_dirs:
    f = 70000000 - root.total + d.total
    if f >= 30000000:
        ans2 = min(ans2, d.total)
print(ans1, ans2)
