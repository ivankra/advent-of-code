#!/usr/bin/env python
import sys
import re

drawing = []
for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    else:
        drawing.append(line)

N = int(drawing.pop().split()[-1])
stacks = []
for i in range(N):
    stacks.append([])
    for line in drawing:
        j = 1+i*4
        if j < len(line) and line[j] != ' ':
            stacks[i].append(line[j])
    stacks[i] = list(reversed(stacks[i]))

stacks1 = [list(s) for s in stacks]
stacks2 = [list(s) for s in stacks]

for line in sys.stdin:
    m = re.fullmatch('move ([0-9]+) from ([0-9]) to ([0-9])$', line.strip())
    assert m, line
    k = int(m[1])
    i = int(m[2])
    j = int(m[3])

    for _ in range(k):
        stacks1[j-1].append(stacks1[i-1].pop())

    stacks2[j-1] += stacks2[i-1][-k:]
    stacks2[i-1] = stacks2[i-1][:-k]

ans1 = ''.join(s[-1] for s in stacks1)
ans2 = ''.join(s[-1] for s in stacks2)
print(ans1, ans2)
