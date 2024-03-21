n, k = list(map(int, input().split()))
coin = set()
for _ in range(n):
    coin.add(int(input()))
dp = [0] * (k+1)

for i in range(1, k+1):
    temp = []
    for c in coin:
        if i >= c and dp[i-c] != -1:
            temp.append(dp[i-c] + 1)
    if not temp:
        dp[i] = -1
    else:
        dp[i] = min(temp)

print(dp[k])
