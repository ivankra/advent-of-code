#!/usr/bin/env python
import sys

walls = set()  # [(x,y)]
for line in sys.stdin.read().strip().split('\n'):
    p = [list(map(int, s.split(','))) for s in line.split(' -> ')]
    for i in range(1, len(p)):
        assert p[i-1][0] == p[i][0] or p[i-1][1] == p[i][1]
        a = list(p[i-1])
        b = list(p[i])
        while a != b:
            walls.add(tuple(a))
            if a[0] != b[0]:
                a[0] += 1 if a[0] < b[0] else -1
            else:
                a[1] += 1 if a[1] < b[1] else -1
        walls.add(tuple(b))

max_y = max(y for (x, y) in walls)
blocked = set(walls)
source = (500, 0)
assert source not in blocked
ans1 = 0

while True:
    x, y = source
    while y <= max_y:
        if (x, y+1) not in blocked:
            y += 1
        elif (x-1, y+1) not in blocked:
            x -= 1
            y += 1
        elif (x+1, y+1) not in blocked:
            x += 1
            y += 1
        else:
            blocked.add((x, y))
            ans1 += 1
            break

    if y > max_y:
        break

print(ans1)
