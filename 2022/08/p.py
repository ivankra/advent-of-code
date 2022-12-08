#!/usr/bin/env python
import sys

A = sys.stdin.read().strip().split('\n')
n, m = len(A), len(A[0])


def score(i, j):
    edge = False
    scenic = 1

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        vis = 0

        for k in range(1, max(n, m) + 10):
            if not (0 <= i + dy*k < n and 0 <= j + dx*k < m):
                edge = True
                break

            vis += 1
            if A[i+dy*k][j+dx*k] >= A[i][j]:
                break

        scenic *= vis

    return edge, scenic


ans1, ans2 = 0, 0
for i in range(n):
    for j in range(m):
        edge_visible, scenic = score(i, j)
        ans1 += edge_visible
        ans2 = max(ans2, scenic)

print(ans1, ans2)
