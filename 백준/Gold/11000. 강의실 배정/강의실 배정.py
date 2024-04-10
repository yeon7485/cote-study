import sys
import heapq

n = int(input())
time = []
for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    time.append((s, t))

time.sort()
heap = [time[0][1]]
for i in range(1, n):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))
