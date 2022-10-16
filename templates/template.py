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
def solve():
  start_here


def main():
  if not TESTS:
    solve()
    return

  t, = I()
  while t:
    solve()
    t -= 1

if __name__ == "__main__":
  main()
