#!/usr/bin/env python
import sys, re, collections

sensors = []
for line in sys.stdin:
    m = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line.strip())
    assert m, line
    sensors.append(((int(m[1]), int(m[2])), (int(m[3]), int(m[4]))))


def solve2(mx):
    ans = 0
    for y in range(mx):
        evs = collections.defaultdict(lambda: 0)
        evs[0] = 0
        evs[mx] = 0
        for s, b in sensors:
            d = abs(s[0] - b[0]) + abs(s[1] - b[1]) - abs(y - s[1])
            if d >= 0:
                evs[s[0]-d] += 1
                evs[s[0]+d+1] -= 1

        x0, k0 = -1000000, 0
        for x1 in sorted(evs.keys()):
            k1 = k0 + evs[x1]
            if k0 == 0 and 0 <= x0 < mx:
                return x0*4000000+y
            x0, k0 = x1, k1


print('mx=20:', solve2(20))
print('mx=4M:', solve2(4000000))
