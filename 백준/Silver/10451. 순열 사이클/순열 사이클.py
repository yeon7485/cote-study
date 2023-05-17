import sys
sys.setrecursionlimit(2000)

def dfs(x):
    visited[x] = True
    n = arr[x-1]
    if not visited[n]:
        dfs(n)

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False] * n

    result = 0
    for x in range(1, n+1):
        if not visited[x]:
            dfs(x)
            result += 1
    print(result)