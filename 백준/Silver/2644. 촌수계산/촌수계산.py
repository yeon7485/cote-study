n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
connect = [[] for _ in range(n + 1)]
for i in range(m):
    c, d = arr[i]
    if d not in connect[c]:
        connect[c].append(d)
    if c not in connect[d]:
        connect[d].append(c)

visited = [False] * (n + 1)
rst = 0


def dfs(cnt, x):
    global rst
    if x == b:
        rst = cnt
        return
    if not visited[x]:
        visited[x] = True
        for c in connect[x]:
            dfs(cnt + 1, c)


dfs(rst, a)
print(-1) if rst == 0 else print(rst)
