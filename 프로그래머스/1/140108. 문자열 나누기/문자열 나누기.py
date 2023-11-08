def solution(s):
    answer = 0
    
    while len(s) > 1:
        x = s[0]
        a, b = 0, 0
        for i, ch in enumerate(s):
            if ch == x:
                a += 1
            else:
                b += 1
            if a == b:
                answer += 1
                s = s[i+1:]
                break
        if a != b:
            break
            
    if len(s) != 0:
        answer += 1
    return answer
