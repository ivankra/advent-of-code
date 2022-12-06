#!/usr/bin/env python
import sys

def priority(c):
    if 'a' <= c <= 'z': return ord(c) - ord('a') + 1
    if 'A' <= c <= 'Z': return ord(c) - ord('A') + 27
    raise Exception()


def solve1(lines):
    ans = 0
    for line in lines:
        n = len(line)
        A = set(line[:n//2])
        B = set(line[n//2:])
        C = A & B
        assert len(C) == 1
        ans += priority(list(C)[0])
    return ans


def solve2(lines):
    ans = 0
    counts = {}
    for i, line in enumerate(lines):
        for x in set(line):
            counts[x] = counts.get(x, 0) + 1
        if i % 3 == 2:
            sh = [x for x in counts.keys() if counts[x] == 3]
            assert len(sh) == 1, counts
            ans += priority(sh[0])
            counts = {}
    return ans


lines = [s.strip() for s in sys.stdin]
print(solve1(lines), solve2(lines))
