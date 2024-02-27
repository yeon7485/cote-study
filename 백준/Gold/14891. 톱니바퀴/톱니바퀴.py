gear = [list(map(int, input())) for _ in range(4)]
k = int(input())
case = [list(map(int, input().split())) for _ in range(k)]
result = 0


def turn(arr, f):
    if f == 1:
        return arr[7:8] + arr[0:7]
    elif f == -1:
        return arr[1:8] + arr[0:1]
    return arr


for i in range(k):
    contact = [[gear[c][2], gear[c + 1][6]] for c in range(3)]
    n, flag = case[i]
    n -= 1
    d = [0, 0, 0, 0]
    d[n] = flag
    if n != 0:
        for l in range(n - 1, -1, -1):
            if contact[l][0] != contact[l][1]:
                d[l] = d[l + 1] * -1
            if d[l] == 0:
                break
    if n != 3:
        for r in range(n, 3):
            if contact[r][0] != contact[r][1]:
                d[r + 1] = d[r] * -1
            if d[r + 1] == 0:
                break

    for t in range(4):
        gear[t] = turn(gear[t], d[t])

for i in range(4):
    if gear[i][0] == 1:
        result += 2 ** i

print(result)
