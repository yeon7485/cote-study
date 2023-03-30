# 코딩은 체육과목 입니다
# https://www.acmicpc.net/problem/25314

n = int(input())
type = ''

for l in range(int(n / 4)):
    type += 'long '

type += 'int'
print(type)
