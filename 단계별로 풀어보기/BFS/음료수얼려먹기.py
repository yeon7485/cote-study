from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    if graph[x][y] == 1:
        return False
    while queue:
        print(queue)
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                print(*graph,end='\n')
    return True

# N, M을 공백을 구준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 BFS 수행
        if bfs(i, j) == True:
            print(i, j)
            result += 1

print(result)
