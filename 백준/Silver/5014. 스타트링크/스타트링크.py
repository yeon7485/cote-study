from collections import deque

F, S, G, U, D = map(int, input().split())
rst = -1
count = [0] * (F + 1)


def bfs():
    global rst
    queue = deque()
    queue.append(S)
    count[S] = 1

    while queue:
        x = queue.popleft()
        if x == G:
            return count[x] - 1
        else:
            for i in (x + U, x - D):
                if 0 < i <= F and count[i] == 0:
                    count[i] = count[x] + 1
                    queue.append(i)
    return 'use the stairs'



print(bfs())
