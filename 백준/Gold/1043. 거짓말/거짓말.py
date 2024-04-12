from collections import deque

N, M = map(int, input().split())
KNOW = list(map(int, input().split()[1:]))
isKnow = [False] * (N + 1)
nums = [[] for _ in range(N+1)]
party = []
ans = 0
for _ in range(M):
    arr = list(map(int, input().split()))
    party.append(arr[1:])
    for i in range(1, arr[0] + 1):
        for j in range(1, arr[0] + 1):
            if i != j and arr[j] not in nums[arr[i]]:
                nums[arr[i]].append(arr[j])

queue = deque()
for k in KNOW:
    queue.append(k)
    isKnow[k] = True
    while queue:
        x = queue.popleft()
        for n in nums[x]:
            if not isKnow[n]:
                queue.append(n)
                isKnow[n] = True

for i in range(M):
    go = True
    for p in party[i]:
        if isKnow[p]:
            go = False
            break
    if go:
        ans += 1

print(ans)
