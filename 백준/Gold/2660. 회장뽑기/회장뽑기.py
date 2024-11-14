from collections import deque

N = int(input())
friend = [[] for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    if a not in friend[b]:
        friend[b].append(a)
    if b not in friend[a]:
        friend[a].append(b)


def bfs(n):
    queue = deque([n])
    visited = [-1 for _ in range(N + 1)]
    visited[n] = 0
    while queue:
        x = queue.popleft()
        for f in friend[x]:
            if visited[f] == -1:
                visited[f] = visited[x] + 1
                queue.append(f)
    return max(visited)


min_score = 50
score = [0 for _ in range(N + 1)]
result = []

for i in range(1, N + 1):
    s = bfs(i)
    min_score = min(min_score, s)
    score[i] = s

for i in range(1, N + 1):
    if score[i] == min_score:
        result.append(i)

print(min_score, len(result))
print(*result)
