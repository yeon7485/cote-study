import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if not visited[x][y] and ground[x][y] == 1:
        visited[x][y] = True
        for p in range(4):
            nx = x + dx[p]
            ny = y + dy[p]
            dfs(nx, ny)
        return True
    return False


TC = int(input())

for t in range(TC):
    m, n, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        a, b = map(int, input().split())
        ground[b][a] = 1

    result = 0

    for i in range(m):
        for j in range(n):
            if dfs(j, i):
                result += 1
    print(result)
