from collections import deque


def fire_bfs():
    while fq:
        x, y = fq.popleft()
        if fire[x][y] == 0:
            fire[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or maze[nx][ny] == '#':
                continue
            if maze[nx][ny] == '.' and fire[nx][ny] == 0:
                fq.append((nx, ny))
                fire[nx][ny] = fire[x][y] + 1
    return


def j_bfs():
    ret = 'IMPOSSIBLE'
    while jq:
        x, y = jq.popleft()
        if escape[x][y] == 0:
            escape[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return escape[x][y]
            if maze[nx][ny] == '.' and escape[nx][ny] == 0:
                if fire[nx][ny] > escape[x][y] + 1 or fire[nx][ny] == 0:
                    jq.append((nx, ny))
                    escape[nx][ny] = escape[x][y] + 1
    return ret


r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

jq = deque()
fq = deque()
fire = [[0 for __ in range(c)] for _ in range(r)]
escape = [[0 for _b in range(c)] for _a in range(r)]

for a, mz in enumerate(maze):
    for b, m in enumerate(mz):
        if m == "J":
            jq.append((a, b))
        elif m == "F":
            fq.append((a, b))

fire_bfs()
result = j_bfs()

print(result)
