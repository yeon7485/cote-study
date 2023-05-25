import math

def solution(n, stations, w):
    answer = 0
    start = 1
    
    for s in stations:
        
        total = s - w - start
        if total > 0:
            answer += math.ceil(total / ((2*w) + 1))
        
        start = s + w + 1
    
    if start <= n:
        total = n + 1 - start
        answer += math.ceil(total / ((2*w) + 1))
    
    return answer