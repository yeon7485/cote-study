# 최댓값
# https://www.acmicpc.net/problem/2566

maxValue = 0
maxCol = 1
maxRow = 1

for i in range(9):
    arr = list(map(int, input().split()))
    if max(arr) > maxValue:
        maxValue = max(arr)
        maxCol = i+1
        maxRow = arr.index(maxValue) + 1

print(maxValue)
print(maxCol, maxRow)
