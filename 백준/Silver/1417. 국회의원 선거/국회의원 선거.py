import heapq

N = int(input())
one = int(input())
heap = []
result = 0

for i in range(N - 1):
    n = int(input())
    heapq.heappush(heap, -n)

while heap:
    x = -heapq.heappop(heap)
    if one > x:
        break
    one += 1
    result += 1
    heapq.heappush(heap, -x + 1)

print(result)
