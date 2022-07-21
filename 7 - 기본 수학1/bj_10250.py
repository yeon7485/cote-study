# ACM 호텔

import math

T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    a = math.ceil(n / h)
    if n % h == 0:
        b = h
    else:
        b = n % h

    if a < 10:
        print(f'{b}0{a}')
    else:
        print(f'{b}{a}')