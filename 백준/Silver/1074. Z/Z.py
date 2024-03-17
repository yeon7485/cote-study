import sys

sys.setrecursionlimit(100000)

n, r, c = list(map(int, input().split()))


def func(x, r, c):
    if x == 0:
        return 0
    half = (2 ** x) // 2
    if r < half and c < half:
        return func(x - 1, r, c)
    if r < half <= c:
        return half * half + func(x - 1, r, c - half)
    if r >= half > c:
        return 2 * half * half + func(x - 1, r - half, c)
    return 3 * half * half + func(x - 1, r - half, c - half)


print(func(n, r, c))
