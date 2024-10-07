# 조약돌 꺼내기

M = int(input())
stone = list(map(float, input().split()))
K = int(input())
n = sum(stone)
ans = 0

if M == 1:
    print(1.0)
elif K == 1:
    print(1.0)
else:
    for i in range(M):
        temp_sum = n
        temp_prob = 1
        if K > stone[i]: continue
        for j in range(K):
            temp_prob *= stone[i] / temp_sum
            stone[i] -= 1
            temp_sum -= 1
        ans += temp_prob

    print(ans)