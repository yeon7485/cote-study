# 좌표 정렬하기

import sys
n = int(sys.stdin.readline())
xy = []

for _ in range(n):
    i = list(map(int, sys.stdin.readline().split()))
    xy.append(i)

xy.sort()
for i in xy:
    print(*i)


