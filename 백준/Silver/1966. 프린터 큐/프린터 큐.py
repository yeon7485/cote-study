from collections import deque

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    queue = deque()
    rst = 0
    for i in range(N):
        queue.append((i, arr[i]))
    while True:
        if N == 1:
            print(1)
            break
        idx, score = queue.popleft()
        rst += 1
        flag = True
        for q in queue:
            if q[1] > score:
                queue.append((idx, score))
                rst -= 1
                flag = False
                break
        if idx == M and flag:
            print(rst)
            break
