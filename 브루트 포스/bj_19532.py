# 수학은 비대면강의입니다

a, b, c, d, e, f = map(int, input().split())
check = False
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a * i + b * j == c:
            if d * i + e * j == f:
                print(i, j)
                check = True
                break
    if check:
        break
