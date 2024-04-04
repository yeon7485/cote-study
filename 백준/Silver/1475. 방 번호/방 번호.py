room = input()
nums = {}
ans = 0
sn = 0

for r in room:
    if r not in nums:
        nums[r] = 1
    else:
        nums[r] += 1
    if r == '6' or r == '9':
        sn += 1

sn = sn // 2 + sn % 2
nums['6'] = sn
nums['9'] = sn
print(max(nums.values()))
