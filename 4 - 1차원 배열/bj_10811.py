# 바구니 뒤집기
# https://www.acmicpc.net/problem/10811

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
result = arr.copy()

for _ in range(m):
    i, j = map(int, input().split())
    a = [i for i in range(i-1, j)]
    b = list(reversed(a))

    for idx in range(len(a)):
        result[a[idx]] = arr[b[idx]]
    arr = result.copy()
print(*result)
