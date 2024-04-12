N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]


def func(n, x, y):
    half = n // 2
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != board[x][y]:
                func(half, x, y)
                func(half, x, y + half)
                func(half, x + half, y)
                func(half, x + half, y + half)
                return

    ans[board[x][y]] += 1


func(N, 0, 0)
for a in ans:
    print(a)
