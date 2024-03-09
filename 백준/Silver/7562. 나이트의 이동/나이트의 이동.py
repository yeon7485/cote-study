from collections import deque

T = int(input())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1


for _ in range(T):
    N = int(input())
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    queue = deque()
    queue.append((a, b))
    board = [[0] * N for __ in range(N)]
    board[a][b] = 1
    bfs()
    print(board[c][d] - 1)
