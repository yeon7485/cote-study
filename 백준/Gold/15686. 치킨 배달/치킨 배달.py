N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

visited_chicken = [False] * len(chicken)
sel_chicken = []
result = 1e10


def func(n, count):
    global result
    if count == M:
        sum_house = 0
        for h in house:
            min_house = 1e10
            for sel in sel_chicken:
                min_house = min(abs(h[0] - chicken[sel][0]) + abs(h[1] - chicken[sel][1]), min_house)
            sum_house += min_house
        result = min(sum_house, result)
        return

    for i in range(n, len(chicken)):
        if not visited_chicken[i]:
            sel_chicken.append(i)
            visited_chicken[i] = True
            func(i + 1, count + 1)
            visited_chicken[i] = False
            sel_chicken.pop()


func(0, 0)
print(result)
