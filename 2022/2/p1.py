#!/usr/bin/env python3
import sys

total_score = 0

def beaten(a, b):  # a is beaten by b?
    if a in (1, 2, 3): a = 'RPS'[a-1]
    if b in (1, 2, 3): b = 'RPS'[b-1]
    if a == 'R' and b == 'P': return True
    if a == 'S' and b == 'R': return True
    if a == 'P' and b == 'S': return True
    return False


for line in sys.stdin:
    a, b = line.split()

    #         R       P       S
    a = {'A': 1, 'B': 2, 'C': 3}[a]
    b = {'X': 1, 'Y': 2, 'Z': 3}[b]

    score = b
    if beaten(a, b):
        score += 6
    elif a == b:
        score += 3
    else:
        assert beaten(b, a)
        score += 0

    total_score += score

print(total_score)
