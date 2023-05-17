from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    cnt = 0
    if graph[x][y] == 0:
        return 0
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            graph[x][y] = 0
            cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
count = []
for i in range(n):
    for j in range(n):
        cnt = bfs(i, j)
        if cnt != 0:
            result += 1
            count.append(cnt)
print(result)
count.sort()
for c in count:
    print(c)