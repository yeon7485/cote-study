from collections import deque


def bfs(x, y):
    size = 1
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
            if draw[nx][ny] == 0 or visited[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
            size += 1
    return size


n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
draw = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1 and not visited[i][j]:
            result += 1
            max_size = max(max_size, bfs(i, j))

print(result)
print(max_size)
