# 베르트랑 공준

def isPrime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

prime = list()
for i in range(2, (123456 * 2) + 1):
    if isPrime(i):
        prime.append(i)

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for p in prime:
        if n < p and p <= 2*n:
            count += 1
    
    print(count)
            
