# 반복수열

import math

def dfs(x):
    if x in arr:
        print(arr.index(x))
        return False
    arr.append(x)
    n = 0
    nums = list(map(int, str(x)))
    for num in nums:
        n += int(math.pow(num, p))
    dfs(n)


a, p = map(int, input().split())
arr = []
dfs(a)