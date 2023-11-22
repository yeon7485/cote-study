import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
d = [0] * (n + 1)
d[0] = 0

for i in range(1, n + 1):
    d[i] = d[i - 1] + num[i - 1]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(d[y] - d[x - 1])
