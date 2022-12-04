#!/usr/bin/env python
import sys

class Segment:
    def __init__(self, a, b):
        self.a = min(a, b)
        self.b = max(a, b)

    def contains(self, other):
        return self.a <= other.a <= self.b and self.a <= other.b <= self.b

    def overlaps(self, other):
        return (
            self.a <= other.a <= self.b or
            self.a <= other.b <= self.b or
            other.a <= self.a <= other.b or
            other.a <= self.b <= other.b
        )


ans = 0

for line in sys.stdin:
    p = [list(map(int, x.split('-'))) for x in line.strip().split(',')]
    s1 = Segment(p[0][0], p[0][1])
    s2 = Segment(p[1][0], p[1][1])
    if s1.overlaps(s2): ans += 1

print(ans)
