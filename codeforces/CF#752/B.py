import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil, log2, factorial
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br
 
TESTS = 1 
"""
Facts and Data representation
Constructive? Top bottom up down
"""
def solve():
  n, = I()
  a = I()
  if n % 2 == 0:
    print('YES')
    return

  for i in range(1, n):
    if a[i - 1] >= a[i]:
      print('YES')
      return
  print('NO')

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
