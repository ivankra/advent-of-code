#!/usr/bin/env python
import sys, re

monkeys = []
for line in sys.stdin:
    line = line.rstrip()

    m = re.match('^Monkey ([0-9]+):', line)
    if m:
        assert len(monkeys) == int(m[1])
        cur = {'count': 0}
        monkeys.append(cur)

    m = re.match(' +Starting items: ([0-9 ,]+)', line)
    if m:
        cur['items'] = list(map(int, m[1].split(', ')))

    m = re.match(' +Operation: new = (.*)', line)
    if m:
        cur['op'] = m[1]

    m = re.match(' +Test: divisible by ([0-9]+)', line)
    if m:
        cur['test'] = int(m[1])

    m = re.match(' +If (true|false): throw to monkey ([0-9]+)', line)
    if m:
        cur[m[1]] = int(m[2])

for round in range(20):
    for i, m in enumerate(monkeys):
        m['count'] += len(m['items'])
        for x in m['items']:
            x = eval(m['op'], {'old': x}) // 3
            j = m['true'] if x % m['test'] == 0 else m['false']
            monkeys[j]['items'].append(x)
        m['items'].clear()

ccs = list(sorted([m['count'] for m in monkeys]))
ans1 = ccs[-1] * ccs[-2]
print(ans1)
