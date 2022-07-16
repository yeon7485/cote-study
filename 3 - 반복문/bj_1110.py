# 더하기 사이클

n = int(input())
count = 0
a = n
while True:
    a = (a % 10) * 10 + (a // 10 + a % 10) % 10
    count += 1
    if a == n:
        break
print(count)