n = int(input())
visited = [False] * (n+1)
arr = []


def dfs():
    if len(arr) == n:
        print(*arr)
        return

    for i in range(1, n+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            dfs()
            arr.pop()
            visited[i] = False


dfs()