# 안전 영역

import copy
import sys

sys.setrecursionlimit(100000)

def dfs(x, y, i):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if arr[x][y] >= i:
        arr[x][y] = 0
    
        dfs(x, y - 1, i)
        dfs(x, y + 1, i)
        dfs(x + 1, y, i)
        dfs(x - 1, y, i)
        return True
    return False

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


maxHeight = 0
for i in range(1, 101):
    arr = copy.deepcopy(graph)
    result = 0
    for x in range(n):
        for y in range(n):
            if dfs(x, y, i) == True:
                result += 1
    maxHeight = max(maxHeight, result)

print(maxHeight)