import sys
import heapq

n = int(input())
small_heap = []
large_heap = []
mid = 1e9
for i in range(1, n+1):
    x = int(sys.stdin.readline().strip())
    if x > mid:
        heapq.heappush(large_heap, x)
    else:
        heapq.heappush(small_heap, -x)

    # 균형 맞춰주기
    if len(small_heap) - len(large_heap) > 1:
        heapq.heappush(large_heap, -heapq.heappop(small_heap))
    elif len(large_heap) - len(small_heap) > 1:
        heapq.heappush(small_heap, -heapq.heappop(large_heap))

    if len(large_heap) > len(small_heap):
        mid = large_heap[0]
    else:
        mid = -small_heap[0]
    print(mid)
