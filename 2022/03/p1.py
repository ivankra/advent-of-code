#!/usr/bin/env python
import sys

def priority(c):
    if 'a' <= c <= 'z': return ord(c) - ord('a') + 1
    if 'A' <= c <= 'Z': return ord(c) - ord('A') + 27
    raise Exception()


ans = 0

for line in sys.stdin:
    line = line.strip()
    n = len(line)
    A, B = line[:n//2], line[n//2:]

    As = set(A)
    Bs = set(B)
    Cs = As & Bs
    assert len(Cs) == 1
    for c in Cs:
        ans += priority(c)

print(ans)
