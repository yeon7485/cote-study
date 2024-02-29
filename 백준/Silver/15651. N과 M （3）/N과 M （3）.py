n, m = list(map(int, input().split()))
visited = [False] * (n + 1)
arr = []


def dfs(count):
    if count == m:
        print(*arr, end='\n')
        return

    for i in range(1, n + 1):
        arr.append(i)
        dfs(count + 1)
        arr.pop()


dfs(0)
