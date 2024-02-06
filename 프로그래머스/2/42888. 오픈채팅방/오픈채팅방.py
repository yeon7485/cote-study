def solution(record):
    record = [l.split(' ') for l in record]
    dic = {}
    li = []
    
    for w in record:
        if w[0] == 'Enter' or w[0] == 'Change':
            dic[w[1]] = w[2]
                
        if w[0] == 'Enter':
            li.append([w[1],'in'])
                
        elif w[0] == 'Leave':
            li.append([w[1],'out'])

    for i in range(len(li)):
        if li[i][1] == 'in':
            li[i] = f'{dic[li[i][0]]}님이 들어왔습니다.'
            
        else :
            li[i] = f'{dic[li[i][0]]}님이 나갔습니다.'
    return li