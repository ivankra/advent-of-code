#!/usr/bin/env python
import sys
text = sys.stdin.read()
sums = [sum(map(int, b.split())) for b in text.split('\n\n')]
sums.sort()
print(sums[0], sum(sums[-3:]))
