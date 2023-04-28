def solution(dirs):
    answer = 0
    arr = []
    pre = [0, 0]
    now = [0, 0]
    result = []
    
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            if now[1] < 5:
                pre, now = now, [now[0], now[1] + 1]
            else:
                continue
        elif dirs[i] == 'D':
            if now[1] > -5:
                pre, now = now, [now[0], now[1] - 1]
            else:
                continue
        elif dirs[i] == 'L':
            if now[0] > -5:
                pre, now = now, [now[0] - 1, now[1]]
            else:
                continue
        else:
            if now[0] < 5:
                pre, now = now, [now[0] + 1, now[1]]
            else:
                continue
        arr.append([pre[0], pre[1], now[0], now[1]])
    
    for a in arr:
        li = [a[2], a[3], a[0], a[1]]
        if a not in result and li not in result:
            result.append(a)
    return len(result)