def solution(today, terms, privacies):
    answer = []
    term = {}
    
    for t in terms:
        ts = t.split()
        term[ts[0]] = int(ts[1])
    
    for i, p in enumerate(privacies):
        date, x = p.split()
        year = int(date[0:4])
        month = int(date[5:7]) + term[x]
        day = int(date[8:]) - 1
        
        if day == 0:
            month -= 1
            day = 28
        if month > 12:
            if month % 12 == 0:
                year += (month // 12) - 1
                month = 12
            else:
                year += month // 12
                month %= 12

        print(year, month, day)
        tdy = list(map(int, today.split('.')))
        
        if tdy[0] > year:
            answer.append(i+1)
            continue
        elif tdy[1] > month and tdy[0] == year:
            answer.append(i+1)
            continue
        elif tdy[2] > day and tdy[1] == month and tdy[0] == year:
            answer.append(i+1)
            continue
    
    return answer