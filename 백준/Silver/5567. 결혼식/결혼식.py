from collections import deque

n = int(input())
m = int(input())
friend = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    if a not in friend[b]:
        friend[b].append(a)
    if b not in friend[a]:
        friend[a].append(b)


def bfs():
    queue = deque([1])
    while queue:
        x = queue.popleft()
        for f in friend[x]:
            if visited[f] == 0:
                visited[f] = visited[x] + 1
                queue.append(f)


bfs()
result = 0
for i in range(2, n + 1):
    if 0 < visited[i] < 3:
        result += 1

print(result)
