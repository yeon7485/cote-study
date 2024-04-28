from collections import deque

N = int(input())
K = int(input())
apple = []
for _ in range(K):
    x, y = map(int, input().split())
    apple.append((x-1, y-1))
L = int(input())
turn = deque()
for _ in range(L):
    x, c = input().split()
    turn.append((x, c))
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]  # 우, 하, 좌, 상
d = 0
time = 0
length = 0

queue = deque()
queue.append((0, 0))

while True:
    x, y = queue.popleft()
    nx = x + dx[d]
    ny = y + dy[d]
    time += 1
    if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
        print(time)
        break
    elif (nx, ny) in queue:
        print(time)
        break

    temp = deque()
    temp.append((x, y))
    while queue:
        temp.append(queue.popleft())
    queue.append((nx, ny))
    if (nx, ny) in apple:
        length += 1
        apple.remove((nx, ny))

    for i in range(length):
        queue.append(temp.popleft())

    if turn and int(turn[0][0]) == time:
        if turn[0][1] == 'L':
            if d % 2 == 0:
                d = 3 - d
            else:
                d -= 1
        else:
            if d % 2 == 0:
                d += 1
            else:
                d = 3 - d
        turn.popleft()

       