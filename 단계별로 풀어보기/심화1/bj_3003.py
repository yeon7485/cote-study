# 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003

chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
result = []

for i in range(len(arr)):
    result.append(chess[i] - arr[i])

print(*result)
