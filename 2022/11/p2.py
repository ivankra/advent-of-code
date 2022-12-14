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

mods = [m['test'] for m in monkeys]
for m in monkeys:
    m['items'] = [{mod: x % mod for mod in mods} for x in m['items']]

for round in range(10000):
    for i, m in enumerate(monkeys):
        m['count'] += len(m['items'])
        for x in m['items']:
            y = {
                mod: eval(m['op'], {'old': val}) % mod
                for mod, val in x.items()
            }
            j = m['true'] if y[m['test']] == 0 else m['false']
            monkeys[j]['items'].append(y)
        m['items'].clear()

ccs = list(sorted([m['count'] for m in monkeys]))
ans2 = ccs[-1] * ccs[-2]
print(ans2)
