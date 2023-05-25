import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n = int(input())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

visited = [True] + [False] * n

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
count = 0

for v in visited:
    if v:
        count += 1
print(count-2)
