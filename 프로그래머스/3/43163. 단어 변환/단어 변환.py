from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [9999] * len(words)
    queue = deque()
    queue.append(begin)
    
    while queue:
        w = queue.popleft()
        if w == target:
            return visited[words.index(target)]
        
        for i in range(len(words)):
            if cnt(w, words[i]):       
                queue.append(words[i])
                if w == begin:
                    visited[i] = 1
                else:
                    visited[i] = min(visited[i], visited[words.index(w)] + 1)
            
            
def cnt(a, b):
    count = 0
    for i in range(len(a)):
        if not a[i] == b[i]:
            count += 1
    return True if count == 1 else False
    
    
