from collections import deque

N = int(input())
area = [list(input()) for _ in range(N)]
queue = deque()
visited_col = [[False] * N for _ in range(N)]
visited_row = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

b, e = [], []

for i in range(N):
    for j in range(N):
        if area[i][j] == 'B':
            b.append((i, j))
        elif area[i][j] == 'E':
            e.append((i, j))

bx, by = b[1][0], b[1][1]
ex, ey = e[1][0], e[1][1]

if b[0][0] == bx:
    queue.append((bx, by, 0, 0))
    visited_row[bx][by] = True
else:
    queue.append((bx, by, 1, 0))
    visited_col[bx][by] = True


def bfs(ex, ey, ec):
    while queue:
        x, y, c, ct = queue.popleft()
        if x == ex and y == ey and c == ec:
            print(ct)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if ((nx == 0 and ny == 0) or (nx == 0 and ny == N - 1)
                    or (nx == N - 1 and ny == 0) or (nx == N - 1 and ny == N - 1)):
                continue
            if area[nx][ny] == '1':
                continue

            if c and 0 < nx < N - 1 and not visited_col[nx][ny]:
                if area[nx - 1][ny] != '1' and area[nx + 1][ny] != '1':
                    queue.append((nx, ny, 1, ct+1))
                    visited_col[nx][ny] = True
            if not c and 0 < ny < N - 1 and not visited_row[nx][ny]:
                if area[nx][ny - 1] != '1' and area[nx][ny + 1] != '1':
                    queue.append((nx, ny, 0, ct+1))
                    visited_row[nx][ny] = True

        if 0 < x < N - 1 and 0 < y < N - 1:
            if (area[x - 1][y - 1] != '1' and area[x - 1][y + 1] != '1'
                    and area[x + 1][y - 1] != '1' and area[x + 1][y + 1] != '1'):
                if c and not visited_row[x][y]:
                    if area[x][y - 1] != '1' and area[x][y + 1] != '1':
                        queue.append((x, y, 0, ct+1))
                        visited_row[x][y] = True
                elif not c and not visited_col[x][y]:
                    if area[x - 1][y] != '1' and area[x + 1][y] != '1':
                        queue.append((x, y, 1, ct+1))
                        visited_col[x][y] = True
    print(0)


if e[0][0] == ex:
    bfs(ex, ey, 0)
else:
    bfs(ex, ey, 1)


