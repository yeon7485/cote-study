# 부녀회장이 될테야

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    if n == 1:
        print(1)
        continue
    elif k == 0:
        print(n)
        continue
    else:
        num = []
        for j in range(1, n + 1):
            num.append(j)
        
        for x in range(k):
            for y in range(1, n):
                num[y] += num[y-1]
        print(num[-1]) 


    

