import sys
INF = 10**20
MOD = 10**9 + 7
from math import gcd
from math import ceil, log2, factorial
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br

def fastio():
  import sys
  from io import StringIO 
  from atexit import register
  global input
  sys.stdin = StringIO(sys.stdin.read())
  input = lambda : sys.stdin.readline().rstrip('\r\n')
  sys.stdout = StringIO()
  register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
fastio()

I = lambda:list(map(int,input().split()))
TESTS = 1 
"""
Facts and Data representation
Constructive? Top bottom up down
"""

maps = {}
for i in range(10):
  first = str(i)
  second = str((i + 1) % 10)
  third = str((i + 2) % 10)
  maps[first + second] = third

def can(x):
  return x in maps

def solve(case):
  n, = I()
  s = list(input())

  stack = []
  i = 0
  while i < len(s):
    stack.append(s[i])
    was = False
    while len(stack) > 1:
      ab = stack[-2] + stack[-1]
      if can(ab):
        print(stack)
        was = True
        ok = maps[ab]
        stack.pop()
        stack.pop()
        stack.append(ok)
      else:
        break

    print("H", stack)

    if was and i + 2 < n:
      if can(s[i + 1] + s[i + 2]):
        i += 1
        stack.append(s[i])
    i += 1
  
  print('Case #' + str(case) + ': ' + ''.join(stack))
  


def main():
  if not TESTS:
    solve()
    return

  t, = I()
  for i in range(t):
    solve(i + 1)
    t -= 1

if __name__ == "__main__":
  main()
