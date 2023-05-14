# 회사에 있는 사람

import sys

n = int(sys.stdin.readline())
enter = []

for _ in range(n):
    log = input().split()
    if log[1] == 'enter':
        enter.append(log[0])
    else:
        enter.remove(log[0])

enter.sort(reverse=1)
for e in enter:
    print(e)
