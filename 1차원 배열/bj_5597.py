# 과제 안 내신 분..?
# https://www.acmicpc.net/problem/5597

arr = [i + 1 for i in range(30)]
for _ in range(28):
    n = int(input())
    if n in arr:
        arr.remove(n)

for a in arr:
    print(a)
