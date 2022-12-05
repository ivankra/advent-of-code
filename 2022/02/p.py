#!/usr/bin/env python3
import sys

def beaten(a, b):  # a is beaten by b?
    return b == a + 1 or (b == 1 and a == 3)


ans1, ans2 = 0, 0

for line in sys.stdin:
    line = line.split()
    a = {'A': 1, 'B': 2, 'C': 3}[line[0]]
    b_part1 = {'X': 1, 'Y': 2, 'Z': 3}[line[1]]

    for b in 1, 2, 3:
        score = b
        if beaten(a, b):
            outcome = 'Z'
            score += 6
        elif a == b:
            outcome = 'Y'
            score += 3
        else:
            outcome = 'X'
            assert beaten(b, a)

        if b == b_part1:
            ans1 += score
        if outcome == line[1]:
            ans2 += score

print(ans1, ans2)
