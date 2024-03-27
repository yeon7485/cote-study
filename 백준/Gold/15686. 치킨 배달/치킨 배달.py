N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i, j])
        elif board[i][j] == 1:
            home.append([i, j])

visited = [False] * len(chicken)
temp = []
result = int(1e9)


def func(n, s):
    global result
    if n == M:
        ans = 0
        for h in home:
            min_home = 2 * N
            for t in temp:
                min_home = min(min_home, abs(t[0] - h[0]) + abs(t[1] - h[1]))
            ans += min_home
        result = min(result, ans)
        return

    for i in range(s, len(chicken)):
        if not visited[i]:
            temp.append(chicken[i])
            visited[i] = True
            func(n + 1, i)
            temp.pop()
            visited[i] = False


func(0, 0)
print(result)
