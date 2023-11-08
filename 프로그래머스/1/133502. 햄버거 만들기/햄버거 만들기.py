def solution(ingredient):
    answer = 0
    s = []
    
    for i in ingredient:
        s.append(i)
        if len(s) >= 4 and s[-4:] == [1, 2, 3, 1]:
            answer += 1
            del s[-4:]
            
    return answer