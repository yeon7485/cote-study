N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]
rst = 0
for i in range(N-1, -1, -1):
    rst += K // coins[i]
    K %= coins[i]

print(rst)
