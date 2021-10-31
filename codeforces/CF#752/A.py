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
  ans = 0
  
  cur = 1
  for i in range(n):
    if a[i] > ans + i + 1:
      change = a[i] - (ans + i + 1)
      ans += change
  print(ans)

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
