# 소인수분해

N = int(input())

x = 2
while N > 1:
    if N % x == 0:
        print(x)
        N = N // x
        x = 2
    else:
        x += 1