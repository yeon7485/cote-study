# lv.2 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])

    def bfs(x, y):
        nonlocal answer
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))
        return maps[-1][-1]

    answer = bfs(0, 0)
    if maps[-1][-1] == 1:
        answer = -1
    return answer


test1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
test2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(test1))
print(solution(test2))