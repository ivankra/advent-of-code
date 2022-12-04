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
    a, bo = line.split()

    #         R       P       S
    a = {'A': 1, 'B': 2, 'C': 3}[a]

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
            score += 0
        if outcome == bo:
            break

    total_score += score

print(total_score)
