# 수 정렬하기 2

import sys

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()
for i in num:
    print(i)