#!/usr/bin/env python
import sys, re

sensors = []
for line in sys.stdin:
    m = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line.strip())
    assert m, line
    sensors.append(((int(m[1]), int(m[2])), (int(m[3]), int(m[4]))))


def solve1(y):
    segs = []
    for s, b in sensors:
        d = abs(s[0] - b[0]) + abs(s[1] - b[1])
        # abs(x - s[0]) + abs(y - s[1]) <= d
        # abs(x - s[0]) <= d - abs(y - s[1])
        if d - abs(y - s[1]) < 0: continue
        d -= abs(y - s[1])
        segs.append((s[0] - d, s[0] + d))

    evs = {}
    for a, b in segs:
        evs.setdefault(a, []).append(1)
        evs.setdefault(b, []).append(-1)

    ans = 0
    x0, k0 = 0, 0
    for x1 in sorted(evs.keys()):
        k1 = k0 + sum(evs[x1])
        if k0 > 0:
            ans += x1 - x0
        x0, k0 = x1, k1

    return ans


print('y=10:', solve1(10))
print('y=2M:', solve1(2000000))
