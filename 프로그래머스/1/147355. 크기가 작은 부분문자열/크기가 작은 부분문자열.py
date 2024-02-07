def solution(t, p):
    answer = 0
    l = len(t) - len(p) + 1
    num = []
    for i in range(l):
        x = int(t[i:i+len(p)])
        if x <= int(p):
            answer += 1
    
    return answer