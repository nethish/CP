#!/bin/python3

from itertools import permutations
from math import factorial

N = 8
for i in range(1, N + 1):
  a = [j for j in range(i)]
  al = permutations(a)
  
  ans = 0

  for a in al:
    b = a + a[::-1]
    for j in range(len(b)):
      for k in range(j):
        ans += b[k] > b[j]

  f = factorial(i)
  s = i * i
  print(ans, i, s, f, ans // i, ans // s, ans // f)
