# 셀프 넘버

num = set(range(1, 10001))

def d(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum + n

for i in range(1, 10001):
    if d(i) in num:
        num.remove(d(i))

for n in num:
    print(n)
    
