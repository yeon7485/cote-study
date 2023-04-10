# 바구니 순서 바꾸기
# https://www.acmicpc.net/problem/10812

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    # idx = i-1
    # temp = []
    # for x in range(k-1, j):
    #     temp.append(arr[x])
    # for x in range(i-1, k-1):
    #     temp.append(arr[x])

    # for x in range(len(temp)):
    #     arr[idx] = temp[x]
    #     idx += 1

    # 개쩌는 풀이.. 앞으로 이렇게 풀자
    arr[i-1:j] = arr[k-1:j]+arr[i-1:k-1]

print(*arr)
