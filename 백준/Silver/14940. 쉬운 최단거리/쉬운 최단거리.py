# 쉬운 최단거리
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True


for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            queue.append((i, j))
            board[i][j] = 0
            visited[i][j] = True
            break

bfs()
for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 1:
            board[i][j] = -1

for col in range(N):
    print(*board[col])