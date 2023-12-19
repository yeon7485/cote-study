
from collections import deque
import sys


def dfs_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                area[i][j] = 1
                dfs_wall(count + 1)
                area[i][j] = 0


def bfs():
    queue = deque()
    for v in virus:
        queue.append(v)
    copy_area = [item[:] for item in area]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copy_area[nx][ny] == 0:
                    queue.append((nx, ny))
                    copy_area[nx][ny] = 2

    global max_count
    count = 0
    for i in range(n):
        for j in range(m):
            if copy_area[i][j] == 0:
                count += 1

    max_count = max(max_count, count)
    return


n, m = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = []
max_count = 0

for x, ar in enumerate(area):
    for y, a in enumerate(ar):
        if a == 2:
            virus.append((x, y))

dfs_wall(0)
print(max_count)
