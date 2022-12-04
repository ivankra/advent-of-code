#!/usr/bin/env python
import sys
text = sys.stdin.read()
blocks = text.split('\n\n')
sums = [sum(map(int, b.split())) for b in text.split('\n\n')]
sums.sort()
print(sums[-1])
print(sum(sums[-3:]))
