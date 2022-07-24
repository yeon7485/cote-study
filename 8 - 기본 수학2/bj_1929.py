# 소수 구하기

import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n + 1):
    check = True
    if i != 1:
        for j in range(2, int(i**(1/2)) + 1):
            if i % j == 0:
                check = False
                break
        if(check):
            print(i)
        