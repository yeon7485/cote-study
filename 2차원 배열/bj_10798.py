# 세로읽기
# https://www.acmicpc.net/problem/10798

maxLen = 0
arr = []
for i in range(5):
    arr.append(input())
    if maxLen < len(arr[i]):
        maxLen = len(arr[i])

result = ''
for i in range(maxLen):
    for j in range(5):
        if len(arr[j]) > i:
            result += arr[j][i]

print(result)
