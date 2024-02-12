from collections import deque
import sys
input = sys.stdin.readline

d = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

def bfs(y,x):
    q =deque()
    q.append([y,x])
    visited[y][x] = True

    while q:
        r,c = q.popleft()
        
        for i in range(8):
            dr = r+d[i][0]
            dc = c+d[i][1]

            if(0<=dr<h and 0<=dc<w and maps[dr][dc] == 1 and not visited[dr][dc]):
                visited[dr][dc] = True
                q.append([dr,dc])
            
while True:
    w, h = map(int,input().split())
    
    if (w == 0 and h == 0):
        break
    
    maps = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not visited[i][j] :
                bfs(i,j)
                count+=1

    print(count)