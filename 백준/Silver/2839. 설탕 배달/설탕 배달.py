n = int(input())
d = [5001] * (n + 5)
d[3] = d[5] = 1

for i in range(6, n + 1):
    d[i] = min(d[i - 5] + 1, d[i - 3] + 1)

if d[n] > 5000:
    print(-1)
else:
    print(d[n])
