# 소수 찾기

N = int(input())

num = map(int, input().split())

for n in num:
    if n == 1:
        N -= 1
    else:
        for i in range(2, n):
            if n % i == 0:
                N -= 1
                break
print(N)
