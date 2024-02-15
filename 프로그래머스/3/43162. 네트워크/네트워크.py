import sys

sys.setrecursionlimit(10000)

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)
            answer += 1
            
    return answer


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

