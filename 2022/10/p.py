#!/usr/bin/env python
import sys

lines = [l.rstrip() for l in sys.stdin.read().strip().split('\n')]

X = [1,1]  # X[i>=0] = val during i-th cycle
for i, line in enumerate(lines):
    if line == 'noop':
        X.append(X[-1])
    else:
        val = int(line.split()[1])
        X.append(X[-1])
        X.append(X[-1] + val)

ans1 = 0
for i, x in enumerate(X):
    if i == 20 or (i >= 60 and i % 40 == 20):
        ans1 += i * X[i]
print(ans1)

i = 1
for y in range(6):
    s = ''
    for x in range(40):
        s += '#' if x-1 <= X[i] <= x+1 else '.'
        i += 1
    print(s)
# BPJAZGAP
