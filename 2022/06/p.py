#!/usr/bin/env python
import sys

text = sys.stdin.read().strip()

def solve(m):
    for k in range(m, len(text)+1):
        suf = text[:k][-m:]
        if len(set(suf)) == m:
            return k

print(solve(4), solve(14))
