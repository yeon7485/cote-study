import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

visited = [True] + [False] * n

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

result = 1
i = 1
while True:
    dfs(graph, i, visited)
    if False not in visited:
        break
    result += 1
    i = visited.index(False)

print(result)