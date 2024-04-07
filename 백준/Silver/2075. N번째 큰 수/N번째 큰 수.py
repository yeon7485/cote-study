import sys
import heapq

N = int(input())
heap = []
for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for a in arr:
        heapq.heappush(heap, a)
        if len(heap) > N:
            heapq.heappop(heap)
print(heapq.heappop(heap))
