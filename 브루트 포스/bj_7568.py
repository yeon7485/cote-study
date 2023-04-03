# 덩치

n = int(input())

bulk = list()
rank = list()
for i in range(n):
    bulk.append(list(map(int, input().split())))
    rank.append(1)

for i in range(n):
    for j in range(n):
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            rank[i] = rank[i] + 1
        
print(*rank)