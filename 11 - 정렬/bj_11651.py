# 좌표 정렬하기 2

import sys
n = int(sys.stdin.readline())
xy = []

for _ in range(n):
    i = list(map(int, sys.stdin.readline().split()))
    i[0], i[1] = i[1], i[0]
    xy.append(i)

xy.sort()
for i in xy:
    print(f'{i[1]} {i[0]}')

