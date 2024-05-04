k = int(input())
sign = input().split()
visited = [False] * 10
arr = []
ans = []
max_ans = 0
min_ans = int('9' * (k+1))


def back(x):
    global max_ans, min_ans
    if x == k + 1:
        check = True
        for j in range(k):
            if sign[j] == '>':
                if not arr[j] > arr[j+1]:
                    check = False
                    break
            elif sign[j] == '<':
                if not arr[j] < arr[j+1]:
                    check = False
                    break

        if check:
            ans = ''.join(map(str, arr))
            max_ans = max(max_ans, int(ans))
            min_ans = min(min_ans, int(ans))
        return
    for i in range(10):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            back(x + 1)
            arr.pop()
            visited[i] = False


back(0)
print(max_ans)
min_ans = str(min_ans)
print(min_ans.zfill(k+1))
