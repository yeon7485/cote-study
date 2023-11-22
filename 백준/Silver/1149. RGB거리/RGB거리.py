n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(3)] for __ in range(n)]

for it in range(3):
    d[0][it] = cost[0][it]

for i in range(1, n):
    d[i][0] = cost[i][0] + min(d[i - 1][1], d[i - 1][2])
    d[i][1] = cost[i][1] + min(d[i - 1][0], d[i - 1][2])
    d[i][2] = cost[i][2] + min(d[i - 1][0], d[i - 1][1])

print(min(d[n - 1]))