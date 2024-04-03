from collections import deque

n, k = map(int, input().split())
queue = deque()
result = []

for i in range(1, n + 1):
    queue.append(i)

x = 0
while len(result) < n:
    num = queue.popleft()
    x += 1
    if x == k:
        result.append(num)
        x = 0
    else:
        queue.append(num)

ans = ''
for r in result:
    ans += str(r) + ', '

print(f'<{ans[:-2]}>')