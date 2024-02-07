def solution(t, p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        x = int(t[i:i+len(p)])
        if x <= int(p):
            answer += 1
    
    return answer