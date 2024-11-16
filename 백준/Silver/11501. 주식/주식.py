T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    max_price = 0
    money = 0

    for i in range(N - 1, -1, -1):
        if days[i] > max_price:
            max_price = days[i]
        else:
            money += max_price - days[i]

    print(money)
