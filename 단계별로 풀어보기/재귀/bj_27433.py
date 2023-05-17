# 팩토리얼 2

import sys
sys.setrecursionlimit(2000)

def recur(x):
    if x == 0:
        return 1
    return x * recur(x-1)

n = int(input())
print(recur(n))