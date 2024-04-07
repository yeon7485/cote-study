import sys
import heapq

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            a, b = heapq.heappop(heap)
            print(b)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
