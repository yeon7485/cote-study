n = int(input())
nums = list(map(int, input().split()))
cnt = list(map(int, input().split()))
op = ['+', '-', '*', '//']
cal = []
visited_cal = []
max_rst, min_rst = int(-1e9), int(1e9)

for i in range(4):
    for _ in range(cnt[i]):
        cal.append(op[i])
        visited_cal.append(False)


def func(x, now):
    global max_rst, min_rst
    if x == (n - 1):
        max_rst = max(max_rst, now)
        min_rst = min(min_rst, now)
        return

    for i in range(len(cal)):
        if not visited_cal[i]:
            temp = now
            if cal[i] == '+':
                temp += nums[x + 1]
            elif cal[i] == '-':
                temp -= nums[x + 1]
            elif cal[i] == '*':
                temp *= nums[x + 1]
            elif cal[i] == '//':
                temp = int(now / nums[x + 1])
            visited_cal[i] = True
            func(x + 1, temp)
            visited_cal[i] = False


func(0, nums[0])
print(max_rst, min_rst)
