def solution(today, terms, privacies):
    answer = []
    term = {}
    
    for t in terms:
        a, b = t.split()
        term[a] = int(b)
        
    for i, p in enumerate(privacies):
        a, b = p.split()
        year, month, date = list(map(int, a.split('.')))
        month += term[b]
        
        if month > 12:
            if month % 12 == 0:
                year += month // 12 - 1
                month = 12
            else:
                year += month // 12
                month %= 12
        
        t = list(map(int, today.split('.')))
        
        if t[0] < year:
            continue
        if t[1] < month and t[0] == year:
            continue
        if t[2] < date and t[1] == month and t[0] == year:
            continue
            
        answer.append(i+1)
            
    
    return answer