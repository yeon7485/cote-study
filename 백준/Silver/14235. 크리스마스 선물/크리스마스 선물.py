import heapq

n = int(input())
heap = []
for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        if not heap:
            print(-1)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        for i in range(arr[0]):
            heapq.heappush(heap, arr[i + 1] * -1)
