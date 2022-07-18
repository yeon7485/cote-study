# 벌집

import sys

n = int(sys.stdin.readline())
count = 1
result = 1
while n > count:
    count += 6 * result
    result += 1
print(result)