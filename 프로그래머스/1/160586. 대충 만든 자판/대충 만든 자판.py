def solution(keymap, targets):
    answer = []
    keydict = {}
    
    for key in keymap:
        for i, k in enumerate(key):
            keydict[k] = min(i + 1, keydict[k]) if k in keydict else i + 1
    
    for target in targets:
        count = 0
        for t in target:
            if t not in keydict:
                count = -1
                break
            count += keydict[t]
        answer.append(count)
    return answer