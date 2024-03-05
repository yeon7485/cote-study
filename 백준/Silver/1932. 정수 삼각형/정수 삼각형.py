n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * d for d in range(1, n+1)]

dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + arr[i][0]
    for j in range(1, i):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]
    dp[i][i] = dp[i - 1][i - 1] + arr[i][i]


print(max(dp[-1]))
