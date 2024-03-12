n = int(input())
glass = [int(input()) for _ in range(n)]
if n == 1:
    print(glass[0])
elif n == 2:
    print(glass[0] + glass[1])

else:
    d = [0] * n
    d[0] = glass[0]
    d[1] = glass[0] + glass[1]
    d[2] = max(d[1], glass[0] + glass[2], glass[1] + glass[2])

    for i in range(3, n):
        d[i] = max(d[i - 1], d[i - 2] + glass[i], d[i - 3] + glass[i - 1] + glass[i])
    print(d[-1])
