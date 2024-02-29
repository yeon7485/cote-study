n, m = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
arr = []


def dfs(count):
    if count == m:
        print(*arr, end='\n')
        return

    for i in num:
        if count == 0 or (i not in arr and i > arr[-1]):
            arr.append(i)
            dfs(count + 1)
            arr.pop()


dfs(0)
