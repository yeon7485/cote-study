n, m = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
arr = []


def dfs(count):
    if count == m:
        print(*arr, end='\n')
        return

    for i in num:
        arr.append(i)
        dfs(count + 1)
        arr.pop()


dfs(0)
