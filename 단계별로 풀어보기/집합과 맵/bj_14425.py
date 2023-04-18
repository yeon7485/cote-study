# 문자열 집합

n, m = map(int, input().split())
inc = []
word = []

count = 0

for i in range(n):
    inc.append(input())

for i in range(m):
    word.append(input())

for w in word:
    if w in inc:
        count += 1

print(count)