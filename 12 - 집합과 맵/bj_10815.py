# 숫자 카드

import sys

n = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in num1:
    dic[i] = 1

for i in num2:
    if i in dic.keys():
        print(1, end = ' ')
    else:
        print(0, end = ' ')