def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        arr = []
        for i in range(len(s)):
            if s[i] in skill:
                arr.append(s[i])
        
        check = True
        for i in range(len(arr)):
            if skill.find(arr[i]) != i:
                check = False
                break
                
        if check:
            answer += 1
            
        
    return answer