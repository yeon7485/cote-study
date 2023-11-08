def solution(survey, choices):
    answer = ''
    test = ['RT', 'CF', 'JM', 'AN']
    d = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        score = abs(4 - choices[i])
        if score == 0:
            continue
        if choices[i] < 4:
            d[survey[i][0]] += score
        else:
            d[survey[i][1]] += score
    
    for t in test:
        if d[t[0]] < d[t[1]]:
            answer += t[1]
        else:
            answer += t[0]
    return answer