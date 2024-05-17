T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    candy = sorted(list(map(int, input().split())))
    ans = 1e9

    for i in range(N - K + 1):
        for j in range(i + K - 1, N):
            ans = min(ans, candy[j] - candy[i])

    print(f'#{t+1} {ans}')
