import sys

sys.setrecursionlimit(100000)

n, m = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
visited = [False] * len(num)
arr = []


def dfs(count):
    if count == m:
        print(*arr)
        return

    for i in range(len(num)):
        if i > 0 and num[i - 1] == num[i] and not visited[i - 1]:
            continue
        arr.append(num[i])
        visited[i] = True
        dfs(count + 1)
        arr.pop()
        visited[i] = False


dfs(0)
