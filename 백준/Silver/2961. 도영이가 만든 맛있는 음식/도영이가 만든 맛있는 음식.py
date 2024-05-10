N = int(input())
flavor = [list(map(int, input().split())) for _ in range(N)]
arr = []
answer = 1e9


def back(x, n):
    global answer
    if x == n:
        sour = 1
        bitter = 0
        for a in arr:
            sour *= flavor[a][0]
            bitter += flavor[a][1]
        answer = min(answer, abs(sour - bitter))
        return
    for i in range(x, N):
        if x == 0 or i > arr[-1]:
            arr.append(i)
            back(x + 1, n)
            arr.pop()


for t in range(1, N + 1):
    back(0, t)

print(answer)
