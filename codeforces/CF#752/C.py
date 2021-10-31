import sys
INF = 10**20
MOD = 10**9 + 7
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
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

def removable(el, idx):
  if el % (idx + 2):
    return True
  return False

def solve():
  n, = I()
  a = I()
  lcm = 1
  iter = 2
  all = []
  while lcm < 10 ** 10:
    lcm = (lcm * iter) // gcd(lcm, iter)
    all.append(lcm)
    iter += 1

  if a[0] % 2 == 0:
    print('NO')
    return
  
  for i in range(1, min(len(all), n)):
    if a[i] % all[i] == 0:
      print('NO')
      return
  print('YES')

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

