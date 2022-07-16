# 한수

def d(n):
    if n < 100:
        return n
    else:
        sum = 99
        for i in range(100, n + 1):
            arr = list(map(int, str(i)))
            if (arr[0] + arr[2]) / 2 == arr[1]:
                sum += 1
    return sum
    
num = int(input())
print(d(num))