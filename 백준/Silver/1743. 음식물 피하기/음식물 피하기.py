import sys
sys.setrecursionlimit(100000)

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1


def dfs(x, y):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                count += 1
                dfs(nx, ny)


result = 0

for a in range(N):
    for b in range(M):
        if board[a][b] == 1 and not visited[a][b]:
            count = 0
            dfs(a, b)
            result = max(result, count)

print(result)
