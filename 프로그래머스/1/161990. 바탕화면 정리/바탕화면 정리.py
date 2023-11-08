def solution(wallpaper):
    answer = [50, 50, 0, 0]
    
    for i, x in enumerate(wallpaper):
        for j, y in enumerate(x):
            if x[j] == '#':
                answer = [ min(answer[0], i), min(answer[1], j), max(answer[2], i+1), max(answer[3], j+1)]
    
    return answer