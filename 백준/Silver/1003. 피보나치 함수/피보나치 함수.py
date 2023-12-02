t = int(input())
for _ in range(t):
    N = int(input())
    d = [[1, 0], [0, 1]]
    for i in range(2, N + 1):
        x = d[i - 1][0] + d[i - 2][0]
        y = d[i - 1][1] + d[i - 2][1]
        d.append([x, y])
    print(d[N][0], d[N][1])