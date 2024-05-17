T = int(input())
for t in range(T):
    A, B, C = map(int, input().split())
    ans = 0

    while C <= B:
        B -= 1
        ans += 1
        if B == 0:
            ans = -1
            break

    if ans > -1:
        while B <= A:
            A -= 1
            ans += 1
            if A == 0:
                ans = -1
                break
    print(f'#{t + 1} {ans}')