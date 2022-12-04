#!/usr/bin/env python
import sys

def priority(c):
    if 'a' <= c <= 'z': return ord(c) - ord('a') + 1
    if 'A' <= c <= 'Z': return ord(c) - ord('A') + 27
    raise Exception()


ans = 0
counts = {}
group_size = 0

for line in sys.stdin:
    line = line.strip()
    n = len(line)
    A, B = line[:n//2], line[n//2:]

    for x in set(line):
        counts[x] = counts.get(x, 0) + 1

    group_size += 1
    if group_size == 3:
        sh = [x for x in counts.keys() if counts[x] == 3]
        assert len(sh) == 1, counts
        ans += priority(sh[0])
        group_size = 0
        counts = {}

print(ans)
