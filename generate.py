#!/bin/python
from random import random
from random import randint as r

# =========
MAX = 100000
# M = r(10000, MAX - 100)
# print(MAX, M)
# a = []
# s = set()
#
# A, B = 0, 10**9
#
# for i in range(MAX):
#   ok = r(A, B)
#   while ok in s:
#     ok = r(A, B)
#   a.append(ok)
#   s.add(ok)
#
# print(*a)

print(MAX, MAX // 2)
print(*range(0, MAX, 2))
