n, m = list(map(int, input().split()))
visited = [False] * (n + 1)
arr = []


def dfs(count):
    if count == m:
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                return
        print(*arr, end='\n')
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(count + 1)
            arr.pop()
            visited[i] = False


dfs(0)
