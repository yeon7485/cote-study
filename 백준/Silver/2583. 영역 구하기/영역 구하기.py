from collections import deque

m, n, k = list(map(int, input().split()))
square = [list(map(int, input().split())) for _ in range(k)]
board = [[0] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for s in square:
    a, b, c, d = s
    for i in range(b, d):
        for j in range(a, c):
            board[i][j] = -1


def bfs(p, q):
    result = 1
    queue.append((p, q))
    board[p][q] = 1
    while queue:
        x, y = queue.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                    board[nx][ny] = 1
                    result += 1

    return result


width = []
cnt = 0
queue = deque()

for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            width.append(bfs(i, j))
            cnt += 1

width.sort()
print(cnt)
print(*width)
