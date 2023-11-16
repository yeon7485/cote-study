import sys

sys.setrecursionlimit(100000)


def dfs(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if not visited[x][y] and area[x][y] == color:
        visited[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            dfs(nx, ny, color)
        return True
    return False


n = int(input())
area = [list(input()) for _ in range(n)]
RGB = ['R', 'G', 'B']
RB = ['R', 'B']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rst1 = 0
rst2 = 0

for c in RGB:
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, c):
                rst1 += 1

for i, ar in enumerate(area):
    for j, a in enumerate(ar):
        if a == 'G':
            area[i][j] = 'R'

for c in RB:
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, c):
                rst2 += 1

print(rst1, rst2)
