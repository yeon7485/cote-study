import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

num = 0
while len(heap) >= 2:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    heapq.heappush(heap, first + second)
    num += first + second
print(num)
