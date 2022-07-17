# 상수

a, b = input().split()
x, y = int(a[::-1]), int(b[::-1])

print(max(x, y))