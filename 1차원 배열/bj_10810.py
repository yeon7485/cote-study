# 공 넣기
# https://www.acmicpc.net/problem/10810

n, m = map(int, input().split())
li = []

for _ in range(n):
    li.append(0)

for i in range(m):
    x, y, n = map(int, input().split())
    for j in range(x, y + 1):
        li[j-1] = n

print(*li)
