import sys


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[False] * M for _ in range(N)]
max_sum = 0


def dfs(x, y, cnt, s):
    global max_sum
    if cnt == 3:
        max_sum = max(max_sum, s)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, cnt + 1, s + board[nx][ny])
                visited[nx][ny] = False


def cal_o(x, y, s):
    global max_sum
    if (x == 0 and y == 0) or (x == 0 and y == M - 1) or (x == N - 1 and y == 0) or (x == N - 1 and y == M - 1):
        return
    if x == 0 and y < M - 1:
        c = s + board[x][y - 1] + board[x][y + 1] + board[x + 1][y]  # ㅜ
        max_sum = max(max_sum, c)
    elif x == N - 1 and y < M - 1:
        d = s + board[x][y - 1] + board[x][y + 1] + board[x - 1][y]  # ㅗ
        max_sum = max(max_sum, d)
    elif y == 0 and x < N - 1:
        b = s + board[x - 1][y] + board[x + 1][y] + board[x][y + 1]  # ㅏ
        max_sum = max(max_sum, b)
    elif y == M - 1 and x < N - 1:
        a = s + board[x - 1][y] + board[x + 1][y] + board[x][y - 1]  # ㅓ
        max_sum = max(max_sum, a)
    else:
        a = s + board[x - 1][y] + board[x + 1][y] + board[x][y - 1]  # ㅓ
        b = s + board[x - 1][y] + board[x + 1][y] + board[x][y + 1]  # ㅏ
        c = s + board[x][y - 1] + board[x][y + 1] + board[x + 1][y]  # ㅜ
        d = s + board[x][y - 1] + board[x][y + 1] + board[x - 1][y]  # ㅗ
        max_sum = max(max_sum, a, b, c, d)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, board[i][j])
        visited[i][j] = False
        cal_o(i, j, board[i][j])

print(max_sum)
