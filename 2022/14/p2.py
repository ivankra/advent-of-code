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
ans2 = 0

for x in range(-10000, 10000):
    blocked.add((x, max_y+2))

while source not in blocked:
    x, y = source
    while True:
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
            ans2 += 1
            break

print(ans2)
