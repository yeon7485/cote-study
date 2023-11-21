n = int(input())
floor = [0] * (n + 1)

for f in range(n):
    floor[f + 1] = int(input())

if n == 1:
    print(floor[1])

elif n == 2:
    print(floor[1] + floor[2])

else:
    d = [0] * (n + 1)
    d[1] = floor[1]
    d[2] = floor[1] + floor[2]
    d[3] = max(floor[1] + floor[3], floor[2] + floor[3])

    for i in range(4, n + 1):
        d[i] = max(d[i - 2] + floor[i], d[i - 3] + floor[i - 1] + floor[i])

    print(d[n])
