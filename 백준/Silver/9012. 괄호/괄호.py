T = int(input())
for _ in range(T):
    arr = []
    st = input()
    if st[0] == ')':
        print('NO')
        continue
    for s in st:
        if s == '(':
            arr.append(s)
        else:
            if len(arr) > 0:
                arr.pop()
            else:
                arr.append(s)
                break

    if len(arr) == 0:
        print('YES')
    else:
        print('NO')
