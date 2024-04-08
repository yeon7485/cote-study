import sys
import heapq

n, m = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))
heap = []
for c in cards:
    heapq.heappush(heap, c)

for i in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x + y)
    heapq.heappush(heap, x + y)

print(sum(heap))