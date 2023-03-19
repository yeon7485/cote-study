# 대표값2

import sys

num = []

for _ in range(5):
    num.append(int(sys.stdin.readline()))

num.sort()
avg = sum(num) // len(num)

print(avg)
print(num[5 // 2])
