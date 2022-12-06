#!/usr/bin/env python
import sys
import re

text = sys.stdin.read().strip()
ans1 = None

for k in range(4, len(text)+1):
    suf = text[:k][-4:]

    if len(set(suf)) == 4:
        ans1 = k
        break

print(ans1)
