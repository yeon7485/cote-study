def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for bab in babbling:
        for i, b in enumerate(baby):
            if b in bab:
                bab = bab.replace(b, str(i))
            
        if bab.isdigit():
            flag = True
            for i in range(len(bab)-1):
                if bab[i] == bab[i+1]:
                    flag = False
                    break
            if flag:
                answer += 1
    return answer