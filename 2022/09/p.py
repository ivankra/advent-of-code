#!/usr/bin/env python
import sys

DIRS = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

class State:
    def __init__(self, k):
        self.pos = [[0, 0] for _ in range(k)]  # head to tail
        self.visited = set([tuple(self.pos[-1])])

    def move(self, d):
        d = DIRS[d]
        self.pos[0][0] += d[0]
        self.pos[0][1] += d[1]

        for i in range(1, len(self.pos)):
            H = self.pos[i-1]
            T = self.pos[i]
            d = (H[0] - T[0], H[1] - T[1])
            if abs(d[0]) == 2 and d[1] == 0:
                T[0] += d[0] // 2
            elif abs(d[1]) == 2 and d[0] == 0:
                T[1] += d[1] // 2
            elif d[0] != 0 and d[1] != 0 and abs(d[0]) + abs(d[1]) >= 3:
                T[0] += 1 if d[0] > 0 else -1
                T[1] += 1 if d[1] > 0 else -1

        self.visited.add(tuple(self.pos[-1]))


s2 = State(2)
s10 = State(10)

for line in sys.stdin:
    d, r = line.split()
    for _ in range(int(r)):
        s2.move(d)
        s10.move(d)

print(len(s2.visited), len(s10.visited))
