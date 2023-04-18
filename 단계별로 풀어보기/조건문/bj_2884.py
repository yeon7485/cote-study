# 알람 시계

h, m = map(int, input().split())
if m < 45:
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h, m + 15)
else:
    print(h, m - 45)