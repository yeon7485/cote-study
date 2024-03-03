def cnt(a, b):
    ret = 0
    if a == 1:
        ret = b
    elif a == 2:
        ret = w * 2 + h - b
    elif a == 3:
        ret = (w * 2 + h * 2) - b
    elif a == 4:
        ret = b + w
    return ret


w, h = list(map(int, input().split()))
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
dong = list(map(int, input().split()))
d = cnt(dong[0], dong[1])
result = 0

for i in range(n):
    x, y = store[i]
    s = cnt(x, y)
    if s >= d:
        result += min(s - d, d + (w + h) * 2 - s)
    else:
        result += min(d - s, (w + h) * 2 - d + s)

print(result)