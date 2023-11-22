n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(3)] for __ in range(n)]

# 초기값 설정
d[0][0] = rgb[0][0]
d[0][1] = rgb[0][1]
d[0][2] = rgb[0][2]

for i in range(1, n):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + rgb[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + rgb[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + rgb[i][2]

print(min(d[n - 1]))