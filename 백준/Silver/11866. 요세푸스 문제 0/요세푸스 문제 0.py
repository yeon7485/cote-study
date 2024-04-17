from collections import deque

n, k = map(int, input().split())
queue = deque()
ans = []
for i in range(1, n+1):
    queue.append(i)

x = 1
while queue:
    if x == k:
        ans.append(queue.popleft())
        x = 1
    else:
        temp = queue.popleft()
        queue.append(temp)
        x += 1

s = '<'
for a in ans:
    s += str(a) + ', '
print(f'{s[:-2]}>')