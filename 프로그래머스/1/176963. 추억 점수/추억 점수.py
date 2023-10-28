def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    answer = []
    
    for pto in photo:
        a = 0
        for p in pto:
            if p in dictionary:
                a += dictionary[p]
        answer.append(a)
    return answer