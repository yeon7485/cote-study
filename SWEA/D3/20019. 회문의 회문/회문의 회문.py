T = int(input())
for t in range(T):
    s = input()
    n = len(s)
    a, b = s[:n // 2], s[-1:-(n//2 + 1):-1]
    ans = 'NO'
    if a == b:
        n = len(a)
        c, d = a[:n // 2], a[-1:-(n//2 + 1):-1]
        if c == d:
            ans = 'YES'

    print(f'#{t + 1} {ans}')
