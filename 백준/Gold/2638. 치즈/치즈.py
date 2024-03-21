from collections import deque

N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
result = 0


def bfs():
    queue.append((0, 0))
    melt = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if board[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                elif visited[nx][ny] and board[nx][ny] == 1:
                    melt.append((nx, ny))

    for a, b in melt:
        board[a][b] = 0
    return len(melt)


while True:
    visited = [[False] * M for _ in range(N)]
    cnt = bfs()
    if cnt == 0:
        print(result)
        break
    result += 1
