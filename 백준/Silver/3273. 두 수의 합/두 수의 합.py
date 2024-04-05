import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

result = 0
left, right = 0, n-1
while left < right:
    plus = nums[left] + nums[right]
    if plus == x:
        result += 1
        left += 1
    elif plus < x:
        left += 1
    else:
        right -= 1

print(result)