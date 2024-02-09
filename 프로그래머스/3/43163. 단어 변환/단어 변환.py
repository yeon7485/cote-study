from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [9999] * len(words)
    queue = deque()
    queue.append(begin)
    
    while queue:
        cur = queue.popleft()
        if cur == target:
            return visited[words.index(target)]
        
        for i in range(len(words)):
            if cnt(cur, words[i]) == 1:       
                queue.append(words[i])
                if cur == begin:
                    visited[i] = 1
                else:
                    visited[i] = min(visited[i], visited[words.index(cur)] + 1)
                
            
def cnt(a, b):
    count = 0
    for i in range(len(a)):
        if not a[i] == b[i]:
            count += 1
    return count
    
    