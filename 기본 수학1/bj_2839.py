# 설탕 배달

n = int(input())

count = 0
while True:
    if n % 5 == 0:
        count += n // 5
        break
    else:
        n -= 3
        count += 1
        
        if n <= 2 and n != 0:
            count = -1
            break

print(count)

