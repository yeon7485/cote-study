from collections import deque


def bfs(s):
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True
                parent[g] = v


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
for i in range(2, n+1):
    print(parent[i])
