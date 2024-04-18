from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = []
    queue = deque()
    rev = 0
    if n > 0:
        arr = list(map(int, input()[1:-1].split(',')))
        for a in arr:
            queue.append(a)
    else:
        no_used = input()

    for i in range(len(p)):
        if p[i] == 'R':
            rev += 1
        else:
            if len(queue) == 0:
                queue.append(0)
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if len(queue) == 0:
        print('[]')
    elif queue[0] == 0:
        print('error')
    else:
        if rev % 2 == 1:
            queue.reverse()
        ans = '['
        for q in queue:
            ans += str(q) + ','
        print(ans[:-1] + ']')
