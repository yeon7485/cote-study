from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return True


T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(T):
    m, n, k = list(map(int, input().split()))
    graph = [[0 for _ in range(m)] for __ in range(n)]
    visited = [[False] * m for _ in range(n)]
    point = []
    result = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
        point.append((b, a))

    for p in point:
        a, b = p
        if not visited[a][b] and graph[a][b] == 1:
            bfs(a, b)
            result += 1

    print(result)
