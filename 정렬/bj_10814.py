# 나이순 정렬

import sys

n = int(sys.stdin.readline())
member = []

for _ in range(n):
    m = sys.stdin.readline().split()
    m[0] = int(m[0])
    member.append(m)

member.sort(key = lambda x: x[0])

for m in member:
    print(f'{m[0]} {m[1]}')
