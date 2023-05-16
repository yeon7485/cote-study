def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    if e not in graph[s]:
        graph[s].append(e)
    if s not in graph[e]:
        graph[e].append(s)

for g in graph:
    g.sort()

dfs(graph, start, visited)