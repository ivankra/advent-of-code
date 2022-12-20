#!/usr/bin/env pypy3
import sys

data = [int(s) for s in sys.stdin.read().split()]

def solve1():
    A = [(i, x) for (i, x) in enumerate(data)]
    N = len(A)

    for k in range(N):
        i = [j for j in range(N) if A[j][0] == k][0]
        x = A[i]
        A = A[:i] + A[(i+1):]
        j = (i + x[1]) % (N - 1)
        A = A[:j] + [x] + A[j:]

    i = [j for j in range(N) if A[j][1] == 0][0]
    return A[(i+1000)%N][1] + A[(i+2000)%N][1] + A[(i+3000)%N][1]

def solve2():
    A = [(i, x*811589153) for (i, x) in enumerate(data)]
    N = len(A)

    for rep in range(10):
        for k in range(N):
            i = [j for j in range(N) if A[j][0] == k][0]
            x = A[i]
            A = A[:i] + A[(i+1):]
            j = (i + x[1]) % (N - 1)
            A = A[:j] + [x] + A[j:]

    i = [j for j in range(N) if A[j][1] == 0][0]
    return A[(i+1000)%N][1] + A[(i+2000)%N][1] + A[(i+3000)%N][1]

print(solve1(), solve2())
