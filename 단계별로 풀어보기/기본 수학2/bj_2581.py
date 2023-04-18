# 소수

m = int(input())
n = int(input())

num = []
result = []
for i in range(m, n + 1):
    num.append(i)
    if i == 1:
        result.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                result.append(i)
                break
            
if num == result:
    print(-1)
else:
    a = [x for x in num if x not in result]
    print(sum(a))
    print(a[0])
