# 좌표 압축

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

x = list(set(num))
x.sort()

dic = dict()

for i in range(len(x)):
    dic[x[i]] = i

for l in num:
    print(dic[l], end=' ')
