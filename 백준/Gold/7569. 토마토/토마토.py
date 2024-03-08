from collections import deque

M, N, H = list(map(int, input().split()))
tomato = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dh = [1, -1, 0, 0, 0, 0]
result = 0


def bfs():
    while queue:
        x, y, h = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nh < H:
                if tomato[nh][ny][nx] == 0:
                    queue.append((nx, ny, nh))
                    tomato[nh][ny][nx] = tomato[h][y][x] + 1
    return


queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((k, j, i))

bfs()
for i in range(H):
    for j in range(N):
        if 0 in tomato[i][j]:
            print(-1)
            exit(0)
        result = max(max(tomato[i][j]), result)

print(result - 1)
