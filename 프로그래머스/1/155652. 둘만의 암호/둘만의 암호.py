def solution(s, skip, index):
    answer = ''
    alpa = 'abcdefghijklmnopqrstuvwxyz'
    
    for sk in skip:
        alpa = alpa.replace(sk, '').strip()
    
    print(alpa)
    for ch in s:
        idx = (alpa.find(ch) + index) % len(alpa)
        answer += alpa[idx]
    return answer