N = int(input())
nums = list(map(int, input().split()))
visited = [False] * N
max_sum = 0
a = []


def func(x):
    global max_sum
    if x == N:
        a_sum = 0
        for i in range(1, N):
            a_sum += abs(a[i - 1] - a[i])
        max_sum = max(max_sum, a_sum)
        return
    for i in range(N):
        if not visited[i]:
            a.append(nums[i])
            visited[i] = True
            func(x + 1)
            a.pop()
            visited[i] = False


func(0)
print(max_sum)
