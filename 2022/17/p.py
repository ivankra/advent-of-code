#!/usr/bin/env python3
import sys

moves = sys.stdin.read().strip()

shapes = '''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''
shapes = [s.split('\n') for s in shapes.strip().split('\n\n')]

class Sim:
  def __init__(self):
    self.blocked = set()
    self.max_y = 0
    self.move_i = 0

  def good(self, shape, y0, x0):
    for i, row in enumerate(shape):
      for j, ch in enumerate(row):
        if ch == '#':
          if (y0-i, x0+j) in self.blocked or y0-i == 0 or not (0 <= x0+j < 7):
            return False
    return True

  def simulate(self, shape):
    y0 = self.max_y + len(shape) + 3
    x0 = 2
    assert self.good(shape, y0, x0)

    while True:
      ch = moves[self.move_i % len(moves)]
      self.move_i = (self.move_i + 1) % len(moves)

      if ch == '<' and self.good(shape, y0, x0-1):
        x0 -= 1
      elif ch == '>' and self.good(shape, y0, x0+1):
        x0 += 1

      if self.good(shape, y0-1, x0):
        y0 -= 1
      else:
        break

    assert self.good(shape, y0, x0)
    for i, row in enumerate(shape):
      for j, ch in enumerate(row):
        if ch == '#':
          self.blocked.add((y0-i, x0+j))
          self.max_y = max(self.max_y, y0-i)

    return (y0, x0)

def solve1():
  sim = Sim()
  for r in range(2022):
    sim.simulate(shapes[r % len(shapes)])
  return sim.max_y

def solve2():
  sim = Sim()
  tape_idx = {}
  tape = []
  prev_y0 = -100000000

  for r in range(100000000):
    prev_my = sim.max_y
    (y0, x0) = sim.simulate(shapes[r % len(shapes)])

    state = [
      y0 - prev_y0,
      x0,
      sim.max_y - prev_my,
      r % len(shapes),
      sim.move_i % len(moves),
    ]
    prev_y0 = y0

    M = 1000
    if len(tape) < M:
      state += [r]
    else:
      idx = [-i for i in range(1, M)]
      state += [tape[-i][0] for i in idx]
      state += [tape[-i][1] for i in idx]
    state = tuple(state)
  
    if state in tape_idx:
      period_st = tape_idx[state]
      period_len = len(tape) - tape_idx[state]
      break
    else:
      tape_idx[state] = len(tape)
      tape.append(state)

  print('period start=%d len=%d' % (period_st, period_len))

  L = 1000000000000
  ans2 = sum(tape[i][2] for i in range(period_st))
  L -= period_st
  tape = tape[period_st:]; assert len(tape) == period_len
  ans2 += sum(tape[i][2] for i in range(len(tape))) * (L // period_len)
  L %= period_len
  ans2 += sum(tape[i][2] for i in range(L))
  return ans2

print(solve1(), solve2())
