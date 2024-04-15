import heapq

N = int(input())
heap = []
max_day = 0
ans = 0

for _ in range(N):
    d, w = map(int, input().split())
    max_day = max(max_day, d)
    heapq.heappush(heap, (-w, d))

assign = [False] * (max_day + 1)

while heap:
    w, d = heapq.heappop(heap)

    for i in range(d, 0, -1):
        if not assign[i]:
            assign[i] = True
            ans += -w
            break
print(ans)
