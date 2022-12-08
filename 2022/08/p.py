#!/usr/bin/env python
import sys

A = sys.stdin.read().strip().split('\n')
n, m = len(A), len(A[0])

def visible(i, j):
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        h = []
        for k in range(0, max(n,m) + 1):
            if 0 <= i + dy*k < n and 0 <= j + dx*k < m:
                h.append(A[i+dy*k][j+dx*k])
        if len(h) == 1 or h[0] > max(h[1:]):
            return True
    return False


def scenic(i, j):
    res = 1
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        h0 = A[i][j]
        hh = []
        for k in range(1, max(n,m) + 1):
            if 0 <= i + dy*k < n and 0 <= j + dx*k < m:
                h = A[i+dy*k][j+dx*k]
                hh.append(h)
                if h >= h0:
                    break
        res *= len(hh)
    return res



ans1, ans2 = 0, 0
for i in range(n):
    for j in range(m):
        ans1 += visible(i, j)
        ans2 = max(ans2, scenic(i, j))

print(ans1, ans2)
