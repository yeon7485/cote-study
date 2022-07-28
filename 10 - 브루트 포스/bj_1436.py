# 영화감독 숌

n = int(input())
count = 0
x = 665
while True:
    x += 1
    if str(x).find('666') != -1:
        count += 1
    
    if count == n:
        break
    
print(x)