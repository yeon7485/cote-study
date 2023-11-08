def solution(park, routes):
    point = []
    start = [0, 0]
    width = len(park[0])
    height = len(park)
    
    for i in range(len(park)):
        if 'S' in park[i]:
            start = [i, park[i].index('S')]
    point = start
    
    for route in routes:
        op = route[0]
        n = int(route[2])
        check = True
        
        if op == 'N' and point[0] - n >= 0:
            for i in range(point[0] - n, point[0]):
                if park[i][point[1]] == 'X':
                    check = False
                    break
            if check:
                point[0] -= n
                
        elif op == 'S' and point[0] + n < height:
            for i in range(point[0], point[0] + n + 1):
                if park[i][point[1]] == 'X':
                    check = False
                    break
            if check:
                point[0] += n
                
        elif op == 'W' and point[1] - n >= 0:
            for i in range(point[1] - n, point[1]):
                if park[point[0]][i] == 'X':
                    check = False
                    break
            if check:
                point[1] -= n
                
        elif op == 'E' and point[1] + n < width:
            for i in range(point[1], point[1] + n + 1):
                if park[point[0]][i] == 'X':
                    check = False
                    break
            if check:
                point[1] += n
    
    return point
