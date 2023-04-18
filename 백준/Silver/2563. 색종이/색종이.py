n = int(input())

arr = [[0 for j in range(100)] for i in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1

cnt = 0
for a in arr:
    cnt += a.count(1)
print(cnt)
