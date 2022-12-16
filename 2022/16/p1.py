#!/usr/bin/env python
import sys, re, collections

Vflow = {}
Vadj = {}
Vid = {}

for line in sys.stdin:
    m = re.match(r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)', line.strip())
    assert m, line
    Vflow[m.group(1)] = int(m.group(2))
    Vadj[m.group(1)] = m.group(3).split(', ')

V = list(sorted(Vflow.keys()))
for i, v in enumerate(V):
    Vid[v] = i
N = len(Vflow)
assert Vid['AA'] == 0
Vadj = {Vid[x]: [Vid[y] for y in Vadj[x]] for x in Vadj}
Vflow = [Vflow[x] for x in V]

states = {(0, 0): 0}  # (pos, open) => ans
t = 0
ans1 = 0

while t < 30:
    print('t=%d st=%d' % (t, len(states)))
    next = collections.defaultdict(lambda: 0)

    for (pos, open), su in states.items():
        st1 = (pos, open)
        next[st1] = max(next[st1], su)

        if (open & (1 << pos)) == 0 and Vflow[pos] > 0:
            st1 = (pos, open | (1 << pos))
            su1 = su + (30 - (t+1)) * Vflow[pos]
            next[st1] = max(next[st1], su1)
            ans1 = max(ans1, su1)

        for pos1 in Vadj[pos]:
            st1 = (pos1, open)
            next[st1] = max(next[st1], su)

    states = next
    t += 1

print(ans1)
