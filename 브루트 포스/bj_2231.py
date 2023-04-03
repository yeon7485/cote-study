# 분해합

n = int(input())

count = 1
result = 0
while count < n:
    
    arr = list(map(int, str(count)))

    if sum(arr) + count == n:
        result = count
        break
    else:
        count += 1

print(result)
