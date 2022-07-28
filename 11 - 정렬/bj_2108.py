# 통계학

import sys
from statistics import *
from collections import Counter

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

print(int(round(sum(num) / n, 0)))
print(num[len(num) // 2])

if n == 1:
    print(num[0])
else:
    s = Counter(num).most_common()
    if s[0][1] == s[1][1]:
        print(s[1][0])
    else:
        print(s[0][0])

print(num[-1] - num[0])
