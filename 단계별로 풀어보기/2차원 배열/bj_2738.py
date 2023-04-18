# 행렬 덧셈
# https://www.acmicpc.net/problem/2738

n, m = map(int, input().split())
a, b = [], []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

result = []

for i in range(n):
    r = []
    for j in range(m):
        r.append(a[i][j] + b[i][j])
    result.append(r)

for r in result:
    print(*r)
