#!/usr/bin/env python
import sys

lines = [l.rstrip() for l in sys.stdin.read().strip().split('\n')]

def H(r, c):
    if r < 0 or r >= len(lines) or c < 0 or c >= len(lines[r]): return 999
    ch = lines[r][c]
    if ch == 'S': ch = 'a'
    if ch == 'E': ch = 'z'
    return ord(ch) - ord('a') + 1


dist = {}
Q = []

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == 'S':
            dist[(r, c)] = 0
            Q.append((r, c))

ans1 = -1
i = 0
while i < len(Q):
    r, c = Q[i]
    i += 1

    if lines[r][c] == 'E':
        ans1 = dist[(r, c)]

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dy, c + dx
        if H(rr, cc) <= H(r, c) + 1 and (rr, cc) not in dist:
            dist[(rr, cc)] = dist[(r, c)] + 1
            Q.append((rr, cc))


print(ans1)
