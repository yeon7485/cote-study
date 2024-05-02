import sys

sys.setrecursionlimit(1000000)


def back(x, k, arr):
    global temp
    if x == 6:
        print(*temp)
    for i in range(k):
        if x == 0 or arr[i] > temp[-1]:
            temp.append(arr[i])
            back(x + 1, k, arr)
            temp.pop()


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    k = nums[0]
    nums = nums[1:]
    visited = [False] * k
    temp = []
    back(0, k, nums)
    print()
