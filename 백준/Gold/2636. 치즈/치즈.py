from collections import deque


def air_bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                    board[nx][ny] = -1


def cheese_bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    queue.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1
                if board[nx][ny] < 0:
                    melt.add((x, y))


n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
melt = set()
queue = deque()
cnt = 0

while True:
    queue.append((0, 0))
    air_bfs()  # 공기 BFS
    positive = False
    # 치즈가 남아있는지 검사
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                positive = True
                break
        if positive:
            break

    # 모두 녹았을 때
    if not positive:
        print(cnt)
        print(len(melt))
        break
    else:
        cnt += 1
        rst = 0
        melt.clear()
        # 치즈 부분 BFS
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    queue.append((i, j))
                    cheese_bfs()

        # 녹는 부분 공기로 만들기
        for mt in melt:
            x, y = mt
            board[x][y] = 0

        # 공기 부분 다시 0으로 만들기
        for i in range(n):
            for j in range(m):
                if board[i][j] < 0:
                    board[i][j] = 0
