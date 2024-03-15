n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))
arr = []
result = 0
visited = [False] * n


def dfs(x):
    global result
    if len(arr) > 0 and sum(arr) == s:
        result += 1
    for i in range(x, n):
        if not visited[i]:
            arr.append(nums[i])
            visited[i] = True
            dfs(i)
            visited[i] = False
            arr.pop()


dfs(0)
print(result)
