# 공 바꾸기
# https://www.acmicpc.net/problem/10813

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

print(*arr)
