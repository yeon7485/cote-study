from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                queue.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1
    return


m, n = list(map(int, input().split()))
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

for i, tm in enumerate(tomato):
    for j, t in enumerate(tm):
        if t == 1:
            queue.append((i, j))

bfs()

zero = False
result = 0
for tm in tomato:
    if 0 in tm:
        zero = True
        break
    result = max(result, max(tm))

if zero:
    result = -1
else:
    result -= 1

print(result)
