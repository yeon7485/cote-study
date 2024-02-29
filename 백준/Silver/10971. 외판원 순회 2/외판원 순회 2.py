n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
route = []
minCost = 1e10


def dfs(count):
    global minCost
    if count == n:
        cost = 0
        for j in range(n-1):
            cost += graph[route[j]][route[j + 1]]
        if graph[route[n-1]][route[0]] != 0:
            cost += graph[route[n-1]][route[0]]
            minCost = min(cost, minCost)
        return

    for i in range(n):
        if count == 0 or (not visited[i] and graph[route[-1]][i] != 0) :
            route.append(i)
            visited[i] = True
            dfs(count + 1)
            route.pop()
            visited[i] = False


dfs(0)
print(minCost)