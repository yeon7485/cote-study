k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for line in lan:
        cnt += line // mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)