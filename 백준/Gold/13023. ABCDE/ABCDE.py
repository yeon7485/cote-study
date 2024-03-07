n, m = list(map(int, input().split()))
friend = [[] for _ in range(n)]
result = 0

for _ in range(m):
    a, b = list(map(int, input().split()))
    if b not in friend[a]:
        friend[a].append(b)
    if a not in friend[b]:
        friend[b].append(a)


def dfs(num, count, visited):
    global result
    if count == 4:
        result = 1
        return True
    visited[num] = True
    for f in friend[num]:
        if not visited[f]:
            visited[f] = True
            dfs(f, count + 1, visited)
            visited[f] = False


for i in range(n):
    visited = [False] * n
    dfs(i, 0, visited)
    if result:
        break

print(result)
