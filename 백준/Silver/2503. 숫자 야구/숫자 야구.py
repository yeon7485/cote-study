from itertools import permutations

N = int(input())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = list(permutations(data, 3))

for _ in range(N):
    n, strike, ball = map(int, input().split())
    n = list(str(n))
    rm = 0
    for i in range(len(nums)):
        s, b = 0, 0
        i -= rm
        for j in range(3):
            if n[j] == nums[i][j]:
                s += 1
            elif n[j] in nums[i]:
                b += 1
        if strike != s or ball != b:
            nums.remove(nums[i])
            rm += 1
print(len(nums))
