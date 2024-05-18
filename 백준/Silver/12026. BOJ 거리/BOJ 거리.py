N = int(input())
block = input()
dp = [1e9] * N
dp[0] = 0

for i in range(N):
    for j in range(i + 1, N):
        if block[i] == 'B' and block[j] == 'O' or \
                block[i] == 'O' and block[j] == 'J' or \
                block[i] == 'J' and block[j] == 'B':
            dp[j] = min(dp[j], dp[i] + (j-i)**2)

if dp[N-1] == 1e9:
    print(-1)
else:
    print(dp[N-1])
