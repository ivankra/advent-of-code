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

for line in sys.stdin:
    m = re.fullmatch('move ([0-9]+) from ([0-9]) to ([0-9])$', line.strip())
    assert m, line
    k = int(m[1])
    i = int(m[2])
    j = int(m[3])
    stacks[j-1] += stacks[i-1][-k:]
    stacks[i-1] = stacks[i-1][:-k]

print(''.join(s[-1] for s in stacks))
