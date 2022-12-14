#!/usr/bin/env python
import sys, functools

def compare(a, b):
    if type(a) != type(b):
        if type(a) is not list: a = [a]
        if type(b) is not list: b = [b]
        assert type(a) == type(b)

    if type(a) is list:
        i = 0
        while i < max(len(a), len(b)):
            if len(a) != len(b):
                if i >= len(a):
                    return 1  # right
                if i >= len(b):
                    return -1  # wr
            res = compare(a[i], b[i])
            if res != 0:
                return res
            i += 1
    elif a < b:
        return 1
    elif a > b:
        return -1
    return 0


packets = []

ans1 = 0
for i, block in enumerate(sys.stdin.read().strip().split('\n\n')):
    a, b = block.split('\n')
    a, b = eval(a), eval(b)
    packets += [a, b]
    r = compare(a, b)
    assert r in (1, -1)
    if r == 1:
        ans1 += i+1

packets += [ [[2]], [[6]] ]
packets.sort(key=functools.cmp_to_key(compare))
packets.reverse()

ans2 = 1
for i, x in enumerate(packets):
    if x == [[2]]: ans2 *= i+1
    if x == [[6]]: ans2 *= i+1

print(ans1, ans2)
