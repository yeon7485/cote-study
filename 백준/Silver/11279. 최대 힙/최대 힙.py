import sys
import heapq

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)
        
