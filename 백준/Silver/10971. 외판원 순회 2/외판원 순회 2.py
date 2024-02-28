n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
minCost = 1e10

def dfs(next, cost):
    global n, graph, visited, minCost
    if cost < minCost:
        if all(visited) and next==0:
            minCost = min(minCost, cost)
        for i in range(n):
            if graph[next][i] > 0 and not visited[i]:
                visited[i] += 1
                dfs(i, cost + graph[next][i])
                visited[i] -= 1

dfs(0, 0)
print(minCost)