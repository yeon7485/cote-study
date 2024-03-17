n = int(input())
count = 0
visited_col = [False] * n
visited_right = [False] * (n * 2 - 1)
visited_left = [False] * (n * 2 - 1)


def func(x):
    global count
    if x == n:
        count += 1
        return

    for i in range(n):
        if not visited_col[i] and not visited_right[i + x] and not visited_left[x - i + n - 1]:
            visited_col[i] = True
            visited_right[i + x] = True
            visited_left[x - i + n - 1] = True
            func(x + 1)
            visited_col[i] = False
            visited_right[i + x] = False
            visited_left[x - i + n - 1] = False


func(0)
print(count)
