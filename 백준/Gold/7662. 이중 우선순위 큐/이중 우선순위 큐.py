import sys
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    nums = {}
    for i in range(k):
        op, x = sys.stdin.readline().split()
        x = int(x)
        if op == 'I':
            if x in nums:
                nums[x] += 1
            else:
                nums[x] = 1
                heapq.heappush(min_heap, x)
                heapq.heappush(max_heap, -x)
        elif op == 'D':
            if nums:
                if x == 1:
                    while -max_heap[0] not in nums:
                        heapq.heappop(max_heap)
                    nums[-max_heap[0]] -= 1
                    if nums[-max_heap[0]] == 0:
                        del (nums[-max_heap[0]])

                else:
                    while min_heap[0] not in nums:
                        heapq.heappop(min_heap)
                    nums[min_heap[0]] -= 1
                    if nums[min_heap[0]] == 0:
                        del (nums[min_heap[0]])

    if nums:
        while min_heap[0] not in nums:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')
