N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
result = 1e9


def team(n, x):
    global result
    if n == N // 2:
        r1, r2 = 0, 0
        for j in range(N):
            for k in range(j + 1, N):
                if visited[j] and visited[k]:
                    r1 += S[j][k] + S[k][j]
                if not visited[j] and not visited[k]:
                    r2 += S[j][k] + S[k][j]
        result = min(result, abs(r1 - r2))
        return

    for i in range(x, N):
        if not visited[i]:
            visited[i] = True
            team(n + 1, i)
            visited[i] = False


team(0, 0)
print(result)
