#!/usr/bin/env python3
import sys, re

cubes = set()
for line in sys.stdin:
    x,y,z = [int(s) for s in line.strip().split(',')]
    cubes.add((x,y,z))


def adjacent(a):
    for i in range(3):
        for d in [-1, 1]:
            b = list(a)
            b[i] += d
            yield tuple(b)


def is_external(pos):
    seen = set([pos])
    stk = [pos]
    minx = min(min(c) for c in cubes)
    maxx = max(max(c) for c in cubes)

    while len(stk) > 0:
        a = stk.pop()
        if min(a) < minx or max(a) > maxx:
            return True

        for b in adjacent(a):
            if b in cubes:
                continue
            if b not in seen:
                seen.add(b)
                stk.append(b)

    return False


ans1, ans2 = 0, 0

for a in cubes:
    for b in adjacent(a):
        if b not in cubes:
            ans1 += 1
            if is_external(b):
                ans2 += 1

print(ans1, ans2)
