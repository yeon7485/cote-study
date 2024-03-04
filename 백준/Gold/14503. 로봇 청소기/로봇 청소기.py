n, m = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]
result = 0


while True:

    if board[r][c] == 0:
        board[r][c] = 2
        result += 1

    if board[r+1][c] > 0 and board[r-1][c] > 0 and board[r][c+1] > 0 and board[r][c-1] > 0:
        r = r + dx[(d + 2) % 4]
        c = c + dy[(d + 2) % 4]
        if board[r][c] == 1:
            break

    elif board[r+1][c] == 0 or board[r-1][c] == 0 or board[r][c+1] == 0 or board[r][c-1] == 0:
        d = d - 1 if d > 0 else 3
        nx = r + dx[d]
        ny = c + dy[d]
        if board[nx][ny] == 0:
            r = nx
            c = ny

print(result)
