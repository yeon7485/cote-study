def solution(players, callings):
    answer = players
    dict = {}
    
    for i in range(len(answer)) :
        dict[answer[i]] = i
    
    for call in callings :
        x = dict[call]
        dict[answer[x-1]] = x
        dict[call] = x-1
        
        answer[x-1], answer[x] = answer[x], answer[x-1]
        
    return answer